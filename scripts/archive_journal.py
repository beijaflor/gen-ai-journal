#!/usr/bin/env python3
"""STEP_10 (+ STEP_11 metadata, #209) — archive a finished cycle, idempotently.

Assembles ``journals/<date>/`` from the finished workdesk (a live cycle) or,
when the workdesk is already clean, re-derives it from the existing archive
(golden replay / eval). In one pass it:

  * copies 00 / 01 / 50 (the assembled journals + editorial plan),
  * copies the sources/ set and every summaries/*.json,
  * builds 99_unified_summaries.md and 02_omitted_summaries.md **fresh from the
    JSON in Python** (replacing the old jq/echo loop),
  * writes + validates journal-metadata.json (main from 00's H3 count, annex
    from 01's H3 count, omitted from the 02 build, total from the summary
    count; asserts main+annex+omitted == total), and — in a live run only —
  * marks the cycle published in Supabase and clears the workdesk (git rm).

Safety:
  --dry-run   print the plan, write nothing.
  --into DIR  eval mode: build the tree under DIR/<date>/ and SKIP every
              production side effect (no Supabase, no workdesk git rm), so a
              golden reproduction never touches the real archive/DB.
  live run (no --into) prompts before the Supabase + git-rm steps unless --yes.

Usage:
    uv run scripts/archive_journal.py 2026-08-22                 # live
    uv run scripts/archive_journal.py 2026-08-22 --dry-run       # plan only
    uv run scripts/archive_journal.py 2026-08-22 --into /tmp/eval10   # eval
"""

import glob
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow import git_gh, partition  # noqa: E402

MARK_PUBLISHED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mark_published.py")

# The six curated files the archive keeps under sources/ (copied when present;
# the first three are required to build 02 + metadata).
SOURCE_FILES = [
    "sources.md",
    "curated_journal_sources.md",
    "curated_annex_journal_sources.md",
    "curated_annex_selected.md",
    "non_main_sources.md",
    "omitted_sources.md",
]
REQUIRED_SOURCES = {"sources.md", "curated_journal_sources.md", "omitted_sources.md"}


# --------------------------------------------------------------------------- #
# builders
# --------------------------------------------------------------------------- #
def jp_date(date):
    y, m, d = date.split("-")
    return f"{y}年{m}月{d}日号"


def _entry(stem, obj):
    c = obj["content"]
    return f"\n## {stem}\n\n**{c['title']}**\n\n出典: {c['url']}\n\n{c['summaryBody']}\n\n---\n"


def build_99(summary_files, date):
    out = [f"# 全記事要約 {jp_date(date)}\n\n"
           "この週に収集・要約された全記事の完全なアーカイブです。\n\n---\n"]
    for f in summary_files:
        with open(f, encoding="utf-8") as fh:
            obj = json.load(fh)
        out.append(_entry(Path(f).stem, obj))
    return "".join(out)


def build_02(summary_files, omitted_ids, date):
    out = [f"# 非掲載記事要約 {jp_date(date)}\n\n"
           "メインジャーナルおよびAnnexジャーナルに掲載されなかった記事の"
           "要約集です。\n\n---\n"]
    n = 0
    for f in summary_files:
        stem = Path(f).stem
        idnum = re.match(r"(\d+)_", stem)
        if idnum and idnum.group(1) in omitted_ids:
            with open(f, encoding="utf-8") as fh:
                obj = json.load(fh)
            out.append(_entry(stem, obj))
            n += 1
    return "".join(out), n


