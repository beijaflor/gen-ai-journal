---
name: summarize-pdf
description: Generate a schema-valid Japanese summary for a PDF source URL by downloading, extracting text with pypdf, and routing through the URL-mode JSON pipeline. Invoked automatically by call-gemini.py when a URL is detected as PDF; can also be invoked directly for re-generation. Issue #141.
allowed-tools: Read, Edit, Bash, Grep, Glob
---

# Summarize PDF Source

This skill exists because the HTML-first pipeline (BeautifulSoup over the raw
bytes inside `call-gemini.py`) is fundamentally wrong for PDFs. When given a
PDF, BS4 produces garbled text — and if the garbled text clears the 500-char
blocked-content guard, Gemini will fabricate a plausible-looking summary from
the URL slug + domain. The summary passes schema validation, nothing downstream
notices, and the editor finds out only after the journal has been published
(see Issue #141 for the incident report on the Nork Research 2026-05-13 press
release, ID 199 in journal 2026-05-30).

The fix is to **make PDF handling a detection decision, not a recovery
decision**. The PDF path is taken *before* any extraction runs, based on a
Content-Type / URL-suffix probe. The PDF path is also **fail-closed**: if
extraction does not produce a meaningful amount of text, the script emits a
`BLOCKED-PDF:` stub rather than letting Gemini hallucinate. This guarantees
that small PDFs cannot silently produce URL-slug fabrications.

## When this skill runs

You will rarely need to invoke this skill explicitly. The plumbing is wired in:

- `scripts/call-gemini.py --url <URL>` probes the URL up front (HEAD +
  Content-Type, plus a `.pdf` suffix shortcut) and, when the URL is a PDF,
  delegates to the PDF pipeline automatically.
- `scripts/bulk_summarize.py` calls `call-gemini.py --url`, so batch runs
  pick up the PDF routing transparently. A PDF URL in `workdesk/sources.md`
  is handled without any human intervention.

Use this skill directly when:

- A PDF summary was produced by the legacy HTML path and needs to be
  re-generated against the correct extraction. Trigger phrases:
  - "re-summarize the PDF for [ID]"
  - "regenerate [ID] as PDF"
  - "this is a PDF, redo it"
- You want to force the PDF path for a URL whose Content-Type lies (e.g.
  `application/octet-stream` for a PDF-by-suffix).
- You need to cap pages for a very large PDF (front-matter mode for the
  Stanford HAI Index Report or similar 400-page reports).

## Contract

Inputs:

- **ID** (3-digit, zero-padded; e.g. `199`) — used in the output filename.
- **URL** — the PDF URL. Must resolve to a real PDF, not an HTML landing page.
- **pages** (optional, integer) — cap the number of leading pages read. Use
  for huge reports where front matter is the relevant section.

Outputs:

- `workdesk/summaries/${ID}_${domain}.json` — schema-valid v1.0 summary, with
  `content.url` pinned to the input URL.
- On extraction failure: a `BLOCKED-PDF:` stub at the same path (NOT a fake
  JSON file). The stub is what the human reviewer sees during STEP_02 review.

Side effects:

- Downloads the PDF to `.playwright-mcp/pdf_<random>.pdf` and cleans it up
  before returning. The directory is gitignored.
- Marks the URL as `[x]` in `workdesk/sources.md` only when the
  invocation comes through `bulk_summarize.py` and the result is a real
  summary or a blocked-stub (which carries actionable BLOCKED-PDF context).

## Steps the skill performs

1. **Probe** — `scripts/modules/pdf_router.is_pdf_url(url)` runs a HEAD with
   redirect-following and a `.pdf` URL-suffix check. The suffix wins when
   present, because some CDNs serve PDFs with
   `Content-Type: application/octet-stream` and the HEAD alone would miss
   them.

2. **Download** — `scripts/modules/pdf_extractor.download_pdf(url, tmp_path)`
   pulls the bytes via curl (same User-Agent as the HTML path; redirects
   followed; 120-second timeout default).

3. **Extract** — pypdf is invoked through `uv run --with pypdf` so the
   dependency stays optional. Per-page text is collected; `pages=N` caps the
   read at the first N pages.

4. **Verify (fail-closed)** — the extraction is rejected if total chars are
   below `PDF_MIN_TOTAL_CHARS` (currently 400) OR if no page produced at
   least `PDF_MIN_CHARS_PER_NONEMPTY_PAGE` (currently 50) characters. These
   thresholds reject scanned/image-only PDFs and corrupted downloads — the
   "never allow generation from filename, URL slug, or partial binary
   artifacts" guarantee from the issue's outside review.

5. **Truncate (if needed)** — the extracted text is capped at
   `PDF_MAX_CHARS` (currently 60,000) by selecting the leading N pages that
   fit in the budget. Truncation is recorded in metrics for editor audit.

6. **Build prompt** — `_build_url_mode_prompt_with_text` in
   `scripts/call-gemini.py` loads `prompts/summarize-json.prompt`,
   substitutes `{{url}}`, replaces the `{{fetch:"..."}}` directive with the
   extracted text, and resolves the remaining `{{file:...}}` includes
   (criteria, scoring, editorial persona).

