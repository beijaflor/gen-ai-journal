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
- **200 OK but `Content-Type` is non-HTML** (e.g. PDF, video) → document and stop; this skill cannot summarize binary content

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

**Known gap (follow-up)**: `call-gemini.py` does not currently expose a `--content` flag or stdin-content mode for "I already have the article text, just summarize it". The workaround above uses `--file` with a hand-built prompt, which bypasses the URL-mode JSON pipeline (the script only auto-applies the structured-output JSON pipeline when `--url` is set). If validation fails on the resulting output, escalate to **Step 6**. A clean fix would be a new `--content <path>` flag that reuses the URL-mode JSON pipeline with externally supplied article text — tracked as a follow-up.

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

## Relationship to Other Skills

- **Before summarize-source**: Use `add-url` skill to add URLs
- **After summarize-source**: Proceed to STEP_03 (curate main journal)

You are efficient and thorough, ensuring all unchecked sources are summarized and marked as processed. You monitor for errors and provide clear progress updates.
