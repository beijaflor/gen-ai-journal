#!/usr/bin/env python3
"""Single source of truth for how the workflow recognises and cleans URLs.

Historically ``list_urls.py`` and ``remove_urls.py`` each carried their own copy
of the URL regex; when one drifted, the set operations they feed (STEP_04/05
partitioning) silently disagreed. This module hosts the one regex and the small
set of helpers both scripts import, so they can never drift again.
"""

import re

# The pattern list_urls.py has always used. Matches an http(s) URL, allowing one
# balanced (...) group in the path (Wikipedia-style URLs) but stopping at
# whitespace and markdown brackets.
URL_PATTERN = r'https?://[^\s\[\]()]+(?:\([^\)]*\))?[^\s\[\]()]*'

# Trailing punctuation that is never part of the URL itself.
_TRAILING_PUNCT = re.compile(r'[.,;:!?)]+$')


def clean_url(url):
    """Strip trailing punctuation from a URL.

    Kept identical to the historical behaviour so refactoring the two scripts
    onto this helper does not change their output.
    """
    return _TRAILING_PUNCT.sub('', url)


def urls_in_line(line):
    """Return the cleaned URLs contained in a single line (may be empty)."""
    return [clean_url(u) for u in re.findall(URL_PATTERN, line)]


def extract_urls(text):
    """Return every cleaned URL found in ``text`` (order preserved)."""
    return [clean_url(u) for u in re.findall(URL_PATTERN, text)]


def exact_filter(lines, remove_set):
    """Return the lines whose URLs are NOT exact members of ``remove_set``.

    A line is dropped only when one of the whole URLs it contains is an exact
    match for a removal URL. This avoids the prefix-collision bug of substring
    matching (``".../A95B"`` wrongly matching ``".../A95B-FP8"``). ``remove_set``
    entries are cleaned the same way so trailing punctuation on either side does
    not matter.
    """
    remove = {clean_url(u) for u in remove_set}
    kept = []
    for line in lines:
        if not any(u in remove for u in urls_in_line(line)):
            kept.append(line)
    return kept
