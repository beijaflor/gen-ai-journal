#!/usr/bin/env python3
"""
Generate platform/worker/src/prompt.generated.ts from prompts/summarize-json.prompt.

Inlines {{file:...}} includes (criteria, persona) exactly like call-gemini.py,
and replaces the trailing {{fetch:"{{url}}"}} with runtime placeholders the
cloud pipeline (#166) substitutes per article. Re-run whenever the prompt or
criteria files change:

    uv run scripts/build_prompt_module.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = ROOT / "prompts" / "summarize-json.prompt"
OUT = ROOT / "platform" / "worker" / "src" / "prompt.generated.ts"


def main() -> None:
    text = PROMPT.read_text()

    def inline(m: re.Match) -> str:
        return (PROMPT.parent / m.group(1)).resolve().read_text()

    text = re.sub(r"\{\{file:([^}]+)\}\}", inline, text)
    # The local pipeline injects fetched content here; the Worker substitutes at runtime.
    text = text.replace('{{fetch:"{{url}}"}}', "URL: {{url}}\n\n{{content}}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "// GENERATED FILE — do not edit. Source: prompts/summarize-json.prompt\n"
        "// Regenerate with: uv run scripts/build_prompt_module.py\n"
        f"export const SUMMARIZE_PROMPT_TEMPLATE = {json.dumps(text, ensure_ascii=False)};\n"
    )
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
