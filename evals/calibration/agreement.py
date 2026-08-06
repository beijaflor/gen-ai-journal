#!/usr/bin/env python3
"""Judge-vs-human agreement: percent agreement + Cohen's kappa per rubric.

Usage:
    uv run --with pyyaml evals/calibration/agreement.py [results/latest-judge.json]

Reads human_labels.yaml (Layer-③ labels) and a promptfoo judge-run
output JSON. With --repeat runs, the judge verdict per (fixture, rubric)
is the majority vote across repeats. Prints a per-rubric table and an
overall verdict against the calibration gate (agreement >= 0.8 AND
kappa >= 0.4).
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

CALIBRATION_DIR = Path(__file__).resolve().parent
EVALS_DIR = CALIBRATION_DIR.parent
LABELS_PATH = CALIBRATION_DIR / "human_labels.yaml"

AGREEMENT_GATE = 0.8
KAPPA_GATE = 0.4


def load_judge_verdicts(results_path: Path):
    """Extract judge pass/fail per (fixture_id, rubric metric), majority-voted."""
    data = json.loads(results_path.read_text(encoding="utf-8"))
    results = data.get("results")
    if isinstance(results, dict):
        results = results.get("results")
    if not isinstance(results, list):
        raise SystemExit(
            f"Unrecognized promptfoo output shape in {results_path} — "
            "expected results[.results] to be a list"
        )

    votes = defaultdict(list)  # (fixture_id, metric) -> [bool, ...]
    for row in results:
        meta = row.get("testCase", {}).get("metadata") or row.get("metadata") or {}
        fixture_id = meta.get("fixture_id")
        if fixture_id is None:
            continue
        grading = row.get("gradingResult") or {}
        for comp in grading.get("componentResults") or []:
            metric = (comp.get("assertion") or {}).get("metric")
            if metric and metric.startswith("judge_"):
                votes[(fixture_id, metric)].append(bool(comp.get("pass")))

    verdicts = {}
    for key, vote_list in votes.items():
        counts = Counter(vote_list)
        verdicts[key] = {
            "verdict": counts[True] >= counts[False],
            "votes": f"{counts[True]}/{len(vote_list)} pass",
            "unstable": len(counts) > 1,
        }
    return verdicts


def cohens_kappa(pairs):
    """pairs: list of (human_bool, judge_bool)."""
    n = len(pairs)
    if n == 0:
        return float("nan")
    observed = sum(1 for h, j in pairs if h == j) / n
    human_pass = sum(1 for h, _ in pairs if h) / n
    judge_pass = sum(1 for _, j in pairs if j) / n
    expected = human_pass * judge_pass + (1 - human_pass) * (1 - judge_pass)
    if expected == 1.0:
        return 1.0
    return (observed - expected) / (1 - expected)


def main() -> int:
    import yaml

    results_path = Path(
        sys.argv[1] if len(sys.argv) > 1 else EVALS_DIR / "results" / "latest-judge.json"
    )
    if not results_path.is_absolute() and not results_path.exists():
        results_path = EVALS_DIR / results_path

    labels_doc = yaml.safe_load(LABELS_PATH.read_text(encoding="utf-8"))
    labeled = [
        (str(row["fixture_id"]), row["rubric"], str(row["verdict"]).lower() == "pass")
        for row in labels_doc["labels"]
        if row.get("verdict") in ("pass", "fail")
    ]
    if not labeled:
        print(
            "No filled-in labels in human_labels.yaml yet — review a judge run "
            "in `npm run view` and record verdicts first."
        )
        return 1

    judge = load_judge_verdicts(results_path)

    per_rubric = defaultdict(list)
    missing = []
    unstable_count = 0
    for fixture_id, rubric, human_pass in labeled:
        entry = judge.get((fixture_id, rubric))
        if entry is None:
            missing.append((fixture_id, rubric))
            continue
        per_rubric[rubric].append((human_pass, entry["verdict"]))
        if entry["unstable"]:
            unstable_count += 1

    print(f"Judge run: {results_path}")
    print(f"Labels:    {len(labeled)} filled, {len(missing)} without a matching judge result\n")
    print(f"{'rubric':30s} {'n':>3s} {'agreement':>10s} {'kappa':>7s}  gate")
    all_ok = True
    for rubric in sorted(per_rubric):
        pairs = per_rubric[rubric]
        agreement = sum(1 for h, j in pairs if h == j) / len(pairs)
        kappa = cohens_kappa(pairs)
        ok = agreement >= AGREEMENT_GATE and kappa >= KAPPA_GATE
        all_ok = all_ok and ok
        status = "OK — may be trusted" if ok else "NOT calibrated — advisory only"
        print(f"{rubric:30s} {len(pairs):3d} {agreement:10.2f} {kappa:7.2f}  {status}")

    if unstable_count:
        print(
            f"\nNote: {unstable_count} (fixture × rubric) judge verdicts were "
            "unstable across --repeat runs — consider tightening those rubrics."
        )
    for fixture_id, rubric in missing:
        print(f"Missing judge result for fixture {fixture_id} / {rubric}")

    print(
        "\nGate: agreement >= 0.8 AND kappa >= 0.4 per rubric before any "
        "judge score is used for gating decisions."
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
