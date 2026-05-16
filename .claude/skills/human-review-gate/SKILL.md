---
name: human-review-gate
description: Blocking human review gate for AI-drafted planning documents. Opens the file in a tmux popup with vim, blocks until the editor closes, and verifies an approval marker. Use at every "AI drafts → human reviews → AI proceeds" handoff (STEP_03b editorial plan, STEP_07 assembly strategy, etc.).
allowed-tools: Bash, Read, Edit, AskUserQuestion
---

# Human Review Gate

Many workflow steps require a human to review an AI-drafted planning document before
the workflow can continue. This skill is the **single mechanism** for that gate. Use
it at every such handoff.

## When to Use This Skill

Use this skill whenever:

- A workflow step requires human review of an AI-drafted document before
  proceeding (e.g. STEP_03b approves `editorial_plan_YYYY_MM_DD.md`, STEP_07
  approves the assembly strategy section appended to the same plan).
- The agent has just regenerated or substantially edited a planning document
  that was already approved — re-review is required.
- Any future step adds a human-in-the-loop checkpoint over a markdown artifact.

Do **not** use this skill for:

- Quick yes/no confirmations (use `AskUserQuestion` directly).
- Reviewing diffs or PRs (use `gh pr review`).
- Soliciting feedback on a draft that has not yet been written to a file.

## Contract

A review gate has succeeded if and only if **both** are true after the call:

1. The human has reviewed the document — either by editing it inside the vim popup,
   or by explicitly approving it through an `AskUserQuestion` confirmation that
   names the file.
2. The file contains an approval marker matching the agreed pattern.

The agent **may write the approval marker** only after the human has explicitly
confirmed approval through `AskUserQuestion`. The agent **MUST NOT** silently
auto-approve based on diff inspection, time elapsed, or assumptions about intent.

## Default Approval Markers

Planning documents in this repo use checked-checkbox approval lines:

```
- [x] APPROVED - Ready for STEP_04 curation             (STEP_03b)
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08         (STEP_07)
```

The agent writes the line as `- [ ]` (unchecked). It is flipped to `- [x]` either
by the human inside vim, or by the agent's `Edit` tool after the human's explicit
`AskUserQuestion` approval.

## Workflow

### 1. Pre-Flight

Before invoking the gate:

- [ ] The planning document is fully drafted and saved to disk.
- [ ] An unchecked approval line is present in the file as the canonical
  marker, e.g. `- [ ] APPROVED - Ready for STEP_04 curation`.
- [ ] Working directory is the repo root.

### 2. Invoke the Gate

```bash
bash scripts/review_in_popup.sh \
  workdesk/editorial_plan_YYYY_MM_DD.md \
  '^- \[x\] APPROVED'
```

Replace the file path and pattern for the calling step. The script:

1. Opens the file in `vim` inside a blocking `tmux display-popup -E` popup.
2. Blocks until the human closes vim.
3. Re-reads the file from disk and `grep -E`-matches the approval pattern.
4. Returns exit code:
   - `0` → approval marker found, proceed.
   - `1` → marker not found, fall back to verbal approval (see §3).
   - `2` → not in a tmux session, fall back to verbal approval (see §4).
   - `3` → usage error in the skill invocation, fix the call.

### 3. Handle Results

**Exit 0 (approved in vim):**

- Confirm to the user with one short sentence (e.g. "Editorial plan approved, proceeding to STEP_04.").
- Continue the workflow.

**Exit 1 (no marker found after popup closed):**

The human may have:

