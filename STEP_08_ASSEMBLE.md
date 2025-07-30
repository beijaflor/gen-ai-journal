# Step 8: Assemble Final Journals

This step creates the final, publication-ready journal documents by assembling the reviewed summaries into complete journal formats.

## Objective

Transform reviewed summaries into complete, publication-ready journal documents with proper structure, introductions, and editorial flow.

## Input Files

- **Reviewed Main Summaries:** `workdesk/unified_summaries_main.md` (or `workdesk/reviewed_main_summaries.md`)
- **Reviewed Annex Summaries:** `workdesk/unified_summaries_annex.md` (or `workdesk/reviewed_annex_summaries.md`)
- **Main Sources List:** `workdesk/curated_journal_sources.md`
- **Annex Sources List:** `workdesk/curated_annex_journal_sources.md`
- **Empty Journal Templates:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`

## Assembly Process

### 1. Assemble Main Journal

Edit `workdesk/weekly_journal_YYYY_MM_DD.md`:

- [ ] **Add Header Section:**
  ```markdown
  # GenAI週刊 YYYY年MM月DD日号
  
  今週のAI・コーディング関連の重要な動向をお届けします。
  
  ## 今週のハイライト
  [主要トピックの概要を2-3行で]
  ```

- [ ] **Write Introduction:**
  - Brief overview of the week's main themes
  - Highlight significant developments or trends
  - Set context for the selected articles
  - Apply editorial persona voice

- [ ] **Add Article Sections:**
  - Include each refined summary from main summaries
  - Organize by theme, importance, or logical flow
  - Add section headers as needed
  - Ensure smooth transitions between articles

- [ ] **Add Closing Section:**
  - Brief wrap-up or forward-looking perspective
  - Reference annex journal if relevant
  - Call-to-action or engagement prompt

### 2. Assemble Annex Journal

Edit `workdesk/annex_journal_YYYY_MM_DD.md`:

- [ ] **Add Header Section:**
  ```markdown
  # GenAI週刊 Annex YYYY年MM月DD日号
  
  メインジャーナルからは漏れたものの、独自の価値を持つ記事の特集です。
  
  ## Annexについて
  [B-side的価値について簡潔に説明]
  ```

- [ ] **Write Editorial Introduction:**
  - Explain this week's annex selections
  - Note why these articles provide unique value
  - Reference the "B-side" character and experimental insights

- [ ] **Add Article Sections:**
  - Include refined summaries from annex summaries
  - Maintain the "B-side" experimental character
  - Include editorial comments explaining selection rationale
  - Highlight contrarian viewpoints or emerging trends

### 3. Format and Polish

- [ ] **Consistent Formatting:**
  - Uniform heading levels (# ## ###)
  - Proper link formatting with working URLs
  - Consistent section structures
  - Clean markdown syntax

- [ ] **Cross-References:**
  - Link between main and annex where relevant
  - Reference related articles within same journal
  - Add contextual connections

- [ ] **Final Editorial Pass:**
  - Ensure engaging introductions
  - Verify logical flow from article to article
  - Maintain consistent editorial voice throughout
  - Check for typos and formatting issues

## Quality Standards

Final journals must:
- [ ] Have clear, engaging introductions that set context
- [ ] Flow logically from article to article
- [ ] Maintain consistent editorial voice (friendly, technical, startup-minded)
- [ ] Provide value beyond simple article summaries
- [ ] Be ready for publication without further editing
- [ ] Include working links and proper formatting

## Output Files

- **Main Journal:** `workdesk/weekly_journal_YYYY_MM_DD.md` (complete, publication-ready)
- **Annex Journal:** `workdesk/annex_journal_YYYY_MM_DD.md` (complete, publication-ready)

## Next Step

[STEP_09_VERIFY.md](STEP_09_VERIFY.md) - Verify URLs and perform final quality checks