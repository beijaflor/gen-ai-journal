"""Soft metric (weight 0 in config): does content.url echo vars.url exactly?

Production silently overwrites content.url on any mismatch
(call-gemini.py:1030-1037), so a raw mismatch never reaches a human —
this must never hard-fail a row. But the prompt's #1 CRITICAL rule is
the URL rule, and this metric measures how often the model actually
honors it. A drop after a prompt edit means the edit weakened the rule.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import parse_summary


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": True, "score": 0.0, "reason": f"unparseable output: {err}"}

    expected = context["vars"]["url"]
    actual = (data.get("content") or {}).get("url")
    if actual == expected:
        return {"pass": True, "score": 1.0, "reason": "URL echoed exactly"}
    return {
        "pass": True,
        "score": 0.0,
        "reason": f"URL mismatch (production would pin): got {actual!r}, want {expected!r}",
    }
