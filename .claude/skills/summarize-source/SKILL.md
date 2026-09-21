---
name: summarize-source
description: Generate summaries for unchecked sources in workdesk/sources.md. Supports single URL, batch processing, and re-generation of existing summaries via a structured fallback chain. Use after adding URLs with add-url skill.
allowed-tools: Read, Edit, Bash, Grep, Glob
---

# Summarize Source URLs

This skill generates Japanese summaries for unchecked URLs in `workdesk/sources.md`. It can process a single URL by ID, batch-process all unchecked URLs at once, or **re-generate an existing summary** via a structured fallback chain when an earlier attempt produced poor output.

## When to Use This Skill

Use this skill when:
- User says "summarize the sources" or "generate summaries"
- After adding URLs with `add-url` skill
- User wants to process unchecked URLs in sources.md
- Need to generate summary for a specific ID
- **Re-generation triggers** (fallback chain in [Re-generation Workflow](#re-generation-workflow)):
  - "re-generate summary [ID]"
  - "re-summarize [ID]"
  - "regenerate [ID]"
  - "redo summary for [ID]"
  - "fix summary [ID]" (when an existing summary is wrong/low quality)

## Workflow Options

**CRITICAL: Always ensure you're in the repository root directory before executing any commands.**

```bash
cd /Users/shootani/Dropbox/github/gen-ai-journal
```

### Option 1: Batch Process All Unchecked URLs

This is the most common workflow for processing multiple unchecked sources. **All summaries are generated as structured JSON with native Gemini schema enforcement.**

```bash
uv run scripts/bulk_summarize.py
```

**What it does**:
1. Scans `workdesk/sources.md` for unchecked entries `- [ ] XXX. URL`
2. For each unchecked URL:
   - Generates **structured JSON summary** using Gemini AI with native schema enforcement
   - Validates against JSON v1.0 schema (scores, topics, metadata)
   - Saves to `workdesk/summaries/XXX_domain.json`
   - Marks as checked `- [x]` in sources.md
3. Uses context caching for efficiency (automatic)
4. Provides progress updates and final summary

**When to use**: Processing 2+ unchecked URLs at once

### Option 2: Single URL by ID

For processing a specific URL when you need more control.

**Steps**:

1. **Find the URL in sources.md**:
   ```bash
   grep "- \[ \] 089\." workdesk/sources.md
   ```

2. **Extract the URL** from the output

3. **Generate summary**:
   ```bash
   uv run scripts/call-gemini.py --url "URL_HERE" --output workdesk/summaries/089_domain_name.json
   ```

4. **Validation**:
   - Schema validation happens automatically with native Gemini schema enforcement
   - Script exits with error if validation fails
   - Check stderr for validation error details

5. **Mark as checked** in sources.md:
   - Use Edit tool to change `- [ ] 089.` to `- [x] 089.`

**When to use**:
- Processing a single specific URL
- Retrying a failed summary
- Testing summary generation

### Option 3: Batch Process Specific Range

For processing a subset of unchecked URLs.

```bash
# First, manually mark the URLs you DON'T want to process as checked temporarily
# Then run bulk_summarize.py
# After processing, uncheck the temporarily checked ones if needed
```

**Note**: This is more complex and usually not needed. Prefer Option 1 or Option 2.

## Re-generation Workflow

Use this workflow when an existing summary is **already on disk** but is wrong, hallucinated, or low quality, and the user asks to regenerate it. Trigger phrases:

- "re-generate summary [ID]"
- "re-summarize [ID]"
- "regenerate [ID]"
- "redo summary for [ID]" / "fix summary [ID]"

Re-generation **must follow the fallback chain below in order**. Do not skip steps. Each step has a clear failure signal that escalates to the next step. After success, **report which step succeeded** so the editor can audit later (e.g. `Regeneration succeeded at Step 4 (curl-fed retry)`).

### Step 1 — Diagnose existing summary

Read the existing JSON to understand the failure mode before doing anything else.

```bash
# Workdesk (in-progress) summaries:
ls workdesk/summaries/${ID}_*.json 2>/dev/null

# Or, if already archived to a published journal:
ls journals/*/summaries/${ID}_*.json 2>/dev/null
```

Read the file with the Read tool, then classify the likely root cause:

- **Title looks invented from the domain name** (e.g. `title: "Qiitaの記事"` for a Qiita URL) → fetch likely failed, page returned an error or login wall
- **Summary describes the company/product, not the article** (e.g. summary of WSJ.com instead of the WSJ article) → paywall or bot block returned a generic landing page
- **`oneSentenceSummary` and `summaryBody` are vague or about a 404 page** → broken URL or redirect to home
- **Schema-valid but contradicts the URL slug** → wrong page fetched (redirect, A/B test, geo-block)
- **Empty or truncated `summaryBody`** → upstream timeout

Note the diagnosis in your reasoning before proceeding.

### Step 2 — HTTP probe with curl

Check the live HTTP status and redirect chain:

```bash
curl -sIL --max-time 10 \
  -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  "$URL"
```

Interpret:

- **200 OK with no auth/paywall hints** → page is healthy, jump to **Step 4** (standard retry)
- **301/302 chain** → note the final URL; if it differs materially from the input (e.g. redirected to a login page), treat as paywall (**Step 3**)
- **401 / 403** → likely paywall or bot block → **Step 3**
- **404 / 410** → page is dead; report to user, do not regenerate
- **5xx** → transient server issue; wait briefly and retry **Step 2** once before moving on
- **200 OK and `Content-Type: application/pdf`** (or URL ends in `.pdf`) → re-run
  `call-gemini.py --url "$URL"` and let the PDF router (Issue #141) take over.
  No manual fetch needed; the script will download, extract via pypdf,
  fail-closed if extraction is poor, and produce a schema-valid JSON.
  For huge reports, add `--pages 25` to extract only front matter.
- **200 OK but `Content-Type` is non-HTML and non-PDF** (e.g. video) → document
  and stop; this skill cannot summarize that content

If the headers look healthy but you saw paywall language in the existing summary (Step 1), also fetch a small body sample to LLM-judge whether the page is gated:

```bash
curl -sL --max-time 10 -A '...' "$URL" | head -c 4000
```

Look for telltale phrases: "Subscribe to continue", "Sign in to read", "members only", a near-empty `<article>` tag, or a paywall component name in HTML class attributes.

### Step 3 — Paywall path: swap to Hacker News thread

If Step 2 indicates a paywall (4xx, login redirect, or LLM-judged gated content), search Hacker News via the Algolia API and re-summarize the thread instead.

```bash
# URL-encode the input URL, then query Algolia
ENCODED=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1], safe=''))" "$URL")
curl -s --max-time 10 "https://hn.algolia.com/api/v1/search?query=${ENCODED}" \
  | python3 -c "import sys, json; d = json.load(sys.stdin); \
      hits = [h for h in d.get('hits', []) if h.get('url') and h.get('points', 0) >= 5]; \
      print(json.dumps([{'id': h['objectID'], 'title': h['title'], 'url': h['url'], 'points': h.get('points', 0)} for h in hits[:5]], indent=2))"
```

Pick the hit whose `url` matches the input most closely (exact match preferred; otherwise highest-point hit pointing at the same article slug). Convert its `objectID` to an HN thread URL:

```
https://news.ycombinator.com/item?id=<objectID>
```

Then run standard generation against the HN thread URL:

```bash
uv run scripts/call-gemini.py \
  --url "https://news.ycombinator.com/item?id=<objectID>" \
  --output "workdesk/summaries/${ID}_news_ycombinator_com.json"
```

**Mandatory**: after success, document the URL→HN swap in your report so it's auditable. The `content.url` field in the resulting JSON will (correctly) point to the HN thread, not the original paywalled article. Mention both in the user-facing summary report:

```
Step 3 succeeded. Original URL: <paywalled URL>
Replaced with HN thread: https://news.ycombinator.com/item?id=<id>
Output: workdesk/summaries/${ID}_news_ycombinator_com.json
```

If no HN hit exists, skip to **Step 6** (Playwright).

### Step 4 — Standard retry with call-gemini

If the HTTP probe in Step 2 looks healthy and the page isn't paywalled, the most likely cause is a transient Gemini hiccup. Re-run the standard generation:

```bash
# Determine domain slug for filename (same convention as initial generation)
DOMAIN=$(python3 -c "from urllib.parse import urlparse; \
  print(urlparse('$URL').netloc.replace('.', '_').replace('-', '_'))")

uv run scripts/call-gemini.py \
  --url "$URL" \
  --output "workdesk/summaries/${ID}_${DOMAIN}.json"
```

Then validate:

```bash
uv run scripts/validate_summaries.py "workdesk/summaries/${ID}_${DOMAIN}.json"
```

Read the regenerated JSON and sanity-check that `title`, `oneSentenceSummary`, and `summaryBody` actually describe the article (not the diagnosis from Step 1). If it still looks bad, escalate to **Step 5**.

### Step 5 — Curl-fed retry

If `call-gemini.py --url` keeps producing a bad summary even though the page is healthy, the in-script fetch may be hitting a path that bot-walls Gemini's fetcher (e.g. JS-heavy SPA where the in-script extractor returns navigation chrome only). Fetch the raw HTML manually with curl, extract readable text, and feed it to Gemini through the `--file` path with the JSON prompt template.

```bash
# 1. Fetch raw HTML and extract readable text (mirrors call-gemini's own approach)
RAW=$(mktemp)
python3 - "$URL" > "$RAW" <<'PY'
import sys, subprocess
from bs4 import BeautifulSoup
url = sys.argv[1]
html = subprocess.check_output([
    'curl', '-sL', '--max-time', '30',
    '-A', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    '-H', 'Accept-Language: ja,en;q=0.9',
    url,
])
soup = BeautifulSoup(html, 'html.parser')
for tag in soup(['script', 'style', 'noscript']):
    tag.decompose()
text = ' '.join(chunk.strip() for line in soup.get_text().splitlines() for chunk in line.split('  ') if chunk.strip())
print(text)
PY
```

Then assemble a prompt by inlining the extracted text into `prompts/summarize-json.prompt`. The cleanest route is to call the script with `--file` after substituting `{{url}}` and replacing the auto-fetched template marker with the curled content. **Today there is no `--content` / stdin-content flag on `call-gemini.py`** — see the gap note below. As a workaround, write a temporary prompt file and pass it via `--file`:

```bash
TMP=$(mktemp --suffix=.prompt)
python3 - "$URL" "$RAW" > "$TMP" <<'PY'
import sys, pathlib
url, raw_path = sys.argv[1], sys.argv[2]
template = pathlib.Path('prompts/summarize-json.prompt').read_text()
content = pathlib.Path(raw_path).read_text()
# Replace {{url}} placeholder, then replace the template's fetch directive
# with the literal content. The template uses a "# Article Content" marker.
prompt = template.replace('{{url}}', url)
# Strip any @fetch directive and append content under the marker
import re
prompt = re.sub(r'@fetch\([^)]*\)', '', prompt)
if '# Article Content' in prompt:
    head, _ = prompt.split('# Article Content', 1)
    prompt = head + '# Article Content\n\n' + content
else:
    prompt = prompt + '\n\n# Article Content\n\n' + content
print(prompt)
PY

uv run scripts/call-gemini.py \
  --file "$TMP" \
  --output "workdesk/summaries/${ID}_${DOMAIN}.json" \
  --model gemini-3-flash-preview
```

**Preferred path (Issue #141)**: `call-gemini.py` now exposes a `--content
<path>` flag that reuses the URL-mode JSON pipeline (schema enforcement, URL
pinning, `originalTitle` invariant) with externally supplied article text.
When you have the article body and just need the structured summary,
**prefer this over the hand-built `--file` prompt above**:

```bash
# 1. Get the article text into a temp file (curl + BS4, Playwright snapshot,
#    OCR, etc.). $RAW from the snippet above works as-is.
# 2. Run the URL-mode pipeline against the supplied text. --url is required
#    (it is pinned into content.url).
uv run scripts/call-gemini.py \
  --url "$URL" \
  --content "$RAW" \
  --output "workdesk/summaries/${ID}_${DOMAIN}.json"
```

The hand-built `--file` workflow above is kept for completeness but should
only be needed if `--content` cannot represent the request (rare).

### Step 6 — Playwright last resort

If curl-fed retry still produces a bad summary (likely a JS-rendered SPA, e.g. some Notion/Twitter/X pages, dynamic dashboards), fall back to Playwright MCP to capture the rendered DOM:

1. `mcp__playwright__browser_navigate` to the URL
2. `mcp__playwright__browser_snapshot` (returns an accessibility tree of the rendered page) — or `mcp__playwright__browser_evaluate` with `() => document.body.innerText` to get rendered text directly
3. Save the extracted text to a temp file, then run the same `--file` flow as **Step 5** with the Playwright-extracted content

Always close the browser tab after extraction (`mcp__playwright__browser_close`) to free resources.

If Playwright also fails, stop and report:

```
Regeneration failed at all 6 steps for ID ${ID}.
Last successful step: <none>
URL: <url>
Diagnosis: <step 1 finding>
Recommendation: manual review or omit from journal
```

### Re-generation reporting requirements

Every regeneration run must end with a structured report so the editor can audit:

```
ID: ${ID}
URL: ${URL}
Diagnosis (Step 1): <e.g. "title invented from domain; summaryBody describes wsj.com landing page">
HTTP probe (Step 2): <status code + redirect chain>
Resolved at: Step <N> (<step name>)
Output file: workdesk/summaries/${ID}_${DOMAIN}.json
URL swap (if Step 3): original → HN thread <url>
Notes: <anything unusual>
```

Do NOT mark the URL as `[x]` checked in `sources.md` until validation passes (`uv run scripts/validate_summaries.py <output>`).

## Progress Tracking

For batch operations:

1. Create TodoWrite entry before starting: "Batch summarize unchecked sources"
2. Let the script run (it provides its own progress output)
3. Monitor output for any failures
4. Mark todo as completed when script finishes
5. Report: "Generated X summaries, Y failed (if any)"

## Summary File Naming Convention

Summaries are saved to `workdesk/summaries/` with this pattern:

```
XXX_domain_name.json
```

Where:
- `XXX` = 3-digit ID (001, 002, 089, etc.)
- `domain_name` = simplified domain (example_com, github_com, etc.)
- Extension = always `.json` (structured JSON)

Examples:
- `089_example_com.json` (structured JSON with scores and topics)
- `090_github_com.json` (JSON format with v1.0 schema)
- `091_qiita_com.json` (all summaries use JSON format)

## What This Skill Does

- ✅ Generates structured JSON summaries for URLs using native Gemini schema
- ✅ Validates JSON against v1.0 schema (scores, topics, metadata)
- ✅ Generates Japanese summaries using Gemini AI
- ✅ Marks URLs as checked/processed after successful summary
- ✅ Handles batch processing efficiently with context caching
- ✅ Reports progress and errors
- ✅ Creates summary files in workdesk/summaries/ (.json format only)

## What This Skill Does NOT Do

- ❌ Does NOT add new URLs to sources.md (use `add-url` skill)
- ❌ Does NOT validate or check for duplicates (done by `add-url`)
- ❌ Does NOT modify the URL itself

## Key Responsibilities

1. **Summary Generation**: Call Gemini AI to generate high-quality Japanese summaries
2. **File Management**: Save summaries to correct location with proper naming
3. **Status Updates**: Mark URLs as checked after successful summary
4. **Error Handling**: Report failures, continue with remaining URLs
5. **Efficiency**: Use batch processing and context caching when possible

## Project Standards

- Summaries MUST be in Japanese (as per EDITOR_PERSONALITY.md)
- Use absolute paths when referencing files
- Summary filenames: lowercase, underscores, descriptive
- Always verify summary file was created before marking as checked
- Documentation in English, summaries in Japanese

## File Locations

- **Sources list**: `workdesk/sources.md`
- **Summaries**: `workdesk/summaries/XXX_filename.json`
- **JSON schema**: `schema/summary-v1-schema.json`
- **Batch script**: `scripts/bulk_summarize.py`
- **Single script**: `scripts/call-gemini.py`
- **Validation script**: `scripts/validate_summaries.py`
- **Prompt template**: `prompts/summarize-json.prompt`
- **Workflow docs**: `workflow/STEP_02_GENERATE_SUMMARIES.md`

## Validation contract

**Every summary, regardless of generation path, must pass `scripts/validate_summary.py` before being written to `workdesk/summaries/`.** This is a hard requirement: the gemini primary path enforces it inline, and any fallback path (direct HTTP fetch, Playwright-rendered fetch, or any other future path) must invoke the same validator before persisting JSON to disk.

**Why this exists**: validation rules used to live inline in `scripts/call-gemini.py`, which meant fallback paths bypassed schema/topic-count/required-field checks and let invalid summaries reach the workflow. Issue #113 consolidated all rules into `scripts/validate_summary.py` so every path goes through the same gate.

**How fallback paths must use it**:

1. Generate the summary JSON (whatever the source — direct fetch, Playwright, etc.).
2. Write the candidate JSON to a temporary path (NOT directly to `workdesk/summaries/`).
3. Run the validator:
   ```bash
   python scripts/validate_summary.py /tmp/candidate.json
   ```
   Exit code `0` = pass; non-zero = fail with reason on stderr.
4. **Only on pass**: move the candidate file into `workdesk/summaries/XXX_domain.json`.
5. **On fail**: do NOT write to `workdesk/summaries/`. Either retry, escalate to the next fallback path, or surface the validation error to the user. Never write a summary that failed validation.

**Programmatic use** (when scripting in Python rather than shelling out):

```python
from validate_summary import validate
result = validate(summary_dict)
if not result.ok:
    raise RuntimeError(f"Summary failed validation: {result.first_error}")
```

The validator API:
- `validate(summary: dict) -> ValidationResult` — primary entry point; `result.ok` is bool, `result.errors` lists every detected error, `result.first_error` returns the first one.
- `validate_first_error(summary: dict) -> (bool, str | None)` — backwards-compatible tuple form.
- CLI: `python scripts/validate_summary.py path/to/summary.json` — exit 0 / non-zero with stderr message.

The rules enforced (extracted from the original inline checks): required top-level/metadata/content fields, version `1.0`, dimension scores 0-5, composite scores 0-100, topics array length 1-5, and the title / oneSentenceSummary / summaryBody length bounds.

## Post-generation QA gates

After a batch (or single-URL) generation, run these two review gates before treating STEP_02 as complete. Unlike the schema validator above (a hard, mechanical gate), these are **review** gates: the first is a lint you fix, the second routes *editorial* decisions to a human.

### 1. Format lint (rendering)

`validate_summary.py` checks the JSON schema but NOT whether `summaryBody` renders cleanly on the detail page. Run the format linter and fix any flagged body (reformat mashed/escaped-newline bodies into real newlines — see its docstring for the three defects):

```bash
uv run scripts/check_summary_format.py workdesk/summaries
```

### 2. Paywall review gate — human decides (do NOT auto-resolve)

Paywall / anti-bot workarounds are **editorial, not mechanical**: a Step-3 Hacker News swap summarizes a *discussion thread*, not the article, and a paywalled-domain link walls the reader out. The automatic fallback chain must NOT decide these silently. After generation, list every paywalled / proxy-summarized source and route it through the **`human-review-gate`** skill so a human decides each one:

```bash
uv run scripts/list_paywalled_sources.py --out workdesk/paywall_review.md
```

The sheet groups sources into three buckets:
- **A. HN-proxied** — `content.url` is a Hacker News thread; the summary describes the discussion, not the article (Step-3 swaps).
- **B. Unfetchable** — fail-closed `BLOCKED:` stub or dead link (no content, no proxy).
- **C. Paywalled-domain link** — a real summary was produced but the reader-facing link is gated; `⚠` marks a body that may actually be a block-page summary (verify it).

For each source the human marks a decision: `keep` (accept the HN proxy / gated link as-is) · `drop` (remove the source + summary, leave an ID gap) · `full-text` (human supplies the real article text → re-summarize via Step 5 `--content`) · `annotate` (keep but note the paywall for readers). Then invoke the `human-review-gate` skill on `workdesk/paywall_review.md`: **AI drafts the list → human reviews & marks decisions → AI applies them.** Only after the gate is approved is STEP_02 done.

## JSON Validation

When using JSON format (default), summaries are automatically validated against the v1.0 schema:

**Validation checks**:
- ✓ Required fields present (title, url, scores, topics, etc.)
- ✓ Version = "1.0"
- ✓ Dimension scores in range 0-5 (signal, depth, uniqueness, practical, antiHype)
- ✓ Composite scores in range 0-100 (mainJournal, annexPotential, overall)
- ✓ Topics array has 1-5 elements
- ✓ String length constraints (title: 1-200, summaryBody: 100-1200, etc.)

**If validation fails**: Script exits with error message, URL remains unchecked, no file written.

## URL Validation

After JSON generation, `call-gemini.py` validates that the `content.url` field in the generated JSON **exactly matches** the input URL passed via `--url`. Gemini sometimes resolves redirects or hallucinates different URLs, which can indicate the wrong page was fetched and the summary content may be incorrect.

**Validation behavior**:
- ✓ After schema validation, `content.url` is compared against the input URL
- If mismatch detected: summarization is **automatically retried once** (warning printed to stderr)
- If retry also mismatches: script exits with error code 1 (URL mismatch persists after retry)
- Entry remains unchecked for manual intervention if retry fails

**If URL mismatch occurs**:
1. Check stderr for "Warning: URL mismatch, retrying summarization..."
2. If retry resolves it: continues normally (info logged)
3. If retry fails: "Error: URL mismatch after retry. Expected '...', got '...'"
4. Re-run generation manually or investigate if the URL has redirects/paywall

### Manual Validation

To validate existing JSON summaries:

```bash
# Validate all summaries in workdesk
uv run scripts/validate_summaries.py workdesk/summaries

# Validate specific file
uv run scripts/validate_summaries.py workdesk/summaries/001_example.json

# Verbose mode (show all files)
uv run scripts/validate_summaries.py workdesk/summaries --verbose

# Quiet mode (only summary)
uv run scripts/validate_summaries.py workdesk/summaries --quiet
```

**Use cases**:
- Verify summaries after batch generation
- Check integrity before committing
- Validate after manual edits
- CI/CD pipeline integration

## summaryBody format definition

**This is the single source-of-truth definition for how `summaryBody`
Markdown must be represented inside the JSON string.** Two other places
implement this exact spec and must be kept in sync with it:

- `prompts/summarize-json.prompt` — the "Markdown formatting rules"
  subsection under the `summaryBody` field instructions (item 7) tells the
  generating model to follow this spec.
- `scripts/check_summary_format.py` — the format linter (`lint_body`) that
  enforces this spec as a QA gate (see check 4 below).

If the spec ever needs to change, update this section first, then the
prompt and the linter to match.

`summaryBody` is GitHub-flavored Markdown, written in Japanese, stored as a
JSON string value:

- **Line breaks are real newline characters.** In the JSON text they appear
  as the ordinary `\n` escape JSON itself uses to represent a newline inside
  a string — **never** the literal two-character text `\n` (a backslash
  followed by the letter "n") sitting inside otherwise-unescaped prose. The
  body is never a single line when it contains any heading or list.
- **Blocks** (paragraphs, headings, lists) are separated by a **blank
  line** — a real double newline (`\n\n` once JSON-decoded).
- **Headings**: `##` or `###`, each **alone on its own line**, followed by a
  blank line before the body text that follows it. A heading is never glued
  to the text before it (`…です。## 見出し`) or the text after it
  (`## 見出し本文が続く。`).
- **Lists**: each item on its **own line**; a blank line precedes the list;
  bullets use `- `, numbered items use `1. `, `2. `, …; a bold label inside
  an item is `**ラベル**: 説明`.
- **Bold** (`**…**`) marks tool/product/technical names.
- No leading/trailing whitespace in the body; no literal `\n` anywhere.

### Correct example (JSON string value, decoded)

```markdown
### 検証の概要

**Claude Code** を使った大規模リファクタリングの実例を検証した記事。

- **対象**: 10万行規模のモノリポ
- **手法**: エージェントによる段階的な移行

既存のワークフローに組み込みたいチームは必読。
```

### Wrong — do not do these

1. **Literal `\n`** — the two characters backslash-n appear as visible text
   instead of a real newline: `"### 概要\n本文\n\n- 項目1"` where `\n` here
   is literal text, not an actual line break.
2. **Mashed single line** — a heading or list is present but the whole body
   has no real newline anywhere, OR a heading/multiple list items are
   crammed onto one physical line even though other lines elsewhere do have
   real breaks: `"### 概要 本文が続く 1. **項目**: 説明 2. **項目**: 説明"`.
3. **Glued heading** — a heading runs directly into the text immediately
   before or after it with no line break, merging the heading label with a
   sentence: `"## 記事の概要PC Watch編集部が高性能な生成AIモデルを検証した記事を紹介する。"`.

### Rendering contract (for the website repo)

This repo only produces the JSON; the **detail-page renderer lives in a
separate website repo** and cannot be changed from here. That renderer MUST
treat every real newline in `summaryBody` as Markdown block structure — a
blank line starts a new paragraph/heading/list block — and must NOT collapse
newlines or display them as literal text. Because a spec-compliant body
never contains a literal `\n`, the renderer should never need any special
handling for that escape sequence. If a published page shows a visible `\n`
or a heading merged into body text, the JSON itself violates this spec —
verify with `scripts/check_summary_format.py` and fix the source JSON;
don't work around it in the renderer.

## Post-generation QA checklist (4 checks)

`validate_summaries.py` only checks the **schema** (required fields, score
ranges, topic count, length bounds). A summary can be schema-valid and still be
wrong. After generating summaries — and again before STEP_03 curation — verify
these four things for each source. Any failure → re-generate (see
[Re-generation Workflow](#re-generation-workflow)) or omit the source.

### 1. Not a dead link (404)
The source URL must resolve (2xx/3xx). A 404/410 means the page is gone — omit or
replace it; never summarize a redirect-to-home. Note: **401/403 is usually a
paywall/anti-bot wall, not a dead link** (see check 3), and a host can 403 an
automated request yet load fine in a real browser — retry before declaring it dead.

```bash
uv run scripts/verify_urls.py workdesk/sources.md   # batch live health (reports broken vs blocked)
uv run scripts/check_link.py "<URL>"                # single URL
```

### 2. Title matches the original article
The summary's `title` (and `originalTitle` for English pieces) must describe the
**actual article**, not a guess from the URL/domain. Red flags: a title like
"Qiitaの記事" or the bare domain name, or `content.url` ≠ the input URL.
`call-gemini.py` already enforces `content.url == input URL` (auto-retries once);
for the *title*, cross-check against the page's real `<title>`:

```bash
curl -sL --max-time 10 -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' "<URL>" \
  | grep -oiE '<title>[^<]*' | head -1
python3 -c "import json;c=json.load(open('workdesk/summaries/<ID>_<dom>.json'))['content'];print('title:',c['title']);print('orig :',c.get('originalTitle'));print('url  :',c['url'])"
```

If the title doesn't correspond to the page, the fetch likely failed → re-generate.

### 3. Not blocked by a paywall / anti-bot wall
The summary must describe the article, not a "Subscribe to read" / login /
Cloudflare / "Enable JavaScript" interstitial. Red flags: a `BLOCKED-*` stub, a
summary that describes the company/product instead of the article, generic
landing-page content, or a 401/403.

```bash
uv run scripts/summary_review.py workdesk/summaries/ --only-suspicious   # flags thin/fabricated rows
grep -rlE "Subscribe to read|Enable JavaScript|Just a moment|Cloudflare|アクセスが|BLOCKED" workdesk/summaries/
```

Recover a genuinely gated page with the real browser (Playwright MCP: navigate →
`() => document.body.innerText`) fed back through
`call-gemini.py --url "<URL>" --content <captured.txt>`; if the body is truly
inaccessible (hard paywall), omit it. **Retry in a real browser before declaring
a page blocked** — cold-session 403s are often transient.

### 4. summaryBody is not mis-formatted
`summaryBody` must render cleanly on the detail page per the canonical
[summaryBody format definition](#summarybody-format-definition) above: **real
line breaks**, no literal `\n` escape sequences, no heading glued to
adjacent text, and no `1. **item**` lists or headings mashed onto one line.
Schema validation does **not** catch this. Run the format linter — the same
one used as this repo's QA gate — instead of scanning manually, and
reformat any hit into intro paragraph → bullet list (bold labels) → closing
paragraph with real newlines (preserving every fact):

```bash
uv run scripts/check_summary_format.py workdesk/summaries
```

(Run the same check against `journals/<date>/summaries/*.json` to audit an
already-archived cycle.)

## Error Handling

- If summary generation fails, report the error but continue with remaining URLs
- If network timeout occurs, retry once or skip and report
- If file write fails, report and continue
- Never mark a URL as checked if summary generation failed
- Always provide a final summary of successes and failures

## Examples

### Example 1: Batch Process All Unchecked

**User says**: "Generate summaries for all unchecked sources"

**Skill activates and**:
1. ✓ Runs `uv run scripts/bulk_summarize.py`
2. ✓ Script finds 15 unchecked URLs
3. ✓ Generates 15 structured summaries with native Gemini schema validation
4. ✓ All 15 summaries pass schema validation
5. ✓ Marks all 15 as checked
6. ✓ Reports: "Generated 15 summaries successfully"

### Example 2: Single URL

**User says**: "Generate summary for ID 089"

**Skill activates and**:
1. ✓ Finds URL in sources.md for ID 089
2. ✓ Runs call-gemini.py with URL
3. ✓ Validates structure against v1.0 schema
4. ✓ Saves summary to workdesk/summaries/089_example_com.json
5. ✓ Marks ID 089 as checked in sources.md
6. ✓ Reports: "Generated summary for ID 089"

### Example 3: After Using add-url Skill

**Workflow**:
1. User adds 5 URLs with `add-url` skill → IDs 089-093 (unchecked)
2. User says "now summarize them"
3. `summarize-source` skill activates
4. Runs bulk_summarize.py → generates 5 JSON summaries
5. All 5 summaries validated and saved as .json files
6. All 5 IDs now checked in sources.md

## Performance Notes

- **Context caching**: Automatically enabled in bulk_summarize.py for faster processing
- **Rate limits**: Gemini API has rate limits; bulk_summarize.py handles this
- **Timeout**: Default 120 seconds per URL; adjustable in scripts
- **Retries**: Scripts have built-in retry logic for transient failures

## Troubleshooting

**Issue**: Summary generation times out
**Solution**: Increase timeout in call-gemini.py or retry manually

**Issue**: Some summaries failed in batch
**Solution**: Re-run bulk_summarize.py (it will skip already-checked URLs)

**Issue**: Summary file created but not marked as checked
**Solution**: Manually mark as checked using Edit tool

**Issue**: JSON validation fails
**Solution**:
1. Check error message for specific validation failure
2. Common issues: score out of range, topics array wrong size, missing required field
3. Re-run generation - Gemini will try again with schema enforcement

**Issue**: Want to re-generate a summary
**Solution**: Use the [Re-generation Workflow](#re-generation-workflow) (triggers: "re-generate summary [ID]", "re-summarize [ID]", "regenerate [ID]"). It walks the 6-step fallback chain — diagnose, HTTP probe, paywall→HN swap, standard retry, curl-fed retry, Playwright last resort — and reports which step succeeded. Avoid the old "uncheck and re-run bulk" approach for known-bad summaries; it doesn't address paywall or fetch-failure root causes.

## Batch retry with Playwright

When `scripts/summary_review.py` flags suspicious rows, or when a human reviewer
identifies summaries that were clearly fabricated from a URL/domain (BS4
extraction failed on a JS-rendered or bot-blocked page), use the **batch retry
workflow** to fix multiple summaries at once.

**Trigger phrases the user might use**:

- "re-summarize 092 164 251"
- "fix summaries 164 and 192 with Playwright"
- "retry these IDs with the rendered page"

**Workflow per ID**:

For each ID provided, the skill performs these steps in sequence:

1. **Look up the URL** from the appropriate sources file:
   - Active week: `workdesk/sources.md`
   - Already-published journal: `journals/YYYY-MM-DD/sources/sources.md`
   ```bash
   grep -E "^- \[.\] 164\." workdesk/sources.md
   ```

2. **Fetch the rendered page with Playwright MCP**, since BS4 already failed.
   Two options, in order of preference:

   - **Playwright MCP (preferred)**: navigate to the URL via the
     `mcp__playwright__browser_navigate` tool, then capture the rendered text
     with `mcp__playwright__browser_evaluate` (e.g.
     `() => document.body.innerText`) or `browser_snapshot`. Save the
     extracted text to a temp file (e.g. `/tmp/164_rendered.txt`).

   - **CLI fallback**: re-run `call-gemini.py` with the
     `--auto-fallback-playwright` flag, which retries the fetch via the
     in-process Playwright integration when BS4 extraction is below the
     quality threshold. This is the simpler one-shot path:
     ```bash
     uv run scripts/call-gemini.py \
       --url "URL_FROM_SOURCES" \
       --auto-fallback-playwright \
       --output workdesk/summaries/164_domain.json
     ```

3. **Send the rendered content through `call-gemini.py`** (only needed when
   you used the MCP option in step 2 to capture text manually):
   ```bash
   # Replace the {{fetch:"..."}} block in the prompt with the captured text,
   # then pipe to call-gemini.py via --file or stdin.
   ```

4. **Replace the existing JSON file** in `workdesk/summaries/` (or the
   published `journals/YYYY-MM-DD/summaries/` directory) — the schema
   validation in `call-gemini.py` ensures the new file is well-formed before
   it overwrites the old one.

5. **Verify** with `scripts/summary_review.py` that the previously suspicious
   row is no longer flagged (or run `validate_summaries.py` to confirm
   schema compliance):
   ```bash
   uv run scripts/summary_review.py workdesk/summaries/ --only-suspicious
   ```

**Quality gate signals** (from Issue #108, Layer 1):

`call-gemini.py` now emits a stderr warning when BS4 extracts fewer than 200
characters from a page (the typical failure mode for JS-rendered articles).
When you see `WARN: extracted only N chars from <url>`, treat the resulting
summary as suspect even if schema validation passes.

**Review table** (from Issue #108, Layer 2):

After a bulk run, append `--review-table` to surface suspicious summaries:

```bash
uv run scripts/bulk_summarize.py --review-table
# Or stand-alone over an existing directory:
uv run scripts/summary_review.py journals/2026-04-18/summaries/ --only-suspicious
```

Use the flagged IDs as input to the batch retry workflow above.

## Relationship to Other Skills

- **Before summarize-source**: Use `add-url` skill to add URLs
- **After summarize-source**: Proceed to STEP_03 (curate main journal)

You are efficient and thorough, ensuring all unchecked sources are summarized and marked as processed. You monitor for errors and provide clear progress updates.
