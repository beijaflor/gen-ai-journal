---
name: human-review-gate
description: Blocking human review gate for AI-drafted planning documents. Opens the file in a tmux popup with vim, blocks until the editor closes, and verifies a human-authored approval marker. Use at every "AI drafts → human reviews → AI proceeds" handoff (STEP_03b editorial plan, STEP_07 assembly strategy, etc.).
allowed-tools: Bash, Read, AskUserQuestion
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

1. The file has been opened in vim by the human, and they have closed the editor.
2. The file contains a human-authored approval marker matching the agreed pattern.

The agent **MUST NOT** write the approval marker on the human's behalf. The human
authors the marker inside vim. Writing the approval line for the human defeats
the entire purpose of this gate.

## Default Approval Markers

Planning documents in this repo use checked-checkbox approval lines:

```
- [x] APPROVED - Ready for STEP_04 curation             (STEP_03b)
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08         (STEP_07)
```

The agent writes the line as `- [ ]` (unchecked). The human flips it to `- [x]`
inside vim during review. The grep pattern matches the checked form only.

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
   - `1` → marker not found, **do not proceed**.
   - `2` → not in a tmux session, fall back (see §4).
   - `3` → usage error in the skill invocation, fix the call.

### 3. Handle Results

**Exit 0 (approved):**

- Confirm to the user with one short sentence (e.g. "Editorial plan approved, proceeding to STEP_04.").
- Continue the workflow.

**Exit 1 (not approved):**

- Do **not** continue past the gate.
- Read the file to surface any inline comments or edits the human left.
- Use `AskUserQuestion` to ask what revisions are needed, or summarize the
  edits you noticed and propose next steps.
- After making revisions, **re-invoke this skill**.

**Exit 1 with no edits visible:**

- The human may have closed the popup without acting. Ask whether they want
  to retry the review or take a different path.

### 4. Fallback: No tmux Session (Exit 2)

If `scripts/review_in_popup.sh` exits with `2`, the user is not running Claude
Code inside tmux. The skill cannot pop a blocking editor. Fall back to:

1. Tell the user explicitly:

   > "I can't open a tmux popup (no tmux session detected). Please review the
   > file at `<path>` in your editor and add the line `- [x] APPROVED ...`
   > yourself when ready."

2. Use `AskUserQuestion` with options:
   - "I've reviewed and approved the file"
   - "Needs revision — I'll describe changes"

3. Only after the user selects "approved", re-run the grep check yourself:

   ```bash
   grep -qE '^- \[x\] APPROVED' workdesk/editorial_plan_YYYY_MM_DD.md
   ```

   If still not present, ask the user to add it. Do **not** write it for them.

### 5. Re-Review After Agent Edits

If the agent modifies the planning document after a successful gate (e.g.
STEP_07 appends Assembly Strategies to the same file approved in STEP_03b),
the prior approval **does not cover the new content**. Re-invoke this skill
with the new section's approval marker before proceeding.

Practical rule: every time the agent wants to advance past a documented review
gate, the most recent action on the planning file must be an editor-close
captured by this skill.

## What This Skill Does NOT Do

- ❌ Does NOT write the approval marker for the human.
- ❌ Does NOT auto-approve based on diff inspection or "the file looks done".
- ❌ Does NOT batch multiple review gates into one popup — one file per call.
- ❌ Does NOT silently retry on failure; on exit 1, surface the failure to
  the user and discuss before retrying.

## Why a tmux Popup

The popup gives:

- **Synchronous blocking.** The agent's `Bash` call only returns when vim exits.
  No way to "forget" the gate.
- **Full-file context.** The human sees the entire document, not chat snippets.
- **In-place editing.** Edits land in the same file the next step consumes.
- **Auditability.** The file's `mtime` and any subsequent `git diff` make it
  obvious that a human touched the document.

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
- **After** this skill (exit 0): the calling step proceeds (curation, assembly, etc.).
- **After** this skill (exit 1): AI iterates on the draft and re-invokes.

You are strict about the gate's contract. You never write the approval marker
yourself, and you never proceed past a gate without a successful exit 0 from
this skill (or an explicit chat-based fallback when tmux is unavailable).
