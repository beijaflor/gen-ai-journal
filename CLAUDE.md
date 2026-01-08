# Project Overview

This repository creates weekly curated journals about Generative AI in coding, following a systematic 14-step workflow.

# Editorial Guidelines

## Language Requirements
- **Journal content**: ALWAYS write in Japanese
- **Documentation/prompts**: Write in English
- **Editorial voice**: @EDITOR_PERSONALITY.md - read and adopt this persona when editing journal content

## File Organization
- Journal entries: `journals/YYYY-MM-DD/` directory structure
- Workflow steps: `STEP_01_*.md` through `STEP_14_*.md` files
- Curation criteria: `criteria/` directory

# Code Style & Tools

## File Formatting
- Use standard Markdown for all content
- Use 2-space indentation for nested lists
- Follow consistent heading hierarchy (# ## ###)

## Scripts & Commands
- Use `uv run` for processing scripts
- Key scripts: `process_sources.py`, `scripts/unite_summaries.py`, `scripts/bulk_summarize.py`
- Always use absolute paths when referencing files

## Agent Skills
- **add-url skill**: Validates and adds URLs to workdesk/sources.md one-by-one
  - Invoked automatically when user provides links or mentions "add to journal"
  - Performs duplication checking but does NOT generate summaries
  - URLs are added as unchecked entries: `- [ ] XXX. https://...`

- **summarize-source skill**: Generates summaries for unchecked sources
  - Invoked when user wants to "summarize sources" or "generate summaries"
  - Can process single URL by ID or batch-process all unchecked URLs
  - Uses `uv run scripts/bulk_summarize.py` for batch operations
  - Marks URLs as checked after successful summary generation

## Frequently Used Commands
```bash
# Create journal directory structure
mkdir -p journals/YYYY-MM-DD/{sources,summaries}

# Process and sanitize source URLs
uv run process_sources.py workdesk/sources.md

# STEP_01 & STEP_02: Add URLs and Generate Summaries

# Add URLs one-by-one (via add-url skill - recommended for interactive use)
# The skill validates, checks duplicates, and adds to sources.md as unchecked

# Batch generate summaries for all unchecked URLs (STEP_02)
uv run scripts/bulk_summarize.py

# Dry run to see what would be processed
uv run scripts/bulk_summarize.py --dry-run

# One-shot URL summarization (for single URL)
uv run scripts/call-gemini.py --url "https://example.com/article" --output workdesk/summaries/XXX_domain.md

# DEPRECATED: Old combined workflow (kept for reference)
# uv run scripts/bulk_add_links.py urls.txt

# Aggregate summaries
uv run scripts/unite_summaries.py workdesk/sources.md workdesk/summaries workdesk/unified_summaries.md

# Generate non-main sources after main journal curation (STEP_04)
uv run scripts/list_urls.py workdesk/curated_journal_sources.md | uv run scripts/remove_urls.py workdesk/sources.md workdesk/non_main_sources.md

# Generate unified summaries for non-main sources (STEP_05)
uv run scripts/unite_summaries.py workdesk/non_main_sources.md workdesk/summaries workdesk/unified_summaries_annex.md

# Search for URL in markdown files
grep -l "YOUR_URL_HERE" **/*.md

# Sanitize URL (remove tracking params and fragments)
uv run scripts/sanitize_url.py "URL_HERE"
```

## Editorial Planning Workflow (STEP_03b)

After gathering and summarizing sources, identify editorial themes BEFORE curation:

```bash
# STEP_03b: Plan Editorial Themes (AI-assisted with human review)

# 1. AI analyzes all summaries
#    - Read workdesk/unified_summaries.md
#    - Identify 5-8 cohesive themes
#    - Map articles to themes
#    - Draft theme introductions (Japanese, 2-3 sentences)
#    - Draft "今週のハイライト" outline (3-4 paragraphs)
#    - Create workdesk/editorial_plan_YYYY_MM_DD.md

# 2. Human reviews and approves (MANDATORY REVIEW GATE)
#    - Review themes for coherence
#    - Edit titles, introductions, article mappings
#    - Refine highlight outline
#    - Check ✅ APPROVED in planning document
#    - Commit approved plan to git

# 3. Proceed to STEP_04 with theme-driven curation
#    - Curate articles that fit approved themes
#    - Organize curated_journal_sources.md by themes
#    - Use planning document as blueprint for STEP_08 (Assembly)
```

**Planning Document Structure:**
- 5-8 theme titles (Japanese)
- Article-to-theme mappings (article IDs)
- Theme introductions (2-3 sentences each)
- "今週のハイライト" draft (meta-analysis)
- Theme coverage summary

**Benefits:**
- Theme-driven curation (not article-driven)
- Transparent editorial decisions
- Faster assembly (themes pre-planned)
- Human review gate ensures quality

# Workflow Management

## Next Journal Date Management

### **Date Source**: 
Next journal date is determined by the title in `workdesk/sources.md`:
```
# Sources for Journal 2025-09-07
```

### **URL Structure**:
- **Workdesk summaries** (before publication): `/journals/2025-09-07/001/`
- **Published summaries** (after publication): `/journals/2025-09-07/001/`
- **URLs remain stable** throughout editorial workflow

### **Editorial Workflow**:
1. **Start new week**: Update `workdesk/sources.md` title with next journal date
2. **Content accumulation**: Summaries accessible via `/journals/YYYY-MM-DD/xxx/`
3. **Journal publication**: Same URLs now serve published content
4. **No URL migration**: Links shared during development remain valid

### **Summary Detail Pages**:
- **Workdesk summaries**: Link to `/journals/[next-date]/[id]/` from homepage sidebar
- **Journal summaries**: Link to `/journals/[date]/[id]/` from summaries pages
- **Single route**: `src/pages/journals/[date]/[id].astro` handles both types
- **Content detection**: Automatically serves workdesk or published content based on date

### **Commands**:
```bash
# Check next journal date
grep "^# Sources for Journal" workdesk/sources.md

# Start new journal week (update sources.md title)
# Manual: Edit "# Sources for Journal YYYY-MM-DD" in workdesk/sources.md
```

## Step Execution
- Follow workflow steps sequentially: STEP_01 → STEP_03 → **STEP_03b** → STEP_04 → STEP_14
- **STEP_03b (NEW)**: Plan editorial themes with mandatory human review gate before curation
- **Modern workflow**: Create draft PR after STEP_03 or STEP_03b (recommended) for collaborative editing
- Update TodoWrite frequently to track progress
- Mark steps complete only when fully finished
- Convert draft PR to "Ready for review" at STEP_12

## File Updates
- When updating workflow: modify README.md workflow section AND relevant STEP_XX files
- Keep documentation synchronized across all related files
- Use Edit tool for existing files, Write tool only for new files

## Quality Standards
- Verify all links work before finalizing journals
- Ensure consistent editorial voice throughout
- Maintain separation between main journal (essential) and annex journal (unique insights)