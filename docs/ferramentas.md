# Ferramentas (tools)

[← Voltar ao índice](index.md)

Os nomes abaixo são as strings exatas usadas em [regras de permissão](configuracao.md), listas de tools de subagents e matchers de [hooks](hooks.md).

A coluna **Permissão** indica se a tool pergunta antes de agir no *Manual mode*, para caminhos dentro do diretório de trabalho. Em **auto mode** (padrão nos planos Pro, Max e Team) um classificador decide a maior parte desses prompts. Tools de arquivo marcadas com "Não" — como `Read`, `Grep` e `Glob` — ainda perguntam para caminhos **fora** do diretório de trabalho.

## Arquivos e código

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `Read` | Lê o conteúdo de arquivos (inclui imagens, PDFs e notebooks) | Não |
| `Write` | Cria ou sobrescreve arquivos | Sim |
| `Edit` | Faz edições pontuais em arquivos | Sim |
| `NotebookEdit` | Altera células de notebooks Jupyter | Sim |
| `Glob` | Encontra arquivos por padrão de nome | Não |
| `Grep` | Busca padrões no conteúdo dos arquivos | Não |
| `LSP` | Inteligência de código via language servers: definições, referências, erros de tipo | Não |

## Execução

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `Bash` | Executa comandos shell | Sim |
| `PowerShell` | Executa comandos PowerShell nativamente (Windows) | Sim |
| `Monitor` | Roda um comando em background e devolve cada linha de saída ao Claude, para ele reagir a logs, mudanças de arquivo ou status. Também abre WebSocket e trata cada mensagem como evento | Sim |

## Web

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `WebFetch` | Busca o conteúdo de uma URL | Sim |
| `WebSearch` | Faz buscas na web | Sim |

## Agentes e orquestração

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `Agent` | Cria um subagent com contexto próprio para uma tarefa. Com *agent teams*, uma chamada com `name` pode lançar um teammate | Não |
| `Workflow` | Roda um *dynamic workflow*: um script que orquestra muitos subagents em background e devolve um resultado consolidado | Sim |
| `SendMessage` | Envia mensagem para outro agente: teammate, subagent retomado, ou outra sessão sua (local, web ou Remote Control) | Não |
| `ListAgents` | Lista os agentes que o Claude pode mensagear com `SendMessage`. Sustenta o `/list-agents` | Não |
| `Skill` | Executa uma skill dentro da conversa principal | Sim |

## Planejamento e worktrees

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `EnterPlanMode` | Entra em plan mode para desenhar a abordagem antes de codar | Não |
| `ExitPlanMode` | Apresenta o plano para aprovação e sai do plan mode | Sim |
| `EnterWorktree` | Cria um git worktree isolado e entra nele (ou entra em um existente por `path`) | Sim |
| `ExitWorktree` | Sai do worktree e volta ao diretório original | Não |

## Tarefas e agendamento

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `TaskCreate` | Cria uma tarefa na lista | Não |
| `TaskGet` | Detalhes de uma tarefa | Não |
| `TaskList` | Lista todas as tarefas com status | Não |
| `TaskUpdate` | Atualiza status, dependências, detalhes ou apaga tarefas | Não |
| `TaskOutput` | Saída de uma tarefa em background (**depreciada** em favor de `Read` no arquivo de saída) | Não |
| `TaskStop` | Para uma tarefa em background por ID (também aceita teammate ou agente nomeado) | Não |
| `TodoWrite` | Checklist da sessão. Desabilitada por padrão em favor das tools `Task*`; reative com `CLAUDE_CODE_ENABLE_TASKS=0` | Não |
| `CronCreate` | Agenda um prompt recorrente ou único dentro da sessão | Não |
| `CronDelete` | Cancela uma tarefa agendada por ID | Não |
| `CronList` | Lista as tarefas agendadas da sessão | Não |
| `ScheduleWakeup` | Reagenda a próxima iteração de um `/loop` auto-pautado (entre 1 minuto e 1 hora) | Não |

## MCP

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `ToolSearch` | Busca e carrega tools deferidas quando o *tool search* está ligado | Não |
| `ListMcpResourcesTool` | Lista recursos expostos por servidores MCP conectados | Não |
| `ReadMcpResourceTool` | Lê um recurso MCP específico por URI | Não |
| `WaitForMcpServers` | Espera servidores MCP que ainda estão conectando (só aparece com tool search desligado) | Não |

## Interação com você

| Tool | Descrição | Permissão |
| --- | --- | --- |
| `AskUserQuestion` | Faz perguntas de múltipla escolha para levantar requisitos ou resolver ambiguidade | Não |
| `PushNotification` | Manda notificação de desktop, e push no celular quando o Remote Control está conectado | Não |
| `SendUserFile` | Envia arquivos da sessão para você, com legenda opcional | Não |
| `Artifact` | Publica um HTML/Markdown como *artifact*: página interativa e privada no claude.ai | Sim |
| `ShareOnboardingGuide` | Sobe o `ONBOARDING.md` e devolve um link para colegas (usado pelo `/team-onboarding`) | Sim |
| `ReportFindings` | Reporta achados de code review como lista estruturada (arquivo, resumo, cenário de falha) | Não |
| `RemoteTrigger` | Cria, atualiza, roda e lista *Routines* no claude.ai. Sustenta o `/schedule` | Não |
| `EndConversation` | Encerra a sessão, em casos raros de abuso sustentado (v2.1.213+) | Não |

## Regras de permissão por tool

| Formato da regra | Vale para | Detalhe |
| --- | --- | --- |
| `Bash(npm run *)` | `Bash`, `Monitor` | Casamento por padrão de comando |
| `PowerShell(Get-ChildItem *)` | `PowerShell` | Casamento por padrão de comando |
| `Read(~/secrets/**)` | `Read`, `Grep`, `Glob`, `LSP` | Casamento por padrão de caminho |
| `Edit(/src/**)` | `Edit`, `Write`, `NotebookEdit` | Casamento por padrão de caminho |
| `Skill(deploy *)` | `Skill` | Casamento por nome de skill |
| `Agent(Explore)` | `Agent` | Casamento por tipo de subagent |
| `WebFetch(domain:example.com)` | `WebFetch` | Casamento por domínio |
| `WebSearch` | `WebSearch` | Sem especificador: libera ou nega a tool inteira |

## Limites do `Bash`

| Resultado | O que o Claude recebe |
| --- | --- |
| Sucesso | Inline até ~30.000 caracteres; acima disso, o caminho de um arquivo salvo no diretório da sessão (truncado acima de 64 MiB) mais uma prévia do início |
| Falha | Inline até ~10.000 caracteres; acima disso, um trecho de início e fim, sem caminho de arquivo |

## Adicionar tools novas

- **Tool de verdade** → conecte um [servidor MCP](funcionalidades.md#mcp--model-context-protocol).
- **Workflow reutilizável baseado em prompt** → escreva uma [skill](funcionalidades.md#skills), que roda pela tool `Skill` em vez de virar uma entrada nova.

Para ver o que está ativo na sua sessão: `/status`.
