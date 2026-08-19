---
title: Hooks
nav_order: 8
---

# Hooks

[← Voltar ao índice](index.md)

Hooks executam comandos, requisições HTTP, tools MCP ou prompts automaticamente quando o Claude Code atinge um ponto do ciclo de vida: editar arquivo, terminar um turno, pedir permissão, compactar contexto etc. Use `/hooks` para ver o que está configurado na sessão.

## Eventos

### Sessão

| Evento | Quando dispara |
| --- | --- |
| `SessionStart` | Quando a sessão começa ou é retomada |
| `SessionEnd` | Quando a sessão termina |
| `Setup` | Preparação única em CI/scripts (com `--init-only` ou modo `-p`) |
| `ConfigChange` | Quando um arquivo de configuração muda durante a sessão |
| `InstructionsLoaded` | Quando `CLAUDE.md` ou `.claude/rules/*.md` é carregado |
| `CwdChanged` | Quando o diretório de trabalho muda |
| `DirectoryAdded` | Quando um diretório é adicionado no meio da sessão |
| `FileChanged` | Quando um arquivo monitorado muda em disco |

### Turno e prompt

| Evento | Quando dispara |
| --- | --- |
| `UserPromptSubmit` | Antes do Claude processar o seu prompt |
| `UserPromptExpansion` | Quando um comando de barra expande para um prompt |
| `MessageDisplay` | Enquanto o texto da resposta é exibido |
| `Stop` | Quando o Claude termina de responder |
| `StopFailure` | Quando o turno termina por erro de API |

### Tools

| Evento | Quando dispara |
| --- | --- |
| `PreToolUse` | Antes de uma chamada de tool executar (**pode bloquear**) |
| `PostToolUse` | Depois de uma chamada de tool ter sucesso |
| `PostToolUseFailure` | Depois de uma chamada de tool falhar |
| `PostToolBatch` | Depois que um lote de chamadas paralelas resolve |
| `PermissionRequest` | Quando uma chamada precisa de decisão de permissão |
| `PermissionDenied` | Quando o auto mode nega uma chamada |

### Agentes e tarefas

| Evento | Quando dispara |
| --- | --- |
| `SubagentStart` | Quando um subagent é criado |
| `SubagentStop` | Quando um subagent termina |
| `TaskCreated` | Quando uma tarefa está sendo criada |
| `TaskCompleted` | Quando uma tarefa é marcada como concluída |
| `TeammateIdle` | Quando um teammate de *agent team* vai ficar ocioso |

### Contexto e integrações

| Evento | Quando dispara |
| --- | --- |
| `PreCompact` | Antes da compactação de contexto |
| `PostCompact` | Depois da compactação |
| `Notification` | Quando o Claude Code manda uma notificação |
| `Elicitation` | Quando um servidor MCP pede input do usuário |
| `ElicitationResult` | Depois que o usuário responde à elicitação |
| `WorktreeCreate` | Quando um worktree está sendo criado |
| `WorktreeRemove` | Quando um worktree está sendo removido |

## Onde configurar

| Local | Escopo |
| --- | --- |
| `~/.claude/settings.json` | Todos os projetos (só na sua máquina) |
| `.claude/settings.json` | Um projeto (versionável, compartilhável) |
| `.claude/settings.local.json` | Um projeto (só na sua máquina) |
| Managed policy settings | Toda a organização |
| `hooks/hooks.json` de um plugin | Enquanto o plugin estiver habilitado |
| Frontmatter de skill/subagent | Durante a invocação daquela skill/subagent |

Estrutura de aninhamento:

```
evento (ex.: PreToolUse, Stop)
  └── grupo de matcher (filtra por nome de tool, tipo de agente, ...)
        └── handlers (command | http | mcp_tool | prompt | agent)
```

## Matchers

| Padrão | Avaliação | Exemplos |
| --- | --- | --- |
| `"*"`, `""`, omitido | Casa tudo | dispara sempre |
| Letras, dígitos, `_`, `-`, espaços, `,`, `\|` | String exata ou lista | `Bash`, `Edit\|Write`, `code-reviewer` |
| Outros caracteres | Regex JavaScript (sem âncora) | `^Notebook`, `mcp__memory__.*` |

Campos de matcher por evento:

