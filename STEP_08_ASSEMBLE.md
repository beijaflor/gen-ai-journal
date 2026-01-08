# Step 8: Assemble Final Journals

This step transforms the refined summaries into complete, publication-ready journal documents with proper structure, introductions, and editorial flow.

## Objective

Create publication-ready journals that match the format of published examples (see `journals/2025-12-06/00_weekly_journal_2025_12_06.md` for reference).

## Input Files

- **Editorial Plan:** `workdesk/editorial_plan_YYYY_MM_DD.md` (APPROVED from STEP_03b)
- **Refined Summaries:**
  - `workdesk/unified_summaries_main.md` (18-25 articles)
  - `workdesk/unified_summaries_annex.md` (remaining articles)
- **Source Lists:**
  - `workdesk/curated_journal_sources.md` (theme-organized from STEP_04)
  - `workdesk/curated_annex_journal_sources.md`
- **Empty Templates:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`

## Assembly Process Overview

STEP_08 is a **manual editorial process** split into 3 sub-steps:

- **STEP_08a**: Organize content and create thematic structure
- **STEP_08b**: Generate journal draft with editorial content
- **STEP_08c**: Polish and verify completeness

---

## STEP_08a: Verify Structure & Refine Plan

**Note:** Theme organization was completed in STEP_03b and STEP_04. This step verifies and refines the approved plan.

### 1. Review Editorial Plan and Refined Summaries

- [ ] Read `workdesk/editorial_plan_YYYY_MM_DD.md` (approved themes and structure)
- [ ] Read `workdesk/unified_summaries_main.md` completely
- [ ] Read `workdesk/unified_summaries_annex.md` completely
- [ ] Verify themes still make sense with final article selection

### 2. Verify Thematic Organization

**For Main Journal** (already organized in STEP_04):
- [ ] Review theme-organized `workdesk/curated_journal_sources.md`
- [ ] Confirm 6-7 thematic sections from editorial plan
- [ ] Verify article distribution within themes is balanced
- [ ] Check logical flow and narrative arc

**Note:** Theme organization was completed in STEP_04 based on the approved editorial plan. If adjustments are needed:
- [ ] Document rationale for changes
- [ ] Update editorial plan if themes evolved significantly during curation

**For Annex Journal** (target: 5-6 sections):
- [ ] Group articles emphasizing B-side character
- [ ] Create descriptive Japanese section titles
- [ ] Common annex themes:
  - Advanced Tactics & Unconventional Wisdom
  - Substantive Critique & Contrarian Views
  - Niche Explorations & Deep Dives
  - Failed Experiments & Cautionary Tales
  - Security Risks & Technical Debt

### 3. Refine Meta-Commentary

- [ ] Review "今週のハイライト" outline from editorial plan
- [ ] Polish to final form (3-4 paragraphs)
- [ ] Ensure it reflects actual curated articles (not just planned ones)
- [ ] Plan "おわりに" conclusion themes
- [ ] Note cross-cutting insights from editorial plan

---

## STEP_08b: Generate Journal Draft

### Main Journal Assembly

#### 1. Header & Introduction

Create `workdesk/weekly_journal_YYYY_MM_DD.md` with:

```markdown
# GenAI週刊 YYYY年MM月DD日号

今週のAI・コーディング関連の重要な動向をお届けします。

## 今週のハイライト

[Use polished version from editorial_plan_YYYY_MM_DD.md - 3-4 paragraphs covering:
- Week's main narrative arc and themes (from planning document)
- Contradictions or tensions between developments
- Significant shifts in industry thinking
- Why this week matters to developers]

---
```

#### 2. Thematic Sections

**For each theme from `workdesk/curated_journal_sources.md` (theme-organized format):**

```markdown
## [Sequential Number]. [Theme Title from Editorial Plan]

[Optional: Theme introduction paragraph from editorial_plan_YYYY_MM_DD.md
 - Use the 2-3 sentence introduction if it helps readers understand the section
 - Omit if the theme title is self-explanatory and articles speak for themselves]

### [Article Japanese Title]

[Article URL - plain text, not markdown link]

[Clean article summary - 300-600 words in Japanese]
[Include: technical concepts, business context, why it matters]
[Exclude: metadata, scores, content type, language, topics tags]

---

### [Next Article in Same Theme...]
```

**Theme Section Order:**
- [ ] Use the sequence from editorial plan OR
- [ ] Reorder for better narrative flow (document why in editorial notes)

**Critical transformation rules**:
- **Include**: Theme title from plan, Japanese article title (##見出し from unified summary), URL, polished summary
- **Exclude**: Original Title, Content Type, Language, Scores, Topics tags, metadata
- **Edit**: Refine summary for editorial voice (see EDITOR_PERSONALITY.md)
- **Format**: Use `---` separator between articles
- **Theme Intro**: Optional - use from editorial plan if it adds value

#### 3. Conclusion

```markdown
## おわりに

