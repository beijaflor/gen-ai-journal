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

---

## Batch 2 (2026-11-23) — "add urls and summarize" (IDs 199–275; 77 added)

Of 77 new URLs, 5 first-pass failures were triaged; 2 needed a human paywall decision. Decisions captured via AskUserQuestion on 2026-11-23 and applied.

- [x] BATCH 2 APPROVED - paywall decisions applied (224 & 238 both dropped)

### B2. Unfetchable — fail-closed BLOCKED stub (hard paywall)
_No usable content; redundant with already-summarized sources. Decision: drop._

- [x] **224** — https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/  → decision: **drop** (HTTP 401 CloudFront hard paywall; Anthropic Nasdaq-debut story already covered by #235 NBC + #232 Guardian; line + stub removed, ID gap left)
- [x] **238** — https://www.economist.com/science-and-technology/2026/11/20/ai-may-have-solved-the-most-important-problem-in-mathematics  → decision: **drop** (HTTP 403 + Cloudflare challenge hard paywall; same math-breakthrough covered by #272 alpo.ge (primary Riemann/GRH-proof report, Lean-formalized) + #239 borretti.me (essay on it); HN thread thin [7 comments]; line + stub removed, ID gap left)

### Other batch-2 recoveries (no human paywall decision needed — recorded for audit)
- **236** ankitg.me (vibecoding inference chip) — transient curl/Gemini timeout on first pass → standard `call-gemini --url` retry succeeded (page HTTP 200), kept.
- **213** oreilly.com (who-builds-the-next-model) + **251** zenn.dev (webterm-ai-era-testing) — format-lint (escaped-newline) → newline-only reformat, facts preserved, re-lint + validate GREEN, kept.
- No HN-swaps, no browser-recoveries, no NEW gated-domain links this batch. Section C (142/143/167) carryover unchanged and still approved.

### Unrelated removal (not a paywall decision)
- **191** developers.googleblog.com (ABFS for massive Git repos) — dropped per explicit user instruction "drop #191"; line + summary removed, ID gap left.
