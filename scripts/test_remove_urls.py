#!/usr/bin/env python3
"""
Tests for remove_urls.py — specifically the prefix-collision fix.

The old implementation removed a line when a removal URL was a *substring*
of the line, so removing ".../Qwen3.8-2.4T-A95B" also dropped the line for
".../Qwen3.8-2.4T-A95B-FP8" (its prefix). That silently under-counted the
non_main partition in STEP_04/05. remove_urls now matches whole URLs exactly.

Run:
    python3 scripts/test_remove_urls.py
    # or:
    uv run scripts/test_remove_urls.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from remove_urls import filter_lines, urls_in_line, clean_url  # noqa: E402


class TestUrlsInLine(unittest.TestCase):
    def test_extracts_and_cleans(self):
        self.assertEqual(
            urls_in_line("- [ ] 077. https://openrouter.ai/openai/gpt-5.6-sol"),
            ["https://openrouter.ai/openai/gpt-5.6-sol"],
        )

    def test_strips_trailing_punctuation(self):
        self.assertEqual(clean_url("https://example.com/a."), "https://example.com/a")

    def test_line_without_url(self):
        self.assertEqual(urls_in_line("# Sources for Journal 2026-08-22"), [])


class TestFilterLines(unittest.TestCase):
    def test_prefix_collision_not_dropped(self):
        """Removing the prefix URL must NOT drop the longer URL's line."""
        lines = [
            "- [ ] 115. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B\n",
            "- [ ] 120. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8\n",
        ]
        kept = filter_lines(lines, {"https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"})
        # Only the exact match (115) is removed; 120 survives.
        self.assertEqual(kept, ["- [ ] 120. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8\n"])

    def test_exact_removal(self):
        lines = [
            "- [ ] 001. https://a.example/x\n",
            "- [ ] 002. https://b.example/y\n",
        ]
        kept = filter_lines(lines, {"https://a.example/x"})
        self.assertEqual(kept, ["- [ ] 002. https://b.example/y\n"])

    def test_non_url_lines_preserved(self):
        lines = ["# Header\n", "\n", "- [ ] 001. https://a.example/x\n"]
        kept = filter_lines(lines, {"https://a.example/x"})
        self.assertEqual(kept, ["# Header\n", "\n"])

    def test_removal_url_with_trailing_punctuation(self):
        """Removal URLs are cleaned too, so trailing punctuation still matches."""
        lines = ["- [ ] 001. https://a.example/x\n"]
        kept = filter_lines(lines, {"https://a.example/x."})
        self.assertEqual(kept, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
