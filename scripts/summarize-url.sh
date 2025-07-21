#!/bin/bash

# One-shot Gemini summarization script
# Usage: ./summarize-url.sh <URL>
# Output: Summary to stdout

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

# Generate prompt and call gemini
sed "s|%%URL%%|$URL|g" /Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt | \
gemini -m "gemini-2.5-flash" --sandbox

# Exit with gemini's exit code
exit ${PIPESTATUS[1]}