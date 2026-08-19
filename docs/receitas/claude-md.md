---
title: CLAUDE.md
parent: Receitas
---

# Receita: CLAUDE.md que funciona

O `CLAUDE.md` é lido em **toda** sessão. Cada linha custa contexto em todas as conversas para sempre — o critério é implacável: só entra o que muda o comportamento do Claude na maioria das sessões.

## O que pôr

| Categoria | Exemplo |
| --- | --- |
| Comandos do projeto | "Testes: `docker exec app php artisan test`. Nunca rode `php` direto no host" |
| Convenções que o código não revela | "Commits em português, padrão `SA-XXXX: descrição`" |
| Armadilhas conhecidas | "`npm run watch` não recompila CSS de página — use `npm run dev`" |
| Arquitetura em 3 linhas | "Monólito Laravel + módulos SPA em `resources/js/spa/`; permissões via pacote MtPermission" |
| Proibições reais | "NUNCA commitar direto na dev — sempre branch própria" |

## O que nunca pôr

- **O que o código já diz** — estrutura de pastas óbvia, lista de dependências. O Claude lê o repo.
- **Procedimentos longos sob demanda** — isso é [skill](skill-customizada.md): custa contexto só quando usada.
- **Documentação de API de terceiros** — envelhece e incha. Linke.
- **Tarefas do momento** ("estamos migrando X") sem data — daqui a 6 meses vira ruído que confunde. Se puser, date.

## Hierarquia

| Arquivo | Vale para |
| --- | --- |
| `~/.claude/CLAUDE.md` | Você, em todo projeto (estilo pessoal, preferências) |
| `CLAUDE.md` na raiz | Todo mundo neste repo |
| `CLAUDE.md` em subpasta | Carregado quando o Claude trabalha naquela subárvore — ideal em monorepo |
| `.claude/rules/*.md` | Regras por tópico, opcionalmente restritas a globs de caminho |

## Teste do valor

Pergunta para cada linha candidata: *"se o Claude errar isso, eu perco tempo?"* Se a resposta é "raramente", corte. Um `CLAUDE.md` de 30 linhas afiadas vale mais que um de 300 — modelo também sofre de fadiga de contexto: instrução enterrada em muro de texto é instrução ignorada.

## Manutenção

- `/memory` edita na hora; `#` no início do prompt oferece salvar a nota no arquivo certo.
- Quando uma seção crescer virando procedimento, extraia para skill.
- `/init` gera o esqueleto inicial analisando o codebase — bom ponto de partida, não de chegada.
