# Step 7: Assemble Final Journals

This step creates the final journal documents using the curated and reviewed summaries.

## Objective

Transform the selected summaries into complete, publication-ready journal documents with proper structure and editorial flow.

## Input Files

- **Reviewed Summaries:** From previous step
- **Main Journal List:** `journals/YYYY-MM-DD/sources/curated_journal_sources.md`
- **Annex Journal List:** `journals/YYYY-MM-DD/sources/curated_annex_journal_sources.md`
- **Empty Journal Files:**
  - `journals/YYYY-MM-DD/weekly_journal_YYYY_MM_DD.md`
  - `journals/YYYY-MM-DD/annex_journal_YYYY_MM_DD.md`

## Assembly Process

### 1. Main Journal Assembly

Edit `journals/YYYY-MM-DD/weekly_journal_YYYY_MM_DD.md`:

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

Edit `journals/YYYY-MM-DD/annex_journal_YYYY_MM_DD.md`:

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

### 3. Format and Polish

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
  - `journals/YYYY-MM-DD/weekly_journal_YYYY_MM_DD.md` (main journal)
  - `journals/YYYY-MM-DD/annex_journal_YYYY_MM_DD.md` (annex journal)

## Next Step

[STEP_08_CLEANUP.md](STEP_08_CLEANUP.md) - Clean up workspace and archive files