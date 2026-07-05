#!/usr/bin/env python3
"""
Model quality eval for the cloud summarization pipeline (#167).

Samples articles from recent published journals (which carry the archived
Gemini summaries as reference), reruns each URL through the LIVE pipeline
via the worker's non-persisting /eval route for each candidate model, and
writes:
  - eval/model-selection/results_<stamp>.jsonl   (raw per-call records)
  - eval/model-selection/report_<stamp>.md       (metrics + side-by-side samples)

Usage:
  uv run scripts/eval/run_model_eval.py --models "@cf/meta/llama-3.3-70b-instruct-fp8-fast" --sample 5
  uv run scripts/eval/run_model_eval.py --models m1,m2 --sample 50 --concurrency 4

Env (scripts/.env): PLATFORM_API_TOKEN; EVAL_URL overrides the worker endpoint.
"""

import argparse
import difflib
import json
import os
import random
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(ROOT / "scripts" / ".env")

EVAL_URL = os.environ.get("EVAL_URL", "https://gen-ai-journal-pipeline.gen-ai-journal.workers.dev/eval")
TOKEN = os.environ.get("PLATFORM_API_TOKEN")
OUT_DIR = ROOT / "eval" / "model-selection"


def build_sample(n: int, weeks: int, seed: int) -> list[dict]:
    """Stratified sample from the most recent `weeks` published journals."""
    journal_dirs = sorted([d for d in (ROOT / "journals").iterdir() if (d / "summaries").is_dir()])[-weeks:]
    pool = []
    for jd in journal_dirs:
        for f in sorted((jd / "summaries").glob("*.json")):
            try:
                doc = json.loads(f.read_text())
            except json.JSONDecodeError:
                continue
            c = doc.get("content", {})
            if not c.get("url") or not c.get("title"):
                continue
            pool.append(
                {
                    "week": jd.name,
                    "file": f.name,
                    "url": c["url"],
                    "language": c.get("language", "en"),
                    "contentType": c.get("contentType", ""),
                    "ref_title": c["title"],
                    "ref_originalTitle": c.get("originalTitle"),
                    "ref_oneSentence": c.get("oneSentenceSummary", ""),
                    "ref_bodyChars": len(c.get("summaryBody", "")),
                    "ref_body_head": c.get("summaryBody", "")[:400],
                }
            )
    rng = random.Random(seed)
    ja = [p for p in pool if p["language"] == "ja"]
    other = [p for p in pool if p["language"] != "ja"]
    rng.shuffle(ja)
    rng.shuffle(other)
    half = n // 2
    sample = ja[:half] + other[: n - min(half, len(ja))]
    rng.shuffle(sample)
    return sample[:n]


def call_eval(url: str, model: str, timeout: int = 150) -> dict:
    t0 = time.time()
    try:
        r = requests.post(
            EVAL_URL,
            json={"url": url, "model": model},
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=timeout,
        )
        out = r.json()
        out["http"] = r.status_code
    except Exception as e:
        out = {"ok": False, "reason": f"CLIENT: {e}", "http": 0}
    out["wallMs"] = int((time.time() - t0) * 1000)
    return out


def similarity(a: str | None, b: str | None) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a.strip(), b.strip()).ratio()


def evaluate_record(item: dict, resp: dict) -> dict:
    rec = {**item, "http": resp.get("http"), "wallMs": resp.get("wallMs"), "ok": resp.get("ok", False)}
    if not resp.get("ok"):
        rec["failure"] = resp.get("reason", "unknown")
        rec["meta"] = resp.get("meta")
        return rec
    doc = json.loads(resp["raw"])
    c = doc["content"]
    rec["meta"] = resp.get("meta")
    rec["out_title"] = c.get("title")
    rec["out_originalTitle"] = c.get("originalTitle")
    rec["out_language"] = c.get("language")
    rec["out_contentType"] = c.get("contentType")
    rec["out_oneSentence"] = c.get("oneSentenceSummary", "")
    rec["out_bodyChars"] = len(c.get("summaryBody", ""))
    rec["out_body_head"] = c.get("summaryBody", "")[:400]
    rec["out_scores"] = c.get("scores", {})
    rec["lang_match"] = c.get("language") == item["language"]
    # Title fidelity: ja sources → title should be near-verbatim vs the archived
    # (itself verbatim-rule'd) title; non-ja → compare originalTitle.
    if item["language"] == "ja":
        rec["title_sim"] = similarity(c.get("title"), item["ref_title"])
    else:
        rec["title_sim"] = similarity(c.get("originalTitle"), item["ref_originalTitle"])
    return rec


def pct(xs: list, p: float):
    if not xs:
        return None
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(len(xs) * p))]


