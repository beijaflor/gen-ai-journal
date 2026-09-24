# Step 1: Create Branch

## Overview
Create a dedicated feature branch for the weekly journal to enable isolated development and clean merge process.

## Commands

### Create and switch to journal branch
```bash
git checkout -b journal/YYYY-MM-DD
```

### Verify branch creation
```bash
git branch
git status
```

## Branch Naming Convention
- Format: `journal/YYYY-MM-DD`
- Example: `journal/2025-07-26`

## Create the Tracking Issue & PR

Every journal week is tracked by a GitHub **issue** and a **pull request** that
the rest of the workflow (progress updates, tag, release) links back to.

- **Tracking issue — create it now, at STEP_01.** Title
  `Journal Workflow - Week of YYYY-MM-DD`, labelled `workflow-tracking`,
  `journal-YYYY-MM-DD`, and a `step-XX` progress label. Prefer the
  **github-sync** skill (it fills the issue/PR templates from the current
  `workdesk/` state); or create it directly:
  ```bash
  gh issue create --title "Journal Workflow - Week of YYYY-MM-DD" \
    --label workflow-tracking --label journal-YYYY-MM-DD --label step-01
  ```
- **Draft PR — created after STEP_03** (see [Step 12](STEP_12_PULL_REQUEST.md)):
  `journal/YYYY-MM-DD → main`, opened as a **draft** and converted to
  "Ready for review" at STEP_12.
- **Cross-link** the issue and the PR to each other so STEP_13/14 (tag &
  release) reference the same thread.

## Next Steps
- Proceed to [Step 2: Add Links](STEP_02_GATHER_SOURCES.md)
- All development work happens on this branch
- Main branch remains clean until final merge

## Notes
- Each journal week gets its own branch
- Enables parallel development of multiple weeks if needed
- Facilitates code review through pull requests
- Maintains clean git history