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

### Step 3: Proceed to STEP_06

Once the human has approved the file (all three Curation Status boxes checked), proceed to STEP_06 with the `[x]`-marked articles as the final annex list.

---

## Output Files

- `workdesk/curated_annex_journal_sources.md`
  - Flat list with editorial comments
  - Curation Status section with approval markers
  - Brief Japanese comments explaining each selection and which signals applied

## Verification

- [ ] `export_curation_flags.py` was run (Step 0a)
- [ ] `non_main_unified_summaries.md` exists (Step 0b)
- [ ] AI candidate pool written (~40–50 articles) with signal annotations
- [ ] "AI candidate pool generated" checked in Curation Status
- [ ] Human has reviewed and checked off "APPROVED" before proceeding
- [ ] No overlap with main journal selections
- [ ] Each selected article has a clear editorial comment

## Next Step

[STEP_06_CREATE_FOCUSED_SUMMARIES.md](STEP_06_CREATE_FOCUSED_SUMMARIES.md) - Create focused summary collections for each journal
