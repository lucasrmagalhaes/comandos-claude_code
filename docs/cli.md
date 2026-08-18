# CLI — comandos e flags de terminal

[← Voltar ao índice](index.md)

Uso básico:

```bash
claude [options] [command] [prompt]
```

Sem argumentos, abre uma sessão interativa. Com `-p/--print`, roda de forma não interativa e sai (bom para pipes e scripts).

## Formas de invocação

| Comando | O que faz |
| --- | --- |
| `claude` | Abre sessão interativa |
| `claude "pergunta"` | Sessão interativa já com o primeiro prompt |
| `claude -p "pergunta"` | Roda headless, imprime a resposta e sai |
| `cat arquivo \| claude -p "pergunta"` | Processa conteúdo vindo do pipe |
| `claude -c` | Continua a conversa mais recente do diretório atual |
| `claude -c -p "pergunta"` | Continua a conversa em modo headless |
| `claude -r "<sessão>" "pergunta"` | Retoma sessão por ID ou nome |

## Subcomandos

| Subcomando | Descrição |
| --- | --- |
| `claude agents` | Abre a *agent view* para monitorar e disparar sessões paralelas em background |
| `claude attach <id>` | Anexa uma sessão em background a este terminal |
| `claude auth login` | Faz login na conta Anthropic |
| `claude auth logout` | Faz logout |
| `claude auth status` | Mostra o status de autenticação (JSON) |
| `claude auto-mode config` | Imprime a configuração efetiva do classificador do auto mode |
| `claude auto-mode critique` | Pede feedback de IA sobre suas regras customizadas de auto mode |
| `claude auto-mode defaults` | Imprime as regras padrão (environment, allow, soft_deny, hard_deny) |
| `claude auto-mode reset` | Restaura a configuração padrão do auto mode |
| `claude daemon status` | Estado do supervisor de sessões em background |
| `claude daemon stop --any` | Para o supervisor e as sessões que ele hospeda |
| `claude doctor` | Diagnóstico read-only de instalação e settings |
| `claude gateway` | Sobe o servidor do *Claude apps gateway* self-hosted |
| `claude import [codex\|gemini]` | Sessão interativa que roda `/import` para trazer config de outros agentes |
| `claude install [target]` | Instala/reinstala o binário nativo (`stable`, `latest` ou versão específica) |
| `claude logs <id>` | Imprime a saída recente de uma sessão em background |
| `claude mcp` | Configura servidores MCP (ver subtabela abaixo) |
| `claude plugin` | Gerencia plugins (ver subtabela abaixo) |
| `claude project purge [path]` | Apaga todo o estado local do projeto (transcripts, tasks, histórico de arquivos) |
| `claude remote-control` | Sobe o servidor de Remote Control para controlar a partir do claude.ai / app |
| `claude respawn <id>` | Reinicia uma sessão em background mantendo a conversa |
| `claude rm <id>` | Remove uma sessão em background da lista |
| `claude self-hosted-runner` | Registra esta máquina/container em um *self-hosted environment* |
| `claude setup-token` | Gera um token OAuth de longa duração para CI e scripts |
| `claude stop <id>` | Para uma sessão em background |
| `claude ultrareview [target]` | Roda o *ultrareview* de forma não interativa |
| `claude update` / `claude upgrade` | Verifica e instala atualizações |

### `claude mcp`

| Comando | Descrição |
| --- | --- |
| `claude mcp add [opts] <nome> <cmdOuUrl> [args...]` | Adiciona um servidor MCP |
| `claude mcp add-json <nome> <json>` | Adiciona um servidor por string JSON |
| `claude mcp add-from-claude-desktop` | Importa servidores do Claude Desktop (macOS e WSL) |
| `claude mcp get <nome>` | Detalhes de um servidor |
| `claude mcp list` | Lista os servidores configurados |
| `claude mcp login <nome>` | Roda o fluxo OAuth do servidor pela linha de comando |
| `claude mcp logout <nome>` | Limpa credenciais OAuth armazenadas |
| `claude mcp remove <nome>` | Remove um servidor |
| `claude mcp reset-project-choices` | Reseta aprovações/rejeições de servidores em `.mcp.json` |
| `claude mcp serve` | Sobe o próprio Claude Code como servidor MCP |

Exemplos:

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