7. **Generate** — the URL-mode JSON pipeline runs as usual:
   `call_gemini_structured(prompt, 'gemini-3-flash-preview')` with the
   native schema enforced.

8. **Post-process** — schema validation, HTML sanitization, URL pinning
   (`content.url` forced to the input URL), `originalTitle` invariant
   enforcement, then write to `workdesk/summaries/${ID}_${domain}.json`.

9. **Report** — stderr lines name the pipeline used (`PDF: routing ...`),
   the extraction metrics (`7 pages, used 7, 45749 chars from 1208863 bytes`),
   and the success/failure verdict. Capture these in the run notes.

## Direct CLI invocations

When you do need to call it explicitly, use `call-gemini.py` directly. The
detection runs by default; pass `--pages` to control truncation.

```bash
# Small PDF — full document. Most common case.
uv run scripts/call-gemini.py \
  --url "https://www.norkresearch.co.jp/pdf/2025DevTool_rel4.pdf" \
  --output "workdesk/summaries/199_norkresearch_co_jp.json"

# Huge report — front-matter only.
uv run scripts/call-gemini.py \
  --url "https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf" \
  --pages 25 \
  --output "workdesk/summaries/073_hai_stanford_edu.json"

# Force the HTML path even though it's a PDF URL (debugging only).
uv run scripts/call-gemini.py \
  --url "https://example.com/file.pdf" \
  --no-pdf-routing \
  --output /tmp/debug.json
```

## Escape hatch: --content for externally extracted text

When the standard pipeline cannot reach a PDF (e.g. requires auth, served via
a Playwright-rendered page), extract the text out of band and feed it through
the same JSON pipeline via the new `--content` flag (Issue #141 follow-up).
This replaces the older "build a `--file` prompt by hand" workaround
documented in `summarize-source` Step 5.

```bash
# 1. Extract text however you can (Playwright, manual OCR, etc.) into a temp file.
cat > /tmp/199_text.txt <<'EOF'
[the article body]
EOF

# 2. Run the URL-mode pipeline against the supplied text.
#    --url is required (it gets pinned into content.url).
uv run scripts/call-gemini.py \
  --url "https://www.norkresearch.co.jp/pdf/2025DevTool_rel4.pdf" \
  --content /tmp/199_text.txt \
  --output workdesk/summaries/199_norkresearch_co_jp.json
```

The `--content` path uses the exact same prompt template, schema enforcement,
URL pinning, and `originalTitle` invariant checks as the URL path. Use it
whenever you have the body text but cannot trust (or use) the automatic fetch.

## Blocked-PDF stubs

When the extraction fails the quality gate (or the download fails), the skill
writes a stub that begins with `BLOCKED-PDF:` to the output path. This is the
same pattern as the HTML `BLOCKED:` stub from Issue #121 — the file is
deliberately not schema-valid so it cannot be promoted into a published
journal, and the marker is easy to grep for during STEP_02 review.

Recovery options for a blocked PDF:

- The PDF may be a scanned image. Use an OCR pipeline (e.g.
  `ocrmypdf input.pdf out.pdf`) and feed the OCRed text through `--content`.
- The PDF may be auth-walled. Fetch it via an authenticated session and use
  `--content`.
- The PDF may be huge and the front matter happens to be empty (table of
  contents only). Try `--pages 50` or similar to advance past the front
  matter.

## Quality / regression guard

If you ever see a PDF summary whose `summaryBody` is generic ("Java/PHP/Python,
low-code, generative AI for coding") or whose `title` matches a translation of
the URL slug, treat that as a regression in the routing layer:

1. Re-run extraction directly and verify it produces ≥ 400 chars of real text
   (`python3 -c "from modules.pdf_extractor import extract_pdf_from_url; ..."`).
2. Confirm `is_pdf_url(URL)` returns True (suffix or HEAD).
3. If extraction is healthy and routing returns True but the LLM still
   hallucinates, the prompt assembly likely lost the article text — inspect
   `_build_url_mode_prompt_with_text` and the `# Article Content` marker.

## Project standards

- All summaries — including PDF-sourced ones — must be in Japanese (see
  EDITOR_PERSONALITY.md).
- All summaries must pass `scripts/validate_summary.py` before being written
  to `workdesk/summaries/` (the URL-mode pipeline enforces this inline).
- Never mark a URL as `[x]` in `sources.md` until validation passes OR a
  BLOCKED-PDF stub has been written. (The blocked stub IS a valid outcome
  — it surfaces the URL for human review rather than hiding the failure.)

## File locations

- Router: `scripts/modules/pdf_router.py`
- Extractor: `scripts/modules/pdf_extractor.py`
- Caller: `scripts/call-gemini.py` (the `--url` branch's PDF block)
- Prompt template: `prompts/summarize-json.prompt`
- Output dir: `workdesk/summaries/${ID}_${domain}.json`

## Relationship to other skills

- **Triggered by `summarize-source`**: when batch processing hits a PDF URL,
  it ends up in this pipeline via `call-gemini.py`'s automatic routing. No
  separate invocation needed.
- **Falls back to `summarize-source` Step 6 (Playwright)**: when a PDF is
  blocked AND the URL is actually an HTML page hiding behind a `.pdf` URL
  (rare but possible), the operator can disable detection with
  `--no-pdf-routing` and use the existing recovery chain.
