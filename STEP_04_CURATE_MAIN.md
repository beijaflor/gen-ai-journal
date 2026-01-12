# Step 4: Curate Main Journal

This step selects the most important and valuable articles for the main journal using a **theme-driven approach** based on the approved editorial plan from STEP_03b.

## Objective

Select 18-25 articles that fit the approved themes, providing essential insights, significant developments, and high-value content for the primary audience.

## Input Files

- **Editorial Plan:** `workdesk/editorial_plan_YYYY_MM_DD.md` (APPROVED from STEP_03b)
- **Source List:** `workdesk/sources.md` (all URLs with checkboxes)
- **Summaries:** `workdesk/unified_summaries.md` (for review)
- **Criteria:** `criteria/curation_criteria.md`

## Curation Process

**IMPORTANT:** This step is now **THEME-DRIVEN**. Follow the approved editorial plan from STEP_03b.

**CRITICAL:** Read entire sources and pick from them and **NEVER** make up false URLs.

### 0. Prepare

- [ ] Read and adopt the editorial persona from `EDITOR_PERSONALITY.md`
  - Adopt the role of a **technical web application engineer** with startup mindset
  - Focus on "why it matters" beyond just "what happened"
  - Apply editorial judgment that is **visionary but grounded**

- [ ] Review approved editorial plan: `workdesk/editorial_plan_YYYY_MM_DD.md`
  - Note identified themes and article mappings
  - Understand the week's narrative arc
  - Review planned article distribution (18-25 articles across 6-7 themes)

### Optional: Export Admin Flags

If you used the Supabase admin system in STEP_03, export flagged summaries to assist with curation:

```bash
# Export admin-flagged summaries to markdown files
uv run scripts/export_curation_flags.py
```

This creates:
- **`workdesk/curated_annex_journal_sources.md`**: Summaries flagged for annex (with ⭐/👍/👎 markers)
- **`workdesk/omitted_sources.md`**: Summaries flagged for omission

**Note:** These are suggestions based on initial admin review, not final decisions. Apply editorial judgment and curation criteria when making final selections.

See [SUPABASE_WORKFLOW_INTEGRATION.md](SUPABASE_WORKFLOW_INTEGRATION.md) for details.

---

### 1. Theme-Based Article Selection

**For each theme in the editorial plan:**

- [ ] Review articles mapped to this theme in the editorial plan
- [ ] Verify each article meets main journal criteria:
  - **Thematic Fit:** Does it align with this specific theme?
  - **Signal Strength:** Is it a primary source or deep analysis?
  - **Uniqueness:** Does it provide unique insights not found elsewhere?
  - **Technical Depth:** Does it discuss trade-offs and architectural perspectives?
  - **Lasting Value:** Will it remain relevant beyond this week?

- [ ] Select final articles for this theme (may differ from plan based on deeper review)
- [ ] Document any deviations from editorial plan with rationale

### 2. Finalize Article Selection

- [ ] Verify total selection: 18-25 articles
- [ ] Ensure thematic coherence across all selected articles
- [ ] Check for unintentional duplicates or redundancy within and across themes
- [ ] Confirm each theme has adequate coverage (typically 3-5 articles per theme)

### 3. Avoid Common Pitfalls

Do NOT include:

- Surface-level tutorials or "getting started" guides
- Pure marketing content or hype pieces
- Duplicate coverage of the same topic
- Personal diary-style blog posts without broader insights
- Articles that don't fit the approved themes (save for annex consideration)

## Output Files

Create or update:

- [ ] `workdesk/curated_journal_sources.md` (theme-organized format)

**NEW FORMAT:** Organize by themes from the editorial plan:

```markdown
# Curated Main Journal Sources - YYYY-MM-DD

## Theme 1: [Japanese Theme Title from Editorial Plan]

- [ ] 007. https://example.com/article-1
- [ ] 012. https://example.com/article-2
- [ ] 023. https://example.com/article-3

## Theme 2: [Japanese Theme Title from Editorial Plan]

- [ ] 001. https://example.com/article-4
- [ ] 015. https://example.com/article-5

## Theme 3: [Japanese Theme Title from Editorial Plan]

- [ ] 003. https://example.com/article-6
- [ ] 009. https://example.com/article-7
- [ ] 018. https://example.com/article-8
- [ ] 025. https://example.com/article-9

[Continue for all themes...]
```

**Benefits:**
- Clear thematic organization for STEP_06 and STEP_08
- Easy to verify theme coverage
- Preserves article IDs for tracking
- Human-readable structure
- Directly maps to approved editorial plan

### 4. Generate Non-Main Sources List

After main journal curation is complete, generate the list of remaining sources for annex consideration:

```bash
uv run scripts/list_urls.py workdesk/curated_journal_sources.md | uv run scripts/remove_urls.py workdesk/sources.md workdesk/non_main_sources.md
```

This command:
1. Extracts URLs from the curated main journal sources
2. Removes those URLs from the complete source list
3. Creates `workdesk/non_main_sources.md` with remaining URLs for annex review

## Verification

- [ ] Confirm 18-25 articles selected
- [ ] All articles align with approved themes from STEP_03b
- [ ] Theme organization in curated_journal_sources.md matches editorial plan
- [ ] No duplicate topics within same theme or across themes
- [ ] Each theme has adequate coverage (typically 3-5 articles)
- [ ] Verify `workdesk/non_main_sources.md` contains remaining sources
- [ ] Document any deviations from editorial plan (see below)

## Deviations from Editorial Plan

If actual curation differs from STEP_03b plan, document here or in editorial plan file:

**Articles added that weren't planned:**
- [Article ID and URL] - Rationale: [Why this article was added despite not being in the plan]

**Articles removed that were planned:**
- [Article ID and URL] - Rationale: [Why this planned article was not selected]

**Theme adjustments:**
- [Describe any theme reorganization or title changes]

These notes will help refine the planning process in future weeks and maintain transparency in editorial decisions.

## Next Step

[STEP_05_CURATE_ANNEX.md](STEP_05_CURATE_ANNEX.md) - Review non-main sources for annex journal
