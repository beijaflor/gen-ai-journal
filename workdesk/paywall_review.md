# Paywalled-source review (STEP_02 gate)

2 source(s) need a human decision. For each, mark a decision inline: `keep` / `drop` / `full-text` (you supply the article text) / `annotate` (note the paywall for readers).

- [x] REVIEWED — decisions applied 2026-11-27 (batch 2).
  - **Anthropic-IPO cluster (orig. 075 Bloomberg / 076 MSN / 077 Reuters):** all three unfetchable (075 = Bloomberg robot-check block-page; 076 = MSN "Continue reading" teaser; 077 = Reuters anti-bot). Per user ("find another story without block"): dropped 076 & 077, and **replaced 075 with a fetchable source** — `financefeeds.com/anthropic-stock-breaks-below-83-ipo-price-as-debut-rally-fades/` (real, content-grounded summary). ID 075 retained; 076/077 are now ID gaps.
  - **065 & 118:** keep as-is (see inline below).

## A. Paywalled → summarized from a Hacker News thread (NOT the article)
_The summary describes an HN discussion, not the source article. Decide: keep the HN-proxy summary, drop the source, or supply full text to re-summarize._

- (none)

## B. Unfetchable — fail-closed BLOCKED stub / dead link
_No usable content and no proxy. Decide: drop, or supply a corrected URL / full text._

- (none)

## C. Paywalled-domain link — real summary, but the reader link is gated
_Summary content is real (metered first view). Decide: keep as-is, annotate the paywall for readers, or drop. Items marked ⚠ may actually be block-page summaries — verify the body._

- [x] **065** — [uxdesign.cc] https://uxdesign.cc/prototypes-have-always-been-the-most-effective-specification-10162107b2ee  → decision: **keep as-is** (real content-grounded summary; confirmed batch 1 & re-confirmed batch 2)
- [x] **118** — [www.nature.com] https://www.nature.com/articles/s41562-026-02566-6  → decision: **keep as-is** (real summary — 487-consultant ChatGPT RCT; verified grounded)

