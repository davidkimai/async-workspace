# CLAUDE.md — Async Collaboration Workspace

This workspace implements the process from `async_workflow.pdf`.

## Core rule

A contributor can either use manual commands or paste the README’s Setup Prompt into an agent.
Always begin by reading this file and `status.tex`, then follow the requested workflow.

## Working rules

1. **Pull first**
   - `git pull origin main`

2. **Branch per write session**
   - `git checkout -b <name>/async-updates`

3. **Contributor scope**
   - Add raw transcripts/notes in your assigned folder:
     - `elizabeth/transcripts & notes`
     - `jason/transcripts & notes`
     - `amy/transcripts & notes`
     - `hayley/transcripts & notes`

4. **Attributed proposals only**
   - Use these color macros in `status.tex`:
     - `\textcolor{elizC}{...}`
     - `\textcolor{amyC}{...}`
     - `\textcolor{jasonC}{...}`
     - `\textcolor{hayleyC}{...}`

5. **Drafting pattern**
   - Keep edits scoped to `status.tex` and your own transcript folder.
   - Add `[DRAFT]` for machine-proposed text.
   - Resolve by discussion only when explicit conflict remains.

6. **Conflicts**
   - For same-line conflicts, run:
     - `python merge-resolve.py status.tex -o status.draft.tex`
   - Keep both versions color-coded and resolve manually in a follow-up edit.

7. **Output flow**
   - `status.tex` is canonical.
   - `status.pdf` is shareable output.

## Assistant contract

- Do not edit outside this workspace unless explicitly asked.
- Preserve attribution and traceability.
- Run only the commands listed by the user or README setup prompt.
- Return clear pass/fail with exact next steps.
