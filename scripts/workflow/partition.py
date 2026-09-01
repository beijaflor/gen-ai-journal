#!/usr/bin/env python3
"""The partition invariant: main + annex + omitted == all sources, disjoint.

Every step that reshapes the three curated sets (STEP_04 curate-main,
STEP_05 curate-annex, STEP_06 focused summaries, STEP_10 archive, and any
mid-cycle #210 revision) re-asserts this here rather than trusting memory.

Source files (canonical names, in workdesk/ during a live cycle and under
journals/<date>/sources/ once archived):

    sources.md                     -> all
    curated_journal_sources.md     -> main
    curated_annex_selected.md      -> annex
    omitted_sources.md             -> omitted
"""

import re
from pathlib import Path

# `- [ ] 196. https://...` or `- [x] 008. https://...` (checkbox state ignored).
_ID_LINE = re.compile(r'^\s*-\s*\[[ xX]\]\s*(\d+)\.')

ALL_FILE = "sources.md"
MAIN_FILE = "curated_journal_sources.md"
ANNEX_FILE = "curated_annex_selected.md"
OMITTED_FILE = "omitted_sources.md"


class PartitionError(AssertionError):
    """Raised when main/annex/omitted do not partition the full source set."""


def read_ids(path):
    """Parse ``- [ ] NNN. url`` lines from ``path`` -> set of ID strings.

    IDs are returned as written (zero-padded ``NNN``); the whole workflow uses
    a single consistent format, so no normalisation is needed. A missing file
    raises FileNotFoundError so callers do not silently treat it as empty.
    """
    ids = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = _ID_LINE.match(line)
            if m:
                ids.add(m.group(1))
    return ids


def assert_partition(all_ids, main, annex, omitted):
    """Assert the three sets partition ``all_ids``. Raise PartitionError, else None.

    The error message names the exact offending IDs so a broken cycle is
    debuggable without re-deriving the sets by hand.
    """
    problems = []

    for a_name, a, b_name, b in (
        ("main", main, "annex", annex),
        ("main", main, "omitted", omitted),
        ("annex", annex, "omitted", omitted),
    ):
        overlap = a & b
        if overlap:
            problems.append(
                f"{a_name} ∩ {b_name} overlap: {sorted(overlap)}"
            )

    union = main | annex | omitted
    missing = all_ids - union
    if missing:
        problems.append(f"in sources but unpartitioned: {sorted(missing)}")
    extra = union - all_ids
    if extra:
        problems.append(f"curated but not in sources: {sorted(extra)}")

    if problems:
        raise PartitionError(
            "partition invariant violated (main+annex+omitted != all sources):\n  "
            + "\n  ".join(problems)
        )
    return None


def _resolve_sources_dir(date, workdesk):
    """Prefer the archived cycle's sources/ dir; fall back to the live workdesk."""
    archived = Path(f"journals/{date}/sources")
    if archived.is_dir():
        return archived
    return Path(workdesk)


def verify(date, workdesk=Path("workdesk")):
    """Read a cycle's curated files and assert the partition.

    Uses ``journals/<date>/sources/`` if that archived directory exists,
    otherwise ``workdesk`` (override the base dir via the ``workdesk`` arg in
    tests). Returns the {name: id-set} mapping on success; raises PartitionError
    (or FileNotFoundError for a missing file) on failure.
    """
    src = _resolve_sources_dir(date, workdesk)
    sets = {
        "all": read_ids(src / ALL_FILE),
        "main": read_ids(src / MAIN_FILE),
        "annex": read_ids(src / ANNEX_FILE),
        "omitted": read_ids(src / OMITTED_FILE),
    }
    assert_partition(sets["all"], sets["main"], sets["annex"], sets["omitted"])
    return sets


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python -m scripts.workflow.partition <YYYY-MM-DD>")
        sys.exit(1)
    try:
        s = verify(sys.argv[1])
    except (PartitionError, FileNotFoundError) as e:
        print(f"❌ {e}")
        sys.exit(1)
    print(
        f"✅ partition holds for {sys.argv[1]}: "
        f"main={len(s['main'])} annex={len(s['annex'])} "
        f"omitted={len(s['omitted'])} total={len(s['all'])}"
    )
