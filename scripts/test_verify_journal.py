#!/usr/bin/env python3
"""Tests for verify_journal.py (STEP_09).

The good mini-journal fixture passes every offline check; a seeded leak,
hierarchy fault, and coverage gap each make it fail — proving the checks catch
faults, not just wave things through. All run with --skip-urls (no network).

Run:
    uv run scripts/test_verify_journal.py
"""

import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_journal  # noqa: E402

FIX_ROOT = Path("tests/fixtures/mini-journal")
DATE = "2099-01-01"
US = "2099_01_01"


def fresh_copy():
    """Copy the fixture cycle into a temp journals-dir; return that dir."""
    tmp = Path(tempfile.mkdtemp())
    shutil.copytree(FIX_ROOT / DATE, tmp / DATE)
    return tmp


class TestGoodFixture(unittest.TestCase):
    def test_passes(self):
        rep = verify_journal.verify(DATE, journals_dir=FIX_ROOT, skip_urls=True)
        self.assertTrue(rep.ok, msg="\n".join(rep.notes))


class TestSeededFaults(unittest.TestCase):
    def _weekly(self, root):
        return root / DATE / f"00_weekly_journal_{US}.md"

    def test_leak_in_weekly_fails(self):
        root = fresh_copy()
        wk = self._weekly(root)
        wk.write_text(wk.read_text(encoding="utf-8") + "\n原題: A Leaked Title\n",
                      encoding="utf-8")
        rep = verify_journal.verify(DATE, journals_dir=root, skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("原題" in f or "score-object" in f for f in rep.failures))

    def test_second_h1_fails_hierarchy(self):
        root = fresh_copy()
        wk = self._weekly(root)
        wk.write_text(wk.read_text(encoding="utf-8") + "\n# 二つ目のH1\n",
                      encoding="utf-8")
        rep = verify_journal.verify(DATE, journals_dir=root, skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("exactly one H1" in f for f in rep.failures))

    def test_skipped_level_fails_hierarchy(self):
        root = fresh_copy()
        wk = self._weekly(root)
        # Jump from ## straight to #### with no ### between.
        text = wk.read_text(encoding="utf-8") + "\n##### 深すぎる見出し\n"
        # ensure a jump: last real heading is ### / #### ; add a big jump
        wk.write_text(text.replace("## 今週のハイライト", "## 今週のハイライト\n\n##### 飛び見出し", 1),
                      encoding="utf-8")
        rep = verify_journal.verify(DATE, journals_dir=root, skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("skipped levels" in f for f in rep.failures))

    def test_coverage_gap_fails(self):
        root = fresh_copy()
        wk = self._weekly(root)
        # Remove a curated main URL from the body -> coverage gap.
        text = wk.read_text(encoding="utf-8")
        text = text.replace("https://alpha.example.com/gpt", "", 1)
        wk.write_text(text, encoding="utf-8")
        rep = verify_journal.verify(DATE, journals_dir=root, skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("curated main URL present" in f for f in rep.failures))

    def test_ref_id_mismatch_fails(self):
        root = fresh_copy()
        wk = self._weekly(root)
        # Break a 参考リンク ID so ref-ids != curated main.
        text = wk.read_text(encoding="utf-8").replace(
            f"/journals/{DATE}/001/", f"/journals/{DATE}/999/", 1)
        wk.write_text(text, encoding="utf-8")
        rep = verify_journal.verify(DATE, journals_dir=root, skip_urls=True)
        self.assertFalse(rep.ok)
        self.assertTrue(any("参考リンク IDs == curated main" in f for f in rep.failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
