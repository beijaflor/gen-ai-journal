# Step 1: Gather and Add Links

This step describes how to collect and add links to the journal workflow.

## Overview

The new workflow involves:
1. Check if a link is valid and unique
2. Manually add links to sources.md
3. Generate summaries using the one-shot script

## Checking Links Before Adding

### Command Usage

```bash
python3 scripts/check_link.py <URL>
```

Example:
```bash
python3 scripts/check_link.py https://example.com/article-about-ai-coding
```

### What the Check Script Does

1. **Sanitizes the URL** - Removes UTM parameters and fragments
2. **Checks for duplicates** - Searches in both sources.md and summaries
3. **Reports status** - Tells you if the URL is unique and ready to add

## Manual Link Addition Process

After checking a link is unique:

1. **Add to sources.md** - Manually edit `workdesk/sources.md` and add the link with an ID
   ```markdown
   ## Main List
   - [ ] 001. https://example.com/article1
   ```

2. **Generate Summary** - Use the one-shot script:
   ```bash
   uv run scripts/call-gemini.py --url "https://example.com/article1" > workdesk/summaries/001_example_com_article1.md
   ```

3. **Mark as Processed** - Update the checkbox in sources.md:
   ```markdown
   ## Main List
   - [x] 001. https://example.com/article1
   ```

## Managing Categories

After adding links, you can manually edit `workdesk/sources.md` to move links between categories:
- **Main List** - Primary articles for the main journal
- **Slides** - Presentation materials
- **Might Be Hype** - Articles that need careful evaluation
- **Better to be Omitted** - Articles to exclude from journals

## Continuous Addition

You can check and add links throughout the week as you discover them:

1. **Check the link**:
   ```bash
   python3 scripts/check_link.py https://blog.example.com/ai-agents-2025
   ```

2. **If unique, add to sources.md and generate summary**:
   ```bash
   # Add to sources.md manually, then:
   uv run scripts/call-gemini.py --url "https://blog.example.com/ai-agents-2025" > workdesk/summaries/001_blog_example_com_ai_agents_2025.md
   ```

## Progress Tracking with GitHub Issues

You can sync your sources to GitHub for progress tracking at any time:

### GitHub Sync Command
```
"Sync workdesk/sources.md to GitHub issue"
```

### What the Sync Does
- Creates or updates a weekly GitHub issue with current progress
- Shows total links, processing status, and completion percentage
- Includes complete source list with checkboxes for team visibility
- Auto-generates appropriate labels and formatting

### When to Sync
- After adding new links to maintain visibility
- After completing summaries (checking boxes)
- Before starting curation process
- At end of weekly collection period

For detailed sync workflow, see [GITHUB_SYNC.md](GITHUB_SYNC.md).

## Next Steps

Once you have added sufficient links (typically 30-50 for a weekly journal):
- Review and categorize links in `workdesk/sources.md`
- Sync to GitHub issue for progress tracking
- Continue to [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md) for journal preparation
- Note: STEP_02 (bulk summarization) is now integrated into the add_link process