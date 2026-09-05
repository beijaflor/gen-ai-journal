#!/usr/bin/env python3
"""Tests for stitch_qa.py (STEP_08 stitch + QA).

Golden: stitching the committed scratch fragments reproduces the archived 00/01
structure (9 themes/40, 5 sections/34) byte-for-byte and passes QA. A seeded
leak in a fragment makes QA fail.

Run:
    uv run scripts/test_stitch_qa.py
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stitch_qa  # noqa: E402

SCRATCH = Path("tests/fixtures/2026-08-22-scratch")
GOLDEN = Path("journals/2026-08-22")
HAVE = SCRATCH.exists() and GOLDEN.exists()


@unittest.skipUnless(HAVE, "golden scratch / cycle not present")
class TestGoldenStitch(unittest.TestCase):
    def test_reproduces_and_passes_qa(self):
        out = tempfile.mkdtemp()
        rep = stitch_qa.run("2026-08-22", scratch=SCRATCH, out_dir=out,
                            sources_dir=GOLDEN / "sources", skip_urls=True)
        self.assertTrue(rep.ok, msg="\n".join(rep.notes))

    def test_byte_identical_to_archived(self):
        out = tempfile.mkdtemp()
        wk, an = stitch_qa.stitch("2026-08-22", SCRATCH, out)
        self.assertEqual(
            wk.read_text(encoding="utf-8"),
            (GOLDEN / "00_weekly_journal_2026_08_22.md").read_text(encoding="utf-8"))
        self.assertEqual(
            an.read_text(encoding="utf-8"),
            (GOLDEN / "01_annex_journal_2026_08_22.md").read_text(encoding="utf-8"))

    def test_structure_counts(self):
        out = tempfile.mkdtemp()
        wk, an = stitch_qa.stitch("2026-08-22", SCRATCH, out)
        wt = wk.read_text(encoding="utf-8")
        self.assertEqual(sum(1 for l in wt.splitlines() if l.startswith("## ")), 11)
        self.assertEqual(sum(1 for l in wt.splitlines() if l.startswith("### ")), 40)
        self.assertEqual(wt.count("#### 参考リンク"), 9)


@unittest.skipUnless(HAVE, "golden scratch / cycle not present")
class TestSeededLeak(unittest.TestCase):
    def test_leak_in_fragment_fails_qa(self):
        scratch = Path(tempfile.mkdtemp()) / "scratch"
        shutil.copytree(SCRATCH, scratch)
        frag = scratch / "main_theme_01.md"
        frag.write_text(frag.read_text(encoding="utf-8") + "\n原題: Leaked\n",
                        encoding="utf-8")
        rep = stitch_qa.run("2026-08-22", scratch=scratch, out_dir=tempfile.mkdtemp(),
                            sources_dir=GOLDEN / "sources", skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("原題" in f or "score-object" in f for f in rep.failures))


class TestFragmentNumbering(unittest.TestCase):
    def _scratch(self):
        scratch = Path(tempfile.mkdtemp()) / "scratch"
        shutil.copytree(SCRATCH, scratch)
        return scratch

    def test_stray_extra_fragment_fails(self):
        scratch = self._scratch()
        (scratch / "main_theme_99.md").write_text("## stray\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            stitch_qa.stitch("2026-08-22", scratch, tempfile.mkdtemp())

    def test_gap_in_numbering_fails(self):
        scratch = self._scratch()
        (scratch / "annex_sec_03.md").unlink()
        with self.assertRaises(ValueError):
            stitch_qa.stitch("2026-08-22", scratch, tempfile.mkdtemp())

    def test_numeric_order_beyond_nine(self):
        """main_theme_10 must follow main_theme_09 (numeric, not lexical)."""
        scratch = self._scratch()
        (scratch / "main_theme_10.md").write_text("### TENTH-THEME-MARKER\n",
                                                  encoding="utf-8")
        wk, _ = stitch_qa.stitch("2026-08-22", scratch, tempfile.mkdtemp())
        text = wk.read_text(encoding="utf-8")
        ninth = (scratch / "main_theme_09.md").read_text(encoding="utf-8")[:40]
        self.assertGreater(text.index("TENTH-THEME-MARKER"), text.index(ninth))


if __name__ == "__main__":
    unittest.main(verbosity=2)
