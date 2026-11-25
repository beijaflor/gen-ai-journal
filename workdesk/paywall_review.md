# Paywalled-source review (STEP_02 gate)

2 source(s) need a human decision. For each, mark a decision inline: `keep` / `drop` / `full-text` (you supply the article text) / `annotate` (note the paywall for readers).

- [x] REVIEWED — decisions applied 2026-11-25 (see inline `decision:` lines below).

## A. Paywalled → summarized from a Hacker News thread (NOT the article)
_The summary describes an HN discussion, not the source article. Decide: keep the HN-proxy summary, drop the source, or supply full text to re-summarize._

- (none)

## B. Unfetchable — fail-closed BLOCKED stub / dead link
_No usable content and no proxy. Decide: drop, or supply a corrected URL / full text._

- [x] **003** — https://www.youtube.com/watch?v=H43e72-2aAs  → decision: **full-text** — transcript fetched (youtube-transcript-api, 59k chars) and re-summarized via `call-gemini --content`. Now a real, content-grounded summary; checked.

## C. Paywalled-domain link — real summary, but the reader link is gated
_Summary content is real (metered first view). Decide: keep as-is, annotate the paywall for readers, or drop. Items marked ⚠ may actually be block-page summaries — verify the body._

- [x] **065** — [uxdesign.cc] https://uxdesign.cc/prototypes-have-always-been-the-most-effective-specification-10162107b2ee  → decision: **keep as-is** — real content-grounded summary from the metered first view; accepted.

