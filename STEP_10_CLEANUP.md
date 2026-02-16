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

# Archive editorial plan (contains theme planning + integrated assembly strategies from STEP_07)
# This is the permanent record of editorial decisions and assembly patterns
mv workdesk/editorial_plan_YYYY_MM_DD.md journals/YYYY-MM-DD/50_editorial_plan_YYYY_MM_DD.md
```

**Note:** The editorial plan is preserved in the archive because:
- Documents editorial theme decisions from STEP_03b
- Contains integrated assembly strategies from STEP_07
- Serves as reference for pattern library evolution
- Provides context for future journal workflows

### 2.1 Verify Editorial Plan Completeness

Before archiving the editorial plan, verify it contains integrated assembly strategies:

**Check for:**
- [ ] All themes documented with article lists
- [ ] Assembly strategies integrated under each theme (added in STEP_07)
- [ ] Planning Status shows: `- [x] Assembly strategies defined (STEP_07)`
- [ ] Each theme has "Assembly Strategy" section with pattern, order, transitions

**Why this matters:**
The archived editorial plan serves as historical reference for:
- Understanding how themes were assembled
- Pattern library evolution (what worked/didn't work)
- Future journal workflows

**Verification command:**
```bash
# Check if editorial plan contains assembly strategies
grep -q "Assembly Strategy" workdesk/editorial_plan_YYYY_MM_DD.md && \
  echo "✅ Editorial plan contains strategies" || \
  echo "⚠️  Warning: No assembly strategies found"
```

If strategies are missing:
- Return to STEP_07 to integrate strategies into editorial plan
- Or document in git commit message that this journal predates STEP_07 workflow

### 3. Archive Source Materials

Move curation and source files:

```bash
# Archive source lists
mv workdesk/curated_journal_sources.md journals/YYYY-MM-DD/sources/
mv workdesk/curated_annex_journal_sources.md journals/YYYY-MM-DD/sources/

# Archive list of truly omitted sources (created in STEP_05)
# This file contains URLs that aren't in main OR annex journals
if [ -f workdesk/non_main_sources.md ]; then
    mv workdesk/non_main_sources.md journals/YYYY-MM-DD/sources/non_main_sources.md
fi

# Archive omitted URLs list (rename for clarity)
if [ -f workdesk/omitted_urls.md ]; then
    mv workdesk/omitted_urls.md journals/YYYY-MM-DD/sources/omitted_sources.md
fi

# Archive original sources if available
if [ -f workdesk/sources.md ]; then
    cp workdesk/sources.md journals/YYYY-MM-DD/sources/sources.md
fi
```

**Why archive non_main_sources.md:**
- Created in STEP_05 after main journal curation
- Lists articles not selected for either main or annex journals
- Provides source of truth for what was truly omitted
- Used to generate `02_omitted_summaries.md` in Section 4

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

# Append all summaries (handling JSON format)
# CRITICAL: Summaries are stored as .json files, not .md files
for file in journals/YYYY-MM-DD/summaries/*.json; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .json)
        title=$(jq -r '.content.title' "$file" 2>/dev/null)
        url=$(jq -r '.content.url' "$file" 2>/dev/null)
        summary=$(jq -r '.content.summaryBody' "$file" 2>/dev/null)

        if [ -n "$title" ] && [ "$title" != "null" ]; then
            echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "## $filename" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "**$title**" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "出典: $url" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "$summary" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "" >> journals/YYYY-MM-DD/99_unified_summaries.md
            echo "---" >> journals/YYYY-MM-DD/99_unified_summaries.md
        fi
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

# Add omitted summaries (handling JSON format)
# CRITICAL: Summaries are stored as .json files, not .md files
for file in journals/YYYY-MM-DD/summaries/*.json; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .json)
        file_number=$(echo "$filename" | grep -o '^[0-9]*' | head -1)
        if [ -n "$file_number" ]; then
            source_url=$(grep "^- \[.\] ${file_number}\." journals/YYYY-MM-DD/sources/sources.md | grep -o 'https://[^[:space:]]*' | head -1)
            if [ -n "$source_url" ] && ! grep -Fq "$source_url" temp_selected.txt; then
                # Extract data from JSON using jq
                title=$(jq -r '.content.title' "$file" 2>/dev/null)
                url=$(jq -r '.content.url' "$file" 2>/dev/null)
                summary=$(jq -r '.content.summaryBody' "$file" 2>/dev/null)

                if [ -n "$title" ] && [ "$title" != "null" ]; then
                    echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "## $filename" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "**$title**" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "出典: $url" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "$summary" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                    echo "---" >> journals/YYYY-MM-DD/02_omitted_summaries.md
                fi
            fi
        fi
    fi
done

# Clean up temporary files
rm -f temp_selected.txt
```

