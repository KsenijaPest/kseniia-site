## Technical Foundations

**Technical Score: 86/100** — Good

Audit date: 2026-09-02. Site: https://kseniiashermin.com (6 pages: /, /about/, /case-studies/, /services/, /for-employers/, /contact/). Method: raw HTTP responses via curl (headers + body, no JS execution) plus TLS/DNS checks, matching how AI crawlers (GPTBot, ClaudeBot, PerplexityBot) actually see the site.

### Score Breakdown

| Category | Score | Weight | Weighted | Status |
|---|---|---|---|---|
| Server-Side Rendering | 100/100 | 25% | 25.0 | Pass |
| Meta Tags & Indexability | 92/100 | 15% | 13.8 | Pass |
| Crawlability | 90/100 | 15% | 13.5 | Pass |
| Security Headers | 45/100 | 10% | 4.5 | Fail |
| Core Web Vitals Risk | 80/100 | 10% | 8.0 | Pass |
| Mobile Optimization | 88/100 | 10% | 8.8 | Pass |
| URL Structure | 98/100 | 5% | 4.9 | Pass |
| Response & Status | 80/100 | 5% | 4.0 | Pass |
| Additional Checks | 78/100 | 5% | 3.9 | Pass |
| **Total** | | | **86.4 → 86** | **Good** |

### Server-Side Rendering Assessment

**Status:** LOW risk
**Rendering Type:** SSG (static-generated, fully server-rendered HTML)
**Framework Detected:** Astro (`<meta name="generator" content="astro">`, `data-astro-cid-*` attributes, `/_astro/` build assets)

This is the single strongest part of the site for GEO. Every page ships full text content in the raw HTML response, before any JavaScript runs:

| Page | Body text visible without JS |
|---|---|
| Home | 3,436 characters |
| About | 3,657 characters |
| Case Studies | 3,356 characters |
| Services | 1,826 characters |
| For Employers | 1,381 characters |
| Contact | 620 characters |

No empty root div, no client-side framework bundle rendering content, no `<noscript>` fallback needed. JavaScript on the page is limited to three small inline scripts (cookie-consent banner, mobile nav toggle, a consent-gated GA4/Clarity loader) plus a deferred Cloudflare beacon — none of it gates content. Two valid `application/ld+json` blocks (Person + ProfessionalService schema) are also present in raw HTML. AI crawlers that don't execute JS will see the same content a human visitor sees.

Minor unrelated bug spotted in passing: the Cloudflare beacon script still has `data-cf-beacon='{"token": "REPLACE_ME"}'` — a placeholder token, so Cloudflare Web Analytics is not actually collecting data. Not an SEO issue, but worth a one-line fix.

### Crawlability & Indexability

**Robots.txt:** Found (200) — `User-agent: *` / `Allow: /`, plus explicit named `Allow: /` rules for GPTBot, ChatGPT-User, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Applebot-Extended, and Bingbot. No Disallow lines, no Crawl-delay, `Sitemap:` directive present and correct. This is close to best-practice for GEO — most sites don't explicitly allow-list AI crawlers.
**XML Sitemap:** Found at `/sitemap-index.xml` → `/sitemap-0.xml`. Valid XML, all 6 URLs present with correct namespaces. Gap: no `<lastmod>` dates on any URL — a minor freshness signal loss for both Google and AI crawlers re-checking for updates.
**Meta Robots:** Indexable on all 6 pages (no `noindex`/`nofollow` meta tag anywhere; no `X-Robots-Tag` header on any response either — confirmed by checking response headers directly).
**Canonical:** Self-referencing on every page, matches the URL exactly (e.g. `/about/` canonical is `https://kseniiashermin.com/about/`).

### Meta Tags Audit

| Tag | Status | Value/Issue |
|---|---|---|
| Title | Present, unique x6 | Home: 67 chars (slightly over the 60-char guideline, acceptable); About/For Employers/Contact are short (23-31 chars) but not empty/generic |
| Description | Present, unique x6 | Home 160 chars (at the limit), Services 155, For Employers 157 — good. About 106, Case Studies 105, Contact 71 — under the 150-160 target, room to add more keyword-rich detail |
| Canonical | Present x6 | Self-referencing, correct |
| Viewport | Present x6 | `width=device-width, initial-scale=1.0, viewport-fit=cover` |
| Language | Present x6 | `<html lang="en">` |
| Open Graph | Complete x6 | og:type, og:title, og:description, og:url, og:image (with width/height 1200x630) on every page |
| Twitter Card | Complete x6 | summary_large_image, title, description, image on every page |

