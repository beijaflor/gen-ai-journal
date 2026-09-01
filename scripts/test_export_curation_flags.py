#!/usr/bin/env python3
"""
Tests for export_curation_flags.py — the 0-omit fix.

When nothing is flagged for omission, export_omitted_sources used to `return`
without writing workdesk/omitted_sources.md. A later `git add ... omitted_sources.md`
then failed (file not found) and aborted the whole staging (recurring
STEP_03b/05 gotcha). The file is now always written, even at 0 omits.

Run:
    python3 scripts/test_export_curation_flags.py
    # or:
    uv run scripts/test_export_curation_flags.py
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# create_client() only needs non-empty env vars; it is lazy (no network until a query),
# so we can import the module with dummy credentials and test the pure file-writer.
os.environ.setdefault("SUPABASE_URL", "https://example.supabase.co")
os.environ.setdefault("SUPABASE_SERVICE_KEY", "dummy-key-for-tests")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import export_curation_flags as ecf  # noqa: E402


class TestExportOmittedSources(unittest.TestCase):
    def setUp(self):
        self._orig = ecf.OMITTED_FILE
        self._tmp = tempfile.NamedTemporaryFile(suffix=".md", delete=False)
        self._tmp.close()
        ecf.OMITTED_FILE = Path(self._tmp.name)

    def tearDown(self):
        ecf.OMITTED_FILE = self._orig
        os.unlink(self._tmp.name)

    def test_zero_omit_still_writes_file(self):
        # Remove the file first to prove the function (re)creates it.
        os.unlink(self._tmp.name)
        ecf.export_omitted_sources([])  # no summaries flagged
        self.assertTrue(ecf.OMITTED_FILE.exists(), "omitted_sources.md must exist even at 0 omits")
        text = ecf.OMITTED_FILE.read_text(encoding="utf-8")
        self.assertIn("# Omitted Sources", text)
        self.assertIn("Total: 0", text)

    def test_with_omits_writes_entries(self):
        meta = [
            {"omit_flag": True, "summary_id": "005", "url": "https://a.example/x"},
            {"omit_flag": False, "summary_id": "006", "url": "https://b.example/y"},
        ]
        ecf.export_omitted_sources(meta)
        text = ecf.OMITTED_FILE.read_text(encoding="utf-8")
        self.assertIn("005. https://a.example/x", text)
        self.assertNotIn("https://b.example/y", text)  # not flagged → excluded


if __name__ == "__main__":
    unittest.main(verbosity=2)
