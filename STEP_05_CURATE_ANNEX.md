# Step 5: Curate Annex Journal

This step reviews and finalizes the annex journal candidate list that was pre-flagged during STEP_04. The annex is the "B-side" collection — articles with genuinely different perspectives, not overflow from main journal themes.

## Objective

Review annex candidates flagged during STEP_04 main curation. These are articles that were excluded from main because they:
- Have an extremely different point of view or unconventional angle
- Are too odd or niche for the main journal's tone
- Cover completely different topics from any main theme

**Key principle:** If an article covers the same subject as a main journal theme, it does NOT belong in the annex. It should either be in the main journal or excluded entirely.

## Input Files

- **Annex candidates (from STEP_04):** `workdesk/curated_annex_journal_sources.md` (pre-flagged during main curation)
- **Non-main summaries:** `workdesk/non_main_unified_summaries.md` (for reference)
- **Supabase flags:** output of `export_curation_flags.py` (Step 0a, optional supplementary signal)
- **Criteria:** `criteria/annex_curation_criteria.md`

---

## Curation Process

### Step 0a: Export Supabase Curation Flags (Required)

Export editor-set flags from Supabase. These represent human pre-curation done during STEP_03 browsing and are the strongest available signal.

```bash
uv run scripts/export_curation_flags.py
```

This outputs a JSON/CSV mapping article IDs to flags:
- `annex_flag=true` — editor explicitly marked for annex consideration (strong inclusion signal)
- `standout_flag=true` — editor marked as exceptional (boost priority)
- `upvote_flag=true` — positive signal
- `downvote_flag=true` — negative signal (deprioritize)

Keep this output in memory for Step 1 signal combination.

### Step 0b: Generate Non-Main Unified Summaries

```bash
uv run scripts/unite_summaries.py workdesk/non_main_sources.md workdesk/summaries workdesk/non_main_unified_summaries.md
```

### Step 1: Review Pre-Flagged Candidates

The annex candidate list (`workdesk/curated_annex_journal_sources.md`) was already created during STEP_04 main curation. Review it and optionally supplement with Supabase flags.

**Verify each candidate against these criteria:**
- **Thematic independence:** Does NOT overlap with any main journal theme
- **Originality:** Unique perspective or novel knowledge?
- **Practical Value:** Actionable for experienced practitioners?
- **Critical Thinking:** Challenges consensus or explores second-order effects?
- **Niche Appeal:** Deep-dives into specialized topics?

**Remove candidates that:**
- Cover the same subject as a main journal theme (these should have been included in main or excluded entirely)
- Are leftover content that didn't make the main journal due to quality, not due to being a different topic
- Are basic tutorials or getting-started guides
- Are pure speculation without substance
- Are marketing material

**Output format:**

```markdown
# Curated Annex Journal Sources - YYYY-MM-DD

## Curation Status
- [ ] AI candidate pool generated
- [ ] Human review completed
- [ ] APPROVED - Ready for STEP_06

---
<!-- Review: check [x] to include, remove line to exclude. Target: ~25-35 articles. -->

- [ ] 050. https://...
  <!-- TerraformにClaude CodeとWezTerm + Hooksを組み合わせたインフラ自動化ワークフロー。Signals: annex_flag ⭐ standout_flag -->

- [ ] 240. https://...
  <!-- MCPのJSON SchemaをCLIに置き換えトークン消費94%削減する手法。Signals: annexPotential 95 -->
```

After writing the file, check off "AI candidate pool generated" in Curation Status.

### Step 2: ⚠️ Human Review Gate

**Stop here. Do not proceed to STEP_06 until the human reviews and approves.**

This gate uses the **`human-review-gate` skill**. The **default path** is a
chat-based `AskUserQuestion` approval: the human reviews the annex selection in
their own editor (Zed, VS Code, etc.) and selects "Approved", after which the
agent flips the approval marker and verifies it on disk. The tmux+vim popup is
an alternative for tmux users. After approving, regenerate `non_main_sources.md`
and re-assert the partition (`uv run python -m scripts.workflow.partition
YYYY-MM-DD`) so annex/omitted stay disjoint from main.

