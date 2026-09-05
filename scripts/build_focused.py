#!/usr/bin/env python3
"""STEP_06 — build the three focused unified-summary files for a cycle.

Wraps the existing unite_summaries.py three times (main / annex / omitted),
then asserts that every curated URL actually resolved to a summary and that the
main/annex/omitted sets still partition the full source list.

    curated_journal_sources.md  -> unified_summaries_main.md
    curated_annex_selected.md   -> unified_summaries_annex.md
    omitted_sources.md          -> omitted_summaries_unified.md

Usage:
    uv run scripts/build_focused.py 2026-08-22
    uv run scripts/build_focused.py 2026-08-22 --out /tmp/eval06     # eval-only target
    uv run scripts/build_focused.py 2099-01-01 \
        --sources-dir tests/fixtures/mini-journal/2099-01-01/sources \
        --summaries-dir tests/fixtures/mini-journal/2099-01-01/summaries --out /tmp/x

``--out`` (default: workdesk/) keeps golden reproductions from overwriting the
real workdesk. Reports the authoritative summary count (unite_summaries's own
tally); a raw ``grep -c '^## '`` over-counts because some summary bodies contain
their own H2 lines.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow import partition  # noqa: E402

UNITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unite_summaries.py")

# (source file, output file, partition-set name)
JOBS = [
    (partition.MAIN_FILE, "unified_summaries_main.md", "main"),
    (partition.ANNEX_FILE, "unified_summaries_annex.md", "annex"),
    (partition.OMITTED_FILE, "omitted_summaries_unified.md", "omitted"),
]

_CREATED = re.compile(r"with (\d+) summaries")
_MISSING = re.compile(r"Missing summaries \((\d+)\)")


def _default_dir(date, kind):
    """kind is 'sources' or 'summaries'; prefer the archived cycle."""
    arc = Path(f"journals/{date}/{kind}")
    if arc.is_dir():
        return arc
    return Path("workdesk") / "summaries" if kind == "summaries" else Path("workdesk")


def build(date, sources_dir=None, summaries_dir=None, out_dir=None):
    sources_dir = Path(sources_dir) if sources_dir else _default_dir(date, "sources")
    summaries_dir = Path(summaries_dir) if summaries_dir else _default_dir(date, "summaries")
    out_dir = Path(out_dir) if out_dir else Path("workdesk")
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"  inputs: sources={sources_dir}  summaries={summaries_dir}  -> {out_dir}")

    sets = {
        "main": partition.read_ids(sources_dir / partition.MAIN_FILE),
        "annex": partition.read_ids(sources_dir / partition.ANNEX_FILE),
        "omitted": partition.read_ids(sources_dir / partition.OMITTED_FILE),
    }

    counts = {}
    for src_name, out_name, key in JOBS:
        src = sources_dir / src_name
        out = out_dir / out_name
        proc = subprocess.run(
            [sys.executable, UNITE, str(src), str(summaries_dir), str(out)],
            text=True, capture_output=True, check=True,
        )
        n = int(_CREATED.search(proc.stdout).group(1))
        mm = _MISSING.search(proc.stdout)
        missing = int(mm.group(1)) if mm else 0
        counts[key] = n
        expected = len(sets[key])
        if missing:
            raise AssertionError(
                f"{key}: {missing} curated URL(s) have no summary\n{proc.stdout}"
            )
        if n != expected:
            raise AssertionError(
                f"{key}: united {n} summaries but {expected} curated IDs "
                f"(source={src}, summaries={summaries_dir})"
            )
        print(f"  {out_name}: {n} summaries")

    # partition invariant over the same source files
    all_ids = partition.read_ids(sources_dir / partition.ALL_FILE)
    partition.assert_partition(all_ids, sets["main"], sets["annex"], sets["omitted"])
    print(f"✅ partition holds: main={counts['main']} annex={counts['annex']} "
          f"omitted={counts['omitted']} total={len(all_ids)}")
    return counts


def main():
    args = sys.argv[1:]
    opts = {"--out": None, "--sources-dir": None, "--summaries-dir": None}
    for flag in list(opts):
        if flag in args:
            i = args.index(flag)
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    positional = [a for a in args if not a.startswith("--")]
    if len(positional) != 1:
        print("Usage: uv run scripts/build_focused.py <YYYY-MM-DD> [--out DIR] "
              "[--sources-dir DIR] [--summaries-dir DIR]")
        sys.exit(1)

    try:
        build(positional[0], sources_dir=opts["--sources-dir"],
              summaries_dir=opts["--summaries-dir"], out_dir=opts["--out"])
    except AssertionError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"❌ missing input: {e.filename or e}")
        print("   STEP_04 writes curated_journal_sources.md; STEP_05 writes "
              "curated_annex_selected.md (approved annex selection) and "
              "export_curation_flags.py writes omitted_sources.md.")
        sys.exit(1)


if __name__ == "__main__":
    main()
