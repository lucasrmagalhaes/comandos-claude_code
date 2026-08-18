# Comandos de barra (`/`)

[← Voltar ao índice](index.md)

Digite `/` no início do prompt para abrir o menu de comandos e skills. `/help` lista o que está disponível na **sua** sessão (o conjunto varia por plano, plataforma e plugins instalados).

---

## Sessão e conversa

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/clear [nome]` | `/reset`, `/new` | Começa uma conversa nova com contexto vazio; a anterior fica em disco e pode ser retomada com `/resume` |
| `/resume [nome]` | `/continue` | Volta para uma conversa anterior |
| `/rewind [checkpoint]` | `/checkpoint`, `/undo` | Restaura código e/ou conversa para um ponto anterior |
| `/branch [nome]` | `/fork` | Cria um *branch* da conversa neste ponto |
| `/fork [prompt]` | — | Copia a conversa atual para uma nova sessão em background |
| `/background [prompt]` | `/bg` | Continua a sessão em background e libera o terminal |
| `/stop` | — | Para esta sessão em background (transcript e worktree são mantidos) |
| `/rename [nome]` | `/name` | Renomeia a conversa atual |
| `/export [arquivo]` | — | Exporta a conversa para arquivo ou clipboard |
| `/copy [N]` | — | Copia a última resposta do Claude (ou a N-ésima mais recente) |
| `/compact [instruções]` | — | Libera contexto resumindo a conversa até aqui |
| `/autocompact [auto\|<tokens>]` | — | Configura o tamanho da janela de auto-compact |
| `/context [all]` | — | Visualiza o uso do contexto como uma grade colorida |
| `/recap` | — | Gera um resumo de uma linha da sessão |
| `/diff` | — | Visualizador interativo de mudanças não commitadas e diffs por turno |
| `/focus` | — | Alterna a visão focada (só o seu prompt, resumo de tools e resposta final) |
| `/btw <pergunta>` | — | Pergunta paralela sem sujar a conversa principal |
| `/goal [condição \| clear]` | — | Define um objetivo — o Claude continua até a condição ser satisfeita |
| `/cd <path>` | — | Move a sessão para outro diretório de trabalho |
| `/add-dir <path>` | — | Adiciona um diretório de trabalho ao acesso da sessão |
| `/brief` | — | Alterna o modo *brief-only* |

## Onde a sessão roda

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/teleport` | `/tp` | Puxa uma sessão da web para este terminal |
| `/web` | — | Continua a sessão atual no claude.ai/code |
| `/desktop` | `/app` | Continua a sessão atual no Claude Code Desktop |
| `/mobile` | `/ios`, `/android` | Mostra QR code para baixar o app mobile |
| `/remote-control [nome]` | `/rc` | Conecta este terminal para sessões de Remote Control |
| `/session` | `/remote` | Mostra a URL e o QR code da sessão remota |
| `/remote-env` | — | Configura o ambiente remoto padrão para sessões de *teleport* |
| `/web-setup` | — | Configura o Claude Code na web (requer conectar a conta GitHub) |
| `/daemon` | — | Gerencia serviços em background: assistants, tarefas agendadas e remote control |

## Modelo, esforço e planejamento

| Comando | Descrição |
| --- | --- |
| `/model [modelo]` | Troca o modelo e salva como padrão |
| `/effort [low\|medium\|high\|xhigh\|max\|auto]` | Define o nível de esforço de raciocínio |
| `/fast [on\|off]` | Liga/desliga o *fast mode* (Opus com saída mais rápida — não rebaixa o modelo) |
| `/advisor [modelo\|off]` | Liga/desliga a *advisor tool*, que consulta um segundo modelo em momentos-chave |
| `/plan [descrição]` | Entra em plan mode direto do prompt, ou mostra o plano da sessão |
| `/ultraplan <prompt>` | O Claude Code na web rascunha um plano que você edita e aprova |

