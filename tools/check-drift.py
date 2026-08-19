#!/usr/bin/env python3
"""Compara os comandos da doc oficial com docs/slash-commands.md.

Sai com código 1 (e relatório no stdout) quando há drift:
- comando na doc oficial que falta no repo;
- comando no repo que sumiu da doc oficial e não está em known-local-only.txt.

Uso: check-drift.py [--source commands.md-baixado]
"""
import pathlib
import re
import sys

from lib_docs import die, fetch

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent


def names_from(text):
    found = set()
    for line in text.split("\n"):
        if line.startswith("|") or line.lstrip().startswith("- "):
            for m in re.finditer(r"`/([a-z][a-z0-9-]*)", line):
                found.add(m.group(1))
    return found


source = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else None
official = names_from(fetch("commands", source))
if len(official) < 40:
    die(f"apenas {len(official)} comandos na doc oficial — o layout deve ter mudado")

ours = names_from((REPO / "docs" / "slash-commands.md").read_text(encoding="utf-8"))
known_local = {
    l.strip()
    for l in (HERE / "known-local-only.txt").read_text(encoding="utf-8").split("\n")
    if l.strip() and not l.startswith("#")
}

missing = sorted(official - ours)
extra = sorted(ours - official - known_local)

if not missing and not extra:
    print(f"sem drift: {len(official)} comandos oficiais, todos cobertos.")
    sys.exit(0)

print("# Drift detectado em docs/slash-commands.md\n")
if missing:
    print("## Na doc oficial, faltando no repo\n")
    for n in missing:
        print(f"- `/{n}`")
if extra:
    print("\n## No repo, ausente da doc oficial (adicione a tabela ou a known-local-only.txt)\n")
    for n in extra:
        print(f"- `/{n}`")
sys.exit(1)
