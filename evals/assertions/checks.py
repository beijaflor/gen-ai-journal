"""All Layer-① assertions in one module.

promptfoo references these as file://assertions/checks.py:<function>.
Each function has the promptfoo contract (output, context) -> GradingResult.
The heavyweight checks delegate to the PRODUCTION validators —
scripts/validate_summary.py (the repo's hard gate, issue #113) and
scripts/summary_review.py — this module is only the signature adapter
plus the eval-only repair-layer simulation.

Semantics mirror call-gemini.py's post-generation repair layer
(lines ~1011-1057): what production ships broken HARD-FAILS here; what
it silently fixes is a SOFT metric (always pass=True, drift reported
via the 0/1 score).
"""

import json
import sys
from pathlib import Path

_EVALS_DIR = Path(__file__).resolve().parents[1]
_SCRIPTS_DIR = _EVALS_DIR.parent / "scripts"
_RESPONSE_SCHEMA_PATH = _EVALS_DIR / "response-schema.json"


def _ensure_scripts_on_path():
    if str(_SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(_SCRIPTS_DIR))


def _parse(output):
    """Parse model output into a summary dict. Returns (data, error)."""
    if isinstance(output, dict):
        data = output
    else:
        try:
            data = json.loads(output)
        except (TypeError, ValueError) as exc:
            return None, f"output is not valid JSON: {exc}"
    if not isinstance(data, dict):
        return None, f"output is JSON but not an object (got {type(data).__name__})"
    return data, None


def _stamp_metadata(data):
    """Replicate call_gemini_structured's unconditional metadata overwrite."""
    metadata = data.setdefault("metadata", {})
    metadata["version"] = "1.0"
    metadata["generatedAt"] = "1970-01-01T00:00:00+00:00"
    metadata["generatedBy"] = "promptfoo-eval"
    return data


def _schema_enum(field_name):
    schema = json.loads(_RESPONSE_SCHEMA_PATH.read_text(encoding="utf-8"))
    return schema["properties"]["content"]["properties"][field_name]["enum"]


def _fail(reason):
    return {"pass": False, "score": 0.0, "reason": reason}


def _ok(reason, score=1.0):
    return {"pass": True, "score": score, "reason": reason}


# --- hard fails: production ships broken (or exits) when these fail ---


def schema_valid(output, context):
    """v1.0 schema via scripts/validate_summary.py (production hard gate)."""
    data, err = _parse(output)
    if err:
        return _fail(err)
    _stamp_metadata(data)

    _ensure_scripts_on_path()
    from validate_summary import validate

    result = validate(data)
    if result.ok:
        return _ok("schema valid")
    return _fail("; ".join(result.errors[:5]))


def language_enum(output, context):
    """content.language in the schema enum. validate_summary doesn't check
    this; with Gemini structured output a failure usually means drift in
    our generated response-schema.json, not a prompt regression."""
    data, err = _parse(output)
    if err:
        return _fail(err)
    allowed = _schema_enum("language")
    language = (data.get("content") or {}).get("language")
    if language in allowed:
        return _ok(f"language={language!r}")
    return _fail(f"language={language!r} not in schema enum {allowed}")


def content_type_enum(output, context):
    """content.contentType in the schema's 8-value enum — the check that
    would have caught the content_types.md (9 categories) drift."""
    data, err = _parse(output)
    if err:
        return _fail(err)
    allowed = _schema_enum("contentType")
    content_type = (data.get("content") or {}).get("contentType")
    if content_type in allowed:
        return _ok(f"contentType={content_type!r}")
    return _fail(f"contentType={content_type!r} not in schema enum ({len(allowed)} values)")


def original_title_invariant(output, context):
    """Asymmetric, mirroring call-gemini.py:1039-1056: non-ja + missing
    ships broken (production only warns) -> hard fail; ja + present is
    silently stripped -> soft signal. null counts as absent."""
    data, err = _parse(output)
    if err:
        return _fail(err)
    content = data.get("content") or {}
    language = content.get("language")
    original_title = content.get("originalTitle")  # None covers absent AND null

    if language != "ja" and not original_title:
        return _fail(
            f"language={language!r} but originalTitle is missing — "
            "production only warns here, so this ships broken"
        )
    if language == "ja" and original_title:
        return _ok(
            f"language='ja' but originalTitle set ({original_title[:50]!r}) — "
            "production silently strips this; soft signal only",
            score=0.0,
        )
    return _ok("originalTitle invariant holds")


# --- soft metrics: production silently repairs; never row-failing ---


def url_fidelity(output, context):
    """Does content.url echo vars.url exactly? Production pins mismatches
    silently (call-gemini.py:1030-1037); the score measures how often the
    prompt's #1 CRITICAL rule is actually honored."""
    data, err = _parse(output)
    if err:
        return _ok(f"unparseable output: {err}", score=0.0)
    expected = context["vars"]["url"]
    actual = (data.get("content") or {}).get("url")
    if actual == expected:
        return _ok("URL echoed exactly")
    return _ok(
        f"URL mismatch (production would pin): got {actual!r}, want {expected!r}",
        score=0.0,
    )


def hallucination_clean(output, context):
    """Heuristic smells via scripts/summary_review.py::evaluate_suspicion —
    a human-review signal by that module's own contract, never a reject."""
    data, err = _parse(output)
    if err:
        return _ok(f"unparseable output: {err}", score=0.0)

    _ensure_scripts_on_path()
    from summary_review import evaluate_suspicion

    suspicious, reasons = evaluate_suspicion(data.get("content") or {})
    if suspicious:
        return _ok(
            f"hallucination smells: {', '.join(reasons)} (human review advised)",
            score=0.0,
        )
    return _ok("no hallucination smells")
