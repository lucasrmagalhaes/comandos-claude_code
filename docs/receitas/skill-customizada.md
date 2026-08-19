---
title: Skill customizada
parent: Receitas
---

# Receita: skill customizada do zero

Uma skill é um `/comando` seu: um arquivo de instruções que o Claude executa quando você digita `/nome` — ou sozinho, quando o pedido bate com a descrição.

## 1. Crie o arquivo

Projeto: `.claude/skills/<nome>/SKILL.md`. Pessoal (todos os projetos): `~/.claude/skills/<nome>/SKILL.md`.

```markdown
---
description: Gera migration + model + teste para uma nova tabela, no padrão do projeto.
argument-hint: [nome-da-tabela]
disable-model-invocation: true
---

Crie a estrutura completa para a tabela $1:

1. Migration em database/migrations/ seguindo o padrão das existentes
2. Model com fillables e casts
3. Teste de feature cobrindo o CRUD

Antes de escrever, leia duas migrations recentes para copiar o estilo.
```

## 2. Os campos que importam

| Campo | Efeito |
| --- | --- |
| `description` | Como o Claude decide **quando** usar a skill sozinho. Capriche nos gatilhos |
| `disable-model-invocation: true` | Só você dispara (via `/nome`). Use para ações com efeito colateral |
| `user-invocable: false` | O oposto: só o Claude dispara; some do menu `/` |
| `argument-hint` | Dica de autocomplete: `[issue] [formato]` |
| `allowed-tools` | Tools liberadas sem prompt **durante o turno da skill** |
| `context: fork` | Roda em subagent isolado (não polui seu contexto) |
| `paths` | Globs que restringem quando a skill carrega automaticamente |
| `model` / `effort` | Sobrescrevem modelo/esforço enquanto a skill está ativa |

## 3. Substituições no corpo

| Sintaxe | Vira |
| --- | --- |
| `$1`, `$2`, … | Argumentos posicionais |
| `$ARGUMENTS` | Tudo que veio depois de `/nome` |
| `` !`comando` `` | Roda o shell **antes** e injeta a saída |
| `@caminho/arquivo` | Injeta o conteúdo do arquivo |

## 4. Teste

Digite `/nome` e confira o menu. A skill não aparece? `/reload-skills` re-escaneia o disco (em versões antigas, reinicie a sessão). Corpo carregado errado? O corpo **só entra no contexto quando invocada** — descrição ruim = skill nunca usada; teste pedir a tarefa com outras palavras e veja se o Claude a puxa.

## Erros comuns

- **Descrição vaga** ("ajuda com testes") — o Claude nunca vai escolhê-la sozinho. Descreva gatilho e resultado.
- **Skill fazendo papel de CLAUDE.md** — fato permanente do projeto vai no `CLAUDE.md`; procedimento sob demanda vai em skill. A skill custa contexto só quando usada; é essa a vantagem.
- **Esquecer `disable-model-invocation`** em skill destrutiva (deploy, limpeza de banco) — o Claude pode invocá-la sozinho.
