# Async Collaboration Workspace

This repo is ready-to-use for async team writing with color-attributed `status.tex` updates.

## One-shot setup for non-technical users

Copy this short block into your agent (Claude, Codex, etc.) and run:

```text
Set up the async workspace now.

Do these commands:
1) If Git is not installed, stop and tell me to install from https://git-scm.com/downloads.
2) If not already present:
   git clone https://github.com/davidkimai/async-workspace.git && cd async-workspace
   else: cd async-workspace
3) git pull origin main
4) Create branch: git checkout -b <your-name>/async-updates
5) Make helper scripts executable:
   chmod +x merge-resolve.py render-status.sh start-claude.sh start-codex.sh
6) Confirm these folders exist: amy, jason, elizabeth, hayley and each has "transcripts & notes".
7) Give me a 4-step checklist to add my first notes.

Stop there and report: ready / blocked.
If a step is blocked, give exact unblock command only.

Do not change any project files yet.
```

## Quick manual fallback (5 lines)

If you prefer to do it yourself:

```bash
git clone https://github.com/davidkimai/async-workspace.git
cd async-workspace
git pull origin main
git checkout -b <your-name>/async-updates
mkdir -p "amy/transcripts & notes" "jason/transcripts & notes" "elizabeth/transcripts & notes" "hayley/transcripts & notes"
```

## How contributors add updates

- Add notes in your folder (`amy/`, `jason/`, `elizabeth/`, `hayley/` + `transcripts & notes`).
- Edit `status.tex` with your color macro:
  - `\textcolor{elizC}{...}`
  - `\textcolor{amyC}{...}`
  - `\textcolor{jasonC}{...}`
  - `\textcolor{hayleyC}{...}`
- Save/commit:

```bash
# if LaTeX is installed
./render-status.sh

git add status.tex "your/name/transcripts & notes"
git commit -m "Async workspace update"
git push -u origin HEAD
```

If LaTeX is missing, use Overleaf and paste `status.tex` there.

## Conflict helper

Same-line conflict in `status.tex`:

```bash
python merge-resolve.py status.tex -o status.draft.tex
```

Keep both options in color and choose one final version in a follow-up edit.

## Optional direct agent wrappers

- Claude: `./start-claude.sh "<task>"`
- Codex: `./start-codex.sh "<task>"`

These are optional, not required.