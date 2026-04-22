#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude CLI not found. Install it first, then rerun this command." >&2
  exit 1
fi

TASK="${1:-Read CLAUDE.md and status.tex, then draft the next [DRAFT] update with clear source attribution and color-coded contribution.}"

claude -p "$TASK"