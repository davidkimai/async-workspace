# Async Collaboration Workspace (PDF-defined)

This folder follows the structure and process from `async_workflow.pdf`:

## Layout

- `status.tex` — canonical living document
- `status.pdf` — rendered PDF output (generated after compile)
- `CLAUDE.md` — orchestration rules for collaborators
- `merge-resolve.py` — helper for conflict-heavy sections
- `elizabeth/transcripts & notes/` — Elizabeth’s raw inputs
- `jason/transcripts & notes/`   — Jason’s raw inputs
- `amy/transcripts & notes/`     — Amy’s raw inputs
- `hayley/transcripts & notes/`  — Hayley’s raw inputs

## Quick setup

1. Clone and update from shared repository:
   ```bash
   git pull origin main
   ```
2. Start your work on your own branch:
   ```bash
   git checkout -b <your-name>-workspace
   ```
3. Add transcripts/notes in your folder as files or markdown notes.
4. Edit `status.tex` with color-coded contributions where you add updates:
   - `\textcolor{elizC}{...}`
   - `\textcolor{amyC}{...}`
   - `\textcolor{jasonC}{...}`
   - `\textcolor{hayleyC}{...}`

## Contribution flow

1. Pull latest `status.tex` and add your updates in your folder.
2. Run Claude Code synthesis to propose `[DRAFT]` updates with source attribution.
3. If there is a same-line conflict, keep both options in color and tag for meeting.
4. Commit and push your branch:
   ```bash
   git add .
   git commit -m "Async workspace: add updates"
   git push
   ```

## Merge conflict helper

If `status.tex` has conflict blocks, convert them with:

```bash
python workspace/merge-resolve.py workspace/status.tex -o workspace/status.draft.tex
```

Then review and manually resolve to a single `status.tex` in a follow-up commit.

## Compile PDF

```bash
cd workspace
./render-status.sh
```

If you do not have LaTeX locally, open the shared Overleaf document and paste the LaTeX after each merge.