## Agentes, tarefas e paralelismo

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/agents` | — | Gerencia configurações de subagents |
| `/subtask <instrução>` | — | Entrega uma tarefa lateral a um subagent que reporta de volta |
| `/list-agents` | `/peers` | Lista os subagents e outras sessões do Claude Code que o Claude pode mensagear |
| `/tasks` | `/bashes` | Lista e gerencia as tarefas em background da sessão |
| `/loops` | — | Lista, cria e apaga *loops* recorrentes e stop-hooks |
| `/loop [intervalo] [prompt]` | `/proactive` | Roda um prompt repetidamente enquanto a sessão estiver aberta |

## Código, revisão e Git

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/init` | — | Inicializa o `CLAUDE.md` com documentação do codebase |
| `/init-verifiers` | — | Cria skill(s) de verificação automática de mudanças de código |
| `/commit` | — | Cria um commit git |
| `/commit-push-pr` | — | Commit, push e abre um PR |
| `/code-review [nível] [--fix] [--comment] [pr#\|branch\|path]` | `/review` | Revisa diff ou PR buscando bugs de correção e limpezas. Níveis: `low`, `medium`, `high`, `xhigh`, `max`, `ultra` |
| `/security-review [--fix] [--comment] [path]` | — | Procura vulnerabilidades de segurança no diff |
| `/simplify [--fix] [path]` | — | Revisa o código alterado por reuso, qualidade e eficiência, e corrige |
| `/verify` | — | Verifica uma solução no codebase |
| `/autofix-pr [prompt]` | — | Dispara uma sessão na web que monitora e corrige o PR do branch atual |
| `/ultrareview [target]` | — | Revisão multi-agente profunda na nuvem, que encontra **e verifica** bugs antes do merge |
| `/batch <instrução>` | — | Planeja uma mudança em larga escala e executa em paralelo em 5–30 worktrees isolados, cada um abrindo um PR |
| `/debug [descrição]` | — | Liga logging de debug da sessão e ajuda a diagnosticar problemas |
| `/design-sync [dica]` | — | Converte o design system React do repo e envia para o Claude Design |
| `/design-login` | — | Autoriza o acesso ao design system para o `/design-sync` |

## Configuração e permissões

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/config [chave=valor ...]` | `/settings` | Abre o painel de configuração, ou seta valores direto |
| `/permissions` | `/allowed-tools` | Gerencia regras de allow, ask e deny de tools |
| `/hooks` | — | Vê as configurações de hooks por evento de tool |
| `/memory` | — | Edita os arquivos `CLAUDE.md` e gerencia a auto memory |
| `/toggle-memory` | — | Liga/desliga a auto memory nesta sessão |
| `/keybindings` | — | Abre (ou cria) o arquivo de atalhos de teclado |
| `/theme [tema\|default]` | — | Troca o tema de cores |
| `/color [cor\|default]` | — | Define a cor da barra de prompt da sessão |
| `/statusline` | — | Configura a status line (barra de status customizada) |
| `/sandbox` | — | Estado e configuração do Bash sandboxed |
| `/terminal-setup` | — | Ajusta o terminal (ex.: `Option+Enter` para nova linha, bell visual) |
| `/tui [default\|fullscreen]` | — | Define o renderizador da interface de terminal |
| `/privacy-settings` | — | Vê e atualiza as configurações de privacidade |
| `/voice [hold\|tap\|off]` | — | Alterna o modo de ditado por voz |
| `/setup-bedrock` | — | Reconfigura autenticação, região ou pins de modelo do Amazon Bedrock |
| `/setup-vertex` | — | Reconfigura autenticação, projeto, região ou pins de modelo do Google Cloud |
| `/fewer-permission-prompts` | — | Varre os transcripts e propõe uma allowlist no `settings.json` para reduzir prompts de permissão |

## Extensões

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/mcp [reconnect <s>\|enable\|disable [<s>\|all]]` | — | Gerencia conexões e OAuth de servidores MCP |
| `/plugin [subcomando]` | `/plugins`, `/marketplace` | Gerencia plugins e marketplaces |
| `/reload-plugins [--force]` | — | Ativa mudanças pendentes de plugin na sessão atual |
| `/skills` | — | Lista as skills disponíveis |
| `/chrome` | — | Configurações do Claude in Chrome |
| `/ide [open]` | — | Gerencia integrações de IDE e mostra o status |
| `/install-github-app` | — | Instala o Claude GitHub App / configura o GitHub Actions |
| `/install-slack-app` | — | Instala o app do Claude no Slack |

