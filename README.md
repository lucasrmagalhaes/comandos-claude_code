# Comandos do Claude Code

Referência consolidada de **todos os comandos e funcionalidades do Claude Code**: comandos de terminal (`claude ...`), comandos de barra (`/...`), skills embutidas, atalhos de teclado, ferramentas internas, hooks e os recursos da plataforma.

> **Referência**: documentação oficial em [code.claude.com/docs](https://code.claude.com/docs/en/overview) + inspeção do binário instalado (`claude 2.1.136`).
> Última consolidação: **18/08/2026**.

## Índice

| Documento | Conteúdo |
| --- | --- |
| [CLI](docs/cli.md) | Subcomandos `claude ...` e todas as flags de linha de comando |
| [Comandos de barra](docs/slash-commands.md) | Todos os `/comandos` embutidos, aliases e skills bundladas |
| [Atalhos de teclado](docs/atalhos.md) | Modo interativo, edição de texto, modo Vim, transcript viewer |
| [Ferramentas](docs/ferramentas.md) | Todas as tools internas e quais pedem permissão |
| [Hooks](docs/hooks.md) | Eventos, matchers, tipos de hook e códigos de saída |
| [Funcionalidades](docs/funcionalidades.md) | Mapa completo de recursos: memória, skills, subagents, MCP, plugins, workflows, worktrees, permissões, sandbox, cloud, IDE, CI/CD |
| [Configuração](docs/configuracao.md) | `settings.json`, diretório `.claude/`, variáveis de ambiente, precedência |

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

## Publicar como site (GitHub Pages)

A pasta `docs/` já está pronta para o Pages (tema `jekyll-theme-cayman`, `docs/_config.yml`).
Para ligar: **Settings › Pages › Source: Deploy from a branch › Branch: `main` / pasta `/docs`**.

> **Status atual**: este repositório é privado e a conta não tem plano com Pages privado — a API do GitHub recusa habilitar (`Your current plan does not support GitHub Pages for this repository`). Para publicar, torne o repositório público ou faça upgrade. Enquanto isso, os Markdown já renderizam direto no GitHub com a navegação do índice acima.
