---
title: Cheatsheet
nav_order: 2
---

# Cheatsheet — uma página

[← Voltar ao índice](index.md)

## Teclas essenciais

| Tecla | Ação |
| --- | --- |
| `Shift+Tab` | Circula os modos de permissão (inclui **plan mode**) |
| `Esc` | Interrompe o Claude |
| `Esc` `Esc` | Rewind: volta código e conversa a um checkpoint |
| `Ctrl+O` | Transcript viewer |
| `Ctrl+B` | Joga a tarefa em execução para background |
| `Ctrl+R` | Busca no histórico de prompts |
| `Ctrl+S` | Guarda/restaura o rascunho do prompt |
| `Option+P` / `Alt+P` | Troca de modelo |
| `Option+T` / `Alt+T` | Liga/desliga extended thinking |
| `Option+O` / `Alt+O` | Liga/desliga fast mode |
| `\` + `Enter` | Nova linha no prompt |
| `?` (input vazio) | Painel de atalhos |

## Prefixos do prompt

| Prefixo | Efeito |
| --- | --- |
| `/` | Comando ou skill |
| `!` | Modo shell (roda o comando, saída vira contexto) |
| `@` | Menciona arquivo/diretório |
| `:` | Emoji shortcode |

## Os 15 comandos que resolvem 90% dos dias

| Comando | Uso |
| --- | --- |
| `/plan` | Planejar antes de editar |
| `/rewind` | Desfazer código + conversa |
| `/code-review` | Revisar o diff atual |
| `/simplify` | Limpar o diff antes do PR |
| `/context` | Ver o que enche a janela de contexto |
| `/compact` | Resumir a conversa e liberar contexto |
| `/clear` | Conversa nova (a antiga fica em `/resume`) |
| `/resume` | Voltar a uma conversa anterior |
| `/btw` | Pergunta lateral sem poluir o contexto |
| `/effort` | `low` mecânico ↔ `max` bug difícil |
| `/permissions` | Regras allow/ask/deny |
| `/hooks` | Automação por evento |
| `/memory` | Editar CLAUDE.md e auto memory |
| `/usage` | O que está consumindo o limite |
| `/doctor` | Config não aplicou? Comece aqui |

## Terminal

```bash
claude -c            # continua a última conversa daqui
claude -p "pergunta" # headless: responde e sai
claude --worktree    # sessão em worktree isolado
claude doctor        # diagnóstico da instalação
```

## Onde cada coisa mora

| O quê | Onde |
| --- | --- |
| Instruções do projeto | `CLAUDE.md` |
| Settings do time | `.claude/settings.json` |
| Settings só seus | `.claude/settings.local.json` (gitignored) |
| Skills / comandos | `.claude/skills/<nome>/SKILL.md` |
| Subagents | `.claude/agents/<nome>.md` |
| Globais (todos os projetos) | os mesmos, sob `~/.claude/` |
