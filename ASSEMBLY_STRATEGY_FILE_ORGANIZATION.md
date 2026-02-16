# Assembly Strategy File Organization Guidelines

**Version:** 1.0
**Last Updated:** 2026-02-15

---

## Overview

This document defines how assembly strategy files should be organized throughout the journal workflow lifecycle, from creation to archival.

---

## File Lifecycle

```
STEP_07 Creation → Integration → Publication → Archive
     │                 │              │            │
  workdesk/      editorial_plan   journals/    [cleanup]
```

---

## Phase 1: STEP_07 Creation (Working Files)

### Location
`workdesk/` directory

### Files Created

1. **Individual Theme Strategies (Optional for testing/review)**
   ```
   workdesk/STEP_07_Theme[N]_[ShortName]_Strategy.md
   ```

   **Examples:**
   - `workdesk/STEP_07_Theme1_Context_Strategy.md`
   - `workdesk/STEP_07_Theme2_Security_Strategy.md`

   **When to use:**
   - When creating strategies one theme at a time
   - When you want human review of individual themes before proceeding
   - For proof-of-concept/testing

   **Lifecycle:**
   - Delete after merging into ALL_THEMES file
   - OR keep as reference during STEP_08

2. **All Themes Combined (Primary deliverable)**
   ```
   workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md
   ```

   **Purpose:**
   - Single source of truth for all assembly strategies
   - Easy to review all themes at once
   - Ready for integration into editorial plan

   **Lifecycle:**
   - Keep until strategies are integrated into editorial plan
   - Reference during STEP_08 assembly
   - Archive after journal publication

### Naming Convention

**Pattern:** `STEP_07_[Scope]_[Description]_[Type].md`

- **Scope:** `Theme1`, `Theme2`, `ALL_THEMES`, etc.
- **Description:** Short theme name or descriptor
- **Type:** `Strategy`, `Assembly`, etc.

**Examples:**
- ✅ `STEP_07_ALL_THEMES_Assembly_Strategies.md`
- ✅ `STEP_07_Theme1_Context_Strategy.md`
- ❌ `assembly_strategies.md` (too vague)
- ❌ `strategies_final_v3.md` (no STEP prefix, version suffix)

---

## Phase 2: Integration into Editorial Plan

### Target File
`workdesk/editorial_plan_YYYY_MM_DD.md`

### Integration Process

1. **Read the all-themes strategy file:**
   ```
   workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md
   ```

2. **For each theme in editorial plan, append the strategy:**

   **Before (STEP_03b output):**
   ```markdown
   ### Theme 1: [Title]

   **Articles:** [list]
   **Theme Introduction:** [intro]
   **Editorial Notes:** [notes]

   ---
   ```

   **After (STEP_07 integration):**
   ```markdown
   ### Theme 1: [Title]

   **Articles:** [list]
   **Theme Introduction:** [intro]
   **Editorial Notes:** [notes]

   ---

   #### Assembly Strategy (Added in STEP_07)

   **Pattern Selected:** [pattern]
   **Rationale:** [rationale]
   [... rest of strategy ...]

   **Status:**
   - [x] Pattern selected
   - [x] Article order finalized
   - [x] Ready for STEP_08

   ---
   ```

3. **Update editorial plan status:**
   ```markdown
   ## Planning Status
   - [x] Initial theme identification (AI-assisted)
   - [x] Human review and refinement
   - [x] Theme introductions drafted
   - [x] Article-to-theme mapping complete
   - [x] APPROVED - Ready for STEP_04 curation
   - [x] Assembly strategies defined (STEP_07)  ← ADD THIS
   ```

4. **Commit the updated editorial plan:**
   ```bash
   git add workdesk/editorial_plan_YYYY_MM_DD.md
   git commit -m "feat: Add STEP_07 assembly strategies to editorial plan"
   ```

### What to Do with STEP_07 Working Files

**Option A: Keep for reference during STEP_08**
- Useful if you want to cross-reference during assembly
- Keep in workdesk until journal is published
- Advantage: Easy to review without scrolling through large editorial plan

**Option B: Delete after integration (Recommended)**
- Strategies are now in editorial plan (single source of truth)
- Reduces file clutter
- Advantage: Clean workdesk, no duplication

**Recommendation:** Option B (delete after integration)

```bash
# After successful integration:
git rm workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md
git commit -m "chore: Remove STEP_07 working file (integrated into editorial plan)"
```

---

## Phase 3: During STEP_08 (Reference)

### Primary Reference
`workdesk/editorial_plan_YYYY_MM_DD.md` (with integrated strategies)

