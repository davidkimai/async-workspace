#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! command -v codex >/dev/null 2>&1; then
  echo "Codex CLI not found. Install it first, then rerun this command." >&2
  exit 1
fi

TASK="${1:-Read CLAUDE.md and status.tex, then draft the next [DRAFT] update with clear source attribution and color-coded contribution.}"

codex --dangerously-skip-permissions -p "$TASK"