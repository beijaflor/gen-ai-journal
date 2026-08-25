#!/usr/bin/env python3
"""
Tests for sanitize_url — specifically the dub.co link-tracking param strip
(via / dub_id), added because granola.ai was submitted 3x across journal
cycles with a rotating `dub_id` query param, defeating substring-based
duplicate detection.

Run:
    python3 scripts/test_sanitize_url.py
    # or:
    uv run scripts/test_sanitize_url.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_link import sanitize_url as sanitize_url_check_link  # noqa: E402
from sanitize_url import sanitize_url as sanitize_url_cli  # noqa: E402


class SanitizeUrlDubTrackingTests(unittest.TestCase):
    def test_granola_via_and_dub_id_stripped(self):
        url = (
            "https://www.granola.ai/"
            "?utm_source=affiliate&via=sidebar&dub_id=GR9SgkWn4Tk3zDYS"
        )
        self.assertEqual(
            sanitize_url_check_link(url), "https://www.granola.ai/"
        )

    def test_via_only_stripped(self):
        url = "https://example.com/page?via=sidebar"
        self.assertEqual(
            sanitize_url_check_link(url), "https://example.com/page"
        )

    def test_dub_id_only_stripped(self):
        url = "https://example.com/page?dub_id=abc123XYZ"
        self.assertEqual(
            sanitize_url_check_link(url), "https://example.com/page"
        )

    def test_legitimate_params_preserved(self):
        # Control case: a non-tracking query param must survive sanitization
        # so the fix doesn't over-strip.
        url = "https://example.com/search?id=123&q=foo"
        result = sanitize_url_check_link(url)
        self.assertIn("id=123", result)
        self.assertIn("q=foo", result)

    def test_check_link_and_cli_copies_agree(self):
        # scripts/check_link.py and scripts/sanitize_url.py maintain
        # duplicate strip lists by design (see CLAUDE.md) — assert they
        # stay in sync for the dub.co case.
        urls = [
            "https://www.granola.ai/?utm_source=affiliate&via=sidebar&dub_id=GR9SgkWn4Tk3zDYS",
            "https://example.com/page?via=sidebar",
            "https://example.com/page?dub_id=abc123XYZ",
            "https://example.com/search?id=123&q=foo",
        ]
        for url in urls:
            self.assertEqual(
                sanitize_url_check_link(url), sanitize_url_cli(url)
            )


if __name__ == "__main__":
    unittest.main()
