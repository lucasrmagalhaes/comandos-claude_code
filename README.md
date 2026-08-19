# Comandos do Claude Code

Referência consolidada de **todos os comandos e funcionalidades do Claude Code**: comandos de terminal (`claude ...`), comandos de barra (`/...`), skills embutidas, atalhos de teclado, ferramentas internas, hooks e os recursos da plataforma.

> **Referência**: documentação oficial em [code.claude.com/docs](https://code.claude.com/docs/en/overview) + inspeção do binário instalado (`claude 2.1.136`).
> Última consolidação: **19/08/2026**.

## Índice

| Documento | Conteúdo |
| --- | --- |
| [Guia do dev](docs/guia-dev.md) | Recorte opinativo: os comandos que mudam o dia a dia + receita de hook rodando formatador em container |
| [CLI](docs/cli.md) | Subcomandos `claude ...` e todas as flags de linha de comando |
| [Comandos de barra](docs/slash-commands.md) | Todos os `/comandos` embutidos, aliases e skills bundladas |
| [Atalhos de teclado](docs/atalhos.md) | Modo interativo, edição de texto, modo Vim, transcript viewer |
| [Ferramentas](docs/ferramentas.md) | Todas as tools internas e quais pedem permissão |
| [Hooks](docs/hooks.md) | Eventos, matchers, tipos de hook e códigos de saída |
| [Funcionalidades](docs/funcionalidades.md) | Mapa completo de recursos: memória, skills, subagents, MCP, plugins, workflows, worktrees, permissões, sandbox, cloud, IDE, CI/CD |
| [Configuração](docs/configuracao.md) | `settings.json`, diretório `.claude/`, variáveis de ambiente, precedência |
| [Cheatsheet](docs/cheatsheet.md) | Teclas, prefixos e comandos essenciais em uma página |
| [settings.json](docs/settings-json.md) | Todas as chaves — página gerada por `tools/gen-settings-keys.py` |
| [Variáveis de ambiente](docs/variaveis-ambiente.md) | Lista completa — página gerada por `tools/gen-env-vars.py` |
| [Receitas](docs/receitas/index.md) | Skill customizada, subagent, CLAUDE.md, hooks de teste e formatação |

## Como usar

- Procurando um comando específico? Comece por [Comandos de barra](docs/slash-commands.md) (dentro da sessão) ou [CLI](docs/cli.md) (no terminal).
- Quer saber o que dá pra automatizar? [Hooks](docs/hooks.md) e [Funcionalidades](docs/funcionalidades.md).
- Quer ajustar comportamento/permissões? [Configuração](docs/configuracao.md).

## Aviso de versão

O Claude Code muda rápido (releases quase diários). Duas fontes convivem aqui:

- **Documentação oficial** — o estado mais recente do produto.
- **Binário instalado (`2.1.136`)** — o que efetivamente existe na máquina onde esta referência foi gerada.

Quando as duas divergem, isso está marcado no texto. Para conferir a sua própria versão:

```bash
claude --version && claude --help
```

## Site (GitHub Pages)

Publicado em **<https://lucasrmagalhaes.github.io/comandos-claude_code/>** — tema `just-the-docs`, com sidebar e busca. A pasta `docs/` é a fonte; qualquer push na `main` republica.

## Manutenção

O Claude Code muda rápido — este repo tem ferramentas para não apodrecer:

| Ferramenta | O que faz |
| --- | --- |
| `tools/check-drift.py` | Compara `docs/slash-commands.md` com a doc oficial; sai com erro listando o que falta. Roda toda segunda via GitHub Actions e abre issue quando há drift (arquivo em `tools/drift.workflow.yml` até ser movido para `.github/workflows/`) |
| `tools/gen-env-vars.py` / `tools/gen-settings-keys.py` | Regeram as páginas de variáveis de ambiente e de chaves do settings a partir da doc oficial |
| `tools/extract-commands.py` | Extrai o registry de comandos do binário instalado: `strings -n 3 "$(readlink -f "$(which claude)")" \| tools/extract-commands.py` |
| `tools/dump-cli-help.sh` | Salva o `--help` de todos os subcomandos para diffar entre versões |
| `tools/known-local-only.txt` | Divergências intencionais (comandos do binário/ocultos que a tabela oficial não lista) |

Fluxo de atualização: rode o drift checker → corrija `docs/slash-commands.md` → regenere as duas páginas geradas → atualize o carimbo de versão.

## Licença

MIT. O conteúdo é uma consolidação em português baseada na [documentação oficial do Claude Code](https://code.claude.com/docs), que é a fonte autoritativa.
