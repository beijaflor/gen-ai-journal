"""Hard fail: content.contentType must be one of the schema's 8 enum values.

validate_summary.py has never checked this field — the golden corpus
contains out-of-enum values as a result (criteria/content_types.md
lists 9 differently-worded categories vs the schema's 8). This is the
check that would have caught that drift.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import parse_summary, schema_enum


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": False, "score": 0.0, "reason": err}

    allowed = schema_enum("contentType")
    content_type = (data.get("content") or {}).get("contentType")
    if content_type in allowed:
        return {"pass": True, "score": 1.0, "reason": f"contentType={content_type!r}"}
    return {
        "pass": False,
        "score": 0.0,
        "reason": f"contentType={content_type!r} not in schema enum ({len(allowed)} values)",
    }
