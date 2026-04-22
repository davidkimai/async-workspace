# CLAUDE.md — Async Collaboration Workspace

This repo is a collaborative workspace template from `async_workflow.pdf`.

## Minimal rules

1. Work in your own folder only:
   - `amy/transcripts & notes/`
   - `jason/transcripts & notes/`
   - `elizabeth/transcripts & notes/`
   - `hayley/transcripts & notes/`

2. Update `status.tex` with color attribution:
   - `\textcolor{elizC}{...}`
   - `\textcolor{amyC}{...}`
   - `\textcolor{jasonC}{...}`
   - `\textcolor{hayleyC}{...}`

3. Start your work on a branch: `git checkout -b <name>/async-updates`

4. For same-line conflicts in `status.tex`, run:
   - `python merge-resolve.py status.tex -o status.draft.tex`
   - resolve manually in `status.tex`.

5. Canonical outputs:
   - `status.tex` (source of truth)
   - `status.pdf` (shared/human-readable output)

Only edit files required by the task, keep attribution clear, and keep changes minimal.