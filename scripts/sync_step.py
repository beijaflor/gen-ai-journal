#!/usr/bin/env python3
"""One command for the per-step sync ritual: commit -> push -> label -> comment.

Replaces the ~11×/cycle hand ritual of staging changes, committing with the
co-author trailer, pushing over gh-cred HTTPS, moving the tracking issue's
``step-NN`` label, and posting a progress comment.

Usage:
    uv run scripts/sync_step.py <NN> "<msg>" [files...] \
        [--issue N] [--no-comment] [--dry-run]

Examples:
    uv run scripts/sync_step.py 06 "STEP_06: focused summaries" --issue 200
    uv run scripts/sync_step.py 04 "curate main" workdesk/curated_journal_sources.md --dry-run

Idempotent: a no-op commit (nothing staged) is skipped, not an error. Under
``--dry-run`` every action is printed and nothing mutates.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow import git_gh  # noqa: E402

TRAILER = "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
DEFAULT_STAGE_PATHS = ["workdesk", "journals"]


def parse_args(argv):
    """Parse ``<NN> <msg> [files...] [--issue N] [--no-comment] [--dry-run]``.

    Returns a dict. Raises ValueError on a malformed invocation.
    """
    args = list(argv)
    dry_run = False
    no_comment = False
    issue = None

    positional = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--dry-run":
            dry_run = True
        elif a == "--no-comment":
            no_comment = True
        elif a == "--issue":
            if i + 1 >= len(args):
                raise ValueError("--issue requires a value")
            issue = args[i + 1]
            i += 1
        elif a.startswith("--issue="):
            issue = a.split("=", 1)[1]
        else:
            positional.append(a)
        i += 1

    if len(positional) < 2:
        raise ValueError("expected <NN> <msg> [files...]")

    step = positional[0]
    if not step.isdigit():
        raise ValueError(f"step number must be digits, got {step!r}")
    step = f"{int(step):02d}"

    return {
        "step": step,
        "msg": positional[1],
        "files": positional[2:],
        "issue": issue,
        "no_comment": no_comment,
        "dry_run": dry_run,
    }


def run_sync(step, msg, files=None, issue=None, no_comment=False, dry_run=False):
    """Execute the sync ritual. Every git/gh call routes through git_gh."""
    files = files or []
    label = f"step-{step}"
    prev_label = f"step-{int(step) - 1:02d}" if int(step) > 1 else None

    # 1. stage
    stage = files if files else DEFAULT_STAGE_PATHS
    git_gh.run(["git", "add", *stage], dry_run=dry_run)

    # 2. commit (skip cleanly if nothing staged)
    if not dry_run and not git_gh.has_staged_changes():
        print("No staged changes — skipping commit (idempotent no-op).")
        committed = False
    else:
        git_gh.run(["git", "commit", "-m", msg, "-m", TRAILER], dry_run=dry_run)
        committed = True

    # 3. push current branch
    branch = git_gh.current_branch()
    if committed:
        git_gh.push(branch, dry_run=dry_run)
    else:
        print(f"Nothing new to push on {branch}.")

    # 4. ensure the step label exists, then move the issue onto it
    git_gh.ensure_label(label, dry_run=dry_run)
    if issue is not None:
        git_gh.swap_label(issue, prev_label, label, dry_run=dry_run)

        # 5. progress comment
        if not no_comment:
            git_gh.comment(issue, msg, dry_run=dry_run)
    else:
        print("No --issue given: skipping label swap and comment.")

    return committed


def main():
    try:
        opts = parse_args(sys.argv[1:])
    except ValueError as e:
        print(f"Error: {e}")
        print(
            'Usage: uv run scripts/sync_step.py <NN> "<msg>" [files...] '
            "[--issue N] [--no-comment] [--dry-run]"
        )
        sys.exit(1)

    run_sync(
        opts["step"],
        opts["msg"],
        files=opts["files"],
        issue=opts["issue"],
        no_comment=opts["no_comment"],
        dry_run=opts["dry_run"],
    )


if __name__ == "__main__":
    main()