### 4.1 Clean Up STEP_07 Working Files

Remove temporary assembly strategy files from workdesk:

```bash
# Clean up STEP_07 working files
# These are temporary files created during STEP_07 assembly planning
# Assembly strategies are now permanently integrated into editorial_plan_YYYY_MM_DD.md (archived above)

# Remove all-themes strategy working file (if exists)
rm -f workdesk/STEP_07_ALL_THEMES_Assembly_Strategies.md

# Remove individual theme strategy files (if exist)
rm -f workdesk/STEP_07_Theme*.md

# Remove demo/proof-of-concept files (if exist)
rm -f workdesk/STEP_07_DEMO*.md
rm -f workdesk/STEP_07_PROOF*.md

echo "✅ STEP_07 working files cleaned up"
```

**Why delete these files:**
- Assembly strategies are now integrated into archived `editorial_plan_YYYY_MM_DD.md`
- Keeping duplicates creates confusion about source of truth
- File lifecycle: Working files → Integration → Deletion
- See `ASSEMBLY_STRATEGY_FILE_ORGANIZATION.md` for details

**Note:** If STEP_07 working files don't exist, this is expected:
- They should have been deleted immediately after integration into editorial plan
- Cleanup here is a safety net to ensure no remnants remain

### 5.1 Clean Up STEP_08 Intermediate Files

Remove any demo or intermediate assembly files from STEP_08:

```bash
# Clean up STEP_08 demo and intermediate files
# These are proof-of-concept or intermediate assembly attempts
# Final assembled journals are archived above

# Remove STEP_08 demo files (if exist)
rm -f workdesk/STEP_08_DEMO*.md
rm -f workdesk/STEP_08_*_Assembled.md

echo "✅ STEP_08 intermediate files cleaned up"
```

**Why delete these files:**
- Final assembled journals (`weekly_journal_YYYY_MM_DD.md`, `annex_journal_YYYY_MM_DD.md`) are archived
- Demo files were for testing/validation during STEP_08 development
- Intermediate assembly attempts should not be preserved

### 5.2 Clean Workspace (General)

Remove remaining temporary and working files:

```bash
# Clean workdesk of completed work
# Specific STEP_07 and STEP_08 files cleaned in sections 4.1 and 5.1 above

# Remove unified summary working files (created in STEP_03, STEP_06)
rm -f workdesk/unified_summaries.md
rm -f workdesk/unified_summaries_main.md
rm -f workdesk/unified_summaries_annex.md

# Remove reviewed files
rm -f workdesk/reviewed_*.md

# Remove any other .md files in workdesk (be careful not to remove files for next cycle)
# Archived files: weekly_journal, annex_journal, editorial_plan (moved above)
# Cleaned files: STEP_07, STEP_08 intermediates (cleaned in 4.1, 5.1)
rm -f workdesk/*.md

# CRITICAL: Remove sources.md to prevent build errors
# The sources.md file is archived in journals/YYYY-MM-DD/sources/
# Keeping it causes the website build to generate pages for workdesk summaries
rm -f workdesk/sources.md

# Remove empty summaries directory
rmdir workdesk/summaries 2>/dev/null || true

# Keep workdesk directory for next cycle
echo "✅ Workdesk cleaned and ready for next cycle"
```

### 6. Mark Summaries as Published (Supabase)

If using the Supabase admin system, mark workdesk summaries as published:

```bash
# Mark all workdesk summaries as published with the journal date
uv run scripts/mark_published.py YYYY-MM-DD
```

**What this does:**
- Updates `journal_date` field in Supabase for all workdesk summaries
- Transitions summaries from draft (workdesk) to published state
- Enables public read access via Row Level Security (RLS) policy
- Preserves summary URLs: `/journals/YYYY-MM-DD/001/` remains valid

**When to run:**
- After archiving journals to `journals/YYYY-MM-DD/`
- Before creating pull request (STEP_12)
- Only run once per journal publication

**Example:**
```bash
uv run scripts/mark_published.py 2025-12-27
# Prompts: "Mark 42 workdesk summaries as published for 2025-12-27? [y/N]"
# Type: y
# Output: "✅ Marked 42 summaries as published"
```

