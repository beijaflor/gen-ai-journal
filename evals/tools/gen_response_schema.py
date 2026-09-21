#!/usr/bin/env python3
"""Generate evals/response-schema.json from get_gemini_schema().

The eval provider needs the same structured-output schema production
uses. Rather than hand-transcribing a third copy (schema/summary-v1-schema.json
and get_gemini_schema() being the other two), this walks the native
Gemini Schema tree returned by get_gemini_schema() and emits the
promptfoo/Gemini JSON dialect (lowercase type names, enum/required/
properties/items/nullable).

Usage:
    uv run evals/tools/gen_response_schema.py

Re-run whenever get_gemini_schema() in scripts/call-gemini.py changes.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from call_gemini_bridge import load_call_gemini

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "response-schema.json"


def _schema_type(schema):
    t = getattr(schema, "type", None)
    if t is None:
        t = getattr(schema, "type_")
    return t


def schema_to_dict(schema, type_enum):
    t = _schema_type(schema)
    out = {"type": type_enum(t).name.lower()}

    if schema.description:
        out["description"] = schema.description
    if schema.nullable:
        out["nullable"] = True
    if list(schema.enum):
        out["enum"] = list(schema.enum)
    if list(schema.required):
        out["required"] = list(schema.required)
    if len(schema.properties):
        out["properties"] = {
            key: schema_to_dict(value, type_enum)
            for key, value in schema.properties.items()
        }
    if type_enum(t).name == "ARRAY":
        out["items"] = schema_to_dict(schema.items, type_enum)

    return out


def main() -> int:
    from google.ai.generativelanguage_v1beta.types import Type

    cg = load_call_gemini()
    native = cg.get_gemini_schema()
    converted = schema_to_dict(native, Type)

    OUTPUT_PATH.write_text(
        json.dumps(converted, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
