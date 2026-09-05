"""Shared library for the weekly-journal workflow automation.

Modules:
    urls          - the single source of the URL regex + set operations.
    partition     - the main/annex/omitted partition invariant.
    git_gh        - git/gh plumbing via the gh-cred HTTPS pattern.
    journal_paths - canonical file paths and blob/Pages URLs for a cycle.

Everything here is mechanics only. Editorial judgement and the three human
review gates (STEP_03b themes, STEP_05 annex, STEP_07 assembly) stay human.
"""
