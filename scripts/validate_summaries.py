#!/usr/bin/env python3
"""
Validate JSON summaries against v1.0 schema.

This script validates all JSON summary files in a directory,
checking structure, score ranges, and required fields.

Usage:
    # Validate all summaries in workdesk
    uv run scripts/validate_summaries.py workdesk/summaries

    # Validate specific file
    uv run scripts/validate_summaries.py workdesk/summaries/001_example.json

    # Verbose output
    uv run scripts/validate_summaries.py workdesk/summaries --verbose
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Tuple, List

def validate_json_summary(data: Dict[str, Any], filepath: str = "") -> Tuple[bool, List[str]]:
    """Validate JSON summary structure against v1.0 schema.

    Returns:
        (success: bool, errors: List[str])
    """
    errors = []

    try:
        # Check required top-level fields
        if 'metadata' not in data:
            errors.append("Missing 'metadata' field")
        if 'content' not in data:
            errors.append("Missing 'content' field")

        if errors:
            return False, errors

        metadata = data['metadata']
        content = data['content']

        # Validate metadata
        if metadata.get('version') != '1.0':
            errors.append(f"Invalid version: {metadata.get('version')}, expected '1.0'")

        if not metadata.get('generatedAt'):
            errors.append("Missing generatedAt in metadata")

        if not metadata.get('generatedBy'):
            errors.append("Missing generatedBy in metadata")

        # Validate content required fields
        required_content_fields = [
            'title', 'url', 'language', 'contentType',
            'oneSentenceSummary', 'summaryBody', 'topics', 'scores'
        ]

        for field in required_content_fields:
            if field not in content:
                errors.append(f"Missing required content field: {field}")

        if 'scores' in content:
            # Validate scores structure
            scores = content['scores']
            required_score_fields = [
                'signal', 'depth', 'uniqueness', 'practical', 'antiHype',
                'mainJournal', 'annexPotential', 'overall'
            ]

            for field in required_score_fields:
                if field not in scores:
                    errors.append(f"Missing required score field: {field}")

            # Validate score ranges
            dimension_scores = {
                'signal': scores.get('signal'),
                'depth': scores.get('depth'),
                'uniqueness': scores.get('uniqueness'),
                'practical': scores.get('practical'),
                'antiHype': scores.get('antiHype')
            }

            for name, score in dimension_scores.items():
                if score is not None:
                    if not isinstance(score, int) or score < 0 or score > 5:
                        errors.append(f"Dimension score '{name}' out of range (0-5): {score}")

            composite_scores = {
                'mainJournal': scores.get('mainJournal'),
                'annexPotential': scores.get('annexPotential'),
                'overall': scores.get('overall')
            }

            for name, score in composite_scores.items():
                if score is not None:
                    if not isinstance(score, int) or score < 0 or score > 100:
                        errors.append(f"Composite score '{name}' out of range (0-100): {score}")

        # Validate topics array
        if 'topics' in content:
            topics = content['topics']
            if not isinstance(topics, list):
                errors.append("Topics must be an array")
            elif len(topics) < 1 or len(topics) > 5:
                errors.append(f"Topics array must have 1-5 elements, got {len(topics)}")

        # Validate string lengths
        if 'title' in content:
            if len(content['title']) < 1 or len(content['title']) > 200:
                errors.append(f"Title length out of range (1-200): {len(content['title'])}")

        if 'oneSentenceSummary' in content:
            if len(content['oneSentenceSummary']) < 10 or len(content['oneSentenceSummary']) > 300:
                errors.append(f"One sentence summary length out of range (10-300): {len(content['oneSentenceSummary'])}")

        if 'summaryBody' in content:
            if len(content['summaryBody']) < 100 or len(content['summaryBody']) > 1200:
                errors.append(f"Summary body length out of range (100-1200): {len(content['summaryBody'])}")

        return len(errors) == 0, errors

    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def validate_file(filepath: Path, verbose: bool = False) -> bool:
    """Validate a single JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        is_valid, errors = validate_json_summary(data, str(filepath))

        if is_valid:
            if verbose:
                print(f"✓ {filepath.name}")
            return True
        else:
            print(f"✗ {filepath.name}")
            for error in errors:
                print(f"  - {error}")
            return False

    except json.JSONDecodeError as e:
        print(f"✗ {filepath.name}")
        print(f"  - Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"✗ {filepath.name}")
        print(f"  - Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Validate JSON summaries against v1.0 schema'
    )
    parser.add_argument(
        'path',
        help='Path to JSON file or directory containing JSON files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output (show all files)'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Quiet mode (only show summary)'
    )

    args = parser.parse_args()

    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path does not exist: {path}", file=sys.stderr)
        sys.exit(1)

    # Collect JSON files
    if path.is_file():
        if not path.suffix == '.json':
            print(f"Error: File must be .json: {path}", file=sys.stderr)
            sys.exit(1)
        json_files = [path]
    else:
        json_files = sorted(path.glob('*.json'))
        if not json_files:
            print(f"No JSON files found in: {path}", file=sys.stderr)
            sys.exit(1)

    # Validate files
    if not args.quiet:
        print(f"Validating {len(json_files)} JSON file(s)...")
        print("=" * 50)

    valid_count = 0
    invalid_count = 0

    for json_file in json_files:
        if validate_file(json_file, verbose=args.verbose):
            valid_count += 1
        else:
            invalid_count += 1

    # Summary
    print("=" * 50)
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
    print(f"Total: {len(json_files)}")

    if invalid_count > 0:
        print(f"\n✗ Validation failed: {invalid_count} file(s) have errors")
        sys.exit(1)
    else:
        print(f"\n✓ All files validated successfully")
        sys.exit(0)


if __name__ == '__main__':
    main()
