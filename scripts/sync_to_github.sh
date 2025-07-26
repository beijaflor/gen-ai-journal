#!/bin/bash

# Sync workdesk/sources.md to GitHub issue via Claude Code MCP
# Usage: ./scripts/sync_to_github.sh

echo "🔄 Generating GitHub issue content from workdesk/sources.md..."
echo

# Generate the issue content
python3 scripts/sync_sources_to_issue.py

echo
echo "📋 Next steps:"
echo "1. Use Claude Code to search for existing issues with the week identifier"
echo "2. If found, update the existing issue with the new body content"
echo "3. If not found, create a new issue with the title and body above"
echo "4. Add the suggested labels: weekly-sources,journal-YYYY-MM-DD"
echo
echo "💡 You can now use this information with Claude Code's GitHub integration!"