#!/usr/bin/env python3
"""
Tests for mark_published.py — the --yes/-y flag and arg parsing.

--yes/-y lets non-interactive/agent runs (STEP_10) skip the input() prompt,
replacing the `printf 'yes\\n' |` workaround.

Run:
    python3 scripts/test_mark_published.py
    # or:
    uv run scripts/test_mark_published.py
"""

import os
import sys
import unittest

# create_client() is lazy and only needs non-empty env vars; import under dummy creds.
os.environ.setdefault("SUPABASE_URL", "https://example.supabase.co")
os.environ.setdefault("SUPABASE_SERVICE_KEY", "dummy-key-for-tests")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mark_published as mp  # noqa: E402


class TestParseArgs(unittest.TestCase):
    def test_scoped_default(self):
        self.assertEqual(mp.parse_args(["2026-08-22"]), ("2026-08-22", False, False))

    def test_yes_long(self):
        self.assertEqual(mp.parse_args(["2026-08-22", "--yes"]), ("2026-08-22", False, True))

    def test_yes_short(self):
        self.assertEqual(mp.parse_args(["-y", "2026-08-22"]), ("2026-08-22", False, True))

    def test_all_null_and_yes(self):
        self.assertEqual(mp.parse_args(["2026-08-22", "--all-null", "--yes"]), ("2026-08-22", True, True))

    def test_missing_date_raises(self):
        with self.assertRaises(ValueError):
            mp.parse_args(["--yes"])

    def test_two_positionals_raises(self):
        with self.assertRaises(ValueError):
            mp.parse_args(["2026-08-22", "2026-08-23"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
