"""Asymmetric check mirroring the production repair layer exactly
(call-gemini.py:1039-1056):

- language != 'ja' and originalTitle missing  -> HARD FAIL
  (production only warns and ships the broken file)
- language == 'ja' and originalTitle present  -> pass with score 0.0
  (production silently strips it — never reaches a human, but the
  metric makes the drift visible)

originalTitle: null is treated as absent (Gemini structured output may
emit the key as null instead of omitting it).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repair_layer import parse_summary


def get_assert(output, context):
    data, err = parse_summary(output)
    if err:
        return {"pass": False, "score": 0.0, "reason": err}

    content = data.get("content") or {}
    language = content.get("language")
    original_title = content.get("originalTitle")  # None covers absent AND null

    if language != "ja" and not original_title:
        return {
            "pass": False,
            "score": 0.0,
            "reason": (
                f"language={language!r} but originalTitle is missing — "
                "production only warns here, so this ships broken"
            ),
        }
    if language == "ja" and original_title:
        return {
            "pass": True,
            "score": 0.0,
            "reason": (
                f"language='ja' but originalTitle set ({original_title[:50]!r}) — "
                "production silently strips this; soft signal only"
            ),
        }
    return {"pass": True, "score": 1.0, "reason": "originalTitle invariant holds"}