### Usage
- STEP_08 reads assembly strategies directly from editorial plan
- No separate files needed
- All context (themes + strategies) in one place

---

## Phase 4: Publication & Archive

### When Journal is Published

1. **Editorial plan moves to journal directory:**
   ```
   workdesk/editorial_plan_2026_02_14.md
   → journals/2026-02-14/editorial_plan_2026_02_14.md
   ```

2. **Assembly strategies preserved within editorial plan**
   - Becomes part of journal archive
   - Useful for future reference: "How did we assemble this theme?"
   - Enables pattern library evolution: "What worked in past journals?"

3. **Cleanup workdesk:**
   ```bash
   # After journal publication:
   git mv workdesk/editorial_plan_2026_02_14.md journals/2026-02-14/
   git rm workdesk/STEP_07_* 2>/dev/null || true  # Remove any remaining STEP_07 files
   git commit -m "chore: Archive editorial plan, cleanup STEP_07 working files"
   ```

---

## Special Cases

### Demo/Proof-of-Concept Files

**Naming:** `STEP_07_DEMO_[Description].md` or `STEP_07_PROOF_OF_CONCEPT_*.md`

**Location:** `workdesk/` during development

**Lifecycle:**
- Keep during initial implementation/testing
- Can move to root or delete once system is proven
- Not needed for regular journal workflow

**Current examples:**
- `workdesk/STEP_07_DEMO_Theme1_Assembly_Strategy.md` (proof of concept)
- `STEP_07_PROOF_OF_CONCEPT_SUMMARY.md` (documentation)

**Recommendation:**
- Keep proof-of-concept files in root as documentation
- Delete demo files once system is production-ready
- OR: Move to `archive/step_07_proof_of_concept/` if you want to preserve history

---

## Directory Structure Reference

### Current Journal Work (workdesk/)

```
workdesk/
├── sources.md                                    # STEP_01-02: Source URLs
├── summaries/                                    # STEP_02: Generated summaries
├── unified_summaries.md                          # STEP_03: Combined summaries
├── unified_summaries_main.md                     # STEP_03: Main journal summaries
├── unified_summaries_annex.md                    # STEP_03: Annex summaries
├── editorial_plan_YYYY_MM_DD.md                  # STEP_03b + STEP_07: Plan + Strategies ⭐
├── curated_journal_sources.md                    # STEP_04: Curated main
├── curated_annex_journal_sources.md              # STEP_05: Curated annex
├── non_main_sources.md                           # STEP_05: Non-main URLs
├── STEP_07_ALL_THEMES_Assembly_Strategies.md     # STEP_07: Working file (delete after merge) 🗑️
├── weekly_journal_YYYY_MM_DD.md                  # STEP_08: Assembled main journal
└── annex_journal_YYYY_MM_DD.md                   # STEP_08: Assembled annex journal
```

**Key points:**
- ⭐ Editorial plan is the **permanent home** for assembly strategies
- 🗑️ STEP_07 working file is **temporary** (delete after integration)

### After Publication (journals/)

```
journals/YYYY-MM-DD/
├── 00_weekly_journal_YYYY_MM_DD.md               # Published main journal
├── 01_annex_journal_YYYY_MM_DD.md                # Published annex journal
├── editorial_plan_YYYY_MM_DD.md                  # Archived plan with strategies ⭐
├── sources/                                      # Source markdown files
└── summaries/                                    # Summary detail pages
```

**Key point:**
- ⭐ Editorial plan (with strategies) archived for future reference

---

## Naming Conventions Summary

### Working Files (Temporary)

| File Type | Pattern | Example | Delete When |
|-----------|---------|---------|-------------|
| All themes strategy | `STEP_07_ALL_THEMES_Assembly_Strategies.md` | workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md | After integration |
| Single theme strategy | `STEP_07_Theme[N]_[Name]_Strategy.md` | workdesk/STEP_07_Theme1_Context_Strategy.md | After merging to ALL_THEMES |
| Demo/proof | `STEP_07_DEMO_*.md` or `STEP_07_PROOF_*.md` | workdesk/STEP_07_DEMO_Theme1_Assembly_Strategy.md | After system proven |

### Permanent Files

