#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "pdflatex not found. Install a TeX toolchain (for example, MacTeX) or use Overleaf." >&2
  exit 1
fi

pdflatex -interaction=nonstopmode status.tex >/tmp/status-pdflatex.log 2>&1
status=$?
if [ "$status" -ne 0 ]; then
  echo "pdflatex failed; inspect /tmp/status-pdflatex.log" >&2
  exit $status
fi

echo "Rendered status.pdf in workspace/"
