"""Domain-aware fetch routing and anti-bot/SPA-shell guard.

Issue #121: Some upstream domains either render content client-side (SPAs)
or front the page with an anti-bot JavaScript challenge. The default curl +
BeautifulSoup pipeline used by ``scripts/call-gemini.py`` then receives no
real article text — and the LLM happily hallucinates a summary anyway.

This module provides three small, pure functions so they can be tested in
isolation and reused from any fetch path:

- ``needs_spa_render(url)`` — should we route this URL through the headless
  (Playwright) path instead of plain curl?
- ``looks_blocked(extracted_text)`` — given the extracted text after
  BeautifulSoup stripping, does it look like an anti-bot interstitial or an
  un-hydrated SPA shell? If so, the LLM call MUST be skipped.
- ``build_blocked_stub(url, reason, ...)`` — produce a clearly-flagged stub
  payload (a short markdown document with a ``BLOCKED:`` marker) suitable
  for writing to ``workdesk/summaries/`` so the URL is not silently retried
  and so a human can spot it on sight during STEP_02 review.

The router and guard are intentionally conservative:

- ``needs_spa_render`` only returns ``True`` for hosts on a small explicit
  allowlist. ``developers.openai.com`` is excluded — it is server-rendered
  and routing it through Playwright would slow it down for no benefit.
- ``looks_blocked`` triggers on either (a) extracted text below a length
  threshold (currently 500 chars — the hallucination cases observed in the
  issue extracted ~41 chars) or (b) literal interstitial signatures that
  are well-documented (Cloudflare's "Just a moment...", OpenAI's
  "Enable JavaScript and cookies to continue", etc.).
"""

from __future__ import annotations

from typing import Tuple
from urllib.parse import urlparse


# Hosts whose pages are rendered client-side and therefore need a headless
# browser. ``openai.com`` is included here because both ``/index/*`` and
# ``/business/*`` sit behind a JS challenge; ``developers.openai.com`` is
# explicitly excluded below because it is server-rendered.
SPA_RENDER_HOSTS = (
    "qwen.ai",
    "chat.qwen.ai",
    "openai.com",
)

# Suffix-match hosts (covers all subdomains of the suffix). E.g. any
# ``*.notion.site`` page is an SPA.
SPA_RENDER_HOST_SUFFIXES = (
    ".notion.site",
)

# Hosts that LOOK like they would match the SPA allowlist but must NOT —
# they are server-rendered and the curl path works fine.
SPA_RENDER_EXCLUDED_HOSTS = (
    "developers.openai.com",
)

# Below this many characters of extracted text we treat the fetch as
# unreliable and refuse to summarise. The verified failure cases in
# Issue #121 extracted ~41 chars; 500 is a comfortable safety margin
# without tripping on legitimately short pages (a real article is
# typically thousands of characters once script/style have been stripped).
BLOCKED_MIN_CHARS = 500

# Substrings that, when present in the extracted text, are a near-certain
# indicator that we got an interstitial and not the article.
INTERSTITIAL_SIGNATURES = (
    # OpenAI's anti-bot gate (literal text confirmed in Issue #121).
    "Enable JavaScript and cookies to continue",
    # Cloudflare's challenge page common phrases.
    "Just a moment...",
    "Checking your browser",
)


def _hostname(url: str) -> str:
    """Return the lower-cased hostname of ``url`` (``''`` if unparseable)."""
    try:
        host = urlparse(url).hostname or ""
    except ValueError:
        return ""
    return host.lower()


def needs_spa_render(url: str) -> bool:
    """Return True if ``url`` should be fetched via a headless browser.

    Routing rules (in order):

    1. If the hostname is in :data:`SPA_RENDER_EXCLUDED_HOSTS`, return False
       even if it would otherwise match — this is what protects
       ``developers.openai.com`` from being routed through Playwright.
    2. If the hostname matches an entry in :data:`SPA_RENDER_HOSTS`
       (exact match or subdomain), return True.
    3. If the hostname ends with one of :data:`SPA_RENDER_HOST_SUFFIXES`,
       return True.
    4. Otherwise, return False (use the plain curl path).
    """
    host = _hostname(url)
    if not host:
        return False

    # Rule 1: explicit exclusions win.
    for excluded in SPA_RENDER_EXCLUDED_HOSTS:
        if host == excluded or host.endswith("." + excluded):
            return False

    # Rule 2: exact-or-subdomain match against the allowlist.
    for allowed in SPA_RENDER_HOSTS:
        if host == allowed or host.endswith("." + allowed):
            return True

    # Rule 3: suffix match (e.g. *.notion.site).
    for suffix in SPA_RENDER_HOST_SUFFIXES:
        if host.endswith(suffix):
            return True

    return False


def looks_blocked(extracted_text: str) -> Tuple[bool, str]:
    """Return ``(is_blocked, reason)`` for already-extracted page text.

    "Extracted" here means: the result of BeautifulSoup stripping out
    ``<script>``/``<style>`` tags and collapsing whitespace, i.e. exactly
    what the LLM would otherwise be asked to summarise.

    Two conditions trigger a block:

    1. The extracted text contains a known interstitial signature
       (Cloudflare challenge, OpenAI anti-bot gate, etc.). This wins over
       the length check so the reason message is actionable.
    2. The extracted text is shorter than :data:`BLOCKED_MIN_CHARS`. This
       catches both un-hydrated SPA shells and unknown anti-bot pages.

    The function never raises — a ``None`` or empty input is treated as
    blocked with a descriptive reason.
    """
    if not extracted_text:
        return True, "extracted text is empty (fetch produced no content)"

    # Interstitial signatures first — they give a more useful reason.
    for sig in INTERSTITIAL_SIGNATURES:
        if sig in extracted_text:
            return True, f"interstitial signature detected: {sig!r}"

    n = len(extracted_text)
    if n < BLOCKED_MIN_CHARS:
        return (
            True,
            f"extracted text too short ({n} chars < {BLOCKED_MIN_CHARS} threshold); "
            "page is likely an un-hydrated SPA shell or anti-bot challenge",
        )

    return False, ""


def build_blocked_stub(
    url: str,
    reason: str,
    extracted_chars: int,
    raw_bytes: int,
    fetcher: str,
) -> str:
    """Render a short markdown stub flagging ``url`` as un-summarisable.

    The first line is intentionally a single ``BLOCKED:`` marker so a
    human scrolling through ``workdesk/summaries/`` cannot miss it. The
    body records the URL, the reason the guard fired, and the byte/char
    counts observed during the fetch — enough context to decide whether
    to (a) retry with a different fetcher, (b) curate the URL as
    annex/omit, or (c) drop it.

    This format is deliberately NOT the schema-valid summary JSON — the
    summary validator would reject it, which is the correct behaviour:
    blocked stubs must never be promoted into the published journal.
    """
    return (
        "BLOCKED: summary suppressed — fetch did not return usable content.\n"
        "\n"
        f"- URL: {url}\n"
        f"- Reason: {reason}\n"
        f"- Fetcher: {fetcher}\n"
        f"- Extracted chars: {extracted_chars}\n"
        f"- Raw bytes: {raw_bytes}\n"
        "\n"
        "This stub was emitted by scripts/modules/fetch_router.py to prevent\n"
        "the LLM from hallucinating a summary against an anti-bot interstitial\n"
        "or an un-hydrated SPA shell. See Issue #121 for context.\n"
        "\n"
        "Action required: re-fetch this URL manually (e.g. via Playwright with\n"
        "an authenticated session, or by archiving the page and feeding the\n"
        "saved HTML), or curate the URL out of the journal.\n"
    )
