#!/usr/bin/env python3
"""
Unified summary validator (v1.0 schema).

This module exposes a single validation entry point that all summary
generation paths (gemini primary, direct-fetch fallback, Playwright
fallback, etc.) must call before writing a summary to disk. The goal is
to keep validation behavior identical across paths so invalid summaries
never reach `workdesk/summaries/`.

API:
    validate(summary: dict) -> ValidationResult
        Returns ValidationResult with .ok flag and structured error info.

    validate_first_error(summary: dict) -> Tuple[bool, Optional[str]]
        Backwards-compatible helper that returns (ok, first_error_message)
        — matches the previous inline call-gemini.py contract.

CLI:
    python scripts/validate_summary.py path/to/summary.json
        Exit 0 on pass; non-zero with stderr message on fail.

The schema rules implemented here are extracted verbatim from the
inline checks previously embedded in `scripts/call-gemini.py` and the
batch checks in `scripts/validate_summaries.py`. No new rules have
been added (issue #113 scope: consolidation only).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Required top-level fields
_REQUIRED_TOP_LEVEL = ("metadata", "content")

# Required metadata fields
_REQUIRED_METADATA_FIELDS = ("version", "generatedAt", "generatedBy")
_EXPECTED_VERSION = "1.0"

# Required content fields
_REQUIRED_CONTENT_FIELDS = (
    "title",
    "url",
    "language",
    "contentType",
    "oneSentenceSummary",
    "summaryBody",
    "topics",
    "scores",
)

# Score field groups
_DIMENSION_SCORE_FIELDS = ("signal", "depth", "uniqueness", "practical", "antiHype")
_COMPOSITE_SCORE_FIELDS = ("mainJournal", "annexPotential", "overall")
_REQUIRED_SCORE_FIELDS = _DIMENSION_SCORE_FIELDS + _COMPOSITE_SCORE_FIELDS

# Length limits
_TITLE_MIN, _TITLE_MAX = 1, 200
_ONE_SENTENCE_MIN, _ONE_SENTENCE_MAX = 10, 300
_SUMMARY_BODY_MIN, _SUMMARY_BODY_MAX = 100, 1200
_TOPICS_MIN, _TOPICS_MAX = 1, 5
_DIMENSION_SCORE_MIN, _DIMENSION_SCORE_MAX = 0, 5
_COMPOSITE_SCORE_MIN, _COMPOSITE_SCORE_MAX = 0, 100


@dataclass
class ValidationResult:
    """Outcome of validating a summary dict.

    Attributes:
        ok: True iff the summary passes every rule.
        errors: List of human-readable error strings. Empty when ok.
        first_error: Convenience accessor for the first error, or None.
    """

    ok: bool
    errors: List[str] = field(default_factory=list)

    @property
    def first_error(self) -> Optional[str]:
        return self.errors[0] if self.errors else None

    def __bool__(self) -> bool:  # noqa: D401 - allows `if result:`
        return self.ok


def _check_top_level(data: Any, errors: List[str]) -> bool:
    """Return True if `data` is a dict with required top-level keys."""
    if not isinstance(data, dict):
        errors.append("Summary must be a JSON object")
        return False
    missing = [k for k in _REQUIRED_TOP_LEVEL if k not in data]
    if missing:
        # Preserve the historical message verbatim from the inline
        # call-gemini.py validator so consumers that match on this
        # string keep working.
        errors.append("Missing required top-level fields: metadata or content")
        return False
    return True


def _check_metadata(metadata: Any, errors: List[str]) -> None:
    if not isinstance(metadata, dict):
        errors.append("Field 'metadata' must be an object")
        return

    version = metadata.get("version")
    if version != _EXPECTED_VERSION:
        errors.append(f"Invalid version: {version}, expected '{_EXPECTED_VERSION}'")

    if not metadata.get("generatedAt"):
        errors.append("Missing generatedAt in metadata")

    if not metadata.get("generatedBy"):
        errors.append("Missing generatedBy in metadata")


def _check_content_required_fields(content: Any, errors: List[str]) -> bool:
    if not isinstance(content, dict):
        errors.append("Field 'content' must be an object")
        return False
    ok = True
    for field_name in _REQUIRED_CONTENT_FIELDS:
        if field_name not in content:
            errors.append(f"Missing required content field: {field_name}")
            ok = False
    return ok


def _check_scores(scores: Any, errors: List[str]) -> None:
    if not isinstance(scores, dict):
        errors.append("Field 'scores' must be an object")
        return

    for field_name in _REQUIRED_SCORE_FIELDS:
        if field_name not in scores:
            errors.append(f"Missing required score field: {field_name}")

    # Note: Python bools are a subclass of int, so True/False would
    # pass the isinstance(int) check. The historical inline validator
    # in call-gemini.py also accepted bools as valid scores; we
    # preserve that behavior verbatim.
    for name in _DIMENSION_SCORE_FIELDS:
        score = scores.get(name)
        if score is None:
            continue
        if (
            not isinstance(score, int)
            or score < _DIMENSION_SCORE_MIN
            or score > _DIMENSION_SCORE_MAX
        ):
            errors.append(
                f"Dimension score out of range "
                f"({_DIMENSION_SCORE_MIN}-{_DIMENSION_SCORE_MAX}): {score}"
            )

    for name in _COMPOSITE_SCORE_FIELDS:
        score = scores.get(name)
        if score is None:
            continue
        if (
            not isinstance(score, int)
            or score < _COMPOSITE_SCORE_MIN
            or score > _COMPOSITE_SCORE_MAX
        ):
            errors.append(
                f"Composite score out of range "
                f"({_COMPOSITE_SCORE_MIN}-{_COMPOSITE_SCORE_MAX}): {score}"
            )


def _check_topics(topics: Any, errors: List[str]) -> None:
    if not isinstance(topics, list):
        errors.append("Topics must be an array")
        return
    if len(topics) < _TOPICS_MIN or len(topics) > _TOPICS_MAX:
        errors.append(
            f"Topics array must have {_TOPICS_MIN}-{_TOPICS_MAX} elements, "
            f"got {len(topics)}"
        )


def _check_string_lengths(content: Dict[str, Any], errors: List[str]) -> None:
    title = content.get("title")
    if isinstance(title, str):
        if len(title) < _TITLE_MIN or len(title) > _TITLE_MAX:
            errors.append(
                f"Title length out of range ({_TITLE_MIN}-{_TITLE_MAX}): {len(title)}"
            )

    one_sentence = content.get("oneSentenceSummary")
    if isinstance(one_sentence, str):
        if len(one_sentence) < _ONE_SENTENCE_MIN or len(one_sentence) > _ONE_SENTENCE_MAX:
            errors.append(
                f"One sentence summary length out of range "
                f"({_ONE_SENTENCE_MIN}-{_ONE_SENTENCE_MAX}): {len(one_sentence)}"
            )

    summary_body = content.get("summaryBody")
    if isinstance(summary_body, str):
        if len(summary_body) < _SUMMARY_BODY_MIN or len(summary_body) > _SUMMARY_BODY_MAX:
            errors.append(
                f"Summary body length out of range "
                f"({_SUMMARY_BODY_MIN}-{_SUMMARY_BODY_MAX}): {len(summary_body)}"
            )


def validate(summary: Dict[str, Any]) -> ValidationResult:
    """Validate a parsed summary dict against the v1.0 schema.

    Args:
        summary: Parsed JSON summary (already deserialized from disk
            or freshly produced by a generator).

    Returns:
        ValidationResult. `.ok` is True iff every rule passed.
        On failure, `.errors` contains every detected error so callers
        can either log all of them or surface only the first.
    """
    errors: List[str] = []

    try:
        if not _check_top_level(summary, errors):
            return ValidationResult(ok=False, errors=errors)

        _check_metadata(summary.get("metadata"), errors)

        content = summary.get("content")
        if _check_content_required_fields(content, errors):
            # `content` is guaranteed to be a dict here.
            assert isinstance(content, dict)
            _check_scores(content.get("scores"), errors)
            _check_topics(content.get("topics"), errors)
            _check_string_lengths(content, errors)
    except Exception as exc:  # defensive: never raise from validate()
        errors.append(f"Validation error: {exc}")

    return ValidationResult(ok=not errors, errors=errors)


def validate_first_error(summary: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Backwards-compatible wrapper matching the original call-gemini API.

    Returns:
        (ok, first_error_message_or_None)
    """
    result = validate(summary)
    return result.ok, result.first_error


def _load_summary(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Load a summary JSON file. Returns (data, error_message)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except FileNotFoundError:
        return None, f"File not found: {path}"
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON in {path}: {e}"
    except OSError as e:
        return None, f"Cannot read {path}: {e}"


def _cli(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a summary JSON file against the v1.0 schema. "
            "Returns exit 0 on pass, non-zero with stderr message on fail."
        )
    )
    parser.add_argument(
        "path",
        help="Path to a summary .json file",
    )
    parser.add_argument(
        "--all-errors",
        action="store_true",
        help="Print every detected error (default: first error only)",
    )
    args = parser.parse_args(argv)

    path = Path(args.path)
    data, load_err = _load_summary(path)
    if load_err is not None:
        print(f"validate_summary: {load_err}", file=sys.stderr)
        return 2

    assert data is not None
    result = validate(data)
    if result.ok:
        return 0

    if args.all_errors:
        for err in result.errors:
            print(f"validate_summary: {path}: {err}", file=sys.stderr)
    else:
        print(
            f"validate_summary: {path}: {result.first_error}",
            file=sys.stderr,
        )
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
