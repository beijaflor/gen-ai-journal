"""Hard fail: content.language must be in the schema enum.

validate_summary.py does not check this field. With Gemini structured
output the enum constraint should make model violations nearly
impossible — a failure here usually means drift in our generated
response-schema.json, not a prompt regression. Diagnose accordingly.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import parse_summary, schema_enum


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": False, "score": 0.0, "reason": err}

    allowed = schema_enum("language")
    language = (data.get("content") or {}).get("language")
    if language in allowed:
        return {"pass": True, "score": 1.0, "reason": f"language={language!r}"}
    return {
        "pass": False,
        "score": 0.0,
        "reason": f"language={language!r} not in schema enum {allowed}",
    }
