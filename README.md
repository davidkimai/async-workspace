# Async Collaboration Workspace

A tiny, collaborative template for async team updates shared through a single attributed `status.tex` document.

## What is this repo?
- Canonical source: `status.tex`
- Shared readable output: `status.pdf` (compiled from LaTeX)
- Conflict helper: `merge-resolve.py`
- Optional launch helpers: `start-claude.sh`, `start-codex.sh`

## 1) Install / setup (minimal)

### If you are comfortable with Git

```bash
git clone https://github.com/davidkimai/async-workspace.git
cd async-workspace
```

If the folder already exists, open that existing folder.

### If you are not technical (copy/paste to AI agent)

Send this to Claude / Codex / your preferred agent:

```text
Clone the repo to local if it is not already here: https://github.com/davidkimai/async-workspace.git
If cloning fails, stop and tell me the exact error.
No other changes.
```

The agent can run this as a first step so you do not need command-line setup.

## Why this prompt is included

`Setup prompts` are increasingly used as a deployment/startup primitive for AI workflows. A quick web check surfaced prompt-first onboarding patterns in AI tool ecosystems (for example, [AI app bootstrap setup prompts](https://github.com/gregmeyer/ai-app-bootstrap/blob/main/get-started/prompts/00-setup-editor.md) and [OpenClaw setup guidance](https://docs.openclaw.ai/start/openclaw)).
This repo keeps setup as a one-shot prompt so non-technical contributors can start fast.

## If you need the repository without terminal

1. Open GitHub in your browser.
2. Click **Code ▸ Download ZIP**.
3. Unzip the file.
4. Open the folder in VS Code (if available).

## Quick notes for first-time contributors

- Put notes in your folder:
  - `amy/transcripts & notes/`
  - `jason/transcripts & notes/`
  - `elizabeth/transcripts & notes/`
  - `hayley/transcripts & notes/`
- Use color macros in `status.tex`:
  - `\\textcolor{elizC}{...}`
  - `\\textcolor{amyC}{...}`
  - `\\textcolor{jasonC}{...}`
  - `\\textcolor{hayleyC}{...}`

## Optional helper commands

```bash
git checkout -b <your-name>/async-updates
./render-status.sh              # optional, if LaTeX is installed
python merge-resolve.py status.tex -o status.draft.tex
```
