#!/usr/bin/env python3
"""
Remove metadata from unified summaries for publication.
Removes: Content Type, Scores, Topics, Language tags
Keeps: Title (##見出し), URL, Summary content
"""

import re
import sys

def clean_metadata(content):
    """Remove metadata sections from summary content."""
    lines = content.split('\n')
    cleaned_lines = []
    skip_until_blank = False

    for line in lines:
        # Skip metadata lines
        if any(marker in line for marker in [
            '**コンテンツタイプ**',
            '**Content Type**',
            '**スコア**',
            '**Score**',
            '**トピック**',
            '**Topics**',
            '**言語**',
            '**Language**',
            '【トピック】',
            '【スコア】',
            '【コンテンツタイプ】',
        ]):
            skip_until_blank = True
            continue

        # Resume after blank line following metadata
        if skip_until_blank and line.strip() == '':
            skip_until_blank = False
            continue

        if not skip_until_blank:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def process_file(input_path, output_path):
    """Process a unified summaries file and remove metadata."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned = clean_metadata(content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"Processed: {input_path} -> {output_path}")

if __name__ == '__main__':
    # Process main journal summaries
    process_file(
        'workdesk/unified_summaries_main.md',
        'workdesk/unified_summaries_main_cleaned.md'
    )

    # Process annex journal summaries
    process_file(
        'workdesk/unified_summaries_annex.md',
        'workdesk/unified_summaries_annex_cleaned.md'
    )

    print("\nMetadata cleanup complete!")
    print("Review cleaned files before replacing originals.")
