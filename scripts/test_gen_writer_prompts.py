#!/usr/bin/env python3
"""Tests for gen_writer_prompts.py (STEP_08 assist).

Snapshot: generate() against the committed fixture editorial_plan reproduces the
committed prompt snapshot exactly. Also unit-tests the parsers.

Run:
    uv run scripts/test_gen_writer_prompts.py
"""

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_writer_prompts as G  # noqa: E402

FIX = Path("tests/fixtures/mini-journal/2099-01-01")
SNAP = Path("tests/fixtures/gen_prompts_snapshot")


class TestParsers(unittest.TestCase):
    def test_parse_curated_main(self):
        secs = G.parse_sections(FIX / "sources" / "curated_journal_sources.md")
        self.assertEqual(len(secs), 2)
        self.assertEqual(secs[0][1], ["001"])
        self.assertIn("Theme T1", secs[0][0])

    def test_parse_curated_annex(self):
        secs = G.parse_sections(FIX / "sources" / "curated_annex_selected.md")
        self.assertEqual(len(secs), 1)
        self.assertEqual(secs[0][1], ["003", "004"])

    def test_parse_plan_strategy_blocks(self):
        blocks = G.parse_plan_blocks(
            FIX / "50_editorial_plan_2099_01_01.md", "ASSEMBLY STRATEGIES")
        self.assertEqual(len(blocks), 2)
        self.assertIn("Single-Focus", blocks[0])
        self.assertIn("Multi-Perspective", blocks[1])

    def test_parse_plan_intro_blocks(self):
        blocks = G.parse_plan_blocks(
            FIX / "50_editorial_plan_2099_01_01.md", "Identified Themes")
        self.assertEqual(len(blocks), 2)

    def test_missing_plan_returns_empty(self):
        self.assertEqual(G.parse_plan_blocks(None, "ASSEMBLY STRATEGIES"), [])


class TestSnapshot(unittest.TestCase):
    def test_generate_matches_snapshot(self):
        prompts = G.generate(
            "2099-01-01",
            FIX / "sources",
            FIX / "50_editorial_plan_2099_01_01.md",
            FIX / "summaries",
            out_dir="scratchpad", scratch_out="scratchpad")
        committed = {p.name for p in SNAP.glob("prompt_*.md")}
        self.assertEqual(set(prompts), committed)
        for name, content in prompts.items():
            expected = (SNAP / name).read_text(encoding="utf-8")
            self.assertEqual(content, expected, msg=f"snapshot drift in {name}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
