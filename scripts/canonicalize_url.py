#!/usr/bin/env python3
"""
Resolve the canonical form of a URL by inspecting the page's HTML <head>.

Looks for canonical signals in this priority order:
  1. <link rel="alternate" hrefLang="x-default" href="...">
  2. <link rel="canonical" href="...">
  3. <meta property="og:url" content="...">

This catches the common pattern where a locale-specific URL (e.g.
https://openai.com/ja-JP/index/foo/) declares an English x-default
canonical at https://openai.com/index/foo/, so subsequent duplicate
checks compare the same article under one identity.

Usage as a module:
    from canonicalize_url import fetch_canonical
    canonical, source = fetch_canonical("https://openai.com/ja-JP/index/foo/")
    # canonical -> "https://openai.com/index/foo/"
    # source    -> "hreflang=x-default"

Usage as a CLI (for debugging / one-off lookups):
    python3 scripts/canonicalize_url.py <URL>
"""

import sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests
from requests.exceptions import RequestException


DEFAULT_USER_AGENT = "Mozilla/5.0 (GenAI Journal Link Checker)"
# Many head sections are well under 32 KiB; bound the response so we don't
# pull whole articles just to read <head>.
DEFAULT_RANGE_BYTES = 32768
DEFAULT_TIMEOUT = 10


class _CanonicalHeadParser(HTMLParser):
    """Extract canonical signals from a document's <head>.

    Records, in document order, the first occurrence of each signal.
    Stops collecting once <body> opens or </head> closes — anything past
    the head is irrelevant and may even be a truncated fragment from the
    Range request.
    """

    def __init__(self):
        super().__init__()
        self.x_default: str | None = None
        self.canonical: str | None = None
        self.og_url: str | None = None
        self._in_head = False
        self._past_head = False

    def handle_starttag(self, tag, attrs):
        if self._past_head:
            return
        tag_lower = tag.lower()
        if tag_lower == "head":
            self._in_head = True
            return
        if tag_lower == "body":
            self._in_head = False
            self._past_head = True
            return
        # Some short pages render meta before any explicit <head> (rare but
        # possible with malformed HTML). Be tolerant: also accept tags at the
        # top of the document until we hit <body>.
        if not self._in_head and not self._past_head:
            pass  # accept top-of-document tags too
        elif not self._in_head:
            return
        attrs_dict = {k.lower(): (v or "") for k, v in attrs}

        if tag_lower == "link":
            rel = attrs_dict.get("rel", "").lower().strip()
            hreflang = attrs_dict.get("hreflang", "").lower().strip()
            href = attrs_dict.get("href", "").strip()
            if not href:
                return
            if rel == "alternate" and hreflang == "x-default":
                if self.x_default is None:
                    self.x_default = href
            elif rel == "canonical":
                if self.canonical is None:
                    self.canonical = href
        elif tag_lower == "meta":
            prop = attrs_dict.get("property", "").lower().strip()
            content = attrs_dict.get("content", "").strip()
            if prop == "og:url" and content and self.og_url is None:
                self.og_url = content

    def handle_endtag(self, tag):
        if tag.lower() == "head":
            self._past_head = True
            self._in_head = False


def parse_canonical_signals(
    html_text: str,
    base_url: str,
) -> tuple[str | None, str | None]:
    """Parse canonical signals from HTML text.

    Returns (canonical_url, source_label) where source_label is one of
    "hreflang=x-default", "rel=canonical", "og:url", or (None, None) if
    no signal is present. Relative hrefs are resolved against base_url.

    Exposed for testability: tests can feed fixture HTML directly without
    hitting the network.
    """
    parser = _CanonicalHeadParser()
    try:
        parser.feed(html_text)
    except Exception:
        # html.parser can raise on edge-case malformed input; tolerate and
        # work with whatever we collected before the error.
        pass

    candidates = [
        ("hreflang=x-default", parser.x_default),
        ("rel=canonical", parser.canonical),
        ("og:url", parser.og_url),
    ]
    for source, href in candidates:
        if not href:
            continue
        resolved = urljoin(base_url, href)
        # Sanity-check: must be http(s).
        scheme = urlparse(resolved).scheme.lower()
        if scheme not in ("http", "https"):
            continue
        return resolved, source
    return None, None


def fetch_canonical(
    url: str,
    timeout: int = DEFAULT_TIMEOUT,
    user_agent: str = DEFAULT_USER_AGENT,
    range_bytes: int = DEFAULT_RANGE_BYTES,
) -> tuple[str | None, str | None]:
    """Fetch the URL's <head> and resolve its canonical URL.

    Returns (canonical_url, source_label) where source_label identifies
    which signal was used, or (None, None) on any of:
      - network failure / timeout
      - non-success HTTP status
      - no canonical signals present
      - canonical scheme is not http(s)

    The canonical is NOT compared against `url` here; the caller decides
    whether the swap is a no-op (e.g. after re-sanitization). This keeps
    self-reference policy out of the helper and in check_link.py where
    sanitization rules live.
    """
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        # Range as a hint; servers that ignore it just return the full body,
        # which we'll truncate ourselves.
        "Range": f"bytes=0-{range_bytes}",
    }
    try:
        response = requests.get(
            url,
            allow_redirects=True,
            timeout=timeout,
            headers=headers,
            stream=False,
        )
    except RequestException:
        return None, None

    # 2xx and 206 (Partial Content) are both fine. Treat 3xx oddly-stuck as ok
    # since requests has already followed allow_redirects=True.
    if response.status_code >= 400:
        return None, None

    # Be safe even if the server ignored the Range header.
    text = response.text[: range_bytes * 2] if response.text else ""
    if not text:
        return None, None

    # Use response.url (post-redirect) as the base for relative href
    # resolution — that's what a browser would do for a <link href="/foo">.
    return parse_canonical_signals(text, response.url)


def _cli() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/canonicalize_url.py <URL>", file=sys.stderr)
        return 1
    url = sys.argv[1]
    canonical, source = fetch_canonical(url)
    if canonical:
        print(f"Input:     {url}")
        print(f"Canonical: {canonical}  (from {source})")
        return 0
    print(f"No canonical URL found for: {url}")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
