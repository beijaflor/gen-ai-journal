# Step 7: Assemble Final Journals

This step creates the final journal documents using the curated and reviewed summaries.

## Objective

Transform the selected summaries into complete, publication-ready journal documents with proper structure and editorial flow.

## Input Files

- **Reviewed Main Summaries:** `workdesk/unified_summaries_main.md` (or `workdesk/reviewed_main_summaries.md` if created)
- **Reviewed Annex Summaries:** `workdesk/unified_summaries_annex.md` (or `workdesk/reviewed_annex_summaries.md` if created)
- **Main Journal List:** `workdesk/curated_journal_sources.md`
- **Annex Journal List:** `workdesk/curated_annex_journal_sources.md`
- **Empty Journal Files:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`

## Assembly Process

### 1. Main Journal Assembly

Edit `workdesk/weekly_journal_YYYY_MM_DD.md`:

- [ ] **Add Header Section:**
  ```markdown
  # GenAI週刊 YYYY年MM月DD日号
  
  今週のAI・コーディング関連の重要な動向をお届けします。
  
  ## 今週のハイライト
  [主要トピックの概要を2-3行で]
  ```

- [ ] **Add Introduction:**
  - Write a brief overview of the week's main themes
  - Highlight significant developments or trends
  - Set context for the selected articles

- [ ] **Add Article Sections:**
  - For each URL in curated main sources
  - Include the corresponding refined summary
  - Organize by theme or importance
  - Add section headers as needed

- [ ] **Add Closing Section:**
  - Brief wrap-up or looking ahead
  - Link to annex journal if relevant

### 2. Annex Journal Assembly

Edit `workdesk/annex_journal_YYYY_MM_DD.md`:

- [ ] **Add Header Section:**
  ```markdown
  # GenAI週刊 Annex YYYY年MM月DD日号
  
  メインジャーナルからは漏れたものの、独自の価値を持つ記事の特集です。
  
  ## Annexについて
  [B-side的価値について簡潔に説明]
  ```

- [ ] **Add Editorial Introduction:**
  - Explain this week's annex selections
  - Note why these articles provide unique value
  - Reference the editorial comments from curation

- [ ] **Add Article Sections:**
  - For each URL in curated annex sources
  - Include both the summary AND the editorial comment
  - Maintain the "B-side" character

### 3. Generate Omitted Summaries

- [ ] **Create Omitted Summaries Document:**
  ```bash
  python3 scripts/unite_summaries.py workdesk/omitted_sources.md workdesk/summaries workdesk/omitted_summaries_unified.md
  ```
  - This creates a unified document of all summaries for omitted articles
  - Will be archived as `02_omitted_summaries.md` in Step 8

### 4. Format and Polish

- [ ] **Consistent Formatting:**
  - Uniform heading levels
  - Proper link formatting
  - Consistent section structures

- [ ] **Cross-References:**
  - Link between main and annex where relevant
  - Reference related articles within same journal

- [ ] **Final Proofread:**
  - Check for typos and formatting issues
  - Ensure smooth editorial flow
  - Verify all links work

## Quality Standards

Ensure final journals:
- Have clear, engaging introductions
- Flow logically from article to article
- Maintain consistent editorial voice
- Provide value beyond simple article summaries
- Are ready for publication

## Output

- **Completed Files:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md` (main journal)
  - `workdesk/annex_journal_YYYY_MM_DD.md` (annex journal)
  - `workdesk/omitted_summaries_unified.md` (omitted article summaries)

## Next Step

[STEP_08_CLEANUP.md](STEP_08_CLEANUP.md) - Clean up workspace and archive files