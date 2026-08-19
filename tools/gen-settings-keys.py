#!/usr/bin/env python3
"""Gera docs/settings-json.md a partir da página oficial settings.

Uso: gen-settings-keys.py [--source arquivo.md] > docs/settings-json.md
"""
import sys

from lib_docs import clean, die, fetch, sections, table_rows

SECTIONS = [
    ("Available settings", "Chaves principais"),
    ("Global config settings", "Config global"),
    ("Worktree settings", "Worktrees"),
    ("Permission settings", "Permissões"),
    ("Sandbox settings", "Sandbox"),
    ("Attribution settings", "Atribuição em commits e PRs"),
]

source = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else None
md = fetch("settings", source)
secs = sections(md)

missing = [s for s, _ in SECTIONS if s not in secs]
if missing:
    die(f"seções não encontradas: {missing} — o layout da página mudou; ajuste este script")

print("""---
title: settings.json
nav_order: 11
---

# `settings.json` — chaves completas

[← Voltar ao índice](index.md)

> Página **gerada** por `tools/gen-settings-keys.py` a partir da
> [documentação oficial](https://code.claude.com/docs/en/settings). As descrições
> ficam em inglês de propósito: regenerar não perde tradução nenhuma.
> Precedência e locais dos arquivos estão em [Configuração](configuracao.md).""")

total = 0
for sec, titulo in SECTIONS:
    rows = [r for r in table_rows(secs[sec]) if r and r[0].startswith("`")]
    if not rows:
        continue
    total += len(rows)
    print(f"\n## {titulo}\n")
    print("| Chave | Descrição |")
    print("| --- | --- |")
    for r in rows:
        desc = " · ".join(clean(c) for c in r[1:] if clean(c))
        print(f"| {clean(r[0])} | {desc} |")

if total < 60:
    die(f"apenas {total} chaves extraídas — o layout da página deve ter mudado")
print(f"\n_{total} chaves._")
