#!/usr/bin/env python3
"""git / gh plumbing, all through the gh-cred HTTPS pattern.

SSH is down on the build machine, so every push/fetch goes over HTTPS with the
gh credential helper, and every ``gh`` call runs with ``GITHUB_TOKEN=""`` so it
uses the keyring auth rather than any injected token.

Testability: everything shells out through the module-level ``run`` function.
Tests monkeypatch ``git_gh.run`` with a recorder to assert that ``--dry-run``
makes zero real invocations and that the planned commands are correct.
"""

import os
import shlex
import subprocess

REMOTE_URL = "https://github.com/beijaflor/gen-ai-journal.git"
CRED_HELPER = "!gh auth git-credential"


def _env():
    """Environment with GITHUB_TOKEN cleared so gh uses keyring auth."""
    e = dict(os.environ)
    e["GITHUB_TOKEN"] = ""
    return e


def _exec(argv, *, check=True, capture=False):
    """The real-execution seam. Tests monkeypatch this with a recorder so they
    can assert that ``--dry-run`` fires it zero times."""
    return subprocess.run(
        argv,
        env=_env(),
        check=check,
        text=True,
        capture_output=capture,
    )


def run(argv, *, dry_run=False, check=True, capture=False):
    """Execute a command (list argv). Honors dry_run by printing, not running.

    This is the single choke point every git/gh call goes through: under
    ``--dry-run`` it prints the plan and never touches ``_exec``, so a recorder
    swapped in for ``_exec`` proves zero real invocations.
    """
    if dry_run:
        print(f"[dry-run] {shlex.join(argv)}")
        return subprocess.CompletedProcess(argv, 0, "", "")
    return _exec(argv, check=check, capture=capture)


def current_branch():
    """Return the current git branch name (read-only; never gated by dry_run)."""
    out = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        text=True,
        capture_output=True,
        check=True,
    )
    return out.stdout.strip()


def has_staged_changes():
    """True if the index has staged changes (so we know whether commit is a no-op)."""
    r = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return r.returncode != 0


def push(ref, *, dry_run=False):
    """Push ``ref`` to the HTTPS remote using the gh credential helper."""
    return run(
        ["git", "-c", f"credential.helper={CRED_HELPER}", "push", REMOTE_URL, ref],
        dry_run=dry_run,
    )


def ensure_label(name, *, color="ededed", dry_run=False):
    """Create (or update) a label; idempotent via --force."""
    return run(
        ["gh", "label", "create", name, "--color", color, "--force"],
        dry_run=dry_run,
    )


def swap_label(issue, frm, to, *, dry_run=False):
    """Move an issue from label ``frm`` to label ``to``.

    Adds ``to`` (checked), then removes ``frm`` best-effort (check=False) so a
    missing previous label does not fail the swap — keeps the call idempotent.
    """
    run(["gh", "issue", "edit", str(issue), "--add-label", to], dry_run=dry_run)
    if frm:
        run(
            ["gh", "issue", "edit", str(issue), "--remove-label", frm],
            dry_run=dry_run,
            check=False,
        )


def comment(issue, body, *, dry_run=False):
    """Post a comment on an issue/PR."""
    return run(
        ["gh", "issue", "comment", str(issue), "--body", body],
        dry_run=dry_run,
    )