def h3_count(path):
    n = 0
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(#{1,6})\s+\S", line)
        if m and len(m.group(1)) == 3:
            n += 1
    return n


def build_metadata(date, weekly_path, annex_path, total, omitted):
    main = h3_count(weekly_path)
    annex = h3_count(annex_path)
    if main + annex + omitted != total:
        raise AssertionError(
            f"metadata math: main({main}) + annex({annex}) + omitted({omitted}) "
            f"!= total({total})"
        )
    meta = {
        "date": date,
        "totalSummaries": total,
        "statistics": {
            "mainSummaries": main,
            "annexSummaries": annex,
            "omittedSummaries": omitted,
        },
    }
    return json.dumps(meta, ensure_ascii=False, indent=2) + "\n", meta


# --------------------------------------------------------------------------- #
# input resolution
# --------------------------------------------------------------------------- #
class Inputs:
    def __init__(self, date, journals_root="journals"):
        us = date.replace("-", "_")
        wd = Path("workdesk")
        self.live = (wd / f"weekly_journal_{us}.md").exists()
        if self.live:
            self.weekly = wd / f"weekly_journal_{us}.md"
            self.annex = wd / f"annex_journal_{us}.md"
            self.plan = wd / f"editorial_plan_{us}.md"
            self.source_of = lambda name: wd / name
            self.summaries_dir = wd / "summaries"
        else:  # archived replay (eval / re-run / fixture)
            arc = Path(journals_root) / date
            self.weekly = arc / f"00_weekly_journal_{us}.md"
            self.annex = arc / f"01_annex_journal_{us}.md"
            self.plan = arc / f"50_editorial_plan_{us}.md"
            self.source_of = lambda name: arc / "sources" / name
            self.summaries_dir = arc / "summaries"

    def summary_files(self):
        return sorted(glob.glob(str(self.summaries_dir / "*.json")))


# --------------------------------------------------------------------------- #
# plan
# --------------------------------------------------------------------------- #
def plan(date, out_base, journals_root="journals"):
    """Return (copies, built, out_dir).

    copies: list of (src Path, dst Path) file copies.
    built:  list of dst Paths written from Python (99/02/metadata).
    """
    us = date.replace("-", "_")
    inp = Inputs(date, journals_root=journals_root)
    out_dir = Path(out_base) / date

    copies = [
        (inp.weekly, out_dir / f"00_weekly_journal_{us}.md"),
        (inp.annex, out_dir / f"01_annex_journal_{us}.md"),
    ]
    if inp.plan.exists():
        copies.append((inp.plan, out_dir / f"50_editorial_plan_{us}.md"))

    for name in SOURCE_FILES:
        src = inp.source_of(name)
        if src.exists():
            copies.append((src, out_dir / "sources" / name))
        elif name in REQUIRED_SOURCES:
            raise FileNotFoundError(f"required source file missing: {src}")

    for f in inp.summary_files():
        copies.append((Path(f), out_dir / "summaries" / Path(f).name))

    built = [
        out_dir / "99_unified_summaries.md",
        out_dir / "02_omitted_summaries.md",
        out_dir / "journal-metadata.json",
    ]
    return inp, copies, built, out_dir


def output_fileset(date, out_base, journals_root="journals"):
    """The set of output paths (relative to out_base) the archive produces."""
    _, copies, built, _ = plan(date, out_base, journals_root=journals_root)
    rel = {str(dst.relative_to(out_base)) for _, dst in copies}
    rel |= {str(b.relative_to(out_base)) for b in built}
    return rel


# --------------------------------------------------------------------------- #
# execute
# --------------------------------------------------------------------------- #
def archive(date, into=None, dry_run=False, assume_yes=False, journals_root="journals"):
    out_base = Path(into) if into else Path("journals")
    eval_mode = into is not None
    inp, copies, built, out_dir = plan(date, out_base, journals_root=journals_root)

    mode = ("DRY-RUN" if dry_run else "eval" if eval_mode
            else "live" if inp.live else "replay: rebuild 99/02/metadata in place")
    print(f"Archiving cycle {date} -> {out_dir}  [{mode}]")
    print(f"  inputs: {'workdesk/' if inp.live else Path(journals_root) / date}")

    if dry_run:
        for _, dst in copies:
            print(f"  copy  {dst.relative_to(out_base)}")
        for b in built:
            print(f"  build {b.relative_to(out_base)}")
        if inp.live and not eval_mode:
            print(f"  supabase: mark_published --yes {date}")
            print("  cleanup: git rm consumed workdesk files, leave workdesk/.gitkeep")
        print(f"  ({len(copies)} copies + {len(built)} built files)")
        return out_dir

    # 1. copies (a replay onto the existing archive resolves src == dst for
    #    every copied file; skip those instead of crashing with SameFileError)
    for src, dst in copies:
        if dst.exists() and src.resolve() == dst.resolve():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # 2. built files (99 / 02 / metadata)
    summary_files = sorted(glob.glob(str(out_dir / "summaries" / "*.json")))
    omitted_ids = partition.read_ids(out_dir / "sources" / "omitted_sources.md")

    (out_dir / "99_unified_summaries.md").write_text(
        build_99(summary_files, date), encoding="utf-8")
    body02, n_omit = build_02(summary_files, omitted_ids, date)
    (out_dir / "02_omitted_summaries.md").write_text(body02, encoding="utf-8")
    meta_text, meta = build_metadata(
        date, out_dir / f"00_weekly_journal_{date.replace('-', '_')}.md",
        out_dir / f"01_annex_journal_{date.replace('-', '_')}.md",
        total=len(summary_files), omitted=n_omit)
    (out_dir / "journal-metadata.json").write_text(meta_text, encoding="utf-8")
    print(f"  built 99 ({len(summary_files)}), 02 ({n_omit}), metadata {meta['statistics']}")

    # 3. production side effects (live only)
    if eval_mode or not inp.live:
        print("  (eval/replay mode: skipping Supabase + workdesk cleanup)")
        return out_dir

    if not assume_yes:
        ans = input(f"Live archive: mark_published --yes {date} and git-rm the "
                    f"workdesk? (yes/no): ")
        if ans.lower() not in ("yes", "y"):
            print("Skipped Supabase + cleanup by request.")
            return out_dir

    subprocess.run([sys.executable, MARK_PUBLISHED, date, "--yes"], check=True)
    _clean_workdesk(inp, dry_run=False)
    return out_dir


def _clean_workdesk(inp, dry_run):
    """git rm the consumed workdesk artifacts; leave workdesk/.gitkeep.

    Only the files we archived (plus the known unified intermediates) are
    removed, so untracked next-cycle scaffolding is never swept away.
    """
    us_files = [inp.weekly, inp.annex, inp.plan,
                Path("workdesk/unified_summaries.md"),
                Path("workdesk/unified_summaries_main.md"),
                Path("workdesk/unified_summaries_annex.md"),
                Path("workdesk/omitted_summaries_unified.md")]
    us_files += [inp.source_of(n) for n in SOURCE_FILES]
    existing = [str(p) for p in us_files if p.exists()]
    if existing:
        git_gh.run(["git", "rm", "-q", "--", *existing], dry_run=dry_run, check=False)
    if (inp.summaries_dir).exists():
        git_gh.run(["git", "rm", "-r", "-q", "--", str(inp.summaries_dir)],
                   dry_run=dry_run, check=False)
    keep = Path("workdesk/.gitkeep")
    keep.parent.mkdir(exist_ok=True)
    keep.write_text("", encoding="utf-8")
    git_gh.run(["git", "add", str(keep)], dry_run=dry_run, check=False)


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    assume_yes = ("--yes" in args) or ("-y" in args)
    into = None
    if "--into" in args:
        i = args.index("--into")
        into = args[i + 1]
        del args[i:i + 2]
    positional = [a for a in args if not a.startswith("-")]
    if len(positional) != 1:
        print("Usage: uv run scripts/archive_journal.py <YYYY-MM-DD> "
              "[--into DIR] [--dry-run] [--yes]")
        sys.exit(1)

    try:
        archive(positional[0], into=into, dry_run=dry_run, assume_yes=assume_yes)
    except (AssertionError, FileNotFoundError) as e:
        print(f"❌ {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
