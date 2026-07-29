"""Hard fail: v1.0 schema validity via scripts/validate_summary.py.

Production also hard-fails here (call-gemini.py exits 1 on validation
failure) — no repair exists, so a failure would ship broken.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import ensure_scripts_on_path, parse_summary, stamp_metadata


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": False, "score": 0.0, "reason": err}

    stamp_metadata(data)

    ensure_scripts_on_path()
    from validate_summary import validate

    result = validate(data)
    if result.ok:
        return {"pass": True, "score": 1.0, "reason": "schema valid"}
    return {"pass": False, "score": 0.0, "reason": "; ".join(result.errors[:5])}
