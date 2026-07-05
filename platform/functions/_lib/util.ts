// Shared helpers for the platform API (epic #155).

export function json(data: unknown, status = 200, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", ...headers },
  });
}

export function error(message: string, status: number): Response {
  return json({ error: message }, status);
}

// Mirrors scripts/check_link.py sanitize_url(): strip tracking params + fragment.
// Heavy canonical/redirect resolution stays in the local pull (check_link.py);
// this is the first, cheap layer.
const TRACKING_PREFIXES = ["utm_", "fbclid", "gclid", "mc_", "ref", "source", "hl"];
const PRESERVE_PARAMS_HOSTS = ["lukew.com", "en.wikipedia.org"];

export function sanitizeUrl(raw: string): string {
  const u = new URL(raw);
  u.hash = "";
  if (!PRESERVE_PARAMS_HOSTS.some((h) => u.hostname.includes(h))) {
    const kept = new URLSearchParams();
    for (const [k, v] of u.searchParams) {
      if (!TRACKING_PREFIXES.some((p) => k.startsWith(p))) kept.append(k, v);
    }
    u.search = kept.toString() ? `?${kept.toString()}` : "";
  }
  return u.toString();
}

// Mirrors scripts/check_link.py validate_url(): public http(s) URLs only.
export function validateUrl(raw: string): string | null {
  let u: URL;
  try {
    u = new URL(raw);
  } catch {
    return "not a valid URL";
  }
  if (u.protocol !== "http:" && u.protocol !== "https:") return "only http(s) URLs are allowed";
  if (raw.length > 2048) return "URL too long (max 2048 chars)";
  const host = u.hostname;
  if (
    host === "localhost" ||
    host.startsWith("127.") ||
    host === "0.0.0.0" ||
    host === "::1" ||
    /^10\./.test(host) ||
    /^192\.168\./.test(host) ||
    /^172\.(1[6-9]|2\d|3[01])\./.test(host)
  ) {
    return "localhost/private addresses are not allowed";
  }
  return null; // valid
}
