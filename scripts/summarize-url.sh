#!/bin/bash

# One-shot Gemini summarization script
# Usage: ./summarize-url.sh <URL>
# Output: Clean summary to stdout (filters out debug info)

URL="$1"

# Check if URL is provided
if [ -z "$URL" ]; then
    echo "Usage: $0 <URL>" >&2
    echo "Example: $0 https://example.com/article" >&2
    exit 1
fi

# Check if prompt.txt exists
if [ ! -f "/Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt" ]; then
    echo "Error: prompt.txt not found" >&2
    exit 1
fi

# Generate prompt and call gemini, then filter output
sed "s|%%URL%%|$URL|g" /Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt | \
gemini -m "gemini-2.5-flash" --sandbox 2>/dev/null | \
sed -n '/^## /,$p' | \
sed '/^\[WebFetchTool\]/d' | \
sed '/^Loaded cached credentials\./d' | \
sed '/^using macos seatbelt/d' | \
sed '/^(node:[0-9]*)/d' | \
sed '/^{$/,$d'

# Exit with success if we got any output
exit 0