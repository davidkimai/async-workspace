# CLAUDE.md — Async Collaboration Workspace

This workspace implements the workflow described in `async_workflow.pdf`.

## Working rules

1. Pull latest before editing:
   - `git pull origin main`
   - Resolve conflicts in the shared branch first.

2. Branch for each local write session:
   - `git checkout -b <name>-<topic-or-date>`
   - Keep only your intended files in your branch.

3. Write in your own area:
   - Add transcripts, references, and notes only under your folder:
     - `elizabeth/transcripts & notes`
     - `jason/transcripts & notes`
     - `amy/transcripts & notes`
     - `hayley/transcripts & notes`

4. Use color markers when proposing edits:
   - Use `\textcolor{elizC}{...}` for Elizabeth
   - Use `\textcolor{amyC}{...}` for Amy
   - Use `\textcolor{jasonC}{...}` for Jason
   - Use `\textcolor{hayleyC}{...}` for Hayley

5. Draft cycle in this workspace:
   - Update `status.tex` with attributed color-coded input.
   - Propose `[DRAFT]` and ask for a meeting only on unresolved conflicts.
   - Commit and push via branch once reviewed.

6. Conflicts:
   - For same-line conflicts from two contributors, use `merge-resolve.py` to retain both versions in color.
   - Escalate to a synchronous meeting when still ambiguous.

## Safety / anti-conflict rule

- This workspace is for async contributions only.
- Avoid silent overwrites in `status.tex`; always keep source attribution and traceability.

## Output flow

- `status.tex` (canonical living doc)
- `status.pdf` (human-readable compiled output, shared externally)

Use `render-status.sh` to generate/update the PDF after each merge.

## Tooling contract for assistants

- Always read this file before editing.
- Never edit folders outside `status.tex` and your assigned contributor folder unless explicitly approved.
- Treat all outputs as attributed draft text until reviewed and merged.
