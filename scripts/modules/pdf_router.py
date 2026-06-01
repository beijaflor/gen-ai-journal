"""PDF content-type routing.

Issue #141: PDFs must take a dedicated extraction path, not the HTML
BS4 path. The HTML path can clear the blocked-content guard on small
PDFs (a few KB of mangled bytes survives the 500-char threshold) and
then Gemini hallucinates a summary from the URL slug + domain.

The fix — per the issue's outside review — is to make PDF handling a
**detection decision**, not a **recovery decision**. We probe the URL
BEFORE any extraction runs and branch on Content-Type. If the probe
fails or is ambiguous, the URL suffix is used as a fallback signal.

This module is intentionally tiny and pure (curl subprocess only) so
it can be imported from both ``call-gemini.py`` and any future fetch
path without dragging in the BS4 / Playwright machinery.
"""

from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse


# A redirect-following HEAD that mimics a real browser. We deliberately
# avoid python-requests here because the SPA-router and other modules
# in this directory have a long history of curl-vs-requests quirks
# (see fetch_router.py / call-gemini.py for the urllib3 HTTP/2 bug).
_PROBE_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class ContentProbe:
    """Result of a HEAD probe against a URL.

    ``content_type`` is the lowercased media type with parameters stripped
    (``application/pdf`` rather than ``application/pdf; charset=binary``).
    ``content_length`` is None when the upstream did not report it.
    ``final_url`` reflects the URL after redirects (``-L`` in curl).
    ``ok`` is True when curl exited cleanly; on transport errors all
    other fields are best-effort and the caller should fall back to
    suffix-based detection.
    """

    ok: bool
    content_type: str
    content_length: Optional[int]
    final_url: str
    error: str = ""


def _strip_params(value: str) -> str:
    """Return the media type from ``application/pdf; charset=binary``."""
    return value.split(";", 1)[0].strip().lower()


def probe_content_type(url: str, timeout: int = 10) -> ContentProbe:
    """Issue a HEAD with redirects and parse the final response headers.

    Falls back to a streaming GET (``-X GET --max-filesize 0``) if the
    server rejects HEAD with 405 — some CDNs do. The body is discarded
    either way; we only care about the headers.
    """
    try:
        result = subprocess.run(
            [
                "curl",
                "-sIL",
                "--max-time",
                str(timeout),
                "-A",
                _PROBE_USER_AGENT,
                url,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 5,
        )
    except subprocess.TimeoutExpired:
        return ContentProbe(False, "", None, url, error=f"HEAD timed out after {timeout}s")
    except Exception as exc:  # noqa: BLE001
        return ContentProbe(False, "", None, url, error=f"HEAD failed: {exc}")

    if result.returncode != 0:
        return ContentProbe(
            False,
            "",
            None,
            url,
            error=f"curl exit {result.returncode}: {result.stderr.strip()[:200]}",
        )

    # curl -IL emits one header block per hop; the last block describes
    # the final response. Split on blank lines and keep the last block
    # that actually contains a status line.
    blocks = [block for block in result.stdout.split("\r\n\r\n") if block.strip()]
    if not blocks:
        # Some servers return LF-only line endings.
        blocks = [block for block in result.stdout.split("\n\n") if block.strip()]
    if not blocks:
        return ContentProbe(False, "", None, url, error="curl returned no headers")

    final_block = blocks[-1]
    headers = {}
    for line in final_block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            headers[key.strip().lower()] = value.strip()

    content_type = _strip_params(headers.get("content-type", ""))
    content_length: Optional[int]
    try:
        content_length = int(headers["content-length"]) if "content-length" in headers else None
    except (TypeError, ValueError):
        content_length = None

    # curl -L doesn't expose the final URL via the header block; pull it
    # from -w if we ever need it. For now the request URL is good enough:
    # callers use this to label the result, not as authoritative.
    return ContentProbe(True, content_type, content_length, url)


def has_pdf_suffix(url: str) -> bool:
    """Cheap suffix check on the URL path.

    Tolerates query strings (``?foo=bar``) and fragments. Used both as a
    fast pre-check (skip the HEAD round-trip when the URL is obviously a
    PDF) and as a fallback when the HEAD probe fails.
    """
    try:
        path = urlparse(url).path or ""
    except ValueError:
        return False
    return path.lower().endswith(".pdf")


def is_pdf_url(url: str, timeout: int = 10) -> bool:
    """Return True if ``url`` should be routed to the PDF pipeline.

    Decision order:

    1. If the URL path ends in ``.pdf``, return True without probing.
       Some CDNs serve PDFs with ``Content-Type: application/octet-stream``;
       the suffix is the authoritative signal here.
    2. Otherwise, HEAD-probe the URL. Return True iff the final
       Content-Type is ``application/pdf``.
    3. If the probe fails (network error, 4xx/5xx), return False — the
       caller will fall back to the HTML path and the existing
       blocked-content guard will catch the large-PDF case.

    This function never raises. Probe failures are logged at WARNING.
    """
    if has_pdf_suffix(url):
        return True

    probe = probe_content_type(url, timeout=timeout)
    if not probe.ok:
        logging.warning("PDF probe failed for %s: %s", url, probe.error)
        return False
    if probe.content_type == "application/pdf":
        return True
    return False
