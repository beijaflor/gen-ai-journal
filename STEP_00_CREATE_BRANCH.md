# Step 0: Create Branch

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

## Next Steps
- Proceed to [Step 1: Add Links](STEP_01_GATHER_SOURCES.md)
- All development work happens on this branch
- Main branch remains clean until final merge

## Notes
- Each journal week gets its own branch
- Enables parallel development of multiple weeks if needed
- Facilitates code review through pull requests
- Maintains clean git history