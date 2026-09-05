#!/usr/bin/env python3
"""Tests for build_focused.py (STEP_06).

Fixture check runs offline in <1s; the golden check reproduces 40/34/119 from
the archived cycle's curated inputs (no network — just reads local files).

Run:
    uv run scripts/test_build_focused.py
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_focused  # noqa: E402

FIX = Path("tests/fixtures/mini-journal/2099-01-01")
GOLDEN_EXISTS = Path("journals/2026-08-22/sources/sources.md").exists()


class TestFixture(unittest.TestCase):
    def test_counts_and_partition(self):
        out = tempfile.mkdtemp()
        counts = build_focused.build(
            "2099-01-01",
            sources_dir=FIX / "sources",
            summaries_dir=FIX / "summaries",
            out_dir=out,
        )
        self.assertEqual(counts, {"main": 2, "annex": 2, "omitted": 2})
        for name in ("unified_summaries_main.md", "unified_summaries_annex.md",
                     "omitted_summaries_unified.md"):
            self.assertTrue((Path(out) / name).exists())

    def test_missing_summary_raises(self):
        # Point at a summaries dir with nothing in it -> every URL unresolved.
        empty = tempfile.mkdtemp()
        with self.assertRaises(AssertionError):
            build_focused.build("2099-01-01", sources_dir=FIX / "sources",
                                summaries_dir=empty, out_dir=tempfile.mkdtemp())


@unittest.skipUnless(GOLDEN_EXISTS, "golden cycle not present")
class TestGolden(unittest.TestCase):
    def test_reproduces_40_34_119(self):
        out = tempfile.mkdtemp()
        counts = build_focused.build("2026-08-22", out_dir=out)
        self.assertEqual(counts, {"main": 40, "annex": 34, "omitted": 119})


if __name__ == "__main__":
    unittest.main(verbosity=2)
