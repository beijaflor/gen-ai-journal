#!/usr/bin/env python3
"""STEP_08 stitch + QA — assemble the writer fragments and gate the result.

The theme/section writers (subagents or hand) drop their drafts in a scratch
dir; the orchestrator writes the frame pieces (header incl. 今週のハイライト,
おわりに; annex header, 編集後記). This script concatenates them in order into
the finished weekly + annex journals, then runs the SAME quality gate as
verify_journal (coverage / leaks / hierarchy / encoding, optional URL health) on
the assembled files — non-zero exit on any fault.

Scratch layout (per cycle):
    weekly_header.md   main_theme_01.md .. main_theme_NN.md   weekly_outro.md
    annex_header.md    annex_sec_01.md  .. annex_sec_MM.md    annex_outro.md

Usage:
    uv run scripts/stitch_qa.py 2026-08-22
    uv run scripts/stitch_qa.py 2026-08-22 --scratch tests/fixtures/2026-08-22-scratch \
        --out /tmp/eval08 --sources-dir journals/2026-08-22/sources --skip-urls
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_journal import verify_paths  # noqa: E402


def _numbered(scratch, glob_pat):
    """Fragments matching ``<prefix>_NN.md`` in numeric order; fail loudly if the
    numbering is not exactly 01..N (a stray extra or renumbered fragment would
    otherwise be silently stitched into the journal)."""
    stem = glob_pat.replace("*.md", "")
    frags = []
    for frag in scratch.glob(glob_pat):
        num = frag.stem[len(stem):]
        if not num.isdigit():
            raise ValueError(f"fragment not numbered {stem}NN.md: {frag.name}")
        frags.append((int(num), frag))
    frags.sort()
    nums = [n for n, _ in frags]
    if nums != list(range(1, len(nums) + 1)):
        raise ValueError(f"{stem}NN.md must be numbered 01..N contiguously, got "
                         f"{[f.name for _, f in frags]}")
    return [f for _, f in frags]


def _concat(scratch, header, glob_pat, outro):
    parts = [(scratch / header).read_text(encoding="utf-8")]
    for frag in _numbered(scratch, glob_pat):
        parts.append(frag.read_text(encoding="utf-8"))
    parts.append((scratch / outro).read_text(encoding="utf-8"))
    return "".join(parts)


def stitch(date, scratch, out_dir):
    """Assemble weekly + annex from the scratch fragments; return their paths."""
    scratch = Path(scratch)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    us = date.replace("-", "_")

    weekly = _concat(scratch, "weekly_header.md", "main_theme_*.md", "weekly_outro.md")
    annex = _concat(scratch, "annex_header.md", "annex_sec_*.md", "annex_outro.md")

    weekly_path = out_dir / f"weekly_journal_{us}.md"
    annex_path = out_dir / f"annex_journal_{us}.md"
    weekly_path.write_text(weekly, encoding="utf-8")
    annex_path.write_text(annex, encoding="utf-8")
    return weekly_path, annex_path


def _resolve_sources(date, sources_dir):
    if sources_dir:
        return Path(sources_dir)
    arc = Path(f"journals/{date}/sources")
    return arc if arc.is_dir() else Path("workdesk")


def run(date, scratch="scratchpad", out_dir="workdesk", sources_dir=None,
        skip_urls=False):
    weekly_path, annex_path = stitch(date, scratch, out_dir)
    src = _resolve_sources(date, sources_dir)
    rep = verify_paths(
        date, weekly_path, annex_path,
        src / "curated_journal_sources.md",
        src / "curated_annex_selected.md",
        skip_urls=skip_urls,
    )
    n_themes = len(list(Path(scratch).glob("main_theme_*.md")))
    n_secs = len(list(Path(scratch).glob("annex_sec_*.md")))
    print(f"stitched weekly ({n_themes} themes) + annex ({n_secs} sections) -> {out_dir}")
    return rep


def main():
    args = sys.argv[1:]
    skip_urls = "--skip-urls" in args
    opts = {"--scratch": "scratchpad", "--out": "workdesk", "--sources-dir": None}
    for flag in list(opts):
        if flag in args:
            i = args.index(flag)
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    positional = [a for a in args if not a.startswith("-")]
    if len(positional) != 1:
        print("Usage: uv run scripts/stitch_qa.py <YYYY-MM-DD> [--scratch DIR] "
              "[--out DIR] [--sources-dir DIR] [--skip-urls]")
        sys.exit(1)

    try:
        rep = run(positional[0], scratch=opts["--scratch"], out_dir=opts["--out"],
                  sources_dir=opts["--sources-dir"], skip_urls=skip_urls)
    except (ValueError, FileNotFoundError) as e:
        print(f"❌ stitch_qa: {e}")
        sys.exit(1)
    print("\n".join(rep.notes))
    if rep.ok:
        print("\n✅ stitch_qa: assembled journals pass QA")
        sys.exit(0)
    print(f"\n❌ stitch_qa: {len(rep.failures)} check(s) failed: "
          + ", ".join(rep.failures))
    sys.exit(1)


if __name__ == "__main__":
    main()