[Write 2-3 paragraphs reflecting on:
- Week's significance
- Forward-looking perspective
- Connection to ongoing trends
- Call to ongoing learning]

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
```

### Annex Journal Assembly

#### 1. Header & Annex Philosophy

Create `workdesk/annex_journal_YYYY_MM_DD.md` with:

```markdown
# GenAI週刊 Annex YYYY年MM月DD日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事の特集です。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深堀りを提供する厳選された「B面」コレクションです。

[Explain this week's B-side character: experimental insights, critical perspectives, niche technical dives]

---
```

#### 2. Thematic Sections

Same format as main journal, but:
- Emphasize critical/contrarian perspectives
- Highlight experimental/failed attempts
- Include technical details too niche for main
- Note security warnings and business realities

#### 3. Annex Conclusion

```markdown
## 編集後記

[Write 2-3 paragraphs reflecting on:
- Why these B-side perspectives matter
- Complementary value to main journal
- Encouragement for deeper exploration]

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
```

---

## STEP_08c: Polish & Verify

### 1. Editorial Voice Check

- [ ] Consistent tone: friendly, technical, startup-minded (see EDITOR_PERSONALITY.md)
- [ ] Smooth transitions between articles
- [ ] Japanese language quality and clarity
- [ ] Technical accuracy maintained

### 2. Source Coverage Verification

**Main Journal**:
```bash
# Extract URLs from journal
grep -o 'https://[^[:space:]]*' workdesk/weekly_journal_YYYY_MM_DD.md | sort -u > temp_main_journal_urls.txt

# Extract URLs from curated sources
grep -o 'https://[^[:space:]]*' workdesk/curated_journal_sources.md | sort -u > temp_main_sources.txt

# Compare - should be identical
diff temp_main_journal_urls.txt temp_main_sources.txt

# Clean up
rm temp_main_journal_urls.txt temp_main_sources.txt
```

**Annex Journal**:
```bash
# Same process for annex
grep -o 'https://[^[:space:]]*' workdesk/annex_journal_YYYY_MM_DD.md | sort -u > temp_annex_journal_urls.txt
grep -o 'https://[^[:space:]]*' workdesk/curated_annex_journal_sources.md | sort -u > temp_annex_sources.txt
diff temp_annex_journal_urls.txt temp_annex_sources.txt
rm temp_annex_journal_urls.txt temp_annex_sources.txt
```

- [ ] All curated sources appear in corresponding journal
- [ ] No URLs missing
- [ ] No duplicate URLs

### 3. Format & Polish

- [ ] Consistent heading levels (# for title, ## for sections, ### for articles)
- [ ] Proper `---` separators between articles
- [ ] Clean markdown syntax
- [ ] All URLs are plain text (not markdown links)
- [ ] No metadata remnants (scores, tags, content type)

### 4. Final Quality Check

- [ ] Engaging introductions that set context
- [ ] Logical flow from article to article
- [ ] "今週のハイライト" provides meta-analysis, not just summary
- [ ] "おわりに" offers reflection and forward perspective
- [ ] Ready for publication without further editing

---

## Example Reference

**Study these published journals for format guidance**:
- `journals/2025-12-06/00_weekly_journal_2025_12_06.md` - Main journal format
- `journals/2025-12-06/01_annex_journal_2025_12_06.md` - Annex journal format

**Key patterns to replicate**:
- Section structure (6-7 sections for main, 5-6 for annex)
- Article format (title, URL, summary with no metadata)
- Meta-commentary style in highlights and conclusions
- Editorial voice and tone

---

## Automation Support (Optional)

For teams preferring script-assisted assembly:

```python
# Pseudocode for extraction script
def extract_clean_summary(unified_summary_file):
    articles = []
    for article in parse_markdown(unified_summary_file):
        # Extract
        title_ja = article.title_japanese
        url = article.url
        summary = article.summary_content

        # Clean - remove metadata
        clean_summary = remove_metadata(summary)

        articles.append({
            'title': title_ja,
            'url': url,
            'summary': clean_summary
        })
    return articles

# Human still organizes into themes and writes meta-content
```

---

## Output Files

- **Main Journal**: `workdesk/weekly_journal_YYYY_MM_DD.md` (complete, publication-ready)
- **Annex Journal**: `workdesk/annex_journal_YYYY_MM_DD.md` (complete, publication-ready)

## Quality Standards

Final journals must:
- [ ] Match format of published journal examples
- [ ] Include ALL URLs from curated source lists
- [ ] Have no metadata remnants (scores, tags, etc.)
- [ ] Contain 3-4 paragraph "今週のハイライト" meta-analysis
- [ ] Organize articles into 5-7 thematic sections
- [ ] Maintain consistent editorial voice throughout
- [ ] Be ready for direct publication

## Next Step

[STEP_09_VERIFY.md](STEP_09_VERIFY.md) - Verify URLs and perform final quality checks
