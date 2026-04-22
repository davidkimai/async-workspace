# Async Collaboration Workspace

This repo is a small setup package for async collaboration. It is designed so teams can add notes, merge them into one living status doc, and keep clear source attribution.

---

## For people new to GitHub (very simple)

### 1) Get the repo (copy + paste)

```bash
# Install Git if needed: https://git-scm.com/downloads
git clone https://github.com/davidkimai/async-workspace.git
cd async-workspace
```

### 2) Open in VS Code

- Open VS Code → **File ▸ Open Folder…** → choose `async-workspace`
- Open terminal inside VS Code (`View ▸ Terminal`)

### 3) Start your own branch

```bash
git pull origin main
git checkout -b <your-name>/async-updates
```

Example: `git checkout -b jason/async-updates`

### 4) Add your work

- Put raw notes/transcripts in your folder:
  - `amy/transcripts & notes/`
  - `jason/transcripts & notes/`
  - `elizabeth/transcripts & notes/`
  - `hayley/transcripts & notes/`
- Add structured updates to `status.tex` using your color macro:
  - `\\textcolor{elizC}{...}`
  - `\\textcolor{amyC}{...}`
  - `\\textcolor{jasonC}{...}`
  - `\\textcolor{hayleyC}{...}`

### 5) Save and share

```bash
# compile PDF if LaTeX is installed
./render-status.sh

git add status.tex "your/name/folder" 
git commit -m "Async workspace update"
git push -u origin HEAD
```

If you can’t install LaTeX, use Overleaf and paste `status.tex` there.

---

## Paste this prompt into Claude/Codex to auto-check setup

Copy everything in the block below and paste it into your agent. This is a normal user prompt, not a system prompt.

```text
Please help me set up this async workspace in the current repo `./`.

Tasks:
1. Check that required items exist: `CLAUDE.md`, `status.tex`, `merge-resolve.py`, `render-status.sh`, and folders `amy/transcripts & notes`, `jason/transcripts & notes`, `elizabeth/transcripts & notes`, `hayley/transcripts & notes`.
2. If anything is missing, create it in the right structure.
3. Make sure executable scripts are runnable if present: `merge-resolve.py`, `render-status.sh`, `start-claude.sh`, `start-codex.sh`.
4. Confirm branch setup command: `git checkout -b <your-name>/async-updates`.
5. Give me a short, copy/paste checklist for contributor work and note any blockers.
6. Keep all suggestions limited to this workspace only.

Then respond with: pass/fail, exact commands run, and next action.
```

---

## Conflict helper

If two people edit the same line in `status.tex`, run:

```bash
python merge-resolve.py status.tex -o status.draft.tex
```

Keep both options in color, then resolve manually.

---

## Optional launch helpers (if you already use these CLI tools)

- Claude: `./start-claude.sh "<your task>"`
- Codex: `./start-codex.sh "<your task>"`

These are optional convenience wrappers.