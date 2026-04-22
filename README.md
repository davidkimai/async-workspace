# Async Collaboration Workspace

This repository is designed to be used **through an AI assistant** rather than manual terminal work.
The agent handles setup and routine work; people mainly provide direction and review output.

## Why this is agent-first

- Lowers technical friction for non-technical contributors.
- Keeps setup and validation consistent across everyone.
- Preserves traceability (`status.tex` is the source of truth, `status.pdf` is the shareable output).

## First run (recommended)

### 1) Paste this prompt into your agent (Claude, Codex, or equivalent)

```text
You are an onboarding assistant for this project.
Goal: prepare the workspace for use locally.

Run only these steps:
1) If folder `async-workspace` does not exist, run:
   git clone https://github.com/davidkimai/async-workspace.git
2) Change into folder:
   cd async-workspace
3) Pull latest:
   git pull origin main
4) Make helper scripts executable:
   chmod +x merge-resolve.py render-status.sh start-claude.sh start-codex.sh
5) Confirm these required paths exist:
   - CLAUDE.md
   - status.tex
   - merge-resolve.py
   - render-status.sh
   - amy/transcripts & notes/
   - jason/transcripts & notes/
   - elizabeth/transcripts & notes/
   - hayley/transcripts & notes/

If the folder already exists, skip cloning and start at step 2.
Do not modify any repo files.
Reply with: READY + git remote + current branch + next step for user.
```

### 2) When the agent returns READY

Run with the repository open in VS Code and proceed with editing flow.

## Standard contributor flow (agent-assisted)

1. **Agent prompt:** Ask agent to draft the next `[DRAFT]` section in `status.tex` from your notes.
2. **Review + adjust:** Contributor reviews and approves.
3. **Commit/push:** Agent can run `git add status.tex` and push on your branch.

## Quick fallback (manual setup)

```bash
git clone https://github.com/davidkimai/async-workspace.git
cd async-workspace
```

If the folder already exists, open it directly.

### Contributor note locations

- `amy/transcripts & notes/`
- `jason/transcripts & notes/`
- `elizabeth/transcripts & notes/`
- `hayley/transcripts & notes/`

### Color macros for proposals in `status.tex`

- `\textcolor{elizC}{...}`
- `\textcolor{amyC}{...}`
- `\textcolor{jasonC}{...}`
- `\textcolor{hayleyC}{...}`

### Optional conflict command

```bash
python merge-resolve.py status.tex -o status.draft.tex
```
