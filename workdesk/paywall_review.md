# Paywalled-source review (STEP_02 gate)

2 source(s) need a human decision. For each, mark a decision inline: `keep` / `drop` / `full-text` (you supply the article text) / `annotate` (note the paywall for readers).

## A. Paywalled → summarized from a Hacker News thread (NOT the article)
_The summary describes an HN discussion, not the source article. Decide: keep the HN-proxy summary, drop the source, or supply full text to re-summarize._

- [x] **049** — https://www.nytimes.com/2026/09/26/business/dealbook/ai-law-discount-billable-hour.html
      proxy: https://news.ycombinator.com/item?id=49872522  → decision: keep (accept HN proxy; approved via human-review-gate, carried from batch 1)

## B. Unfetchable — fail-closed BLOCKED stub / dead link
_No usable content and no proxy. Decide: drop, or supply a corrected URL / full text._

- (none)

## C. Paywalled-domain link — real summary, but the reader link is gated
_Summary content is real (metered first view). Decide: keep as-is, annotate the paywall for readers, or drop. Items marked ⚠ may actually be block-page summaries — verify the body._

- [x] **075** — [www.reuters.com] https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/  → decision: keep (real full-text recovered via Playwright; metered link; approved via human-review-gate 2026-10-03)

