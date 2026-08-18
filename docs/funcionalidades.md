# Funcionalidades

[← Voltar ao índice](index.md)

Mapa do que o Claude Code oferece além dos comandos. Cada item aponta para a documentação oficial correspondente.

---

## Núcleo

| Recurso | O que é |
| --- | --- |
| [Agentic loop](https://code.claude.com/docs/en/how-claude-code-works) | O ciclo ler → planejar → agir → verificar que move o Claude pelo seu projeto |
| [Janela de contexto](https://code.claude.com/docs/en/context-window) | Simulação interativa de como o contexto enche: o que carrega sozinho, quanto custa cada leitura, quando regras e hooks disparam |
| [Prompt caching](https://code.claude.com/docs/en/prompt-caching) | Gerenciado automaticamente. Explica por que trocar de modelo gera um turno lento sem cache, quanto custa `/compact` e por que editar `CLAUDE.md` não aplica no meio da sessão |
| [Compactação](https://code.claude.com/docs/en/model-config) | `/compact` manual e auto-compact configurável por janela de tokens |
| [Diretório `.claude/`](https://code.claude.com/docs/en/claude-directory) | Onde vivem `CLAUDE.md`, settings, hooks, skills, commands, subagents, workflows, rules e auto memory |

## Memória

| Recurso | O que é |
| --- | --- |
| [`CLAUDE.md`](https://code.claude.com/docs/en/memory) | Instruções persistentes de projeto e de usuário. Hierárquico: raiz, subpastas, `~/.claude/CLAUDE.md` |
| Auto memory | O Claude acumula aprendizados sozinho em arquivos de memória tipados. Liga/desliga com `/toggle-memory`; consolida com `/dream` |
| `.claude/rules/*.md` | Regras carregadas junto das instruções (dispara o hook `InstructionsLoaded`) |

## Permissões e segurança

| Recurso | O que é |
| --- | --- |
| [Modos de permissão](https://code.claude.com/docs/en/permission-modes) | `default`, `acceptEdits`, `auto`, `dontAsk`, `plan`, `bypassPermissions`. Alterna com `Shift+Tab` |
| **Auto mode** | Padrão nos planos Pro, Max e Team: um classificador decide a maior parte dos prompts de permissão. Configurável por org (`claude auto-mode config/defaults/critique`) |
| [Regras de permissão](https://code.claude.com/docs/en/permissions) | allow / ask / deny com casamento por comando, caminho, domínio, skill e tipo de subagent |
| [Bash sandboxed](https://code.claude.com/docs/en/sandboxing) | Isolamento de filesystem e rede para execução mais autônoma e segura (`/sandbox`) |
| [Ambientes de sandbox](https://code.claude.com/docs/en/sandbox-environments) | Comparativo: Bash sandboxed, sandbox runtime, dev containers, Docker, VMs |
| [Segurança](https://code.claude.com/docs/en/security) | Salvaguardas do produto e boas práticas |
| [Zero data retention](https://code.claude.com/docs/en/zero-data-retention) | ZDR para contas qualificadas no Claude for Enterprise |

## Skills

| Recurso | O que é |
| --- | --- |
| [Skills](https://code.claude.com/docs/en/skills) | `SKILL.md` com instruções que o Claude carrega **sob demanda**. Invocável por você (`/nome`) ou pelo próprio Claude quando relevante |
| Comandos customizados | Unificados com skills. `.claude/commands/x.md` e `.claude/skills/x/SKILL.md` criam o mesmo `/x` |
| Skills bundladas | `/code-review`, `/simplify`, `/security-review`, `/debug`, `/loop`, `/batch`, `/dataviz`, `/deep-research`, `/verify`, `/claude-api`, `/design-sync`, `/fewer-permission-prompts` |

## Subagents e paralelismo

| Recurso | O que é |
| --- | --- |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Agentes especializados com contexto próprio, definidos em `.claude/agents/*.md`. Rodam em background por padrão |
| [Agent view](https://code.claude.com/docs/en/agent-view) | Uma tela para despachar e acompanhar muitas sessões (`claude agents`) |
| [Agent teams](https://code.claude.com/docs/en/agent-teams) | Várias instâncias trabalhando como time, com tarefas compartilhadas e mensageria entre agentes |
| [Mensagens entre sessões](https://code.claude.com/docs/en/cross-session-messaging) | Listar e mensagear suas outras sessões — locais, em outras máquinas ou na web (`/list-agents`) |
| [Dynamic workflows](https://code.claude.com/docs/en/workflows) | Um script que orquestra dezenas de subagents de forma determinística (fan-out, pipeline, barreiras). Bom para auditorias, migrações e pesquisa cruzada |
| [Worktrees](https://code.claude.com/docs/en/worktrees) | Sessões paralelas isoladas em git worktrees (`--worktree`, `.worktreeinclude`, isolamento de subagent) |
| [Batch](https://code.claude.com/docs/en/commands) | `/batch` executa uma mudança mecânica em 5–30 worktrees isolados, cada um abrindo seu PR |

## Automação

| Recurso | O que é |
| --- | --- |
| [Hooks](hooks.md) | Dispara comandos/HTTP/prompts em ~30 eventos do ciclo de vida |
| [Tarefas agendadas](https://code.claude.com/docs/en/scheduled-tasks) | `/loop` e as tools de cron para rodar prompts em intervalo, fazer polling ou lembretes únicos |
| [Goals](https://code.claude.com/docs/en/goal) | `/goal` define uma condição de conclusão e o Claude segue trabalhando até bater |
| [Routines](https://code.claude.com/docs/en/routines) | Rotinas na nuvem: rodam em cron, por chamada de API ou reagindo a eventos do GitHub (`/schedule`) |
| [Channels](https://code.claude.com/docs/en/channels) | Empurra mensagens, alertas e webhooks para dentro de uma sessão viva, via servidor MCP |
| [Deep links](https://code.claude.com/docs/en/deep-links) | URLs `claude-cli://` que abrem o Claude Code no repo certo com o prompt certo |

## MCP — Model Context Protocol

| Recurso | O que é |
| --- | --- |
| [Conectar servidores](https://code.claude.com/docs/en/mcp-quickstart) | `claude mcp add`, transportes stdio / HTTP / SSE, escopos user/project/local |
| [MCP completo](https://code.claude.com/docs/en/mcp) | Tools, prompts (viram `/mcp__servidor__prompt`), resources (`@servidor:...`), OAuth |
| Tool search | Escala para milhares de tools carregando só o que é necessário, sob demanda |
| [MCP gerenciado](https://code.claude.com/docs/en/managed-mcp) | Allowlists e denylists de servidores para a organização |

## Plugins

| Recurso | O que é |
| --- | --- |
| [Descobrir e instalar](https://code.claude.com/docs/en/discover-plugins) | Marketplaces de plugins com skills, agents, hooks e servidores MCP |
| [Criar plugins](https://code.claude.com/docs/en/plugins) | Estrutura, `plugin.json`, componentes |
| [Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) | Publicar e distribuir para times e comunidades |
| [Dependências](https://code.claude.com/docs/en/plugin-dependencies) | Restrições de versão e bundles curados |

## Sessões

| Recurso | O que é |
| --- | --- |
| [Gerenciar sessões](https://code.claude.com/docs/en/sessions) | Nomear, retomar, bifurcar e alternar (`--continue`, `--resume`, `--from-pr`, `/resume`) |
| [Checkpointing](https://code.claude.com/docs/en/checkpointing) | Rastreia, reverte e resume as edições — `/rewind`, `Esc Esc` |
| Background sessions | `/background`, `claude attach|logs|respawn|stop|rm` |
| [Artifacts](https://code.claude.com/docs/en/artifacts) | Publica a saída da sessão como página viva e interativa no claude.ai (privada, org ou pública) |

## Onde rodar

| Superfície | Doc |
| --- | --- |
| CLI (terminal) | [CLI reference](cli.md) |
| Desktop (macOS, Windows, Linux beta, WSL) | [Desktop](https://code.claude.com/docs/en/desktop) — sessões paralelas com isolamento git, terminal e editor integrados, side chats, computer use, preview de app, revisão visual de diff, painel do simulador iOS |
| VS Code | [VS Code](https://code.claude.com/docs/en/vs-code) — diffs inline, @-menções, revisão de plano |
| JetBrains | [JetBrains](https://code.claude.com/docs/en/jetbrains) — IntelliJ, PyCharm, WebStorm etc. |
| Web | [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) — `--cloud`, `--teleport`, auto-fix de PR |
| Mobile | [Mobile](https://code.claude.com/docs/en/mobile) — iniciar, monitorar e conduzir tarefas pelo celular |
| Remote Control | [Remote Control](https://code.claude.com/docs/en/remote-control) — continuar uma sessão local de qualquer dispositivo |

## Integrações

| Integração | O que faz |
| --- | --- |
| [Chrome](https://code.claude.com/docs/en/chrome) | Testar web apps, depurar com console, preencher formulários, extrair dados |
| [Computer use](https://code.claude.com/docs/en/computer-use) | Abrir apps, clicar, digitar e ver a tela no macOS, direto da CLI |
| [GitHub Actions](https://code.claude.com/docs/en/github-actions) | Responder a `@claude`, automatizar tarefas, transformar issues em PRs |
| [GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server) | Sessões web, code review e marketplaces em instância self-hosted |
| [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) | Integração no fluxo do GitLab |
| [Slack / Claude Tag](https://code.claude.com/docs/en/claude-tag) | Delegar tarefas de código pelo Slack |

## Qualidade de código

| Recurso | O que é |
| --- | --- |
| [Code Review](https://code.claude.com/docs/en/code-review) | Revisão automatizada de PR com análise multi-agente do codebase inteiro |
| [Ultrareview](https://code.claude.com/docs/en/ultrareview) | `/code-review ultra` — revisão profunda multi-agente na nuvem que encontra **e verifica** bugs |
| [security-guidance](https://code.claude.com/docs/en/security-guidance) | Plugin que faz o Claude revisar o próprio código por vulnerabilidades e corrigir na mesma sessão |
| [Claude Security](https://code.claude.com/docs/en/claude-security) | Plugin que varre o codebase e transforma achados em patches |

## Modelo e desempenho

| Recurso | O que é |
| --- | --- |
| [Configuração de modelo](https://code.claude.com/docs/en/model-config) | Escolha do modelo, níveis de effort, contexto estendido, janela de auto-compact |
| [Fast mode](https://code.claude.com/docs/en/fast-mode) | Respostas mais rápidas do Opus (`/fast`, `Option+O`). Não rebaixa o modelo |
| [Advisor tool](https://code.claude.com/docs/en/advisor) | Pareia o modelo principal com um modelo mais forte, consultado em momentos-chave |
| Effort levels | `low`, `medium`, `high`, `xhigh`, `max` (`/effort`, `--effort`) |

## Interface

| Recurso | O que é |
| --- | --- |
| [Output styles](https://code.claude.com/docs/en/output-styles) | Adapta o Claude Code para usos além de engenharia de software |
| [Status line](https://code.claude.com/docs/en/statusline) | Barra customizada com uso de contexto, custos e status do git (`/statusline`) |
| [Fullscreen](https://code.claude.com/docs/en/fullscreen) | Renderização sem flicker, com suporte a mouse e memória estável (`/tui fullscreen`) |
| [Keybindings](https://code.claude.com/docs/en/keybindings) | Atalhos customizáveis em `~/.claude/keybindings.json` (`/keybindings`) |
| [Terminal](https://code.claude.com/docs/en/terminal-config) | `Shift+Enter`, bell ao terminar, tmux, tema, modo Vim |
| [Acessibilidade](https://code.claude.com/docs/en/accessibility) | Leitor de tela (VoiceOver, NVDA), magnificadores, movimento reduzido, temas para daltonismo |
| [Ditado por voz](https://code.claude.com/docs/en/voice-dictation) | Falar os prompts (`/voice`, segurar ou tocar `Space`) |

## Programático

| Recurso | O que é |
| --- | --- |
| [Headless](https://code.claude.com/docs/en/headless) | Rodar o Claude Code por CLI, Python ou TypeScript |
| [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) | Construir agentes de produção com o Claude Code como biblioteca |
| Structured outputs | `--json-schema` e a tool de saída estruturada para JSON validado |
| Streaming | `--output-format stream-json`, `--include-partial-messages`, `--input-format stream-json` |

## Organização e enterprise

| Recurso | O que é |
| --- | --- |
| [Setup para organização](https://code.claude.com/docs/en/admin-setup) | Mapa de decisão: provedor de API, managed settings, políticas, monitoramento, tratamento de dados |
| [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings) | Configuração central sem MDM |
| [Feature availability](https://code.claude.com/docs/en/feature-availability) | O que existe em cada plano e em cada provedor |
| Provedores | [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Claude Platform on AWS](https://code.claude.com/docs/en/claude-platform-on-aws), [Google Cloud Agent Platform](https://code.claude.com/docs/en/google-vertex-ai), [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry) |
| [Gateways](https://code.claude.com/docs/en/gateways) | Credenciais centralizadas, rastreio de uso e controle de custo |
| [Self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments) | Rodar sessões cloud na sua própria infraestrutura |
| [Monitoramento](https://code.claude.com/docs/en/monitoring-usage) | OpenTelemetry |
| [Custos](https://code.claude.com/docs/en/costs) | Rastrear tokens, limites de gasto por time, reduzir custo |
| [Analytics](https://code.claude.com/docs/en/analytics) | Dashboard de adoção e velocidade de engenharia |
| [Dev containers](https://code.claude.com/docs/en/devcontainer) | Ambiente isolado e consistente para o time |
| [Rede corporativa](https://code.claude.com/docs/en/network-config) | Proxy, CA customizada, mTLS |

## Codebases grandes

| Recurso | O que é |
| --- | --- |
| [Monorepos](https://code.claude.com/docs/en/large-codebases) | `CLAUDE.md` aninhados, worktrees esparsos, code intelligence, skills por pacote |

## Diagnóstico

| Recurso | O que é |
| --- | --- |
| [Depurar configuração](https://code.claude.com/docs/en/debug-your-config) | Por que `CLAUDE.md`, settings, hooks, MCP ou skills não aplicaram — use `/context`, `/doctor`, `/hooks`, `/mcp` |
| [Troubleshooting](https://code.claude.com/docs/en/troubleshooting) | CPU/memória altos, travamentos, thrashing de auto-compact, problemas de busca |
| [Instalação e login](https://code.claude.com/docs/en/troubleshoot-install) | `command not found`, PATH, permissões, rede, autenticação |
| [Referência de erros](https://code.claude.com/docs/en/errors) | Mensagens de erro em runtime, o que significam e como corrigir |
| Safe mode | `--safe-mode` sobe com todas as customizações desligadas |
