# Paywalled-source review (STEP_02 gate)

All flagged sources reviewed. Mark a decision inline: `keep` / `drop` / `full-text` (you supply the article text) / `annotate` (note the paywall for readers).

- [x] REVIEWED — decisions applied 2026-11-27 (batch 3).
  - **160 Economist op-ed** ("Nvidia was right to bring back Jensen Huang," Sarah Guo): hard-blocked (403 to curl AND Playwright; anti-bot "Enable JavaScript and cookies" interstitial; only a BLOCKED stub existed). Per user (chose "HN-thread proxy"): **replaced with the Hacker News discussion** `news.ycombinator.com/item?id=50659532` (40 pts / 37 comments). Economist stub deleted; sources.md #160 URL re-pinned to the HN thread; summary describes the discussion, not Guo's argument. ID 160 retained.
- [x] REVIEWED — decisions applied 2026-11-27 (batch 2).
  - **Anthropic-IPO cluster (orig. 075 Bloomberg / 076 MSN / 077 Reuters):** all three unfetchable (075 = Bloomberg robot-check block-page; 076 = MSN "Continue reading" teaser; 077 = Reuters anti-bot). Per user ("find another story without block"): dropped 076 & 077, and **replaced 075 with a fetchable source** — `financefeeds.com/anthropic-stock-breaks-below-83-ipo-price-as-debut-rally-fades/` (real, content-grounded summary). ID 075 retained; 076/077 are now ID gaps.
  - **065 & 118:** keep as-is (see inline below).

## A. Paywalled → summarized from a Hacker News thread (NOT the article)
_The summary describes an HN discussion, not the source article. Decide: keep the HN-proxy summary, drop the source, or supply full text to re-summarize._

- [x] **160** (batch 3) — orig. https://www.economist.com/by-invitation/2026/11/25/nvidia-was-right-to-bring-back-jensen-huang-writes-sarah-guo → **HN-proxy** https://news.ycombinator.com/item?id=50659532  → decision: **keep HN-proxy** (user-chosen; Economist hard-blocked 403 curl+Playwright; summary describes the discussion, not Guo's op-ed)

## B. Unfetchable — fail-closed BLOCKED stub / dead link
_No usable content and no proxy. Decide: drop, or supply a corrected URL / full text._

- (none)

## C. Paywalled-domain link — real summary, but the reader link is gated
_Summary content is real (metered first view). Decide: keep as-is, annotate the paywall for readers, or drop. Items marked ⚠ may actually be block-page summaries — verify the body._

- [x] **065** — [uxdesign.cc] https://uxdesign.cc/prototypes-have-always-been-the-most-effective-specification-10162107b2ee  → decision: **keep as-is** (real content-grounded summary; confirmed batch 1 & re-confirmed batch 2)
- [x] **118** — [www.nature.com] https://www.nature.com/articles/s41562-026-02566-6  → decision: **keep as-is** (real summary — 487-consultant ChatGPT RCT; verified grounded)

