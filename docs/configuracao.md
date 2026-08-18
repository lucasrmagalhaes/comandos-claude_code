# Configuração

[← Voltar ao índice](index.md)

## Fontes de settings e precedência

Da mais forte para a mais fraca:

| Ordem | Fonte | Identificador interno | Onde fica |
| --- | --- | --- | --- |
| 1 | Managed policy | `policySettings` | Definida pela organização (MDM ou [server-managed settings](https://code.claude.com/docs/en/server-managed-settings)) |
| 2 | Flag de CLI | `flagSettings` | `--settings <arquivo-ou-json>` |
| 3 | Projeto, gitignored | `localSettings` | `.claude/settings.local.json` |
| 4 | Projeto, versionado | `projectSettings` | `.claude/settings.json` |
| 5 | Usuário | `userSettings` | `~/.claude/settings.json` |

Controle quais fontes carregar com `--setting-sources user,project,local`.
Para depurar o que realmente aplicou: `/doctor`, `/context`, `/hooks`, `/mcp`, ou `--safe-mode` para subir sem nenhuma customização.

## Diretório `.claude/` do projeto

| Caminho | Versionado? | O que é |
| --- | --- | --- |
| `CLAUDE.md` | sim | Instruções do projeto, lidas em toda sessão |
| `.mcp.json` | sim | Servidores MCP com escopo de projeto, compartilhados com o time |
| `.worktreeinclude` | sim | Arquivos gitignored a copiar para novos worktrees |
| `.claude/settings.json` | sim | Permissões, hooks e configuração |
| `.claude/settings.local.json` | não | Suas sobrescritas pessoais neste projeto |
| `.claude/rules/*.md` | sim | Instruções por tópico, opcionalmente restritas a caminhos de arquivo |
| `.claude/skills/<nome>/SKILL.md` | sim | Skill: gatilho, quem invoca e instruções (pode empacotar arquivos de apoio) |
| `.claude/commands/<nome>.md` | sim | Prompt de arquivo único invocado como `/nome` |
| `.claude/agents/<nome>.md` | sim | Subagent especializado com contexto próprio |
| `.claude/workflows/*.js` | sim | Scripts de dynamic workflow que orquestram muitos subagents |
| `.claude/output-styles/` | sim | Output styles com escopo de projeto |
| `.claude/agent-memory/<agente>/` | sim | Memória persistente de subagent, separada da auto memory da sessão |

## Diretório `~/.claude/` do usuário

| Caminho | O que é |
| --- | --- |
| `CLAUDE.md` | Preferências pessoais válidas em todos os projetos |
| `settings.json` | Settings padrão para todos os projetos |
| `keybindings.json` | Atalhos de teclado customizados (`/keybindings`) |
| `themes/` | Temas de cor customizados |
| `rules/`, `skills/`, `commands/`, `agents/`, `workflows/`, `output-styles/` | Versões pessoais, disponíveis em qualquer projeto |
| `agent-memory/` | Memória persistente de subagents com `memory: user` |
| `projects/<projeto>/memory/` | Auto memory que o Claude escreve e mantém sozinho (`MEMORY.md` como índice) |
| `plugins/` | Plugins e marketplaces instalados |
| `sessions/`, `projects/`, `shell-snapshots/`, `session-env/` | Estado local de execução (transcripts, snapshots de shell). Limpe com `claude project purge` |

## Regras de permissão

Sintaxe usada em `permissions.allow`, `permissions.ask` e `permissions.deny`:

| Regra | Vale para |
| --- | --- |
| `Bash(npm run *)` | `Bash`, `Monitor` |
| `PowerShell(Get-ChildItem *)` | `PowerShell` |
| `Read(~/secrets/**)` | `Read`, `Grep`, `Glob`, `LSP` |
| `Edit(/src/**)` | `Edit`, `Write`, `NotebookEdit` |
| `Skill(deploy *)` | `Skill` |
| `Agent(Explore)` | `Agent` |
| `WebFetch(domain:example.com)` | `WebFetch` |
| `WebSearch` | `WebSearch` (tool inteira) |

Editar pela interface: `/permissions`. Para reduzir prompts com base no seu histórico real: `/fewer-permission-prompts`.

Referência completa das chaves de `settings.json`: [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings).

## Variáveis de ambiente

São muitas (centenas). Os grupos principais:

| Prefixo / variável | Para que serve |
| --- | --- |
| `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL` | Autenticação e roteamento por proxy/gateway |
| `ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU,FABLE}_MODEL` | Fixar o modelo de cada alias |
| `ANTHROPIC_CUSTOM_MODEL_OPTION*` | Adicionar um modelo customizado ao seletor |
| `ANTHROPIC_BEDROCK_*`, `AWS_BEARER_TOKEN_BEDROCK` | Amazon Bedrock |
| `ANTHROPIC_VERTEX_*` | Google Cloud Agent Platform |
| `ANTHROPIC_FOUNDRY_*` | Microsoft Foundry |
| `ANTHROPIC_AWS_*`, `ANTHROPIC_WORKSPACE_ID`, `ANTHROPIC_ORGANIZATION_ID` | Claude Platform on AWS e workload identity federation |
| `API_TIMEOUT_MS`, `API_FORCE_IDLE_TIMEOUT` | Timeouts de API |
| `BASH_DEFAULT_TIMEOUT_MS`, `BASH_MAX_TIMEOUT_MS`, `BASH_MAX_OUTPUT_LENGTH` | Comportamento da tool `Bash` |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Compactação de contexto |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Teto de tokens de saída por resposta |
| `CLAUDE_CODE_ENABLE_TASKS` | Alterna entre as tools `Task*` e o `TodoWrite` |
| `CLAUDE_AX_SCREEN_READER`, `CLAUDE_CODE_ACCESSIBILITY` | Acessibilidade |
| `CLAUDECODE` | Vale `1` dentro de subprocessos criados pelo Claude Code |
| `CLAUDE_CODE_PROCESS_WRAPPER` | Roteia os processos por um launcher corporativo |

Lista completa: [code.claude.com/docs/en/env-vars](https://code.claude.com/docs/en/env-vars).

## Verificação rápida

```bash
claude doctor
```

Dentro da sessão:

| Comando | Mostra |
| --- | --- |
| `/status` | Versão, modelo, conta, conectividade de API, tools |
| `/context` | O que ocupa a janela de contexto agora |
| `/config` | Painel de settings (ou `chave=valor` direto) |
| `/permissions` | Regras de allow / ask / deny em vigor |
| `/hooks` | Hooks configurados por evento |
| `/mcp` | Servidores MCP e seu estado de conexão |
| `/skills` | Skills disponíveis |
| `/doctor` | Checkup de instalação e settings |