```bash
claude mcp add -e API_KEY=xxx meu-server -- npx meu-mcp-server
```

### `claude plugin` (alias `claude plugins`)

| Comando | Descrição |
| --- | --- |
| `claude plugin install\|i <plugin>` | Instala de um marketplace (`plugin@marketplace` para escolher a origem) |
| `claude plugin uninstall\|remove <plugin>` | Desinstala |
| `claude plugin list` | Lista os plugins instalados |
| `claude plugin enable <plugin>` | Habilita um plugin desabilitado |
| `claude plugin disable [plugin]` | Desabilita um plugin |
| `claude plugin update <plugin>` | Atualiza (exige reiniciar para aplicar) |
| `claude plugin marketplace` | Gerencia marketplaces |
| `claude plugin prune` / `autoremove` | Remove dependências auto-instaladas que não são mais necessárias |
| `claude plugin tag [path]` | Cria a tag `{nome}--v{versão}` validando `plugin.json` e o marketplace |
| `claude plugin validate <path>` | Valida um manifesto de plugin ou marketplace |

## Flags

### Sessão e conversa

| Flag | Descrição |
| --- | --- |
| `-c`, `--continue` | Carrega a conversa mais recente do diretório atual |
| `-r`, `--resume [valor]` | Retoma uma conversa por ID/nome, ou abre o seletor interativo |
| `--fork-session` | Ao retomar, cria um novo ID em vez de reutilizar o original |
| `--from-pr [valor]` | Retoma sessão ligada a um PR (número/URL) ou abre o seletor |
| `--session-id <uuid>` | Usa um ID de sessão específico |
| `-n`, `--name <nome>` | Define o nome de exibição da sessão |
| `--no-session-persistence` | Não salva a sessão em disco (só com `--print`) |
| `--teleport` | Traz uma sessão da web para o terminal local |
| `--cloud` | Cria (ou aponta para) uma sessão web no claude.ai |
| `--bg`, `--background` | Inicia como agente em background e retorna imediatamente |
| `--remote-control`, `--rc [nome]` | Inicia sessão interativa com Remote Control ligado |
| `--remote-control-session-name-prefix <prefixo>` | Prefixo dos nomes gerados de sessões de Remote Control |

### Modelo e raciocínio

| Flag | Descrição |
| --- | --- |
| `--model <modelo>` | Modelo da sessão (alias como `opus`/`sonnet` ou nome completo) |
| `--fallback-model <modelo>` | Fallback automático quando o modelo principal está sobrecarregado (só com `--print`) |
| `--effort <nível>` | Nível de esforço: `low`, `medium`, `high`, `xhigh`, `max` |
| `--advisor <modelo>` | Liga a *advisor tool* (consulta um modelo mais forte em momentos-chave) |
| `--autocompact <auto\|tokens>` | Define a janela de auto-compact da sessão |
| `--betas <betas...>` | Headers beta nas requisições (somente usuários de API key) |
| `--max-budget-usd <valor>` | Teto de gasto em dólares (só com `--print`) |
| `--max-turns <n>` | Limita o número de turnos agênticos |

### Permissões e segurança

| Flag | Descrição |
| --- | --- |
| `--permission-mode <modo>` | `default`, `acceptEdits`, `auto`, `dontAsk`, `plan`, `bypassPermissions` |
| `--allowedTools`, `--allowed-tools <tools...>` | Tools que executam sem pedir permissão |
| `--disallowedTools`, `--disallowed-tools <tools...>` | Regras de negação de tools |
| `--tools <tools...>` | Restringe o conjunto de tools embutidas (`""` desliga tudo, `default` liga tudo) |
| `--dangerously-skip-permissions` | Ignora todas as checagens de permissão (só em sandbox sem internet) |
| `--allow-dangerously-skip-permissions` | Adiciona `bypassPermissions` ao ciclo do `Shift+Tab` sem iniciar nele |
| `--permission-prompt-tool <tool>` | Tool MCP que responde aos prompts de permissão em modo não interativo |
| `--safe-mode` | Sobe com todas as customizações desligadas (para depurar config quebrada) |

### Contexto e diretórios

