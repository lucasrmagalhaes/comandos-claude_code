# Guia do dev — o que realmente muda o dia a dia

[← Voltar ao índice](index.md)

Este é um recorte **opinativo**. A lista completa está em [Comandos de barra](slash-commands.md); aqui ficam só os que mudam o resultado do trabalho.

## Os que mudam o jogo

| Comando | Por que importa |
| --- | --- |
| `Shift+Tab` → plan mode (ou `/plan`) | Para tarefa não-trivial, faz o Claude desenhar antes de editar. Maior ganho de qualidade por unidade de esforço — evita 20 minutos de código na direção errada |
| `Esc` `Esc` / `/rewind` | Desfaz **código e conversa** juntos até um checkpoint. Muda seu comportamento: você deixa o Claude tentar coisas mais ousadas porque voltar é barato |
| `/code-review [nível]` | Revisa o diff atual. `low`/`medium` = poucos achados de alta confiança; `high`→`max` = mais cobertura; `ultra` roda multi-agente na nuvem |
| `/context` | Mostra o que está ocupando a janela. É o diagnóstico quando o Claude "esquece" algo — quase sempre é contexto cheio, não burrice do modelo |
| `/permissions` + `/fewer-permission-prompts` | Corta a fadiga de aprovação. O segundo varre seus transcripts e propõe a allowlist com base no que você realmente usa |
| `/hooks` | Automação de verdade: formatar, testar ou validar automaticamente a cada edição. Ver a [receita abaixo](#receita-formatador-rodando-dentro-de-um-container) |
| `/memory` + `/dream` | `/memory` edita o `CLAUDE.md` e a auto memory; `/dream` consolida, funde duplicatas e poda o que ficou obsoleto |

## Segundo nível, subestimados

| Comando | Quando usar |
| --- | --- |
| `/branch` | Bifurca a conversa no ponto atual — "e se fizéssemos por outro caminho" sem perder o fio original |
| `/btw` | Pergunta lateral que **não** entra na conversa principal. Para tirar uma dúvida no meio de uma implementação sem poluir o contexto |
| `/effort` | `low` para mecânico, `xhigh`/`max` para bug difícil. Quase ninguém mexe e paga caro nos dois sentidos |
| `/simplify` | Só qualidade (reuso, duplicação, altitude), não caça bug. Bom antes de abrir PR |
| `/loop 5m <prompt>` | Poll de CI, deploy, fila. Sem intervalo, o próprio Claude escolhe o ritmo |
| `/usage` | Mostra o que está consumindo seu limite, quebrado por skill, subagent e MCP |
| `/doctor` | Quando `CLAUDE.md`, hook ou MCP "não aplicou". Com `--safe-mode`, resolve a maioria dos casos de config quebrada |

## No Desktop, features valem mais que comandos

Boa parte do ganho não é comando, é interface:

- **Sessões paralelas com isolamento git** — cada sessão no seu worktree, sem você gerenciar nada.
- **Revisão visual de diff** e **terminal/editor integrados** — substituem o `/diff` e o vai-e-vem para o terminal.
- **App preview / painel de browser** — verificar a tela sem sair do app.
- **Monitoramento de PR** e **tarefas agendadas**.

## Não gaste tempo com

`/terminal-setup`, `/tui`, `/statusline`, modo Vim e `/desktop` são de CLI e não fazem nada de útil dentro do app Desktop.

---

## Receita: formatador rodando dentro de um container

O caso clássico de quem desenvolve com Docker: o formatador (Pint, PHP-CS-Fixer, Black, Prettier) só existe **dentro** do container, mas o hook recebe o caminho **do host**. É preciso traduzir um no outro.

### 1. Descubra o mapeamento do mount

```bash
docker inspect <container> --format '{{range .Mounts}}{{.Source}} -> {{.Destination}}{{"\n"}}{{end}}'
```

Um resultado como `/Users/voce/proj/application -> /usr/src/app` significa que o host `<raiz>/application/app/Foo.php` é, dentro do container, `/usr/src/app/app/Foo.php`.

### 2. Script em `.claude/hooks/`

Deixar a lógica num script (em vez de espremer tudo no JSON) permite testá-la isoladamente. Este se localiza sozinho a partir do próprio caminho, então não carrega caminho absoluto nenhum:

```bash
#!/usr/bin/env bash
set -uo pipefail

container=<nome-do-container>
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/application"
file="$(jq -r '.tool_response.filePath // .tool_input.file_path // empty')"

[ -n "$file" ] || exit 0

case "$file" in
  "$root"/*.php) ;;
  *) exit 0 ;;
esac

docker ps --format '{{.Names}}' | grep -qx "$container" || exit 0

rel="${file#"$root"/}"
out="$(docker exec "$container" ./vendor/bin/pint "/usr/src/app/$rel" 2>&1)" || exit 0

if printf '%s' "$out" | grep -q 'FIXED'; then
  jq -nc --arg rel "$rel" '{
    suppressOutput: true,
    hookSpecificOutput: {
      hookEventName: "PostToolUse",
      additionalContext: ("Pint reformatou " + $rel + " no container. Releia o arquivo antes de editá-lo novamente.")
    }
  }'
fi
```

Três detalhes que fazem diferença:

- **Guarda de caminho** (`case`) — sai silencioso para arquivos fora do mount ou que não sejam do tipo tratado. Sem isso, o hook tenta formatar tudo.
- **Guarda de container** — se o container estiver parado, sai com 0 em vez de encher a sessão de erro.
- **Aviso de arquivo obsoleto** — o formatador reescreve o arquivo **depois** do `Edit`. Sem avisar, a próxima edição do Claude bate em conteúdo velho e falha. O `additionalContext` manda ele reler; o `suppressOutput` evita poluir o transcript quando nada mudou.

### 3. Ligue em `.claude/settings.local.json`

`settings.local.json` (gitignored) é o lugar certo: nome de container e caminhos são da sua máquina. Se o time inteiro usa o mesmo compose, promova para `.claude/settings.json`.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PROJECT_DIR}/.claude/hooks/pint-container.sh\"",
            "timeout": 60,
            "statusMessage": "Pint no container"
          }
        ]
      }
    ]
  }
}
```

> **Faça merge, não substitua.** Se o arquivo já existe, use `jq` para adicionar a chave `hooks` sem apagar `permissions`. Um `settings.json` inválido desliga **silenciosamente** todas as settings daquele arquivo.

### 4. Teste antes de confiar

O hook recebe JSON no stdin — dá para testar sem abrir sessão nenhuma:

```bash
echo '{"tool_name":"Edit","tool_input":{"file_path":"/caminho/real/App/Foo.php"}}' | bash .claude/hooks/pint-container.sh
```

Teste os quatro ramos: arquivo torto dentro do mount (formata e emite JSON), arquivo já formatado (silêncio), arquivo fora do mount (silêncio), arquivo de outro tipo (silêncio). Depois valide o wiring:

```bash
jq -e '.hooks.PostToolUse[] | select(.matcher == "Edit|Write") | .hooks[] | .command' .claude/settings.local.json
```

Exit 0 e imprimiu o comando = certo. Exit 4 = o matcher não bate. Exit 5 = JSON malformado ou aninhamento errado.

### 5. Permissões

O hook roda como comando de shell **direto** — não passa pelo sistema de permissões. A allowlist só importa para os `docker exec` que o **próprio Claude** dispara:

```json
{ "permissions": { "allow": ["Bash(docker exec:*)"] } }
```

Antes de adicionar, confira se já não está lá:

```bash
jq -r '.permissions.allow[]? | select(test("docker"))' .claude/settings.local.json
```

### Nota sobre quando o hook carrega

Hooks vêm das settings do **diretório do projeto da sessão**. Uma sessão aberta em outra pasta não enxerga o hook, mesmo que o arquivo exista no disco. E o watcher de settings só observa diretórios que já tinham arquivo de settings quando a sessão começou — ao criar o hook pela primeira vez, abra o `/hooks` uma vez (recarrega a config) ou reinicie a sessão.
