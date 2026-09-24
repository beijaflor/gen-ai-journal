"""Tests for ``bulk_summarize.summary_gate`` — the post-generation gate.

call-gemini writes the summary file and exits 0 even when it fails closed, so
``bulk_summarize`` must reject two things before marking a source checked:

  1. a ``BLOCKED:`` plain-text stub (fetch was an interstitial / too short), and
  2. a schema-valid JSON whose ``summaryBody`` is mis-formatted (literal ``\\n``
     escapes, or a heading glued to prose).

A clean JSON summary must pass. These are the gate holes fixed alongside
``fetch_router``'s expanded interstitial signatures.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

# Make ``scripts/`` importable without packaging (mirrors test_fetch_router).
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from bulk_summarize import summary_gate  # noqa: E402


class SummaryGateTest(unittest.TestCase):
    def setUp(self) -> None:
        self._dir = tempfile.TemporaryDirectory()
        self.tmp = Path(self._dir.name)

    def tearDown(self) -> None:
        self._dir.cleanup()

    def _write(self, name: str, text: str) -> Path:
        p = self.tmp / name
        p.write_text(text, encoding="utf-8")
        return p

    def _json(self, name: str, body: str) -> Path:
        return self._write(name, json.dumps({"content": {"summaryBody": body}}, ensure_ascii=False))

    def test_blocked_stub_is_rejected(self) -> None:
        p = self._write(
            "001_x.json",
            "BLOCKED: summary suppressed — fetch did not return usable content.\n\n- URL: https://x/y",
        )
        err = summary_gate(p)
        self.assertTrue(err, "BLOCKED stub must be rejected")
        self.assertIn("blocked", err.lower())

    def test_escaped_newline_body_is_rejected(self) -> None:
        # Literal backslash-n sequences instead of real newlines.
        body = "見出し\\n\\n本文です。\\n1. **項目**: 説明。"
        err = summary_gate(self._json("002_x.json", body))
        self.assertTrue(err)
        self.assertIn("format", err.lower())

    def test_mashed_heading_body_is_rejected(self) -> None:
        body = "### 見出しが本文に癒着している OpenAIが評価用サンドボックスを突破した。 1. **A**: x 2. **B**: y"
        err = summary_gate(self._json("003_x.json", body))
        self.assertTrue(err)
        self.assertIn("format", err.lower())

    def test_clean_body_passes(self) -> None:
        body = "これはきれいな要約本文です。\n\n複数の段落があり、エスケープや癒着はありません。"
        self.assertEqual(summary_gate(self._json("004_x.json", body)), "")


if __name__ == "__main__":
    unittest.main()
