# Step 10: Archive & Cleanup

This final step archives the completed journals and source materials to the permanent directory structure and cleans the workspace.

## Objective

Move completed journals and supporting materials to the permanent archive structure and prepare the workspace for the next weekly cycle.

## Input Files

- **Completed Journals:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`
- **Source Materials:**
  - `workdesk/curated_journal_sources.md`
  - `workdesk/curated_annex_journal_sources.md`
  - `workdesk/omitted_urls.md`
- **Summary Files:**
  - `workdesk/summaries/` directory
  - `workdesk/omitted_summaries_unified.md`

## Archive Process

### 1. Create Archive Directory

```bash
# Create the dated journal directory
mkdir -p journals/YYYY-MM-DD/{sources,summaries}
```

### 2. Archive Journals

Move completed journal files:

```bash
# Archive main and annex journals with proper naming
mv workdesk/weekly_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/00_weekly_journal_YYYY_MM_DD.md
mv workdesk/annex_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/01_annex_journal_YYYY_MM_DD.md
```

### 3. Archive Source Materials

Move curation and source files:

```bash
# Archive source lists
mv workdesk/curated_journal_sources.md journals/YYYY-MM-DD/sources/
mv workdesk/curated_annex_journal_sources.md journals/YYYY-MM-DD/sources/
mv workdesk/omitted_urls.md journals/YYYY-MM-DD/sources/omitted_sources.md

# Archive original sources if available
if [ -f workdesk/sources.md ]; then
    cp workdesk/sources.md journals/YYYY-MM-DD/sources/sources.md
fi
```

### 4. Archive Summaries

Move summary files and create archive summaries:

```bash
# Archive all individual summaries
mv workdesk/summaries/* journals/YYYY-MM-DD/summaries/

# Create comprehensive unified summaries (ALL summaries from the week)
# CRITICAL: 99_unified_summaries.md must contain ALL summaries, not just selected ones
echo "# 全記事要約 YYYY年MM月DD日号

この週に収集・要約された全記事の完全なアーカイブです。

---" > journals/YYYY-MM-DD/99_unified_summaries.md

# Append all summaries
for file in journals/YYYY-MM-DD/summaries/*.md; do
    if [ -f "$file" ]; then
        echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
        echo "## $(basename "$file" .md)" >> journals/YYYY-MM-DD/99_unified_summaries.md
        echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
        cat "$file" >> journals/YYYY-MM-DD/99_unified_summaries.md
        echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
        echo "---" >> journals/YYYY-MM-DD/99_unified_summaries.md
    fi
done

# Create omitted summaries (articles NOT in either journal)
# This requires matching against curated source files to identify selected vs omitted
echo "# 非掲載記事要約 YYYY年MM月DD日号

メインジャーナルおよびAnnexジャーナルに掲載されなかった記事の要約集です。

---" > journals/YYYY-MM-DD/02_omitted_summaries.md

# Extract selected URLs from curated files
grep -o 'https://[^[:space:]]*' journals/YYYY-MM-DD/sources/curated_journal_sources.md > temp_selected.txt
grep -o 'https://[^[:space:]]*' journals/YYYY-MM-DD/sources/curated_annex_journal_sources.md >> temp_selected.txt

# Add omitted summaries
for file in journals/YYYY-MM-DD/summaries/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .md)
        file_number=$(echo "$filename" | grep -o '^[0-9]*' | head -1)
        if [ -n "$file_number" ]; then
            source_url=$(grep "^- \[.\] ${file_number}\." journals/YYYY-MM-DD/sources/sources.md | grep -o 'https://[^[:space:]]*' | head -1)
            if [ -n "$source_url" ] && ! grep -Fq "$source_url" temp_selected.txt; then
                echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                echo "## $filename" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                cat "$file" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                echo "---" >> journals/YYYY-MM-DD/02_omitted_summaries.md
            fi
        fi
    fi
done

# Clean up temporary files
rm -f temp_selected.txt
```

### 5. Clean Workspace

Remove temporary and working files:

```bash
# Clean workdesk of completed work
rm -f workdesk/unified_summaries.md
rm -f workdesk/unified_summaries_main.md
rm -f workdesk/unified_summaries_annex.md
rm -f workdesk/reviewed_*.md
rm -f workdesk/*.md

# CRITICAL: Remove sources.md to prevent build errors
# The sources.md file is archived in journals/YYYY-MM-DD/sources/
# Keeping it causes the website build to generate pages for workdesk summaries
rm -f workdesk/sources.md

# Remove empty summaries directory
rmdir workdesk/summaries 2>/dev/null || true

# Keep workdesk directory for next cycle
```

## Final Archive Structure

The completed archive should look like:

```
journals/YYYY-MM-DD/
├── 00_weekly_journal_YYYY_MM_DD.md   # Main journal (publication-ready)
├── 01_annex_journal_YYYY_MM_DD.md    # Annex journal (publication-ready)
├── 02_omitted_summaries.md           # Summaries of omitted articles
├── 99_unified_summaries.md           # All unified summaries (complete reference)
├── sources/
│   ├── sources.md                    # Original source list with all URLs
│   ├── curated_journal_sources.md    # Main journal selected URLs
│   ├── curated_annex_journal_sources.md  # Annex journal selected URLs
│   └── omitted_sources.md            # URLs not included in either journal
└── summaries/
    └── [individual summary files]     # All individual AI-generated summaries
```

## Quality Verification

**CRITICAL: All files must follow exact naming conventions**

- [ ] **File Naming Convention:**
  - `00_weekly_journal_YYYY_MM_DD.md` (NOT `main_journal.md`)
  - `01_annex_journal_YYYY_MM_DD.md` (NOT `annex_journal.md`)
  - `02_omitted_summaries.md` (articles NOT selected for either journal)
  - `99_unified_summaries.md` (ALL summaries from the week, not just selected)

- [ ] **Required Files Present:**
  - Both numbered journal files (00_, 01_)
  - Comprehensive unified summaries (99_) with ALL summaries
  - Omitted summaries (02_) with non-selected articles only
  - Sources directory with all curation files

- [ ] **Content Verification:**
  - `99_unified_summaries.md` contains ALL weekly summaries (not split files)
  - `02_omitted_summaries.md` contains only non-selected article summaries
  - No `unified_summaries_main.md` or `unified_summaries_annex.md` files
  
- [ ] **Structure Consistency:**
  - Main directory follows standard pattern
  - Gemini edition (if exists) follows same naming pattern
  - All directories have proper organization

- [ ] **Clean Workspace:** workdesk cleaned but preserved for next cycle
- [ ] **Access:** Archived files readable and properly formatted

## Git Commit

Consider committing the archived journal to version control:

```bash
# Add archived journal
git add journals/YYYY-MM-DD/

# Commit with descriptive message
git commit -m "Add weekly journal for YYYY-MM-DD

- Main journal: [brief description of main themes]
- Annex journal: [brief description of annex themes]
- Total sources processed: [number]
- Main articles: [number]
- Annex articles: [number]"
```

## Workspace Ready

After cleanup, the workspace is ready for the next weekly cycle:
- `workdesk/` directory empty and ready
- Archive safely stored in `journals/YYYY-MM-DD/`
- Git repository updated with new journal
- Ready to start Step 1 for next week

## Next Step

Proceed to [STEP_11_GENERATE_METADATA.md](STEP_11_GENERATE_METADATA.md) to generate the mandatory metadata file before creating the pull request.