| File Type | Location | Purpose |
|-----------|----------|---------|
| Editorial plan (with strategies) | workdesk/ → journals/YYYY-MM-DD/ | Single source of truth |
| Pattern library | patterns/assembly/*.md | Reusable patterns |
| Workflow documentation | STEP_07_ASSEMBLY_PLANNING.md | How to do STEP_07 |
| Template | templates/editorial_plan_assembly_strategy_template.md | Strategy structure reference |

---

## Best Practices

### ✅ Do

1. **Always integrate strategies into editorial plan**
   - Single source of truth
   - Easier to review in context
   - Preserved in journal archive

2. **Delete working files after integration**
   - Prevents duplication confusion
   - Keeps workdesk clean
   - Editorial plan has everything needed

3. **Use consistent naming**
   - STEP_07 prefix for all strategy files
   - Descriptive names (ALL_THEMES, Theme1, etc.)
   - Avoid version suffixes (v1, v2, final, etc.)

4. **Commit frequently**
   - After creating ALL_THEMES strategy
   - After integrating into editorial plan
   - After cleanup

5. **Archive editorial plans with journals**
   - Preserves assembly strategies for future reference
   - Enables pattern library evolution
   - Documents decision-making

### ❌ Don't

1. **Don't keep duplicate strategy files**
   - Once integrated into editorial plan, delete working files
   - Exception: During STEP_08 if helpful for reference

2. **Don't scatter strategies across multiple files**
   - Use STEP_07_ALL_THEMES as single working file
   - Merge individual theme files promptly

3. **Don't forget to update editorial plan status**
   - Mark "Assembly strategies defined (STEP_07)" as complete
   - Helps track workflow progress

4. **Don't lose strategies after publication**
   - Always move editorial plan to journals/ directory
   - Strategies are valuable historical reference

5. **Don't use generic filenames**
   - ❌ `strategies.md`
   - ❌ `assembly.md`
   - ✅ `STEP_07_ALL_THEMES_Assembly_Strategies.md`

---

## Quick Reference Workflow

### Creating Strategies (STEP_07)

```bash
# 1. Create all-themes strategy file
# AI creates: workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md

# 2. Review and approve
# Human reviews the file

# 3. Commit working file
git add workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md
git commit -m "feat: STEP_07 assembly strategies for all themes"
```

### Integrating into Editorial Plan

```bash
# 1. Append strategies to editorial plan
# (Copy content from STEP_07_ALL_THEMES file to editorial_plan)

# 2. Update planning status in editorial plan
# (Mark "Assembly strategies defined (STEP_07)" as complete)

# 3. Commit updated editorial plan
git add workdesk/editorial_plan_YYYY_MM_DD.md
git commit -m "feat: Integrate STEP_07 assembly strategies into editorial plan"

# 4. Delete working file (recommended)
git rm workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md
git commit -m "chore: Remove STEP_07 working file (now in editorial plan)"
```

### After Journal Publication

```bash
# 1. Move editorial plan to journal archive
git mv workdesk/editorial_plan_YYYY_MM_DD.md journals/YYYY-MM-DD/

# 2. Cleanup any remaining STEP_07 files
git rm workdesk/STEP_07_* 2>/dev/null || true

# 3. Commit archive
git commit -m "chore: Archive editorial plan with assembly strategies"
```

---

## Troubleshooting

### "I have multiple STEP_07 files in workdesk. Which do I use?"

**Answer:** Use `STEP_07_ALL_THEMES_Assembly_Strategies.md`
- This is the primary deliverable
- Contains all themes
- Delete individual theme files after merging

### "Should I keep STEP_07 files after integrating into editorial plan?"

**Answer:** No (recommended)
- Editorial plan is single source of truth
- Reduces duplication and confusion
- Exception: Can keep during STEP_08 if helpful for reference

### "Where do assembly strategies live after publication?"

**Answer:** In archived editorial plan
- `journals/YYYY-MM-DD/editorial_plan_YYYY_MM_DD.md`
- Strategies are preserved within editorial plan
- Useful for future pattern library evolution

### "Can I create strategies incrementally (theme by theme)?"

**Answer:** Yes, but merge promptly
1. Create individual theme files: `STEP_07_Theme[N]_*.md`
2. Merge into `STEP_07_ALL_THEMES_Assembly_Strategies.md`
3. Delete individual files after merge
4. Then integrate ALL_THEMES into editorial plan

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-15 | Initial guideline created |

---

## Related Documentation

- [STEP_07_ASSEMBLY_PLANNING.md](STEP_07_ASSEMBLY_PLANNING.md) - How to perform STEP_07
- [patterns/assembly/README.md](patterns/assembly/README.md) - Pattern library overview
- [templates/editorial_plan_assembly_strategy_template.md](templates/editorial_plan_assembly_strategy_template.md) - Strategy structure
- [IMPLEMENTATION_SUMMARY_ASSEMBLY_PATTERNS.md](IMPLEMENTATION_SUMMARY_ASSEMBLY_PATTERNS.md) - System overview

---

**Maintained by:** Project contributors
**Questions?** Open an issue or update this guide
