#!/usr/bin/env python3
"""Lint summaryBody *rendering* format (2026-08-29 cycle learning).

`validate_summary.py` checks the JSON **schema** (required fields, score ranges,
lengths) but NOT whether `summaryBody` will *render* cleanly on the detail page.
A body can be schema-valid yet display as literal markup. This linter flags only
**broken rendering** (not stylistic choices — a line-start ``### heading`` renders
fine and is left alone). Three defects, all observed in the 2026-08-29 cycle:

  1. ``escaped-newline`` — the two-character sequence ``\\n`` is used as a line
     break (JSON had ``\\\\n``), so it renders as a literal "\\n". Flagged when
     ``\\n\\n`` appears or ``\\n`` occurs 2+ times (a one-off prose mention of
     ``\\n`` is not flagged).
  2. ``mashed-single-line`` — markdown structure is crammed onto one line so it
     will not render. Two shapes: (a) the whole body is a single line (no real
     newline) while it contains a ``##``–``######`` header or a ``N. **`` list;
     or (b) an individual line crams structure onto itself — 2+ ``N. **`` list
     items on one line, or a header sharing its line with a ``N. **`` item (e.g.
     ``### 主な特徴 1. **…**``). Shape (b) is caught even when the rest of the body
     has real newlines (a *partially* mashed body), which shape (a) alone missed.
  3. ``inline-header`` — a ``##``–``######`` header marker sits mid-line (text
     before it on the same line), so it renders as literal ``###`` instead of a
     heading. Line-start headers are NOT flagged. This includes a header
     glued directly to the preceding text with no space (e.g. ``…です。### 見出し``,
     observed in the 2026-09-12 cycle, #064): the marker still renders literally.

Schema validation passes all three; this linter fails them. Run it as a QA gate
after generation (see the summarize-source skill's post-generation QA checklist)
and against an archived cycle to audit it.

Usage:
    uv run scripts/check_summary_format.py workdesk/summaries
    uv run scripts/check_summary_format.py journals/2026-08-29/summaries --quiet
    uv run scripts/check_summary_format.py workdesk/summaries/158_x.json

Exit 0 = all bodies render-clean; exit 1 = one or more flagged (gate-friendly);
exit 2 = usage error.
"""

import glob
import json
import os
import re
import sys

# A markdown header marker: a run of 2-6 '#' followed by whitespace, matched
# anywhere on the line — line start, after whitespace, OR glued directly to
# preceding text (e.g. "…です。### 見出し"). The glued case is the worst: it
# escapes a "(?:^|\s)#" anchor yet still renders as a literal "###" (see #064).
# Requiring 2+ '#' keeps single-'#' prose ("C#", "#1") from matching; requiring
# a trailing space keeps in-word runs ("page##frag") from matching. Line-start
# headers are excluded downstream in _line_has_inline_header, so widening the
# match here only adds the genuinely-broken mid-line/glued cases.
_HEADER = re.compile(r"#{2,6}\s")
# "1. **Label**" — a numbered + bold list item (the mashed-list signature).
_NUM_BOLD_LIST = re.compile(r"\d+\.\s*\*\*")


def _line_has_inline_header(line: str) -> bool:
    """True if a header marker sits mid-line (a line-start header is fine)."""
    if line.lstrip().startswith("#"):
        return False
    return bool(_HEADER.search(line))


def _line_is_mashed(line: str) -> bool:
    """True if a *single* line crams markdown structure onto itself so it will
    not render as structure. Two signatures: 2+ ``N. **`` list items on one line,
    or a header sharing its line with a ``N. **`` list item (e.g.
    ``### 主な特徴 1. **フル自律運営**: …``). A properly formatted body puts each
    header and each list item on its own line, so neither signature fires on
    clean output. This catches a *partially* mashed body — one crammed line while
    the rest of the body has real newlines — which the whole-body single-line
    check in ``lint_body`` misses.
    """
    n_items = len(_NUM_BOLD_LIST.findall(line))
    if n_items >= 2:
        return True
    return n_items >= 1 and bool(_HEADER.search(line))


def lint_body(body: str) -> list[str]:
    """Return the ordered list of defect labels for a summaryBody (empty = clean)."""
    defects = []
    if "\\n\\n" in body or body.count("\\n") >= 2:
        defects.append("escaped-newline")
    has_structure = bool(_HEADER.search(body)) or bool(_NUM_BOLD_LIST.search(body))
    if has_structure and "\n" not in body:
        # Whole body is one line yet carries structure: nothing renders.
        defects.append("mashed-single-line")
    else:
        # Body has real newlines: check each line for structure crammed onto it.
        lines = body.split("\n")
        if any(_line_is_mashed(line) for line in lines):
            defects.append("mashed-single-line")
        if any(_line_has_inline_header(line) for line in lines):
            defects.append("inline-header")
    return list(dict.fromkeys(defects))  # de-dup, preserve order


def _iter_files(path: str) -> list[str]:
    if os.path.isdir(path):
        return sorted(glob.glob(os.path.join(path, "*.json")))
    return [path]


def check_path(path: str) -> tuple[int, int, list[tuple[str, list[str]]]]:
    """Return (total_json_summaries, flagged_count, [(file, defects), ...])."""
    total = 0
    flagged = []
    for fp in _iter_files(path):
        try:
            with open(fp, encoding="utf-8") as f:
                body = json.load(f).get("content", {}).get("summaryBody", "")
        except (json.JSONDecodeError, OSError):
            # Non-JSON (e.g. a BLOCKED-* stub) is the schema validator's concern.
            continue
        total += 1
        defects = lint_body(body)
        if defects:
            flagged.append((fp, defects))
    return total, len(flagged), flagged


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv or "-q" in argv
    args = [a for a in argv if not a.startswith("-")]
    if len(args) != 1:
        print(
            "Usage: uv run scripts/check_summary_format.py <file-or-dir> [--quiet]",
            file=sys.stderr,
        )
        return 2

    total, n_flagged, flagged = check_path(args[0])
    for fp, defects in flagged:
        print(f"✗ {fp}: {', '.join(defects)}")
    if n_flagged:
        print(f"\n✗ summary-format: {n_flagged}/{total} bodies mis-formatted")
        return 1
    if not quiet:
        print(f"✓ summary-format: all {total} bodies render-clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
