# Async Collaboration Workspace

Drop this repo into a team and let your AI agent handle setup.

## Fastest way to start (for non-technical users)

1. Open this repo in VS Code.
2. Copy the **Setup Prompt** below.
3. Paste it into your agent of choice (Claude, Codex, or any LLM helper).
4. Follow the agent’s outputs.

---

## Paste-in setup prompt

> Copy everything inside this block and send to your agent.

```text
You are an assistant helping me set up an async collaboration workspace.

Context:
- Repo path is `./` (this workspace folder).
- This workspace follows color-attributed async editing from a LaTeX living document.

Your job:
1) Confirm this repo contains only workspace files needed for collaboration.
2) Ensure required files/folders exist:
   - `CLAUDE.md`
   - `status.tex`
   - `merge-resolve.py`
   - `render-status.sh`
   - directories: `amy/transcripts & notes`, `jason/transcripts & notes`, `elizabeth/transcripts & notes`, `hayley/transcripts & notes`
3) If any are missing, create them.
4) Keep file permissions executable where needed (`merge-resolve.py`, `render-status.sh`, `start-claude.sh`, `start-codex.sh`).
5) Set up a beginner-friendly branch plan:
   - suggest branch name template `<your-name>/async-updates`
   - run `git pull origin main`
   - run `git checkout -b <your-name>/async-updates`
6) Give me a simple checklist of next contributor actions:
   - add notes under your own transcript folder
   - edit `status.tex` in your color macro
   - run `./render-status.sh` (only if LaTeX is installed)
   - commit and push branch
7) If LaTeX is not installed, provide the Overleaf fallback.

Also include short command examples for **Claude Code** and **Codex** that only touch this repo, e.g.:
- Claude: `claude -p "..."`
- Codex: `codex --dangerously-skip-permissions -p "..."`

Do not change project logic beyond this workspace setup.
Report results as: pass/fail + exact commands run + next step.
```

---

## What the workspace is

- `status.tex` is the canonical living document.
- `status.pdf` is the human-readable exported version (generated after compile).
- `merge-resolve.py` helps when there are same-line conflicts.
- `render-status.sh` compiles LaTeX when available.
- `start-claude.sh` and `start-codex.sh` are quick launch helpers.

## Optional: one-shot contributor workflow (if you still want manual steps)

```bash
# open latest state
git pull origin main

git checkout -b <your-name>/async-updates

# add your inputs under your personal folder first, then propose edits in status.tex
# e.g. jason/transcripts & notes/

./render-status.sh  # optional (skip if no LaTeX)

git add .
git commit -m "Async workspace update"
git push -u origin HEAD
```

## Conflict helper

If two contributors edit the same line in `status.tex`, run:

```bash
python merge-resolve.py status.tex -o status.draft.tex
```

Then review both color-coded versions manually and keep one final `status.tex`.

## Need direct launcher for your preferred agent

- Claude helper: `./start-claude.sh "<your task>"`
- Codex helper: `./start-codex.sh "<your task>"`

These scripts run with a ready-made prompt scaffold; they are optional and only convenience.