## Conta, uso e ajuda

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/help` | — | Ajuda e comandos disponíveis |
| `/status` | — | Status da sessão: versão, modelo, conta, conectividade de API, tools |
| `/usage` | `/cost`, `/stats` | Custo da sessão, uso do plano e estatísticas de atividade |
| `/whoami` | — | Mostra o nome da conta logada |
| `/login` | — | Entra na conta Anthropic (ou troca de conta) |
| `/logout` | — | Sai da conta |
| `/doctor` | `/checkup` | Checkup de instalação e settings, com correções |
| `/version` | — | Versão que a sessão está rodando (não a que o autoupdate baixou) |
| `/update` | — | Troca para a última versão (a conversa continua) |
| `/install [opções]` | — | Instala o build nativo do Claude Code |
| `/upgrade` | — | Upgrade para o Max (mais limites e mais Opus) |
| `/extra-usage` | — | Configura uso extra para continuar trabalhando ao bater o limite |
| `/passes` | — | Compartilha uma semana grátis de Claude Code com amigos |
| `/release-notes` | — | Changelog em um seletor interativo de versões |
| `/feedback [relato]` | `/bug` | Envia feedback sobre o Claude Code |
| `/exit` | `/quit` | Sai da CLI |

## Aprendizado e extras

| Comando | Aliases | Descrição |
| --- | --- | --- |
| `/powerup` | — | Descobre funcionalidades do Claude Code em lições interativas rápidas |
| `/insights` | — | Gera um relatório HTML analisando suas sessões recentes |
| `/team-onboarding` | — | Monta um guia para colegas embarcarem no Claude Code a partir do seu uso |
| `/dream` | `/learn` | Consolidação reflexiva de memória: revisa a atividade recente, sintetiza aprendizados em arquivos de memória e poda entradas obsoletas |
| `/claude-api [migrate\|managed-agents-onboard\|prompt-audit]` | — | Carrega material de referência da Claude API e Managed Agents |
| `/dataviz [pedido]` | — | Orientação de design para gráficos, dashboards e visualizações |
| `/deep-research <pergunta>` | — | **[Workflow]** Dispara buscas na web em paralelo, cruza fontes e sintetiza um relatório com citações |
| `/schedule` | — | Cria/atualiza/lista *routines* (agentes na nuvem em cron) |
| `/radio` | — | Abre a rádio lo-fi Claude FM |
| `/stickers` | — | Pede adesivos do Claude Code |

## Skills bundladas × comandos embutidos

Duas famílias convivem no mesmo menu `/`:

- **Comandos embutidos** — implementados dentro da CLI (`/clear`, `/model`, `/config`, `/usage`, …). Executam ação local imediata.
- **Skills bundladas** — prompts/procedimentos empacotados que o modelo executa (`/code-review`, `/simplify`, `/debug`, `/loop`, `/batch`, `/dataviz`, `/deep-research`, `/verify`, `/fewer-permission-prompts`, `/claude-api`, `/design-sync`). Podem ser invocadas por você **ou** carregadas pelo próprio Claude quando forem relevantes.

## Comandos customizados

> **Comandos customizados foram unificados com skills.** Um arquivo em `.claude/commands/deploy.md` e uma skill em `.claude/skills/deploy/SKILL.md` produzem os dois o comando `/deploy`. Os arquivos existentes em `.claude/commands/` continuam funcionando.

Skills adicionam recursos que o formato antigo não tinha: um diretório para arquivos de apoio, frontmatter para controlar quem invoca (você ou o Claude), e carregamento sob demanda — o corpo só entra no contexto quando é usado.

| Escopo | Caminho |
| --- | --- |
| Projeto | `.claude/skills/<nome>/SKILL.md` ou `.claude/commands/<nome>.md` |
| Usuário | `~/.claude/skills/<nome>/SKILL.md` ou `~/.claude/commands/<nome>.md` |
| Plugin | `<plugin>/skills/<nome>/SKILL.md` |

Recursos dentro de um comando/skill:

| Recurso | Sintaxe |
| --- | --- |
| Argumentos posicionais | `$1`, `$2`, … |
| Todos os argumentos | `$ARGUMENTS` |
| Executar shell antes | linha iniciada com `!` |
| Referenciar arquivo | `@caminho/arquivo` |

## Comandos de MCP

Servidores MCP podem expor *prompts* como comandos, no formato:

```
/mcp__<servidor>__<prompt> [argumentos]
```

---

## Extras encontrados no binário instalado (`2.1.136`)

Comandos presentes no binário local que **não** aparecem na tabela pública de referência — alguns são internos, ocultos ou dependem de flags/plano:

| Comando | Natureza |
| --- | --- |
| `/pro-trial-expired`, `/rate-limit-options` | Telas internas (aparecem sozinhas quando o caso ocorre) |
| `/bridge-kick` | Diagnóstico interno: injeta falhas de bridge para testar recuperação |
| `/heapdump` | Diagnóstico: escreve um snapshot do heap JS em `~/Desktop` |
| `/stub` | Placeholder interno, não invocável |

E o inverso também vale: comandos documentados como `/cd`, `/whoami`, `/web`, `/subtask`, `/list-agents`, `/verify`, `/design-login` e `/design-sync` **não existem** na 2.1.136 — chegaram em versões posteriores. Rode `claude update` e confira com `/help`.
