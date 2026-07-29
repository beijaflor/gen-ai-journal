"""Shared helpers replicating call-gemini.py's post-generation behavior.

A raw promptfoo eval bypasses production's repair layer entirely, so
assertions must simulate the parts that run unconditionally before a
human ever sees the output. Currently that is only the metadata stamp
(call-gemini.py, call_gemini_structured: version/generatedAt/generatedBy
are overwritten on every response). URL pinning and originalTitle
stripping are deliberately NOT simulated — measuring those raw is the
point of url_fidelity.py and original_title_invariant.py.
"""

import json
import sys
from pathlib import Path

_ASSERTIONS_DIR = Path(__file__).resolve().parent
EVALS_DIR = _ASSERTIONS_DIR.parent
REPO_ROOT = EVALS_DIR.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

RESPONSE_SCHEMA_PATH = EVALS_DIR / "response-schema.json"


def ensure_scripts_on_path() -> None:
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))


def parse_summary(output):
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


def stamp_metadata(data):
    """Replicate the unconditional metadata overwrite in call_gemini_structured."""
    metadata = data.setdefault("metadata", {})
    metadata["version"] = "1.0"
    metadata["generatedAt"] = "1970-01-01T00:00:00+00:00"
    metadata["generatedBy"] = "promptfoo-eval"
    return data


def schema_enum(field_name):
    """Read an enum list for a content field from the generated response schema."""
    schema = json.loads(RESPONSE_SCHEMA_PATH.read_text(encoding="utf-8"))
    return schema["properties"]["content"]["properties"][field_name]["enum"]