| Evento | O matcher casa com |
| --- | --- |
| Eventos de tool | Nome da tool |
| `SessionStart` | `startup`, `resume`, `clear`, `compact`, `fork` |
| `SessionEnd` | `clear`, `resume`, `logout`, `prompt_input_exit`, `other` |
| `Notification` | `permission_prompt`, `idle_prompt`, `auth_success`, … |
| `SubagentStart` / `SubagentStop` | Tipo do agente (`general-purpose`, `Explore`, …) |
| `FileChanged` | Nomes de arquivo literais a observar |
| `StopFailure` | Tipo de erro (`rate_limit`, `overloaded`, `authentication_failed`, …) |

## Campos comuns a todos os handlers

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `type` | sim | `command`, `http`, `mcp_tool`, `prompt` ou `agent` |
| `if` | não | Filtro por regra de permissão (só eventos de tool): `"Bash(git *)"`, `"Edit(*.ts)"` |
| `timeout` | não | Segundos até cancelar. Padrões: 600 (command/http/mcp), 30 (prompt), 60 (agent) |
| `statusMessage` | não | Mensagem customizada do spinner |
| `once` | não | Roda uma vez por sessão e se remove (só skills/subagents) |

## Tipos de handler

### `command`

| Campo | Descrição |
| --- | --- |
| `command` (obrigatório) | Comando shell ou executável |
| `args` | Lista de argumentos (ativa a forma exec) |
| `async` | Roda em background |
| `asyncRewake` | Background + acorda no exit code 2 |
| `shell` | `"bash"` ou `"powershell"` |

**Códigos de saída:**

| Código | Efeito |
| --- | --- |
| `0` | Sucesso; o stdout JSON é interpretado para controle estruturado |
| `2` | Erro **bloqueante** nos eventos aplicáveis (`PreToolUse`, `UserPromptSubmit`, …); o stderr vira o motivo do bloqueio |
| Outros | Erro não bloqueante (a ação prossegue); stderr aparece como aviso |
| Timeout | Hook cancelado, sem decisão — a ação prossegue |

**Saída JSON (exit 0):**

| Campo | Efeito |
| --- | --- |
| `continue: false` | Para o processamento por completo |
| `stopReason` | Mensagem exibida quando `continue: false` |
| `systemMessage` | Aviso mostrado a você |
| `terminalSequence` | Sequência de notificação do terminal |
| `hookSpecificOutput` | Campos por evento (precisa incluir `hookEventName`) |

### `http`

| Campo | Descrição |
| --- | --- |
| `url` (obrigatório) | Endpoint que recebe o POST |
| `headers` | Pares chave-valor com interpolação `$VAR` |
| `allowedEnvVars` | Variáveis de ambiente liberadas nos headers |

Resposta: `2xx` com JSON é interpretado como o stdout de um hook `command`; `2xx` vazio é sucesso sem decisão; não-2xx, falha de conexão ou timeout são erros **não bloqueantes**.

### `mcp_tool`

| Campo | Descrição |
| --- | --- |
| `server` (obrigatório) | Nome do servidor MCP configurado |
| `tool` (obrigatório) | Nome da tool naquele servidor |
| `input` | Argumentos com substituição `${path}` |

A saída de texto da tool é interpretada como o stdout de um hook `command`. Servidor desconectado gera erro não bloqueante.

### `prompt`

| Campo | Descrição |
| --- | --- |
| `prompt` (obrigatório) | Texto enviado ao Claude; use `$ARGUMENTS` para o JSON de entrada |
| `model` | Modelo a usar (padrão: o modelo rápido) |

### `agent`

| Campo | Descrição |
| --- | --- |
| `prompt` (obrigatório) | Diretiva para o subagent |
| `model` | Modelo a usar |

## Placeholders de caminho

| Placeholder | Aponta para |
| --- | --- |
| `${CLAUDE_PROJECT_DIR}` | Raiz do projeto |
| `${CLAUDE_PLUGIN_ROOT}` | Raiz do plugin |
| `${CLAUDE_PLUGIN_DATA}` | Diretório de dados do plugin |

## Desligar tudo

```json
{ "disableAllHooks": true }
```

---

_Verificado contra o binário `2.1.136` e a documentação oficial de 19/08/2026._
