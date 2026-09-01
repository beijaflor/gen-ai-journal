#!/usr/bin/env python3
"""Tests for scripts/workflow/partition.py — the partition invariant.

Covers clean / overlap / gap, plus read_ids parsing and verify() over a
tmp-dir fixture cycle.

Run:
    uv run scripts/test_workflow_partition.py
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow import partition  # noqa: E402
from workflow.partition import (  # noqa: E402
    PartitionError,
    read_ids,
    assert_partition,
)


class TestReadIds(unittest.TestCase):
    def _write(self, text):
        d = tempfile.mkdtemp()
        p = Path(d) / "f.md"
        p.write_text(text, encoding="utf-8")
        return p

    def test_parses_checked_and_unchecked(self):
        p = self._write(
            "# Header\n\n"
            "- [ ] 008. https://a.example/x\n"
            "- [x] 077. https://b.example/y\n"
            "not a source line\n"
        )
        self.assertEqual(read_ids(p), {"008", "077"})

    def test_ignores_non_id_lines(self):
        p = self._write("## Theme T1: something\n\ntext https://z.example/q\n")
        self.assertEqual(read_ids(p), set())


class TestAssertPartition(unittest.TestCase):
    def test_clean_returns_none(self):
        all_ids = {"1", "2", "3", "4"}
        self.assertIsNone(assert_partition(all_ids, {"1"}, {"2"}, {"3", "4"}))

    def test_overlap_raises_and_names_id(self):
        all_ids = {"1", "2", "3"}
        with self.assertRaises(PartitionError) as ctx:
            assert_partition(all_ids, {"1", "2"}, {"2"}, {"3"})
        self.assertIn("2", str(ctx.exception))
        self.assertIn("overlap", str(ctx.exception))

    def test_gap_raises_and_names_missing(self):
        all_ids = {"1", "2", "3", "4"}
        with self.assertRaises(PartitionError) as ctx:
            assert_partition(all_ids, {"1"}, {"2"}, {"3"})  # 4 unpartitioned
        self.assertIn("4", str(ctx.exception))

    def test_extra_curated_id_raises(self):
        all_ids = {"1", "2"}
        with self.assertRaises(PartitionError) as ctx:
            assert_partition(all_ids, {"1"}, {"2"}, {"9"})  # 9 not in sources
        self.assertIn("9", str(ctx.exception))


class TestVerify(unittest.TestCase):
    def _build_cycle(self, main, annex, omitted, all_ids):
        d = Path(tempfile.mkdtemp())

        def dump(name, ids):
            (d / name).write_text(
                "".join(f"- [ ] {i}. https://ex.example/{i}\n" for i in ids),
                encoding="utf-8",
            )

        dump(partition.ALL_FILE, all_ids)
        dump(partition.MAIN_FILE, main)
        dump(partition.ANNEX_FILE, annex)
        dump(partition.OMITTED_FILE, omitted)
        return d

    def test_verify_clean(self):
        d = self._build_cycle(["001"], ["002"], ["003", "004"], ["001", "002", "003", "004"])
        s = partition.verify("9999-01-01", workdesk=d)  # date w/o an archive dir
        self.assertEqual(len(s["all"]), 4)

    def test_verify_injected_overlap_raises(self):
        # 002 wrongly appears in both main and annex.
        d = self._build_cycle(["001", "002"], ["002"], ["003"], ["001", "002", "003"])
        with self.assertRaises(PartitionError):
            partition.verify("9999-01-01", workdesk=d)


if __name__ == "__main__":
    unittest.main(verbosity=2)
