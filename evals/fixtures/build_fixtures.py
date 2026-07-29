#!/usr/bin/env python3
"""Build the committed fixture set from selection.yaml.

For each real entry: load the golden summary (for content.url and
language/contentType hints), fetch the article text with the SAME
production fetchers the pipeline uses (fetch_url_content for HTML,
extract_pdf_from_url for PDFs), and freeze it under fixtures/articles/.
Synthetic entries write their inline text as-is.

The output manifest.json is what tests/generate_tests.py feeds to
promptfoo — after this script runs, evals are network-free except for
the Gemini call itself.

Usage:
    uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py
    uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py --refresh   # re-fetch existing

Idempotent: existing article files are kept unless --refresh is given,
so adding one new fixture doesn't re-hit the network for the others.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from call_gemini_bridge import REPO_ROOT, ensure_scripts_on_path, load_call_gemini

FIXTURES_DIR = Path(__file__).resolve().parent
ARTICLES_DIR = FIXTURES_DIR / "articles"
MANIFEST_PATH = FIXTURES_DIR / "manifest.json"
SELECTION_PATH = FIXTURES_DIR / "selection.yaml"

# Below this, a fetched fixture is almost certainly a blocked/JS-shell
# page and would freeze a useless baseline (mirrors FETCH_QUALITY_MIN_CHARS).
MIN_FETCH_CHARS = 200


def _slug(url: str) -> str:
    domain = urlparse(url).netloc or "unknown"
    return re.sub(r"[^a-z0-9]+", "_", domain.lower()).strip("_")


def _fetch_article_text(url: str, cg) -> tuple[str, str]:
    """Return (text, error). Empty error means success."""
    ensure_scripts_on_path()
    from modules.pdf_router import is_pdf_url

    if url.lower().endswith(".pdf") or is_pdf_url(url):
        from modules.pdf_extractor import extract_pdf_from_url

        result = extract_pdf_from_url(url)
        if not result.ok:
            return "", f"PDF extraction failed: {result.error}"
        return result.text, ""

    text = cg.fetch_url_content(url)
    if text.startswith("[ERROR"):
        return "", f"fetch failed: {text[:200]}"
    if len(text) < MIN_FETCH_CHARS:
        return "", (
            f"fetched only {len(text)} chars (<{MIN_FETCH_CHARS}) — likely a "
            "JS shell or blocked page; not freezing a useless baseline"
        )
    return text, ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh", action="store_true", help="Re-fetch article text even if cached"
    )
    args = parser.parse_args()

    import yaml

    cg = load_call_gemini()
    selection = yaml.safe_load(SELECTION_PATH.read_text(encoding="utf-8"))
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    failures = []

    for fx in selection["fixtures"]:
        fx_id = fx["id"]
        synthetic = fx.get("synthetic", False)

        golden_rel = fx.get("golden_summary")
        golden = None
        if golden_rel:
            golden_path = REPO_ROOT / golden_rel
            golden = json.loads(golden_path.read_text(encoding="utf-8"))

        url = fx.get("url") or golden["content"]["url"]
        article_path = ARTICLES_DIR / f"{fx_id}_{_slug(url)}.txt"

        if synthetic:
            article_path.write_text(fx["article_text_inline"], encoding="utf-8")
            print(f"[{fx_id}] synthetic -> {article_path.name}")
        elif article_path.exists() and not args.refresh:
            print(f"[{fx_id}] cached    -> {article_path.name} (skip fetch)")
        else:
            print(f"[{fx_id}] fetching  {url}")
            text, err = _fetch_article_text(url, cg)
            if err:
                failures.append(f"[{fx_id}] {url}: {err}")
                continue
            article_path.write_text(text, encoding="utf-8")
            print(f"[{fx_id}] fetched   -> {article_path.name} ({len(text)} chars)")

        manifest.append(
            {
                "id": fx_id,
                "url": url,
                "article_text_path": f"fixtures/articles/{article_path.name}",
                "golden_summary": golden_rel,
                "golden_language": golden["content"]["language"] if golden else None,
                "golden_content_type": golden["content"]["contentType"] if golden else None,
                "judge_subset": fx.get("judge_subset", False),
                "synthetic": synthetic,
                "added": str(fx["added"]),
                "reason": fx["reason"],
            }
        )

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nWrote {MANIFEST_PATH} ({len(manifest)} fixtures)")

    if failures:
        print("\nFAILED fixtures (not in manifest — fix or replace in selection.yaml):")
        for f in failures:
            print(f"  {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