- (a) closed the popup without acting (didn't want to use vim), OR
- (b) left inline comments/edits but didn't flip the marker, OR
- (c) decided revisions are needed.

Do not assume which. Read the file to surface any edits the human made
(`git diff` against the previous version), then use `AskUserQuestion` with
options:

- "Approved — flip the marker for me"
- "Needs revision — I'll describe changes"
- "Retry the popup"

If the user selects **"Approved"**, use the `Edit` tool to flip the unchecked
line to checked:

```
old_string: - [ ] APPROVED - Ready for STEP_04 curation
new_string: - [x] APPROVED - Ready for STEP_04 curation
```

Then re-run the grep check to confirm:

```bash
grep -qE '^- \[x\] APPROVED - Ready for STEP_04 curation' workdesk/editorial_plan_YYYY_MM_DD.md
```

On a successful re-check, proceed past the gate.

If the user selects **"Needs revision"**, apply the requested edits and
**re-invoke the popup script** (do not flip the marker yet — the revised
content needs review).

If the user selects **"Retry the popup"**, re-run `scripts/review_in_popup.sh`.

### 4. Fallback: No tmux Session (Exit 2)

If `scripts/review_in_popup.sh` exits with `2`, the user is not running Claude
Code inside tmux. Fall back to chat-based approval:

1. Tell the user explicitly:

   > "I can't open a tmux popup (no tmux session detected). Please review the
   > file at `<path>` in your editor."

2. Use `AskUserQuestion` with options:
   - "I've reviewed and approved — flip the marker for me"
   - "Needs revision — I'll describe changes"

3. If the user selects **"Approved"**, use the `Edit` tool to flip the marker
   (same as §3 above), then re-run the grep check to confirm. On success,
   proceed past the gate.

### 5. Re-Review After Agent Edits

If the agent modifies the planning document after a successful gate (e.g.
STEP_07 appends Assembly Strategies to the same file approved in STEP_03b),
the prior approval **does not cover the new content**. Re-invoke this skill
with the new section's approval marker before proceeding.

Practical rule: every time the agent wants to advance past a documented review
gate, the most recent action on the planning file must be either an editor-close
captured by this skill or an explicit `AskUserQuestion`-mediated approval.

## What This Skill Does NOT Do

- ❌ Does NOT auto-approve based on diff inspection or "the file looks done".
- ❌ Does NOT flip the marker without an explicit `AskUserQuestion` confirmation
  that names the planning file. Verbal approval through chat alone (without the
  structured AskUserQuestion choice) is not sufficient.
- ❌ Does NOT batch multiple review gates into one popup — one file per call.
- ❌ Does NOT silently retry on failure; on exit 1, surface the failure to
  the user and ask through `AskUserQuestion` before retrying or flipping.

## Why a tmux Popup (Primary Path)

The popup gives, when used:

- **Synchronous blocking.** The agent's `Bash` call only returns when vim exits.
- **Full-file context.** The human sees the entire document in one place.
- **In-place editing.** Edits land in the same file the next step consumes.
- **Auditability.** The file's `mtime` and `git diff` make it obvious a human
  touched the document.

If the user prefers not to edit inside vim, the `AskUserQuestion`-mediated
verbal approval (§3 / §4) achieves the same audit trail: the `AskUserQuestion`
response is recorded in the transcript, and the subsequent `Edit` tool call
records the file change.

## Examples

**STEP_03b approval:**

```bash
bash scripts/review_in_popup.sh \
  workdesk/editorial_plan_2026_05_23.md \
  '^- \[x\] APPROVED - Ready for STEP_04 curation'
```

**STEP_07 assembly strategy approval (re-review of same file):**

```bash
bash scripts/review_in_popup.sh \
  workdesk/editorial_plan_2026_05_23.md \
  '^- \[x\] ASSEMBLY PLAN APPROVED - Ready for STEP_08'
```

## Relationship to Other Skills

- **Before** this skill: AI drafts the planning document with an unchecked
  approval line as the last status item.
- **After** this skill (approved): the calling step proceeds (curation, assembly, etc.).
- **After** this skill (revision requested): AI iterates on the draft and re-invokes.

You are strict about the gate's contract. You never flip the approval marker
without an explicit `AskUserQuestion` confirmation, and you never proceed past
a gate without verifying via `grep` that the checked marker is present on disk.
