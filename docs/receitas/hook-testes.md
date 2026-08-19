---
title: Hook de testes
parent: Receitas
---

# Receita: rodar o teste do arquivo tocado a cada edição

Objetivo: o Claude edita `app/Services/FooService.php` → o hook roda `tests/**/FooServiceTest.php` na hora e devolve o resultado **para o Claude**, que corrige sem você pedir.

## 1. O script

`.claude/hooks/testa-arquivo.sh`:

```bash
#!/usr/bin/env bash
set -uo pipefail

file="$(jq -r '.tool_response.filePath // .tool_input.file_path // empty')"
[ -n "$file" ] || exit 0

case "$file" in
  */app/*.php) ;;
  *) exit 0 ;;
esac

base="$(basename "$file" .php)"
test_file="$(find tests -name "${base}Test.php" -print -quit 2>/dev/null)"
[ -n "$test_file" ] || exit 0

if ! out="$(./vendor/bin/phpunit "$test_file" 2>&1 | tail -30)"; then
  echo "Teste falhou após editar $base:" >&2
  echo "$out" >&2
  exit 2
fi
```

O **exit 2** é o truque: em `PostToolUse`, o stderr volta como feedback para o Claude — ele vê a falha e corrige no mesmo turno. Exit 0 = silêncio.

## 2. O wiring

Em `.claude/settings.json` (time) ou `.claude/settings.local.json` (só você):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PROJECT_DIR}/.claude/hooks/testa-arquivo.sh\"",
            "timeout": 120,
            "statusMessage": "Rodando teste do arquivo"
          }
        ]
      }
    ]
  }
}
```

## 3. Teste por pipe antes de confiar

```bash
echo '{"tool_input":{"file_path":"'$PWD'/app/Services/FooService.php"}}' | bash .claude/hooks/testa-arquivo.sh; echo "exit=$?"
```

Confira os três ramos: arquivo com teste que passa (exit 0, silêncio), com teste que falha (exit 2 + stderr), sem teste correspondente (exit 0).

## Variações

- **Só quando o teste existe e é rápido**: suites lentas em hook viram tortura — filtre por diretório ou use `timeout` curto e aceite o cancelamento como "sem veredito".
- **Filtro nativo**: o campo `"if": "Edit(app/**/*.php)"` no hook evita nem spawnar o script para arquivos fora do padrão.
- **Assíncrono**: `"async": true` roda sem bloquear; com `"asyncRewake": true`, um exit 2 tardio ainda acorda o Claude.

## Erros comuns

- **`|| true` no comando de teste** — engole o exit 2 e o hook nunca reporta nada.
- **Suite inteira no hook** — o Claude fica 4 minutos parado por edição. Rode só o teste do arquivo.
- **Esquecer que o hook roda do cwd da sessão** — use `${CLAUDE_PROJECT_DIR}` ou caminhos derivados do próprio script, nunca relativos soltos.
