#!/usr/bin/env python3
"""STEP_08 assist — generate the per-theme / per-section writer prompts.

Reads the authoritative theme→ID mapping from curated_journal_sources.md (and
curated_annex_selected.md), pulls each theme's intro + assembly strategy from
editorial_plan_<date>.md, resolves the article summaries/NNN_*.json paths, and
writes one self-contained writer prompt per theme + per annex section to the
scratch dir. The actual editorial writing (and whether it is dispatched to
subagents or a Workflow) stays with the orchestrator — this only builds the
scaffolding.

IMPORTANT: IDs come from the *curated* files, never the editorial plan's
"Identified Themes" candidate lists — those go stale after STEP_04 trims.

Annex note: the annex-section prompts mirror the curator's grouping in
curated_annex_selected.md. The FINAL annex section structure (titles, how
articles regroup) is an editorial decision taken at the STEP_07/08 assembly
gate, so the number of prompts here need not equal the assembled annex's section
count — deriving those sections automatically would be automating judgment,
which this tooling deliberately does not do.

Usage:
    uv run scripts/gen_writer_prompts.py 2026-08-22
    uv run scripts/gen_writer_prompts.py 2099-01-01 \
        --sources-dir tests/fixtures/mini-journal/2099-01-01/sources \
        --plan tests/fixtures/mini-journal/2099-01-01/50_editorial_plan_2099_01_01.md \
        --summaries-dir tests/fixtures/mini-journal/2099-01-01/summaries --out /tmp/prompts
"""

import glob
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FORMAT_SPEC = "STEP_08_ASSEMBLE.md"
_HEADING = re.compile(r"^(#{2,3})\s+(.*\S)\s*$")
_ID_LINE = re.compile(r"^\s*-\s*\[[ xX]\]\s*(\d+)\.")


def parse_sections(path):
    """Parse a curated file into ordered [(title, [ids])], one per heading that
    has at least one ID line under it."""
    sections = []
    cur_title, cur_ids = None, []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        h = _HEADING.match(line)
        if h:
            if cur_title is not None and cur_ids:
                sections.append((cur_title, cur_ids))
            cur_title, cur_ids = h.group(2), []
            continue
        m = _ID_LINE.match(line)
        if m and cur_title is not None:
            cur_ids.append(m.group(1))
    if cur_title is not None and cur_ids:
        sections.append((cur_title, cur_ids))
    return sections


def parse_plan_blocks(plan_path, section_header):
    """Return the ordered ### blocks under a `## <section_header>` heading."""
    if not plan_path or not Path(plan_path).exists():
        return []
    text = Path(plan_path).read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    # isolate the section
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and section_header in ln:
            start = i + 1
            break
    if start is None:
        return []
    blocks, cur = [], []
    for ln in lines[start:]:
        if ln.startswith("## "):  # next top-level section ends this one
            break
        if ln.startswith("### "):
            if cur:
                blocks.append("".join(cur).strip())
            cur = [ln]
        elif cur:
            cur.append(ln)
    if cur:
        blocks.append("".join(cur).strip())
    return blocks


def resolve_summary(idnum, summaries_dir):
    hits = sorted(glob.glob(str(Path(summaries_dir) / f"{idnum}_*.json")))
    return hits[0] if hits else None


def _prompt(kind, n, title, ids, summaries_dir, out_frag, intro, strategy):
    lines = [
        f"# Writer prompt — {kind} {n:02d}: {title}",
        "",
        f"Format spec: {FORMAT_SPEC}",
        f"Output file: {out_frag}",
        "",
        "## Theme intro (from editorial plan)",
        intro or "(none in plan)",
        "",
        "## Assembly strategy (from editorial plan)",
        strategy or "(none in plan)",
        "",
        f"## Articles ({len(ids)})",
    ]
    for idnum in ids:
        p = resolve_summary(idnum, summaries_dir)
        lines.append(f"- {idnum}: {p if p else '(summary missing!)'}")
    lines += [
        "",
        "## Task",
        "Write this section in Japanese following the format spec and the "
        "assembly strategy above, using ONLY the article summaries listed. "
        f"Write the finished section to {out_frag}.",
        "",
    ]
    return "\n".join(lines)


