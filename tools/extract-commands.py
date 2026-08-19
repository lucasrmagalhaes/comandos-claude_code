#!/usr/bin/env python3
"""Extrai o registry de comandos de barra do binário instalado do Claude Code.

Uso: strings -n 3 "$(readlink -f "$(which claude)")" | extract-commands.py

Imprime TSV: nome, tipo (local|local-jsx|prompt), aliases, argumentHint, descrição.
Comandos com descrição dinâmica saem como <dynamic>. Compare o resultado com
docs/slash-commands.md para achar o que o binário tem e a doc não cobre.
"""
import re
import sys

data = sys.stdin.read()
NAME_RE = re.compile(r'name:"([a-z0-9][a-z0-9:_-]{1,30})"')
found = {}


def near_desc(text, forward):
    m = re.search(r'description:"((?:[^"\\]|\\.){3,250})"', text)
    if not m:
        return None
    seg = text[: m.start()] if forward else text[m.end():]
    return None if 'name:"' in seg else m.group(1)


for m in NAME_RE.finditer(data):
    fw = data[m.end(): m.end() + 420]
    bw = data[max(0, m.start() - 420): m.start()]
    desc = near_desc(fw, True) or near_desc(bw, False)
    getdesc = bool(re.match(r',?get description\(\)', fw))
    ctx = data[max(0, m.start() - 420): m.end() + 520]
    kind = next((k for k in ("local-jsx", "local", "prompt") if f'type:"{k}"' in ctx), "")
    if not kind and "userInvocable:!0" in ctx:
        kind = "prompt"
    if not kind and not getdesc:
        continue
    al = re.search(r"aliases:\[([^\]]*)\]", fw[:260])
    ah = re.search(r'argumentHint:"([^"]*)"', fw[:320])
    entry = (kind, al.group(1).replace('"', "") if al else "",
             ah.group(1) if ah else "", desc or ("<dynamic>" if getdesc else ""))
    prev = found.get(m.group(1))
    if prev is None or (prev[3] in ("", "<dynamic>") and entry[3] not in ("", "<dynamic>")):
        found[m.group(1)] = entry

for name in sorted(found):
    print("\t".join((name, *found[name])))
print(f"# {len(found)} comandos", file=sys.stderr)
