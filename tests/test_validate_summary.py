#!/usr/bin/env python3
"""Smoke tests for `scripts/validate_summary.py`.

Run from the repo root:

    python -m unittest tests.test_validate_summary
    # or
    uv run python -m unittest tests.test_validate_summary

These tests cover the cases enumerated in issue #113 acceptance criteria:
    - valid summary passes
    - missing required field fails
    - >5 topics fails
    - malformed JSON fails (CLI path)
"""

from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Make `scripts/` importable without packaging.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from validate_summary import (  # noqa: E402
    ValidationResult,
    validate,
    validate_first_error,
)


def _valid_summary() -> dict:
    """Return a fresh, schema-compliant summary dict for each test."""
    return {
        "metadata": {
            "version": "1.0",
            "generatedAt": "2026-04-20T16:31:28.727919+00:00",
            "generatedBy": "gemini-3-flash-preview",
        },
        "content": {
            "title": "テスト記事のタイトル",
            "url": "https://example.com/article",
            "language": "ja",
            "contentType": "🔬 Research & Analysis (研究・分析)",
            "oneSentenceSummary": (
                "テスト目的のために用意された、十分な長さを持つ"
                "ワンセンテンスのサマリーです。"
            ),
            "summaryBody": (
                "これは検証用のサマリー本文で、最低文字数（100文字）を"
                "確実に超えるように複数の文を連ねて記述しています。"
                "内容自体は意味を持たないダミーですが、長さの境界条件を"
                "満たすことで、バリデーターが正常に通過することを確認します。"
            ),
            "topics": ["AI", "テスト", "検証"],
            "scores": {
                "signal": 4,
                "depth": 3,
                "uniqueness": 4,
                "practical": 5,
                "antiHype": 3,
                "mainJournal": 80,
                "annexPotential": 70,
                "overall": 78,
            },
        },
    }


class ValidateValidSummaryTest(unittest.TestCase):
    """Valid summary should pass."""

    def test_valid_summary_passes(self) -> None:
        result = validate(_valid_summary())
        self.assertIsInstance(result, ValidationResult)
        self.assertTrue(result.ok, msg=f"Expected pass, got errors: {result.errors}")
        self.assertEqual(result.errors, [])
        self.assertIsNone(result.first_error)

    def test_validate_first_error_wrapper_on_valid(self) -> None:
        ok, msg = validate_first_error(_valid_summary())
        self.assertTrue(ok)
        self.assertIsNone(msg)


