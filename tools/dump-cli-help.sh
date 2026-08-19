#!/usr/bin/env bash
# Salva o --help da CLI e de cada subcomando em um único arquivo,
# para diffar contra docs/cli.md quando o Claude Code atualizar.
# Uso: tools/dump-cli-help.sh > cli-help-$(claude --version | cut -d' ' -f1).txt
set -euo pipefail

echo "### claude --version"
claude --version
echo
echo "### claude --help"
claude --help
for sub in agents auth auto-mode daemon doctor install mcp plugin project setup-token ultrareview update; do
  echo
  echo "### claude $sub --help"
  claude "$sub" --help 2>&1 || true
done
