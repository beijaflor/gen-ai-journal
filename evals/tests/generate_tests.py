"""promptfoo test generators — fixtures/manifest.json -> TestCase list.

generate_tests():       all fixtures (Layer-① deterministic assertion runs)
generate_judge_tests(): only judge_subset fixtures (Layer-② llm-rubric runs)

article_text_path is resolved to an absolute path here so prompt
functions work regardless of promptfoo's working directory; the
committed manifest stays relative for portability.
"""

import json
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parents[1]
MANIFEST_PATH = EVALS_DIR / "fixtures" / "manifest.json"


def _load_manifest():
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(
            f"{MANIFEST_PATH} not found. Build fixtures first:\n"
            "  uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py"
        )
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


# Judge rubrics compare the summary against the source article; the
# excerpt is injected as a var so rubric templates can reference
# {{article_excerpt}}. Bounded so the grader prompt stays cheap.
ARTICLE_EXCERPT_CHARS = 6000


def _to_test(fx, include_article_excerpt=False):
    test = {
        "description": f"{fx['id']}: {fx['reason']}",
        "vars": {
            "url": fx["url"],
            "article_text_path": str(EVALS_DIR / fx["article_text_path"]),
        },
        "metadata": {
            "fixture_id": fx["id"],
            "judge": fx["judge_subset"],
            "synthetic": fx["synthetic"],
            "golden_summary": fx["golden_summary"],
        },
    }
    if include_article_excerpt:
        article = (EVALS_DIR / fx["article_text_path"]).read_text(encoding="utf-8")
        test["vars"]["article_excerpt"] = article[:ARTICLE_EXCERPT_CHARS]
    return test


def generate_tests():
    return [_to_test(fx) for fx in _load_manifest()]


def generate_judge_tests():
    return [
        _to_test(fx, include_article_excerpt=True)
        for fx in _load_manifest()
        if fx["judge_subset"]
    ]