def summarize_model(records: list[dict]) -> dict:
    n = len(records)
    ok = [r for r in records if r["ok"]]
    fails = [r for r in records if not r["ok"]]
    body = [r["out_bodyChars"] for r in ok]
    sims = [r["title_sim"] for r in ok]
    ai_ms = [r["meta"]["aiMs"] for r in ok if r.get("meta", {}).get("aiMs")]
    scores_main = [r["out_scores"].get("mainJournal") for r in ok if r.get("out_scores")]
    return {
        "n": n,
        "success": len(ok),
        "success_rate": round(len(ok) / n, 3) if n else 0,
        "fetch_failures": sum(1 for r in fails if "fetch" in r.get("failure", "") or "extracted" in r.get("failure", "")),
        "model_failures": sum(1 for r in fails if "model" in r.get("failure", "")),
        "lang_match_rate": round(sum(1 for r in ok if r["lang_match"]) / len(ok), 3) if ok else None,
        "title_sim_median": round(statistics.median(sims), 3) if sims else None,
        "title_sim_p25": round(pct(sims, 0.25), 3) if sims else None,
        "body_chars_median": int(statistics.median(body)) if body else None,
        "body_chars_p25_p75": [pct(body, 0.25), pct(body, 0.75)] if body else None,
        "ai_ms_median": int(statistics.median(ai_ms)) if ai_ms else None,
        "mainJournal_ge80_rate": round(sum(1 for s in scores_main if s and s >= 80) / len(scores_main), 3)
        if scores_main
        else None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True, help="comma-separated Workers AI model ids")
    ap.add_argument("--sample", type=int, default=50)
    ap.add_argument("--weeks", type=int, default=3)
    ap.add_argument("--seed", type=int, default=20260706)
    ap.add_argument("--concurrency", type=int, default=4)
    args = ap.parse_args()

    if not TOKEN:
        print("PLATFORM_API_TOKEN missing in scripts/.env")
        return 1
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    sample = build_sample(args.sample, args.weeks, args.seed)
    print(f"Sample: {len(sample)} articles ({sum(1 for s in sample if s['language']=='ja')} ja) × {len(models)} models")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    results_path = OUT_DIR / f"results_{stamp}.jsonl"
    all_records: dict[str, list[dict]] = {m: [] for m in models}

    with results_path.open("w") as sink:
        for model in models:
            print(f"\n=== {model}")
            with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
                futures = {pool.submit(call_eval, item["url"], model): item for item in sample}
                for i, (fut, item) in enumerate(((f, futures[f]) for f in futures), 0):
                    pass  # placeholder; results collected below
                done = 0
                for fut in list(futures):
                    item = futures[fut]
                    rec = evaluate_record(item, fut.result())
                    rec["model"] = model
                    all_records[model].append(rec)
                    sink.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    sink.flush()
                    done += 1
                    flag = "ok" if rec["ok"] else f"FAIL({rec.get('failure','')[:60]})"
                    print(f"  [{done}/{len(sample)}] {flag} {item['url'][:60]}")

    # ---- report ----
    report = [f"# Model eval — {stamp}\n", f"Sample: {len(sample)} articles from last {args.weeks} journals; endpoint: live pipeline `/eval` (non-persisting)\n"]
    report.append("| metric | " + " | ".join(models) + " |")
    report.append("|---|" + "---|" * len(models))
    stats = {m: summarize_model(all_records[m]) for m in models}
    for key in ["n", "success_rate", "fetch_failures", "model_failures", "lang_match_rate", "title_sim_median", "title_sim_p25", "body_chars_median", "body_chars_p25_p75", "ai_ms_median", "mainJournal_ge80_rate"]:
        report.append(f"| {key} | " + " | ".join(str(stats[m].get(key)) for m in models) + " |")
    report.append("\n*(reference: archived Gemini body_chars median = "
                  f"{int(statistics.median([s['ref_bodyChars'] for s in sample]))})*\n")

    report.append("\n## Side-by-side samples (editor spot-check)\n")
    for model in models:
        oks = [r for r in all_records[model] if r["ok"]]
        report.append(f"\n### {model}\n")
        for r in oks[:5]:
            report.append(f"**{r['url']}**  (lang: ref {r['language']} / out {r['out_language']}, title_sim {r['title_sim']:.2f})")
            report.append(f"- ref title: {r['ref_title']}")
            report.append(f"- out title: {r['out_title']}" + (f" / 原題: {r['out_originalTitle']}" if r.get("out_originalTitle") else ""))
            report.append(f"- ref 1文: {r['ref_oneSentence'][:180]}")
            report.append(f"- out 1文: {r['out_oneSentence'][:180]}")
            report.append(f"- out body({r['out_bodyChars']}ch): {r['out_body_head'][:300]}…")
            report.append("")
        for r in [x for x in all_records[model] if not x["ok"]][:8]:
            report.append(f"- FAIL {r['url'][:70]} — {r.get('failure','')[:120]}")

    report_path = OUT_DIR / f"report_{stamp}.md"
    report_path.write_text("\n".join(report))
    print(f"\nWrote {results_path}\nWrote {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
