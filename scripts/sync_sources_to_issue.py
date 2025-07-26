#!/usr/bin/env python3
"""
Generate GitHub issue content from workdesk/sources.md for MCP sync.
Outputs formatted issue title and body for manual creation/update via Claude Code.
"""

import sys
import re
from datetime import datetime, timedelta
from pathlib import Path

def get_current_week():
    """Get current week identifier (YYYY-MM-DD format for Monday of the week)."""
    today = datetime.now()
    # Get Monday of current week
    monday = today - timedelta(days=today.weekday())
    return monday.strftime("%Y-%m-%d")

def read_sources_file():
    """Read workdesk/sources.md and return its content."""
    sources_file = Path("workdesk/sources.md")
    if not sources_file.exists():
        print("Error: workdesk/sources.md not found", file=sys.stderr)
        return None
    
    with open(sources_file, 'r') as f:
        return f.read()

def count_links_by_status(content):
    """Count total, processed, and pending links."""
    if not content:
        return 0, 0, 0
    
    total = len(re.findall(r'- \[[x ]\] \d{3}\.', content))
    processed = len(re.findall(r'- \[x\] \d{3}\.', content))
    pending = total - processed
    
    return total, processed, pending

def get_repo_info():
    """Get current repository name from the working directory."""
    cwd = Path.cwd()
    return cwd.name

def main():
    """Output issue title and body for MCP sync."""
    # Get current week identifier
    week_id = get_current_week()
    
    # Read sources.md
    sources_content = read_sources_file()
    if sources_content is None:
        sys.exit(1)
    
    # Count progress
    total, processed, pending = count_links_by_status(sources_content)
    progress_percentage = int((processed / total) * 100) if total > 0 else 0
    
    # Generate issue title
    title = f"Weekly Journal Sources - Week of {week_id}"
    
    # Generate issue body
    body = f"""# Weekly Journal Sources - Week of {week_id}

## Progress Summary
- **Total Links**: {total}
- **Processed**: {processed} ✅
- **Pending**: {pending} ⏳
- **Completion**: {progress_percentage}%

## Source Links

{sources_content}

---
*This issue tracks the weekly journal source collection and processing.*  
*Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

## Next Steps
- [ ] Complete pending link summaries
- [ ] Review and categorize sources
- [ ] Begin journal curation process
"""

    # Output formatted for MCP
    print("=== GITHUB ISSUE SYNC ===")
    print(f"TITLE: {title}")
    print(f"LABELS: weekly-sources,journal-{week_id}")
    print(f"REPO: {get_repo_info()}")
    print("BODY:")
    print("=" * 40)
    print(body)
    print("=" * 40)
    
    # Output search hint
    print(f"\nSEARCH HINT: Look for existing issue with title containing 'Week of {week_id}'")

if __name__ == "__main__":
    main()