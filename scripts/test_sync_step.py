#!/usr/bin/env python3
"""Tests for sync_step.py — arg parsing and the dry-run/live plan.

The dry-run test monkeypatches git_gh._exec (the real-execution seam) with a
recorder and asserts it is called ZERO times, proving --dry-run mutates nothing,
while the printed plan still lists every action. A live test proves the command
sequence is correct.

Run:
    uv run scripts/test_sync_step.py
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sync_step  # noqa: E402
from workflow import git_gh  # noqa: E402


class Recorder:
    """Stand-in for git_gh._exec that records argv lists instead of running."""

    def __init__(self):
        self.calls = []

    def __call__(self, argv, *, check=True, capture=False):
        self.calls.append(list(argv))

        class _CP:
            returncode = 0
            stdout = ""
            stderr = ""

        return _CP()


class TestParseArgs(unittest.TestCase):
    def test_minimal(self):
        opts = sync_step.parse_args(["06", "msg"])
        self.assertEqual(opts["step"], "06")
        self.assertEqual(opts["msg"], "msg")
        self.assertEqual(opts["files"], [])
        self.assertIsNone(opts["issue"])
        self.assertFalse(opts["dry_run"])

    def test_zero_pads_step(self):
        self.assertEqual(sync_step.parse_args(["6", "m"])["step"], "06")

    def test_files_and_flags(self):
        opts = sync_step.parse_args(
            ["04", "m", "workdesk/a.md", "workdesk/b.md", "--issue", "200",
             "--no-comment", "--dry-run"]
        )
        self.assertEqual(opts["files"], ["workdesk/a.md", "workdesk/b.md"])
        self.assertEqual(opts["issue"], "200")
        self.assertTrue(opts["no_comment"])
        self.assertTrue(opts["dry_run"])

    def test_issue_equals_form(self):
        self.assertEqual(sync_step.parse_args(["06", "m", "--issue=42"])["issue"], "42")

    def test_missing_msg_raises(self):
        with self.assertRaises(ValueError):
            sync_step.parse_args(["06"])

    def test_non_numeric_step_raises(self):
        with self.assertRaises(ValueError):
            sync_step.parse_args(["abc", "m"])


class TestDryRunPlan(unittest.TestCase):
    def setUp(self):
        self._real_exec = git_gh._exec
        self._real_branch = git_gh.current_branch
        self.rec = Recorder()
        git_gh._exec = self.rec
        git_gh.current_branch = lambda: "feat/test-branch"

    def tearDown(self):
        git_gh._exec = self._real_exec
        git_gh.current_branch = self._real_branch

    def test_dry_run_makes_zero_real_calls_and_prints_plan(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            sync_step.run_sync("06", "STEP_06: focused summaries",
                               issue="200", dry_run=True)
        out = buf.getvalue()

        # The mocked runner recorded zero real git/gh invocations.
        self.assertEqual(self.rec.calls, [])

        # ...but the plan lists every action.
        self.assertIn("git add", out)
        self.assertIn("git commit", out)
        self.assertIn("git", out)
        self.assertIn("push", out)
        self.assertIn("gh label create step-06", out)
        self.assertIn("--add-label step-06", out)
        self.assertIn("--remove-label step-05", out)
        self.assertIn("gh issue comment 200", out)


class TestLivePlan(unittest.TestCase):
    def setUp(self):
        self._real_exec = git_gh._exec
        self._real_branch = git_gh.current_branch
        self._real_staged = git_gh.has_staged_changes
        self.rec = Recorder()
        git_gh._exec = self.rec
        git_gh.current_branch = lambda: "feat/test-branch"
        git_gh.has_staged_changes = lambda: True

    def tearDown(self):
        git_gh._exec = self._real_exec
        git_gh.current_branch = self._real_branch
        git_gh.has_staged_changes = self._real_staged

    def test_live_command_sequence(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            sync_step.run_sync("06", "msg", files=["workdesk/x.md"],
                               issue="200", dry_run=False)
        joined = [" ".join(c) for c in self.rec.calls]
        # add the specified file, commit, push branch, label, swap, comment.
        self.assertTrue(any("git add workdesk/x.md" in c for c in joined))
        self.assertTrue(any(c.startswith("git commit") for c in joined))
        self.assertTrue(any("push" in c and "feat/test-branch" in c for c in joined))
        self.assertTrue(any("label create step-06" in c for c in joined))
        self.assertTrue(any("--add-label step-06" in c for c in joined))
        self.assertTrue(any("issue comment 200" in c for c in joined))

    def test_no_comment_skips_comment(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            sync_step.run_sync("06", "msg", issue="200",
                               no_comment=True, dry_run=False)
        joined = [" ".join(c) for c in self.rec.calls]
        self.assertFalse(any("issue comment" in c for c in joined))


if __name__ == "__main__":
    unittest.main(verbosity=2)