Per-page titles/descriptions (all unique, no duplication across pages — good, this was checked explicitly since duplicate titles/descriptions are a common small-site failure):

| Page | Title (chars) | Description (chars) |
|---|---|---|
| Home | Performance Marketing Manager \| Lead Gen at Scale \| Kseniia Shermin (67) | 160 |
| About | About \| Kseniia Shermin (23) | 106 |
| Case Studies | PPC & Paid Search Case Studies \| Kseniia Shermin (48) | 105 |
| Services | PPC & Paid Search Services \| Kseniia Shermin (44) | 155 |
| For Employers | For Employers \| Kseniia Shermin (31) | 157 |
| Contact | Contact \| Kseniia Shermin (25) | 71 |

No hreflang tags — correct, since the site is single-language/single-region, not a defect.

### Security Headers

This is the weak point of the audit.

| Header | Status | Value |
|---|---|---|
| HTTPS | Yes, but not enforced | Valid cert (Google Trust Services, WE1; valid Aug 13 – Nov 11 2026). **However, `http://kseniiashermin.com/` returns a 200 and serves the full page over plain HTTP — it does not redirect to HTTPS.** Verified by byte-for-byte diff of the HTTP and HTTPS homepage responses (identical, 15,547 bytes). |
| HSTS | Missing | No `Strict-Transport-Security` header on any of the 6 pages |
| CSP | Missing | No `Content-Security-Policy` header |
| X-Frame-Options | Missing | Not present |
| X-Content-Type-Options | Missing | Not present |
| Referrer-Policy | Missing | Not present |
| Permissions-Policy | Missing | Not present |

The site is served through Cloudflare (server: cloudflare, cf-ray, cf-cache-status present on every response), which makes all of the above a config change rather than an application rewrite — HSTS, security headers, and a "no HTTP" redirect can all be turned on in Cloudflare (SSL/TLS → Edge Certificates → Always Use HTTPS/HSTS, and Transform Rules or a small Worker for the other headers) without touching the Astro codebase.

Note: `www.kseniiashermin.com` doesn't resolve at all (NXDOMAIN) rather than redirecting to the apex domain. Low priority — nobody is likely to type `www.` for this site — but a quick DNS/redirect rule would close the gap.

### Core Web Vitals Risk Assessment

Static HTML analysis only — treat as directional risk, not a measurement. Validate with PageSpeed Insights / CrUX for field data.

| Vital | Risk Level | Indicators Found |
|---|---|---|
| LCP | Medium | Homepage hero photo (`kseniia-shermin.jpg`) is a native 800×800 iPhone photo weighing 161 KB, displayed at only 140×140 (180×180 on About). No `srcset`/`sizes`, no WebP/AVIF, no `fetchpriority="high"` on what is likely the LCP element. CSS is a single 4.4 KB file with no `media` attribute (technically render-blocking, but small enough to be negligible). No `<link rel="preload">` hints anywhere. |
| INP | Low | Very light JS footprint: 3 small inline scripts (cookie consent, mobile nav toggle, consent-gated GA4/Clarity loader) plus one deferred third-party beacon. No heavy frameworks, no synchronous third-party scripts, DOM is small (~129 elements on the homepage). No inline `onclick`-style handlers found. |
| CLS | Low | All `<img>` tags found carry explicit `width`/`height` attributes. No iframes/embeds. No custom web fonts loaded (no `@font-face`, no Google Fonts link — likely a system font stack), so no font-swap reflow risk. |

