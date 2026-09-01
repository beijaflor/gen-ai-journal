# Step 4b: Mid-Cycle Theme Revision (#210)

A companion to STEP_04/STEP_05. Use it when — **after** the STEP_03b themes were
approved — the editor decides an article (or a small cluster) belongs in a
**different partition** than where curation first placed it: an annex/omitted
article should be **promoted to a new or existing main theme**, or a main
article should be **demoted to the annex**.

This is a mechanical cascade wrapped around one editorial decision. The decision
(is this theme worth adding? does this article belong in main?) stays human and
goes through the review gate. Everything after the decision is deterministic and
ends by **re-asserting the partition invariant** so the change cannot silently
break `main ∪ annex ∪ omitted = all sources`.

> **Worked example (2026-08-22):** mid-cycle, the editor grew Theme 9
> (“AI学習データの調達と汚染 / 希少本破壊・Anna's Archive”). It started from
> **068** and **110**; a corpus re-scan surfaced siblings **052** and **075**,
> which were promoted from the annex pool into the new/expanded main theme
> (068/110 → **+052/075**). All four end up in `curated_journal_sources.md`
> (main), none in annex-selected or omitted — the trace this spec must reproduce.

---

## When to trigger

- A reviewer flags that an annex or omitted article is actually a **main-journal
  story**, or that a main article is really a **B-side**.
- A new cross-cutting **theme** emerges mid-cycle that the STEP_03b plan missed.

Do **not** use this for within-partition reordering (that is ordinary STEP_04
curation) — only when an article crosses the main / annex / omitted boundary.

## The one rule that makes it safe

**Never move just the one article you spotted.** A single promoted article is
usually the visible tip of a cluster. Before re-gating, **re-scan the whole
corpus** (`workdesk/unified_summaries.md` — every summary, not only the curated
sets) for siblings of the same theme, so the theme is populated deliberately
rather than by whichever article happened to catch the eye.

## Promotion cascade (annex/omitted → main)

Run these steps **in this fixed order**. Steps (a)–(b) are the editorial add;
(c)–(e) keep the three sets disjoint and complete.

1. **Re-scan the corpus** for every sibling of the emerging/expanded theme (not
   just the 1–2 spotted). Assemble the candidate ID list.
2. **Re-gate (numbered round).** Present the revised theme + its candidate
   articles through the human review gate (`human-review-gate` skill) as a new,
   numbered revision round appended to `editorial_plan_YYYY_MM_DD.md`
   (e.g. `### Revision Round 2 — Theme 9 expansion`). Get explicit approval.
   Do not proceed on an unapproved round.
3. **Cascade, in order:**
   - **(a) Add the theme to the plan.** Record the (new or expanded) theme and
     its approved article list in `editorial_plan_YYYY_MM_DD.md`.
   - **(b) Add the articles to main.** Insert the promoted IDs under the theme
     in `workdesk/curated_journal_sources.md`.
   - **(c) Remove them from the annex.** Delete the same IDs from the annex pool
     `workdesk/curated_annex_journal_sources.md` **and** the selected annex
     `workdesk/curated_annex_selected.md` (and from any omitted list they were
     on). An ID must live in exactly one partition.
   - **(d) Regenerate the non-main set.**
     ```bash
     uv run scripts/list_urls.py workdesk/curated_journal_sources.md \
       | uv run scripts/remove_urls.py workdesk/sources.md workdesk/non_main_sources.md
     ```
     If you are already past STEP_05, also regenerate the non-main unified
     summaries (`unite_summaries.py … workdesk/unified_summaries_annex.md`) and,
     if past STEP_06, re-run `build_focused.py`.
   - **(e) Re-assert the partition.** This is the guardrail — it cannot be
     skipped:
     ```bash
     uv run python -m scripts.workflow.partition YYYY-MM-DD
     ```
     It reads `curated_journal_sources.md` (main), `curated_annex_selected.md`
     (annex), `omitted_sources.md` (omitted), and `sources.md` (all), and raises
     `PartitionError` naming the exact offending IDs if any set overlaps or the
     union is incomplete. Green here means the revision is consistent.

## Demotion cascade (main → annex) — mirror

Same shape, reversed:

1. Re-scan for siblings that should also drop to the annex.
2. Re-gate the demotion as a numbered round.
3. Cascade, in order:
   - **(a)** Note the demotion in `editorial_plan_YYYY_MM_DD.md` (mark the theme
     or the specific articles as moved to annex, with an `ex-main` annotation).
   - **(b)** Remove the IDs from `workdesk/curated_journal_sources.md`.
   - **(c)** Add them to `workdesk/curated_annex_selected.md` (and the annex pool
     if appropriate).
   - **(d)** Regenerate `non_main_sources.md` (+ unified/focused as in promotion
     step (d)).
   - **(e)** Re-assert the partition with `scripts.workflow.partition`.

## Guardrail (why step (e) is non-negotiable)

`scripts/workflow/partition.py` is the single source of the invariant. Every
reshaping of the curated sets — STEP_04, STEP_05, STEP_06, STEP_10, and any
revision round here — ends with `partition.verify`/`assert_partition`, so a
half-finished move (an article added to main but not removed from the annex, or
dropped from both) fails loudly and names the IDs instead of shipping a journal
where the counts silently don't add up.

## Definition of done

- The revision round is **approved** in `editorial_plan_YYYY_MM_DD.md`.
- The moved IDs live in **exactly one** partition file.
- `non_main_sources.md` (and unified/focused outputs, if regenerated) reflect the
  new main set.
- `uv run python -m scripts.workflow.partition YYYY-MM-DD` exits **0**.
