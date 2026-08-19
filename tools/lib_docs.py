import re
import sys
import urllib.request

BASE = "https://code.claude.com/docs/en/"


def fetch(page, source=None):
    if source:
        with open(source, encoding="utf-8") as f:
            return f.read()
    req = urllib.request.Request(BASE + page + ".md", headers={"User-Agent": "comandos-claude-code-tools"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def sections(md):
    out = {}
    current = None
    for line in md.split("\n"):
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            current = m.group(2).strip()
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def table_rows(section_text):
    rows = []
    for line in section_text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in split_row(line)]
        if not cells or all(set(c) <= set(":- ") for c in cells):
            continue
        rows.append(cells)
    return rows


def split_row(line):
    cells, cur, escaped = [], [], False
    for ch in line.strip().strip("|"):
        if escaped:
            cur.append("\\" + ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == "|":
            cells.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur))
    return cells


def clean(cell):
    cell = re.sub(r"\s+", " ", cell).strip()
    cell = cell.replace("](/docs/", "](https://code.claude.com/docs/")
    return cell


def die(msg):
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)