Bottom line: the only real CWV risk is the unoptimized/oversized hero image, which is a quick fix (resize + compress, or serve via an image CDN/Astro's built-in image optimization).

### Mobile Optimization

**Status:** Optimized
Viewport meta tag correct on all 6 pages. The site's single stylesheet (`/_astro/Layout.D42hlQ_1.css`) contains real media queries (`@media (width<=768px)`, `@media (width<=640px)`) and uses `display:flex`/`display:grid` for layout — genuine responsive design, not just a viewport tag with fixed-width markup. Base font sizes in the CSS are 1rem (16px) for body copy, with smaller sizes (0.8-0.95rem) reserved for secondary text — reasonable. A hamburger nav toggle with `aria-expanded` state is present for mobile navigation. Touch-target sizing (44×44px) can't be fully confirmed from static CSS alone without rendering, but nothing in the markup suggests undersized tap targets.

### URL Structure

**Target URLs:** `https://kseniiashermin.com/`, `/about/`, `/case-studies/`, `/services/`, `/for-employers/`, `/contact/`
**Assessment:** Clean
Flat, one-level-deep, descriptive, all-lowercase, hyphen-separated slugs with no parameters or session IDs. Trailing-slash form is canonical and consistently enforced: requesting `/about` (no trailing slash) returns a single 307 redirect to `/about/` — a minor extra hop, not a chain, and not worth fixing given how small the impact is.

### Response Headers & Status

All 6 pages return `HTTP/2 200`, `content-type: text/html`, `content-encoding: gzip`, and are served via Cloudflare edge cache (`cf-cache-status: HIT`). No redirect chains on the canonical URLs. The one deduction here is structural, not per-page: the missing HTTP→HTTPS redirect (see Security Headers) means the site is technically reachable at two different "origins" (http:// and https://) with identical content and no canonicalizing redirect — a duplicate-content-via-protocol edge case, even though the `<link rel="canonical">` tags mitigate most of the risk for search engines that respect canonicals.

### Agent-Readiness Signals (non-scoring)

#### RFC 8288 Link Headers (Service Discovery)

**Status:** Absent — Not Applicable

No `Link:` headers of any kind on any of the 6 responses. This is a small personal-brand/consultant site (not an API product), with no `/api/` or `/developers/` paths and no API documentation in the nav or sitemap. Per GEO guidance, this signal is only actionable for API-first sites — no recommendation surfaced.

#### Markdown Content Negotiation

**Status:** Not Supported
**Test:** `GET https://kseniiashermin.com/` with `Accept: text/markdown`
**Response Content-Type:** `text/html` (200 OK — request succeeded, server just ignored the Accept header and returned standard HTML)

Forward-looking note: the site is served through Cloudflare (confirmed via `server: cloudflare` and `cf-ray` on every response). If it's on Cloudflare Pages or behind a Cloudflare Worker, markdown content negotiation for AI agents can be added with a small Worker route that returns a markdown version when `Accept: text/markdown` is present — a one-line-of-config-class change, not a rebuild. Given the site's small page count (6 pages) and that `llms.txt` already exists, this is a nice-to-have rather than urgent.

### Priority Actions

1. **[CRITICAL]** None. There is no CRITICAL-severity finding — the site's biggest structural risk area (SSR/JS dependency) is a clean pass.
2. **[HIGH]** Force HTTPS: enable Cloudflare's "Always Use HTTPS" (or an equivalent redirect rule) so `http://kseniiashermin.com/` 301s to `https://`, and turn on HSTS (`Strict-Transport-Security: max-age=31536000; includeSubDomains`). This is a Cloudflare dashboard change, not a code change, and closes the biggest gap in the audit.
3. **[HIGH]** Add the missing security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) via Cloudflare Transform Rules or a lightweight Worker. Same effort tier as #2 — batch these together in one Cloudflare session.
4. **[MEDIUM]** Resize/compress the homepage and About-page hero photo. It's an 800×800, 161 KB native iPhone JPEG displayed at 140-180px — either run it through Astro's built-in `<Image>` optimization (auto WebP/AVIF + responsive sizes) or manually export a properly sized, compressed version. Quick win for LCP.
5. **[MEDIUM]** Add `<lastmod>` dates to the sitemap entries so search engines and AI crawlers can tell when pages last changed — most static-site generators (including Astro's sitemap integration) can populate this automatically from file mtimes.
6. **[LOW]** Lengthen the shorter meta descriptions (About: 106 chars, Case Studies: 105 chars, Contact: 71 chars) toward the 150-160 char range to use the available SERP snippet space and add a bit more keyword context.
7. **[LOW]** Fix the placeholder Cloudflare Analytics token (`data-cf-beacon='{"token": "REPLACE_ME"}'`) — not an SEO issue, but analytics are currently not being collected.
8. **[LOW]** Optional: add a DNS/redirect rule so `www.kseniiashermin.com` resolves (currently NXDOMAIN) rather than erroring for anyone who types the www prefix.
