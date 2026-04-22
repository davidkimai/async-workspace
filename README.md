# Async Collaboration Workspace

A lightweight, timezone-agnostic, color-attributed collaboration workspace template based on **Async Collaboration Workflow**.

This repo is designed so multiple people can add their notes/transcripts, then merge into one traceable living status document:
- `status.tex` (source of truth)
- `status.pdf` (readable output)

---

## Strategic setup (quick, non-technical friendly)

### 1) Open the workspace

1. Open this folder in **VS Code**
   - `File ▸ Open Folder…` → choose `async-workspace`
2. Open the Explorer and confirm you see:
   - `status.tex`
   - `CLAUDE.md`
   - folders: `amy`, `jason`, `elizabeth`, `hayley` (each with `transcripts & notes`)
3. Install recommended VS Code extensions when prompted (LaTeX + Git tools).

### 2) Get the latest version

```bash
# from the repo folder

git pull origin main
```

### 3) Start your own branch

```bash
git checkout -b <your-name>-workspace
```

Examples:
- `git checkout -b jason-iteration-1`
- `git checkout -b amy-meeting-notes`

### 4) Add your notes

Save raw notes/transcripts in your own folder:
- `amy/transcripts & notes/`
- `jason/transcripts & notes/`
- `elizabeth/transcripts & notes/`
- `hayley/transcripts & notes/`

### 5) Update status

Edit `status.tex` and add your contribution in your color:
- `\textcolor{elizC}{...}` for Elizabeth
- `\textcolor{amyC}{...}` for Amy
- `\textcolor{jasonC}{...}` for Jason
- `\textcolor{hayleyC}{...}` for Hayley

### 6) Save, compile, and commit

```bash
# (optional but recommended before commit)
./render-status.sh

# review output + commit

git status
# add files
git add .
git commit -m "Async workspace: add updates"
git push -u origin HEAD
```

> If you only changed LaTeX and want a quick check, compile command will create a PDF so humans can review easily.

---

## Conflict handling (when two people edit same line)

When there is conflicting text in `status.tex`, use the helper script:

```bash
python merge-resolve.py status.tex -o status.draft.tex
```

This keeps both versions in contributor colors so a human can make the final choice.

---

## Integrate with **Claude Code** (non-technical setup)

1. Install Claude Code CLI (if not already):
   - Follow your organization’s normal Claude installation.
2. Open terminal in this repo.
3. Run:

```bash
claude -p "Read CLAUDE.md and status.tex, then draft the next safe [DRAFT] update with source attribution and color-coded text where applicable."
```

4. Ask for an explicit task, e.g.:
> "Summarize today’s inputs from ./jason/transcripts & notes into status.tex as a [DRAFT] for the Decisions section."

Quick one-liner helper (if you prefer):

```bash
./start-claude.sh "Draft a [DRAFT] update for Open Questions from notes in ./amy/transcripts\ \&\ notes"
```

---

## Integrate with **Codex** (non-technical setup)

1. Install Codex CLI and authenticate.
2. Open terminal in this repo.
3. Run:

```bash
codex --dangerously-skip-permissions -p "Read CLAUDE.md and status.tex, then produce a color-coded [DRAFT] proposal from the latest transcripts."
```

4. Keep prompts constrained to this workspace:
- "only touch files under this repo"
- "preserve color attribution"

Quick one-liner helper:

```bash
./start-codex.sh "Propose a [DRAFT] update for Conflicts section from ./hayley/transcripts & notes"
```

---

## VS Code + AI workflow (simple, repeatable)

**Recommended sequence every time:**
1. Pull latest → 2) switch branch → 3) add notes in your folder → 4) update `status.tex` → 5) compile PDF → 6) commit/push.

If your team is non-technical:
- You only need to copy and paste the commands above.
- Use your preferred AI tool (Claude Code or Codex) to draft text.
- Keep edits in your own folder + only patch `status.tex` for proposals.

---

## Notes

- `status.tex` is the canonical source for decisions and references.
- `status.pdf` is the human-friendly output for sharing.

