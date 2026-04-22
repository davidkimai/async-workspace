#!/usr/bin/env python3
"""
merge-resolve.py

Simple conflict visualizer for async LaTeX workflows.
- Reads a file with Git-style conflicts
- Rewrites conflicts into a colorized form in two contributor colors

Usage:
  python merge-resolve.py status.tex -o status.merged.tex
  python merge-resolve.py status.tex
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Map colors/macros to default contributor handles
DEFAULT_COLORS = {
    "elizC": "elizC",
    "amyC": "amyC",
    "jasonC": "jasonC",
    "hayleyC": "hayleyC",
}


def color_for_label(label: str) -> str:
    label = label.lower().strip()
    return {
        "eliz": "elizC",
        "elizabeth": "elizC",
        "amy": "amyC",
        "jason": "jasonC",
        "hayley": "hayleyC",
    }.get(label, "red")


def transform_conflicts(tex: str) -> str:
    """Convert Git conflict chunks to explicit colorized alternatives."""

    pattern = re.compile(
        r"<<<<<<<[ \t]*(.*?)\n(.*?)\n=======\n(.*?)\n>>>>>>>[ \t]*(.*?)\n",
        re.S,
    )

    def repl(match: re.Match[str]) -> str:
        left_label = match.group(1).strip() or "left"
        left_body = match.group(2).rstrip("\n")
        right_body = match.group(3).rstrip("\n")
        right_label = match.group(4).strip() or "right"

        left_color = color_for_label(left_label)
        right_color = color_for_label(right_label)

        return (
            "%%%% AUTO-MERGE HELPERS BEGIN\\n"
            + f"\\textcolor{{{left_color}}}{{%\\n% {left_label}\\n{left_body}\\n}}\n"
            + "%%%% vs\\n"
            + f"\\textcolor{{{right_color}}}{{%\\n% {right_label}\\n{right_body}\\n}}\n"
            + "%%%% AUTO-MERGE HELPERS END\\n"
        )

    return pattern.sub(repl, tex)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate colorized conflict blocks from LaTeX with color tags")
    parser.add_argument("input", help="Input .tex file that may contain git conflict markers")
    parser.add_argument("-o", "--output", help="Output path for rewritten file", default=None)
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {src}")

    content = src.read_text(encoding="utf-8")
    fixed = transform_conflicts(content)

    out = Path(args.output) if args.output else src
    out.write_text(fixed, encoding="utf-8")

    if args.output:
        print(f"Written merged conflict draft to: {out}")
    else:
        print(f"Updated in place: {out}")


if __name__ == "__main__":
    main()
