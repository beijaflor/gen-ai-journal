#!/usr/bin/env python3
"""Lint summaryBody *rendering* format against the canonical spec.

`validate_summary.py` checks the JSON **schema** (required fields, score
ranges, lengths) but NOT whether `summaryBody` will *render* cleanly on the
detail page. A body can be schema-valid yet display as literal markup.

This linter enforces the canonical `summaryBody` Markdown-in-JSON format
defined in `.claude/skills/summarize-source/SKILL.md` under "summaryBody
format definition" -- the same spec `prompts/summarize-json.prompt` targets
in its "Markdown formatting rules" subsection. If the spec changes, update
that section first, then this linter and the prompt to match.

It flags only **broken rendering** (not stylistic choices -- a line-start
``### heading`` followed by a blank line renders fine and is left alone).
Three defect categories, covering every failure mode observed so far:

  1. ``escaped-newline`` -- the two-character sequence ``\\n`` is used as a
     line break (JSON had ``\\\\n``), so it renders as a literal "\\n".
     Flagged when ``\\n\\n`` appears or ``\\n`` occurs 2+ times (a one-off
     prose mention of ``\\n`` is not flagged).
  2. ``mashed-single-line`` -- markdown structure fails to render as
     structure because it isn't separated by real newlines. This covers:
       - the **whole body** is a single line (no real newline at all) while
         containing a ``##``-``######`` header or a ``N. **`` list;
       - a **partial mash**: even when the body DOES have real newlines
         elsewhere, one single line crams together either (a) a header
         glued directly to a list item (bullet or numbered), or (b) two or
         more ``N. **`` list items -- both signatures of markdown structure
         collapsed onto one physical line instead of one-item-per-line.
  3. ``inline-header`` -- a ``##``-``######`` header marker fails to stand
     alone on its own line. This covers:
       - the marker sits **mid-line**, with text before it on the same line
         (renders as literal ``###`` instead of a heading);
       - a header glued directly to the **preceding** text with no space
         (e.g. ``...です。### 見出し``, observed in the 2026-09-12 cycle,
         #064): the marker still renders literally;
       - a header glued directly to the **following** text with no line
         break, i.e. the heading label runs straight into the first
         sentence of body text on the same line (e.g. ``## 記事の概要PC
         Watch編集部が...``). Since legitimate heading labels in this corpus
         are short phrases that never end with a Japanese full stop
         (``。``), a header-start line containing ``。`` is treated as
         glued-forward text rather than a real heading.
     A clean line-start header (alone on its own line, no stray ``。``) is
     NOT flagged.

Schema validation passes all of the above; this linter fails them. Run it as
a QA gate after generation (see the summarize-source skill's post-generation
QA checklist) and against an archived cycle to audit it.

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
# anywhere on the line -- line start, after whitespace, OR glued directly to
# preceding text (e.g. "...です。### 見出し"). The glued case is the worst: it
# escapes a "(?:^|\s)#" anchor yet still renders as a literal "###" (see #064).
# Requiring 2+ '#' keeps single-'#' prose ("C#", "#1") from matching; requiring
# a trailing space keeps in-word runs ("page##frag") from matching. Line-start
# headers are excluded downstream in _line_has_inline_header, so widening the
# match here only adds the genuinely-broken mid-line/glued cases.
_HEADER = re.compile(r"#{2,6}\s")
# "1. **Label**" -- a numbered + bold list item (the mashed-list signature).
_NUM_BOLD_LIST = re.compile(r"\d+\.\s*\*\*")
# A bullet or numbered list-item marker, used (together with _HEADER) to spot
# a header glued to a list item on one physical line -- "(?:^|\s)" so we don't
# match a bare hyphen inside a word (e.g. "AI-駆動") or a decimal mid-word.
_BULLET_ITEM = re.compile(r"(?:^|\s)-\s")
_NUM_ITEM = re.compile(r"(?:^|\s)\d+\.\s")
# Japanese sentence-ending punctuation. A heading LABEL never carries this;
# a heading LINE that does is prose glued onto the heading with no break.
_SENTENCE_END = re.compile(r"。")


def _line_has_inline_header(line: str) -> bool:
    """True if a header marker sits mid-line (a line-start header is fine)."""
    if line.lstrip().startswith("#"):
        return False
    return bool(_HEADER.search(line))


def _line_is_glued_heading(line: str) -> bool:
    """True if a line-start header's label runs directly into body prose.

    A real heading label is short and never ends with "。". A header-start
    line that contains "。" is almost certainly a heading merged with the
    sentence that should have started on the next line after a blank line.
    """
    stripped = line.lstrip()
    if not _HEADER.match(stripped):
        return False
    return bool(_SENTENCE_END.search(line))


def _line_is_partial_mash(line: str) -> bool:
    """True if one physical line crams together markdown structure that
    belongs on separate lines: 2+ numbered-bold list items, or a header
    glued directly to a list item (bullet or numbered)."""
    if len(_NUM_BOLD_LIST.findall(line)) >= 2:
        return True
    if _HEADER.search(line) and (
        _NUM_BOLD_LIST.search(line) or _BULLET_ITEM.search(line) or _NUM_ITEM.search(line)
    ):
        return True
    return False


def lint_body(body: str) -> list[str]:
    """Return the ordered list of defect labels for a summaryBody (empty = clean)."""
    defects = []
    if "\\n\\n" in body or body.count("\\n") >= 2:
        defects.append("escaped-newline")

    has_structure = bool(_HEADER.search(body)) or bool(_NUM_BOLD_LIST.search(body))

    if has_structure and "\n" not in body:
        # The whole body is one line yet contains heading/list markup: none
        # of it can render as structure. This subsumes any inline-header
        # finding below (the header IS the mash), so don't double-flag.
        defects.append("mashed-single-line")
    else:
        lines = body.split("\n")
        if any(_line_is_partial_mash(line) for line in lines):
            defects.append("mashed-single-line")
        if any(
            _line_has_inline_header(line) or _line_is_glued_heading(line)
            for line in lines
        ):
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