**Prerequisites:**
- `scripts/.env` configured with `SUPABASE_URL` and `SUPABASE_SERVICE_KEY`
- Python dependencies installed: `pip install -r requirements.txt`

See [SUPABASE_WORKFLOW_INTEGRATION.md](SUPABASE_WORKFLOW_INTEGRATION.md) for troubleshooting.

---

## Final Archive Structure

The completed archive should look like:

```
journals/YYYY-MM-DD/
├── 00_weekly_journal_YYYY_MM_DD.md   # Main journal (publication-ready)
├── 01_annex_journal_YYYY_MM_DD.md    # Annex journal (publication-ready)
├── 02_omitted_summaries.md           # Summaries of omitted articles
├── 50_editorial_plan_YYYY_MM_DD.md   # Editorial theme planning + assembly strategies ⭐
├── 99_unified_summaries.md           # All unified summaries (complete reference)
├── sources/
│   ├── sources.md                    # Original source list with all URLs
│   ├── curated_journal_sources.md    # Main journal selected URLs
│   ├── curated_annex_journal_sources.md  # Annex journal selected URLs
│   ├── non_main_sources.md           # URLs not in main journal (from STEP_05) ⭐
│   └── omitted_sources.md            # URLs not included in either journal
└── summaries/
    └── [individual summary files]     # All individual AI-generated summaries
```

**⭐ New/Updated files:**
- `50_editorial_plan_YYYY_MM_DD.md` - Now contains integrated assembly strategies from STEP_07
- `sources/non_main_sources.md` - Created in STEP_05, lists non-main articles

**Why preserve editorial_plan:**
- Documents editorial decisions (theme identification, article mapping)
- Contains assembly strategies (pattern selection, article order, narrative arc)
- Enables pattern library evolution by providing historical reference
- Shows "how we thought about this journal" for future workflows

## Quality Verification

**CRITICAL: All files must follow exact naming conventions**

- [ ] **File Naming Convention:**
  - `00_weekly_journal_YYYY_MM_DD.md` (NOT `main_journal.md`)
  - `01_annex_journal_YYYY_MM_DD.md` (NOT `annex_journal.md`)
  - `02_omitted_summaries.md` (articles NOT selected for either journal)
  - `50_editorial_plan_YYYY_MM_DD.md` (with integrated assembly strategies) ⭐
  - `99_unified_summaries.md` (ALL summaries from the week, not just selected)

- [ ] **Required Files Present:**
  - Both numbered journal files (00_, 01_)
  - Editorial plan (50_) with integrated strategies
  - Comprehensive unified summaries (99_) with ALL summaries
  - Omitted summaries (02_) with non-selected articles only
  - Sources directory with all curation files

- [ ] **Editorial Plan Verification:** ⭐
  - `50_editorial_plan_YYYY_MM_DD.md` contains themes
  - Assembly strategies integrated under each theme (from STEP_07)
  - Planning Status shows: `Assembly strategies defined (STEP_07) - [x]`
  - (If this journal predates STEP_07, document in commit message)

- [ ] **Content Verification:**
  - `99_unified_summaries.md` contains ALL weekly summaries (not split files)
  - `02_omitted_summaries.md` contains only non-selected article summaries
  - **CRITICAL**: Verify `02_omitted_summaries.md` actually has content (not just header) ⭐
  - No `unified_summaries_main.md` or `unified_summaries_annex.md` files
  - Sources directory includes `non_main_sources.md` (if applicable) ⭐

**Validation Commands:**
```bash
# Verify omitted summaries has actual content (should be >100 lines)
wc -l journals/YYYY-MM-DD/02_omitted_summaries.md
# Should show significant line count (e.g., 1000+ lines), not just 5-6 lines

# Verify it contains article entries (should be >0)
grep -c '^## ' journals/YYYY-MM-DD/02_omitted_summaries.md
# Should show number of omitted articles (e.g., 100-150)
```

- [ ] **Workdesk Cleanup Verification:** ⭐
  - No STEP_07 working files remain (`STEP_07_*.md`)
  - No STEP_08 demo files remain (`STEP_08_DEMO*.md`)
  - No unified summary working files remain
  - No `sources.md` in workdesk (archived to journals/)

- [ ] **Structure Consistency:**
  - Main directory follows standard pattern
  - All directories have proper organization
  - No temporary or intermediate files in archive

- [ ] **Clean Workspace:** workdesk cleaned but preserved for next cycle
- [ ] **Access:** Archived files readable and properly formatted

**⭐ = New/updated verification items**

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