# platform/ — Cloudflare content platform

Cloud side of the online migration (epic #155). Phase 1 scope: link inbox
(#159), summary collection API (#160), admin console (#161). The journal
website itself is NOT hosted here yet — see the epic for later phases.

Live at: **https://gen-ai-journal.pages.dev**

## Layout

```
wrangler.jsonc        project config: D1 + KV bindings, Access vars
migrations/           D1 schema, applied with wrangler d1 migrations
functions/            Pages Functions = the API (TypeScript)
  _lib/auth.ts        bearer-token + Cloudflare Access JWT verification
  _lib/util.ts        URL sanitize/validate (mirrors scripts/check_link.py), JSON helpers
  api/links/          POST (submit), GET (list), PATCH /:id (status)
public/               static pages (deployed as-is)
  submit/             link submission form + bookmarklet  [Access-protected]
  inbox/              inbox viewer with status filters    [Access-protected]
```

## Auth model

| Caller | Mechanism |
|---|---|
| Local scripts (`pull_inbox.py`, `push_summaries.py`) | `Authorization: Bearer` — token in Pages secret `API_BEARER_TOKEN` = `PLATFORM_API_TOKEN` in `scripts/.env` |
| Browser (submit/inbox/admin pages) | Cloudflare Access wall on the page paths; the `CF_Authorization` cookie JWT is verified in-function for `/api/*` calls (signature via team JWKS, `aud` = `POLICY_AUD` var) |
| Public | `/` only; every `/api/*` write and read requires one of the above |

Access application lives in the Zero Trust dashboard (team
`gentle-hill-7034`): paths `/admin`, `/submit`, `/inbox`, allow-email policy,
One-time PIN login.

## Commands

```bash
# Local dev (local D1; bearer token "dev-token" from .dev.vars)
cd platform
wrangler d1 migrations apply gen-ai-journal-db --local
wrangler pages dev --port 8788

# Schema changes: add migrations/NNNN_*.sql, then
wrangler d1 migrations apply gen-ai-journal-db --remote

# Deploy
wrangler pages deploy ./public --project-name gen-ai-journal --branch main

# Rotate the bearer token
wrangler pages secret put API_BEARER_TOKEN --project-name gen-ai-journal
#   ...and update PLATFORM_API_TOKEN in scripts/.env to match
```

## Bookmarklet

Drag from the /submit page, or create a bookmark with this URL:

```
javascript:window.open('https://gen-ai-journal.pages.dev/submit?url='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title),'_blank')
```
