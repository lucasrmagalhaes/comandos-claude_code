#!/usr/bin/env python3
"""Gera docs/variaveis-ambiente.md a partir da página oficial env-vars.

Uso: gen-env-vars.py [--source arquivo.md] > docs/variaveis-ambiente.md
"""
import re
import sys

from lib_docs import clean, die, fetch, sections, table_rows

source = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else None
md = fetch("env-vars", source)
secs = sections(md)
if "Variables" not in secs:
    die("seção 'Variables' não encontrada — o layout da página mudou; ajuste este script")

rows = [r for r in table_rows(secs["Variables"]) if r and r[0].startswith("`")]
if len(rows) < 100:
    die(f"apenas {len(rows)} variáveis extraídas — o layout da página deve ter mudado")

print("""---
title: Variáveis de ambiente
nav_order: 12
---

# Variáveis de ambiente — lista completa

[← Voltar ao índice](index.md)

> Página **gerada** por `tools/gen-env-vars.py` a partir da
> [documentação oficial](https://code.claude.com/docs/en/env-vars). As descrições
> ficam em inglês de propósito: regenerar não perde tradução nenhuma.
> Os grupos comentados estão em [Configuração](configuracao.md).

| Variável | Descrição |
| --- | --- |""")
for r in rows:
    desc = " · ".join(clean(c) for c in r[1:] if clean(c))
    print(f"| {clean(r[0])} | {desc} |")
print(f"\n_{len(rows)} variáveis._")
