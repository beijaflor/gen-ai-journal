# Paywalled-source review (STEP_02 gate)

5 source(s) needed a human decision. Decisions captured via AskUserQuestion on 2026-11-20 and applied.

- [x] APPROVED - paywall decisions applied (019 & 155 dropped; 142, 143, 167 kept as-is)

## A. Paywalled → summarized from a Hacker News thread (NOT the article)
_The summary describes an HN discussion, not the source article._

- (none — no HN-proxy swaps were used this cycle)

## B. Unfetchable — fail-closed BLOCKED stub / dead link
_No usable content and no proxy. Decision: drop, or supply a corrected URL / full text._

- [x] **019** — https://www.nytimes.com/2026/11/15/business/anthropic-ipo-filing-prospectus.html  → decision: **drop** (hard paywall / DataDome; removed from sources.md + stub deleted, ID gap left)
- [x] **155** — https://www.nytimes.com/2026/11/06/science/ai-exponential-time-hypothesis.html  → decision: **drop** (hard paywall / DataDome; removed from sources.md + stub deleted, ID gap left)

## C. Paywalled-domain link — real summary, but the reader link is gated
_Summary content is real (metered first view). Decision: keep as-is._

- [x] **142** — [uxdesign.cc] https://uxdesign.cc/if-ai-works-from-anywhere-why-are-we-commuting-to-watch-it-f903012aaa86  → decision: **keep as-is**
- [x] **143** — [medium.com] https://medium.com/airbnb-engineering/de-identifying-text-at-scale-how-airbnb-protects-personal-data-in-ai-training-32f3ff8ff7d0  → decision: **keep as-is**
- [x] **167** — [medium.com] https://medium.com/@smoking2man/when-ai-knows-more-than-it-can-offer-how-training-turns-an-intelligent-assistant-into-a-generator-7e700f05163e  → decision: **keep as-is**

## D. Browser-recovered — blocked to the automated fetcher, rendered in a real browser
_These PUBLIC pages (no paywall) returned 429/403/567 to the automated fetcher. Recovered by rendering the live page in a real browser (Playwright) and summarizing the actual rendered article text. No CAPTCHA/challenge was solved (navigate + read only); no payment wall was circumvented. Summaries verified against real content + both QA gates. Decide: keep / drop._

- [x] **152** — https://solana.com/news/the-token-supercycle-oped  (Solana Foundation op-ed by Lily Liu; ~9.2k chars rendered)  → decision: **keep as-is**
- [x] **170** — https://www.businesswire.com/news/home/20261118974464/en/Anthropic-is-Not-a-Safe-AI-Company---Broad-Coalition-of-Scientists-Legal-Scholars-and-Tech-Leaders-Challenge-Anthropics-Safety-Branding-Ahead-of-IPO  (coalition press release; ~7.2k chars)  → decision: **keep as-is**
- [x] **160** — https://hy.tencent.ai/research/hy4-flash  (Tencent Hy4 flash model announcement; ~8.7k chars)  → decision: **keep as-is**

- [x] SECTION D REVIEWED - browser-recovered sources confirmed (all kept)
