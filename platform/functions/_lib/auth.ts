// API authorization (epic #155): two accepted identities.
//  1. Machines (pull_inbox.py / push_summaries.py): Authorization: Bearer <API_BEARER_TOKEN>
//  2. Humans (submit form / inbox / console pages): the Cloudflare Access JWT
//     that the browser carries as the CF_Authorization cookie after passing the
//     Access login wall. /api/* itself is NOT behind Access (machines must reach
//     it), so we verify the JWT signature here against the team's public keys.

export interface Env {
  DB: D1Database;
  REBUILD_THROTTLE: KVNamespace;
  API_BEARER_TOKEN: string;
  TEAM_DOMAIN: string; // e.g. https://gentle-hill-7034.cloudflareaccess.com
  POLICY_AUD: string;  // Access application audience tag
}

interface Jwk {
  kid: string;
  kty: string;
  n: string;
  e: string;
  alg?: string;
}

let jwksCache: { keys: Jwk[]; fetchedAt: number } | null = null;
const JWKS_TTL_MS = 60 * 60 * 1000;
// Floor for forced (kid-miss) refetches: a fresh fetch is authoritative, so a
// kid still missing from a <60s-old cache is genuinely invalid — this keeps
// requests with garbage kids from hammering the certs endpoint.
const JWKS_FORCE_MIN_AGE_MS = 60 * 1000;

async function getJwks(teamDomain: string, force = false): Promise<Jwk[]> {
  if (!force && jwksCache && Date.now() - jwksCache.fetchedAt < JWKS_TTL_MS) return jwksCache.keys;
  const res = await fetch(`${teamDomain}/cdn-cgi/access/certs`);
  if (!res.ok) throw new Error(`JWKS fetch failed: ${res.status}`);
  const body = (await res.json()) as { keys: Jwk[] };
  jwksCache = { keys: body.keys, fetchedAt: Date.now() };
  return body.keys;
}

function b64urlToBytes(s: string): Uint8Array {
  const pad = s.length % 4 === 0 ? "" : "=".repeat(4 - (s.length % 4));
  const bin = atob(s.replace(/-/g, "+").replace(/_/g, "/") + pad);
  return Uint8Array.from(bin, (c) => c.charCodeAt(0));
}

async function verifyAccessJwt(token: string, env: Env): Promise<string | null> {
  // Returns the authenticated email, or null if invalid.
  try {
    const [h, p, sig] = token.split(".");
    if (!h || !p || !sig) return null;
    const header = JSON.parse(new TextDecoder().decode(b64urlToBytes(h)));
    const payload = JSON.parse(new TextDecoder().decode(b64urlToBytes(p)));

    const aud: string[] = Array.isArray(payload.aud) ? payload.aud : [payload.aud];
    if (!aud.includes(env.POLICY_AUD)) return null;
    if (payload.iss !== env.TEAM_DOMAIN) return null;
    const now = Math.floor(Date.now() / 1000);
    if (typeof payload.exp !== "number" || payload.exp < now) return null;

    let jwk = (await getJwks(env.TEAM_DOMAIN)).find((k) => k.kid === header.kid);
    if (!jwk && jwksCache && Date.now() - jwksCache.fetchedAt >= JWKS_FORCE_MIN_AGE_MS) {
      // Unknown kid on a cached key set: Access rotates signing keys (~6-weekly),
      // so the cache may be stale. Refetch once before rejecting.
      jwk = (await getJwks(env.TEAM_DOMAIN, true)).find((k) => k.kid === header.kid);
    }
    if (!jwk) return null;
    const key = await crypto.subtle.importKey(
      "jwk",
      { kty: jwk.kty, n: jwk.n, e: jwk.e, alg: "RS256", ext: true },
      { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
      false,
      ["verify"],
    );
    const ok = await crypto.subtle.verify(
      "RSASSA-PKCS1-v1_5",
      key,
      b64urlToBytes(sig),
      new TextEncoder().encode(`${h}.${p}`),
    );
    return ok ? (payload.email ?? "access-user") : null;
  } catch {
    return null;
  }
}

function getCookie(request: Request, name: string): string | null {
  const cookie = request.headers.get("cookie") ?? "";
  const m = cookie.match(new RegExp(`(?:^|;\\s*)${name}=([^;]+)`));
  return m ? m[1] : null;
}

/** Returns an identity string when authorized, otherwise null. */
export async function authorize(request: Request, env: Env): Promise<string | null> {
  const authHeader = request.headers.get("authorization") ?? "";
  if (authHeader.startsWith("Bearer ")) {
    const token = authHeader.slice(7).trim();
    if (env.API_BEARER_TOKEN && token === env.API_BEARER_TOKEN) return "bearer";
    return null;
  }
  const jwt = request.headers.get("cf-access-jwt-assertion") ?? getCookie(request, "CF_Authorization");
  if (jwt) return verifyAccessJwt(jwt, env);
  return null;
}