| Flag | Descrição |
| --- | --- |
| `--add-dir <dirs...>` | Diretórios adicionais liberados para leitura/escrita |
| `-w`, `--worktree [nome]` | Cria/reutiliza um git worktree para a sessão |
| `--tmux` | Cria sessão tmux para o worktree (requer `--worktree`) |
| `--bare` | Modo mínimo: pula hooks, LSP, plugins, auto memory, CLAUDE.md, keychain |
| `--exclude-dynamic-system-prompt-sections` | Move seções por-máquina do system prompt para a primeira mensagem (melhora reuso de cache) |

### Prompt do sistema e agentes

| Flag | Descrição |
| --- | --- |
| `--system-prompt <texto>` | Substitui o system prompt inteiro |
| `--system-prompt-file <path>` | Idem, a partir de um arquivo |
| `--append-system-prompt <texto>` | Anexa texto ao system prompt padrão |
| `--append-system-prompt-file <path>` | Idem, a partir de um arquivo |
| `--append-subagent-system-prompt <texto>` | Anexa texto ao system prompt de todo subagent |
| `--agent <agent>` | Agente da sessão |
| `--agents <json>` | Define subagents customizados via JSON |
| `--forward-subagent-text` | Emite texto e thinking dos subagents no stream |

### Extensões

| Flag | Descrição |
| --- | --- |
| `--mcp-config <configs...>` | Carrega servidores MCP de arquivos/strings JSON |
| `--strict-mcp-config` | Usa **somente** os servidores de `--mcp-config` |
| `--plugin-dir <path>` | Carrega plugin de diretório ou `.zip` só nesta sessão (repetível) |
| `--plugin-url <url>` | Busca plugin `.zip` de uma URL só nesta sessão (repetível) |
| `--disable-slash-commands` | Desabilita todas as skills/comandos |
| `--settings <arquivo-ou-json>` | Settings adicionais (caminho ou JSON inline) |
| `--setting-sources <fontes>` | Fontes de settings a carregar: `user,project,local` |
| `--channels` | (research preview) Servidores MCP cujas notificações de canal o Claude deve ouvir |
| `--chrome` / `--no-chrome` | Liga/desliga a integração Claude in Chrome |
| `--ide` | Conecta automaticamente à IDE se houver exatamente uma válida |

### Entrada, saída e automação

| Flag | Descrição |
| --- | --- |
| `-p`, `--print` | Imprime a resposta e sai (não interativo) |
| `--output-format <formato>` | `text`, `json` ou `stream-json` (só com `--print`) |
| `--input-format <formato>` | `text` ou `stream-json` (só com `--print`) |
| `--include-partial-messages` | Inclui chunks parciais conforme chegam |
| `--include-hook-events` | Inclui eventos de ciclo de vida de hooks no stream |
| `--replay-user-messages` | Reemite as mensagens do usuário no stdout para confirmação |
| `--json-schema <schema>` | Valida a saída estruturada contra um JSON Schema |
| `--prompt-suggestions` | Emite `prompt_suggestion` com o próximo prompt previsto a cada turno |
| `--file <specs...>` | Baixa recursos no startup no formato `file_id:caminho` |
| `--exec` | Roda um comando shell como job PTY em background em vez de abrir sessão |
| `--init` | Roda hooks `Setup` com matcher `init` antes da sessão |
| `--init-only` | Roda `Setup` e `SessionStart` e sai sem conversar |
| `--maintenance` | Roda hooks `Setup` com matcher `maintenance` |

### Ambiente e depuração

| Flag | Descrição |
| --- | --- |
| `-d`, `--debug [filtro]` | Modo debug com filtro por categoria (ex.: `api,hooks` ou `!1p,!file`) |
| `--debug-file <path>` | Escreve logs de debug em um arquivo |
| `--verbose` | Sobrescreve o modo verbose das settings |
| `-v`, `--version` | Imprime a versão |
| `-h`, `--help` | Ajuda |
| `--environment <id>` | Cria sessão cloud em um *self-hosted environment* |
| `--ref <branch>` | Com `--environment`, base do checkout da sessão |
| `--ax-screen-reader` | Saída amigável a leitor de tela (texto plano, sem bordas/animações) |
| `--teammate-mode` | Como os teammates de *agent team* aparecem |
| `--dangerously-load-development-channels` | Habilita canais fora da allowlist (desenvolvimento local) |

> **Removida**: `--enable-auto-mode` foi removida na v2.1.111 (auto mode virou padrão).
