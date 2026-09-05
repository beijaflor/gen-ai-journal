#!/usr/bin/env python3
"""Tests for archive_journal.py (STEP_10 + STEP_11 metadata, #209).

Covers the 99/02 builders and metadata math on the fixture, the dry-run plan's
file set, that a real archive into a temp dir writes only there, and — when the
golden cycle is present — that it reproduces journals/2026-08-22/ byte-for-byte.

Run:
    uv run scripts/test_archive_metadata.py
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import archive_journal as A  # noqa: E402
from workflow import partition, git_gh  # noqa: E402

FIX_ROOT = "tests/fixtures/mini-journal"
FIX = Path(FIX_ROOT) / "2099-01-01"
GOLDEN = Path("journals/2026-08-22")


class TestBuilders(unittest.TestCase):
    def setUp(self):
        self.files = sorted(str(p) for p in (FIX / "summaries").glob("*.json"))

    def test_99_has_all_entries(self):
        body = A.build_99(self.files, "2099-01-01")
        self.assertEqual(body.count("\n## "), 6)
        self.assertIn("# 全記事要約 2099年01月01日号", body)

    def test_02_only_omitted(self):
        omitted = partition.read_ids(FIX / "sources" / "omitted_sources.md")
        body, n = A.build_02(self.files, omitted, "2099-01-01")
        self.assertEqual(n, 2)
        self.assertEqual(body.count("\n## "), 2)
        # the two omitted IDs (005, 006) appear; a main ID (001) does not
        self.assertIn("## 005_", body)
        self.assertNotIn("## 001_", body)

    def test_metadata_math(self):
        text, meta = A.build_metadata(
            "2099-01-01",
            FIX / "00_weekly_journal_2099_01_01.md",
            FIX / "01_annex_journal_2099_01_01.md",
            total=6, omitted=2)
        self.assertEqual(meta["statistics"],
                         {"mainSummaries": 2, "annexSummaries": 2, "omittedSummaries": 2})
        self.assertEqual(meta["totalSummaries"], 6)
        self.assertTrue(text.endswith("\n"))

    def test_metadata_math_mismatch_raises(self):
        with self.assertRaises(AssertionError):
            A.build_metadata("2099-01-01",
                             FIX / "00_weekly_journal_2099_01_01.md",
                             FIX / "01_annex_journal_2099_01_01.md",
                             total=99, omitted=2)  # 2+2+2 != 99


class TestFixtureArchive(unittest.TestCase):
    def test_real_archive_into_temp(self):
        into = tempfile.mkdtemp()
        A.archive("2099-01-01", into=into, journals_root=FIX_ROOT)
        out = Path(into) / "2099-01-01"
        # inputs copied
        self.assertTrue((out / "00_weekly_journal_2099_01_01.md").exists())
        self.assertEqual(len(list((out / "summaries").glob("*.json"))), 6)
        # built files present and consistent
        meta = json.loads((out / "journal-metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["totalSummaries"], 6)
        self.assertEqual((out / "99_unified_summaries.md").read_text().count("\n## "), 6)
        self.assertEqual((out / "02_omitted_summaries.md").read_text().count("\n## "), 2)


class TestReplayInPlace(unittest.TestCase):
    def test_replay_onto_existing_archive_is_idempotent(self):
        """A clean workdesk + existing journals/<date>/ == replay in place
        (rebuild 99/02/metadata after an archive correction). Must not raise
        SameFileError and must leave the tree byte-identical."""
        import shutil
        root = tempfile.mkdtemp()
        shutil.copytree(FIX, Path(root) / "2099-01-01")
        before = {p: p.read_bytes() for p in Path(root).rglob("*") if p.is_file()}
        cwd = os.getcwd()
        try:
            os.chdir(root)  # no workdesk/ here -> replay mode
            A.archive("2099-01-01", into=root, journals_root=root)
        finally:
            os.chdir(cwd)
        after = {p: p.read_bytes() for p in Path(root).rglob("*") if p.is_file()}
        built = {"99_unified_summaries.md", "02_omitted_summaries.md",
                 "journal-metadata.json"}
        # every input is untouched; only the three built files are added
        for p, b in before.items():
            self.assertEqual(after[p], b, p)
        self.assertEqual({p.name for p in set(after) - set(before)}, built)
        meta = json.loads((Path(root) / "2099-01-01" / "journal-metadata.json")
                          .read_text(encoding="utf-8"))
        self.assertEqual(meta["totalSummaries"], 6)
        # second replay (now with 99/02/metadata present) is byte-idempotent
        try:
            os.chdir(root)
            A.archive("2099-01-01", into=root, journals_root=root)
        finally:
            os.chdir(cwd)
        again = {p: p.read_bytes() for p in Path(root).rglob("*") if p.is_file()}
        self.assertEqual(again, after)


class TestDryRunZeroMutation(unittest.TestCase):
    def test_dry_run_writes_nothing(self):
        into = tempfile.mkdtemp()
        A.archive("2099-01-01", into=into, dry_run=True, journals_root=FIX_ROOT)
        # nothing created under the target
        self.assertEqual(list(Path(into).rglob("*")), [])


@unittest.skipUnless(GOLDEN.exists(), "golden cycle not present")
class TestGolden(unittest.TestCase):
    def test_plan_fileset_equals_archived_tree(self):
        planned = A.output_fileset("2026-08-22", "journals")
        actual = {str(p.relative_to("journals"))
                  for p in GOLDEN.rglob("*") if p.is_file()}
        self.assertEqual(planned, actual)

    def test_real_archive_byte_identical(self):
        into = tempfile.mkdtemp()
        A.archive("2026-08-22", into=into)
        diff = subprocess.run(
            ["diff", "-r", str(Path(into) / "2026-08-22"), str(GOLDEN)],
            capture_output=True, text=True)
        self.assertEqual(diff.returncode, 0, msg=diff.stdout + diff.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
