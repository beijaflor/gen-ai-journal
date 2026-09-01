#!/usr/bin/env python3
"""Tests for scripts/workflow/urls.py — the single source of the URL regex.

Run:
    uv run scripts/test_workflow_urls.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow.urls import (  # noqa: E402
    URL_PATTERN,
    clean_url,
    urls_in_line,
    extract_urls,
    exact_filter,
)


class TestCleanUrl(unittest.TestCase):
    def test_strips_trailing_punctuation(self):
        self.assertEqual(clean_url("https://example.com/a."), "https://example.com/a")
        self.assertEqual(clean_url("https://example.com/a),"), "https://example.com/a")

    def test_leaves_clean_url(self):
        self.assertEqual(clean_url("https://example.com/a"), "https://example.com/a")


class TestUrlsInLine(unittest.TestCase):
    def test_extracts_from_checkbox_line(self):
        self.assertEqual(
            urls_in_line("- [ ] 077. https://openrouter.ai/openai/gpt-5.6-sol"),
            ["https://openrouter.ai/openai/gpt-5.6-sol"],
        )

    def test_checked_line(self):
        self.assertEqual(
            urls_in_line("- [x] 001. https://zenn.dev/mkj/articles/aad5698672aef3"),
            ["https://zenn.dev/mkj/articles/aad5698672aef3"],
        )

    def test_line_without_url(self):
        self.assertEqual(urls_in_line("# Sources for Journal 2026-08-22"), [])


class TestExtractUrls(unittest.TestCase):
    def test_multiple_urls_order_preserved(self):
        text = "a https://a.example/x b\nc https://b.example/y"
        self.assertEqual(extract_urls(text), ["https://a.example/x", "https://b.example/y"])

    def test_pattern_is_the_shared_constant(self):
        # Guard against a silent second copy of the regex creeping back in.
        self.assertIn("https?://", URL_PATTERN)


class TestExactFilter(unittest.TestCase):
    def test_prefix_collision_not_dropped(self):
        lines = [
            "- [ ] 115. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B\n",
            "- [ ] 120. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8\n",
        ]
        kept = exact_filter(lines, {"https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"})
        self.assertEqual(
            kept, ["- [ ] 120. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8\n"]
        )

    def test_exact_removal(self):
        lines = ["- [ ] 001. https://a.example/x\n", "- [ ] 002. https://b.example/y\n"]
        kept = exact_filter(lines, {"https://a.example/x"})
        self.assertEqual(kept, ["- [ ] 002. https://b.example/y\n"])

    def test_non_url_lines_preserved(self):
        lines = ["# Header\n", "\n", "- [ ] 001. https://a.example/x\n"]
        kept = exact_filter(lines, {"https://a.example/x"})
        self.assertEqual(kept, ["# Header\n", "\n"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
