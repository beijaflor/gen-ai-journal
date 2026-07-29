"""Soft metric (weight 0 in config): heuristic hallucination smell.

Wraps scripts/summary_review.py::evaluate_suspicion() — generic title,
site-descriptor language, suspiciously short body. Per that module's
own contract it surfaces candidates for human review, never a hard
reject, so the score is informational (1.0 = clean, 0.0 = suspicious).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import ensure_scripts_on_path, parse_summary


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": True, "score": 0.0, "reason": f"unparseable output: {err}"}

    ensure_scripts_on_path()
    from summary_review import evaluate_suspicion

    suspicious, reasons = evaluate_suspicion(data.get("content") or {})
    if suspicious:
        return {
            "pass": True,
            "score": 0.0,
            "reason": f"hallucination smells: {', '.join(reasons)} (human review advised)",
        }
    return {"pass": True, "score": 1.0, "reason": "no hallucination smells"}