def generate(date, sources_dir, plan_path, summaries_dir, out_dir,
             scratch_out="scratchpad"):
    """Return {prompt_filename: content}. Does not write; main() writes."""
    sources_dir = Path(sources_dir)
    main_sections = parse_sections(sources_dir / "curated_journal_sources.md")
    annex_sections = parse_sections(sources_dir / "curated_annex_selected.md")
    main_intros = parse_plan_blocks(plan_path, "Identified Themes")
    main_strats = parse_plan_blocks(plan_path, "ASSEMBLY STRATEGIES")

    if not main_sections:
        raise ValueError(f"no '## theme' sections with ID lines found in "
                         f"{sources_dir / 'curated_journal_sources.md'}")
    # Intros/strategies are paired with curated themes BY POSITION (i-th theme
    # <-> i-th plan block). Warn when the counts differ so a mid-cycle theme
    # add/remove/reorder (STEP_04b) cannot silently mis-pair them.
    for label, blocks in (("Identified Themes", main_intros),
                          ("ASSEMBLY STRATEGIES", main_strats)):
        if blocks and len(blocks) != len(main_sections):
            print(f"⚠️  plan has {len(blocks)} '{label}' blocks but curated file has "
                  f"{len(main_sections)} themes — intros/strategies are paired by "
                  f"position; check each prompt's heading against its theme title.",
                  file=sys.stderr)

    out = {}
    for i, (title, ids) in enumerate(main_sections, 1):
        intro = main_intros[i - 1] if i - 1 < len(main_intros) else None
        strat = main_strats[i - 1] if i - 1 < len(main_strats) else None
        frag = f"{scratch_out}/main_theme_{i:02d}.md"
        out[f"prompt_main_theme_{i:02d}.md"] = _prompt(
            "main theme", i, title, ids, summaries_dir, frag, intro, strat)

    for i, (title, ids) in enumerate(annex_sections, 1):
        frag = f"{scratch_out}/annex_sec_{i:02d}.md"
        out[f"prompt_annex_sec_{i:02d}.md"] = _prompt(
            "annex section", i, title, ids, summaries_dir, frag, None, None)

    return out


def main():
    args = sys.argv[1:]
    opts = {"--sources-dir": None, "--plan": None, "--summaries-dir": None,
            "--out": "scratchpad"}
    for flag in list(opts):
        if flag in args:
            i = args.index(flag)
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    positional = [a for a in args if not a.startswith("-")]
    if len(positional) != 1:
        print("Usage: uv run scripts/gen_writer_prompts.py <YYYY-MM-DD> "
              "[--sources-dir DIR] [--plan FILE] [--summaries-dir DIR] [--out DIR]")
        sys.exit(1)
    date = positional[0]
    us = date.replace("-", "_")

    sources_dir = opts["--sources-dir"] or (
        f"journals/{date}/sources" if Path(f"journals/{date}/sources").is_dir()
        else "workdesk")
    plan_path = opts["--plan"] or (
        f"journals/{date}/50_editorial_plan_{us}.md"
        if Path(f"journals/{date}/50_editorial_plan_{us}.md").exists()
        else f"workdesk/editorial_plan_{us}.md")
    summaries_dir = opts["--summaries-dir"] or (
        f"journals/{date}/summaries" if Path(f"journals/{date}/summaries").is_dir()
        else "workdesk/summaries")
    out_dir = Path(opts["--out"])
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        prompts = generate(date, sources_dir, plan_path, summaries_dir, str(out_dir),
                           scratch_out=str(out_dir))
    except (ValueError, FileNotFoundError) as e:
        print(f"❌ gen_writer_prompts: {e}")
        sys.exit(1)
    for name, content in prompts.items():
        (out_dir / name).write_text(content, encoding="utf-8")
    n_main = sum(1 for k in prompts if k.startswith("prompt_main_theme"))
    n_annex = sum(1 for k in prompts if k.startswith("prompt_annex_sec"))
    print(f"wrote {n_main} theme + {n_annex} annex-section prompts to {out_dir}")


if __name__ == "__main__":
    main()
