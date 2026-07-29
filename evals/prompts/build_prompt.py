"""promptfoo prompt functions for the summarize-json prompt.

Both functions render through the production assembly path
(``_build_url_mode_prompt_with_text`` in scripts/call-gemini.py), so the
eval sends byte-identical prompts to what production sends for PDF /
pre-extracted-text sources. ``build_candidate`` points the same assembly
at evals/candidates/summarize-json.candidate.prompt for A/B comparison.

Vars contract (set by tests/generate_tests.py):
    url                — source URL, substituted into {{url}}
    article_text_path  — absolute path to the cached article text fixture
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from call_gemini_bridge import REPO_ROOT, SCRIPTS_DIR, load_call_gemini

CANDIDATE_PROMPT = REPO_ROOT / "evals" / "candidates" / "summarize-json.candidate.prompt"


def _build(context, prompt_path=None):
    cg = load_call_gemini()
    v = context["vars"]
    article_text = Path(v["article_text_path"]).read_text(encoding="utf-8")
    return cg._build_url_mode_prompt_with_text(
        v["url"], article_text, str(SCRIPTS_DIR), prompt_path=prompt_path
    )


def build_current(context):
    """Production prompt: prompts/summarize-json.prompt."""
    return _build(context)


def build_candidate(context):
    """Candidate variant: evals/candidates/summarize-json.candidate.prompt."""
    if not CANDIDATE_PROMPT.exists():
        raise FileNotFoundError(
            f"Candidate prompt not found: {CANDIDATE_PROMPT}\n"
            "Create it first, e.g.:\n"
            "  cp prompts/summarize-json.prompt evals/candidates/summarize-json.candidate.prompt"
        )
    return _build(context, prompt_path=str(CANDIDATE_PROMPT))