Human review tasks:
- [ ] Read each candidate and editorial comment
- [ ] Check `[x]` on articles to include
- [ ] Remove lines entirely for articles to exclude
- [ ] Aim for ~25–35 final articles
- [ ] Check off "Human review completed" in Curation Status
- [ ] Check off "APPROVED - Ready for STEP_06" in Curation Status

Signal guide for reviewers:
- `annex_flag ⭐` — you pre-screened this during browsing; strong candidate
- `standout_flag` — marked as exceptional
- `annexPotential ≥ 90` — AI scored highly for annex fit
- No signals noted — AI selected on criteria alone; scrutinize more carefully

### Step 3: Write the approved selection → `workdesk/curated_annex_selected.md`

Once the human has approved the pool (all three Curation Status boxes checked),
write the **final annex selection** — only the `[x]`-marked articles — to
`workdesk/curated_annex_selected.md`, grouped under the section headings the
curator chose. This file (not the candidate pool) is what every downstream
script reads as the annex set: `scripts/workflow/partition.py`,
`build_focused.py` (STEP_06), `gen_writer_prompts.py` / `stitch_qa.py`
(STEP_08), `verify_journal.py` (STEP_09), `archive_journal.py` (STEP_10) and
the website's summary-status derivation.

```markdown
# Curated Annex Journal Sources (Selected) - YYYY-MM-DD

## 1. <section title as the curator grouped it>

- [ ] 006. https://...
- [ ] 016. https://...

## 2. <next section>

- [ ] 052. https://...
```

Only `- [ ] NNN. url` / `- [x] NNN. url` lines are parsed (checkbox state is
ignored); the `##` headings become the annex section scaffold for STEP_08's
writer prompts. Then regenerate `non_main_sources.md` and re-assert the
partition:

```bash
uv run scripts/list_urls.py workdesk/curated_journal_sources.md | uv run scripts/remove_urls.py workdesk/sources.md workdesk/non_main_sources.md
uv run python -m scripts.workflow.partition YYYY-MM-DD   # main + annex + omitted == all, disjoint
```

If the partition check fails, an ID is in two sets (or in none) — fix the
curated files, never the check. Mid-cycle promotions/demotions between main and
annex follow `STEP_04b_THEME_REVISION.md`.

### Step 4: Proceed to STEP_06

With `curated_annex_selected.md` written and the partition green, proceed to STEP_06.

---

## Output Files

- `workdesk/curated_annex_journal_sources.md` — the reviewed **candidate pool**
  - Flat list with editorial comments
  - Curation Status section with approval markers
  - Brief Japanese comments explaining each selection and which signals applied
- `workdesk/curated_annex_selected.md` — the **approved selection** (required by
  every later step; see Step 3)
  - `## ` section headings as grouped by the curator, `- [ ] NNN. url` lines only
- `workdesk/non_main_sources.md` — regenerated after the selection

## Verification

- [ ] `export_curation_flags.py` was run (Step 0a)
- [ ] `non_main_unified_summaries.md` exists (Step 0b)
- [ ] AI candidate pool written (~40–50 articles) with signal annotations
- [ ] "AI candidate pool generated" checked in Curation Status
- [ ] Human has reviewed and checked off "APPROVED" before proceeding
- [ ] `workdesk/curated_annex_selected.md` written from the `[x]` articles (Step 3)
- [ ] `uv run python -m scripts.workflow.partition YYYY-MM-DD` is green
- [ ] No overlap with main journal selections
- [ ] Each selected article has a clear editorial comment

## Next Step

[STEP_06_CREATE_FOCUSED_SUMMARIES.md](STEP_06_CREATE_FOCUSED_SUMMARIES.md) - Create focused summary collections for each journal
