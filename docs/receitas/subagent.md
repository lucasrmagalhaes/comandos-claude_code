---
title: Subagent
parent: Receitas
---

# Receita: subagent especializado

Subagent = um Claude com contexto **próprio**, prompt próprio e ferramentas restritas, que o principal chama para delegar. Bom para: revisão isolada, exploração de código que sujaria seu contexto, tarefas paralelas.

## 1. Crie o arquivo

Projeto: `.claude/agents/<nome>.md`. Pessoal: `~/.claude/agents/<nome>.md`.

```markdown
---
name: revisor-de-migrations
description: Revisa migrations de banco antes do merge. Use quando houver migration nova ou alterada no diff.
tools: Read, Grep, Glob, Bash
model: inherit
memory: project
---

Você revisa migrations Laravel deste projeto. Para cada migration no diff:

1. Cheque reversibilidade (down() correto)
2. Cheque índices para colunas de busca/FK
3. Compare com o padrão das migrations existentes
4. Aponte locks perigosos em tabelas grandes

Responda com uma lista objetiva de problemas, ou "aprovada".
```

## 2. Os campos que importam

| Campo | Efeito |
| --- | --- |
| `name` | Identificador (minúsculas e hífens). Hooks recebem como `agent_type` |
| `description` | Como o principal decide **quando** delegar — mesmo princípio da skill |
| `tools` | Allowlist de tools. Omitiu = herda tudo. Revisor não precisa de `Edit` |
| `model` | `inherit` (padrão), `haiku` para tarefas mecânicas baratas, etc. |
| `memory` | `user`/`project`/`local` — o subagent **aprende entre sessões** |
| `isolation: worktree` | Roda numa cópia isolada do repo (para subagents que editam em paralelo) |
| `maxTurns` | Teto de turnos — bom freio para subagent autônomo |
| `skills` | Skills pré-carregadas no contexto dele (conteúdo inteiro, não só descrição) |

## 3. Use

Peça naturalmente ("revisa as migrations desse diff") ou explicitamente ("usa o revisor-de-migrations"). Subagents rodam em background por padrão; o resultado volta como notificação. `/agents` gerencia os configurados.

## Erros comuns

- **Subagent para tudo** — cada um começa de contexto zero: para pergunta pontual, o principal resolve mais rápido e mais barato. Delegue o que é volumoso ou isolável.
- **Dar `Edit` a um revisor** — restrinja `tools`; revisor que edita vira autor.
- **Esperar que ele veja sua conversa** — não vê. O prompt de delegação precisa ser autossuficiente.