class MissingRequiredFieldTest(unittest.TestCase):
    """Missing required fields must fail."""

    def test_missing_top_level_metadata_fails(self) -> None:
        s = _valid_summary()
        del s["metadata"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("metadata", result.first_error or "")

    def test_missing_top_level_content_fails(self) -> None:
        s = _valid_summary()
        del s["content"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("content", result.first_error or "")

    def test_missing_metadata_version_fails(self) -> None:
        s = _valid_summary()
        del s["metadata"]["version"]
        result = validate(s)
        self.assertFalse(result.ok)
        # Behaves like the original: version=None != '1.0'
        self.assertIn("version", (result.first_error or "").lower())

    def test_missing_metadata_generated_at_fails(self) -> None:
        s = _valid_summary()
        del s["metadata"]["generatedAt"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("generatedAt", result.first_error or "")

    def test_missing_content_title_fails(self) -> None:
        s = _valid_summary()
        del s["content"]["title"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("title", result.first_error or "")

    def test_missing_content_summary_body_fails(self) -> None:
        s = _valid_summary()
        del s["content"]["summaryBody"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("summaryBody", result.first_error or "")

    def test_missing_score_field_fails(self) -> None:
        s = _valid_summary()
        del s["content"]["scores"]["signal"]
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("signal", result.first_error or "")


class TopicsArrayTest(unittest.TestCase):
    """Topics array length must be 1-5."""

    def test_more_than_five_topics_fails(self) -> None:
        s = _valid_summary()
        s["content"]["topics"] = ["a", "b", "c", "d", "e", "f"]  # 6 items
        result = validate(s)
        self.assertFalse(result.ok)
        # The first error here will be about topics length (the topics
        # check runs after content/scores checks have passed).
        joined = " ".join(result.errors)
        self.assertIn("Topics", joined)
        self.assertIn("6", joined)

    def test_zero_topics_fails(self) -> None:
        s = _valid_summary()
        s["content"]["topics"] = []
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Topics", " ".join(result.errors))

    def test_topics_not_an_array_fails(self) -> None:
        s = _valid_summary()
        s["content"]["topics"] = "AI"  # not a list
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Topics must be an array", " ".join(result.errors))

    def test_exactly_five_topics_passes(self) -> None:
        s = _valid_summary()
        s["content"]["topics"] = ["a", "b", "c", "d", "e"]
        result = validate(s)
        self.assertTrue(result.ok, msg=f"Expected pass, got: {result.errors}")


class ScoreRangeTest(unittest.TestCase):
    """Score range checks: dimensions 0-5, composites 0-100."""

    def test_dimension_score_above_max_fails(self) -> None:
        s = _valid_summary()
        s["content"]["scores"]["signal"] = 6
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Dimension score out of range", " ".join(result.errors))

    def test_composite_score_above_max_fails(self) -> None:
        s = _valid_summary()
        s["content"]["scores"]["overall"] = 101
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Composite score out of range", " ".join(result.errors))

    def test_dimension_score_negative_fails(self) -> None:
        s = _valid_summary()
        s["content"]["scores"]["depth"] = -1
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Dimension score out of range", " ".join(result.errors))


class StringLengthTest(unittest.TestCase):
    """String length boundaries."""

    def test_summary_body_too_short_fails(self) -> None:
        s = _valid_summary()
        s["content"]["summaryBody"] = "short"
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn("Summary body length out of range", " ".join(result.errors))

    def test_one_sentence_summary_too_short_fails(self) -> None:
        s = _valid_summary()
        s["content"]["oneSentenceSummary"] = "hi"
        result = validate(s)
        self.assertFalse(result.ok)
        self.assertIn(
            "One sentence summary length out of range",
            " ".join(result.errors),
        )


class CliTest(unittest.TestCase):
    """CLI: exit 0 on pass, non-zero on fail; malformed JSON also fails."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.script = SCRIPTS_DIR / "validate_summary.py"
        cls.assertTrue = unittest.TestCase.assertTrue  # type: ignore[assignment]
        if not cls.script.exists():
            raise unittest.SkipTest(f"Script not found: {cls.script}")

    def _run(self, path: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.script), path],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_valid_returns_zero(self) -> None:
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(_valid_summary(), f, ensure_ascii=False)
            path = f.name
        try:
            proc = self._run(path)
            self.assertEqual(
                proc.returncode,
                0,
                msg=f"stdout={proc.stdout!r} stderr={proc.stderr!r}",
            )
        finally:
            os.unlink(path)

    def test_cli_invalid_returns_nonzero(self) -> None:
        s = _valid_summary()
        s["content"]["topics"] = ["a", "b", "c", "d", "e", "f"]  # 6 items
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(s, f, ensure_ascii=False)
            path = f.name
        try:
            proc = self._run(path)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("validate_summary", proc.stderr)
        finally:
            os.unlink(path)

    def test_cli_malformed_json_returns_nonzero(self) -> None:
        with tempfile.NamedTemporaryFile(
            "w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            f.write("{not valid json")
            path = f.name
        try:
            proc = self._run(path)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("Invalid JSON", proc.stderr)
        finally:
            os.unlink(path)

    def test_cli_missing_file_returns_nonzero(self) -> None:
        proc = self._run("/tmp/this-file-does-not-exist-12345.json")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("File not found", proc.stderr)


class IsolationTest(unittest.TestCase):
    """The validator must not mutate the input dict."""

    def test_validate_does_not_mutate_input(self) -> None:
        s = _valid_summary()
        s_copy = copy.deepcopy(s)
        validate(s)
        self.assertEqual(s, s_copy)


if __name__ == "__main__":
    unittest.main()
