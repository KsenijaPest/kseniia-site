## AI Visibility Analysis — kseniiashermin.com

**AI Visibility Score: 67/100 — Good (with a specific, fixable weak point)**

Score interpretation:
- 0-20: Critical | 21-40: Poor | 41-60: Fair | 61-80: Good | 81-100: Excellent

### Score Breakdown

| Component | Score | Weight | Weighted |
|---|---|---|---|
| Citability | 86/100 | 35% | 30.1 |
| Brand Mentions | 15/100 | 30% | 4.5 |
| Crawler Access | 100/100 | 25% | 25.0 |
| llms.txt | 78/100 | 10% | 7.8 |
| **Total** | | | **67.4 ≈ 67** |

The site is technically excellent (crawler access, llms.txt, on-page schema) and the content itself is unusually citable for a consultant site. The composite score is pulled down almost entirely by one thing: **third-party brand-authority signals are nearly absent**, and the one platform where a real profile does exist (LinkedIn) carries a name-collision risk that could actively confuse AI entity resolution.

---

### Citability Assessment

**Page Citability Score: 86/100** (average of top 5 scoring blocks, site-wide, across homepage/about/case-studies/services)

This is a genuinely strong result. The case-studies page in particular is close to ideal AI-citation format: each entry uses a **stat callout + Context/Platforms/What I did/Result** structure, which is exactly the self-contained, quotable shape that AI answer engines lift verbatim.

**Top citation-ready passages:**

1. **"Scaled the whole lead gen program 5X in 2 years, helping the brand reach #24 on the Inc. 5000 list in 2025"** (Case Studies — iHealthQuotes.com) — Score: 91/100. Direct answer, self-contained, two independent verifiable stats (5X, #24 Inc. 5000), clean structure.
2. **"Grew monthly orders by 36x and reduced cost per order by 2.5x"** across a 30,000+ SKU e-commerce catalog (Case Studies — E-techno) — Score: 91/100. Two stats in one sentence, fully self-contained, industry + scale stated.
3. **"Managed $100,000+/day across six insurance verticals ... scaled the health insurance vertical by 25X"** (Case Studies — Insurance Lead Gen) — Score: 90/100. Highest statistical density on the site; names the exact verticals (Medicare O65, ACA, U65, life, final expense, auto, home).
4. **"Reached operational scale within 90 days"**, full infrastructure built from zero for a mental-health/SUD treatment brand (Case Studies — Riverhouse Wellness) — Score: 82/100. Strong and specific but a single stat, less density than the others.
5. **FAQ answer: "Which industries have you worked in?"** — full vertical list in the schema.org `FAQPage` markup on /services/ — Score: 76/100. Direct Q&A format an AI can lift as-is, but low statistical density.

**Citation-unlikely areas needing improvement:**

- **Client testimonials (About page)** — Score: ~36/100. Five 5-star quotes exist, but every one is attributed only as "LinkedIn recommendation, [month/year]" plus a one-line context tag (e.g. "30 minute consultation") — **no reviewer name, title, or company**. AI systems weigh named, verifiable social proof far more heavily than anonymous quotes; as written these are close to unusable as citations and do little for E-E-A-T.
- **"How I Work" methodology section** (appears on both Home and About, verbatim) — Score: ~50/100. Three good principles ("Start with the goal, not the tactic," "Fix the foundation first," "Then experiment relentlessly") but no supporting numbers or examples tied to them, and the exact duplication across two pages is a missed opportunity rather than two distinct citable passages.
- **Homepage stat strip ("10+ / $100K+ / 5X-36X")** — high scannability but the numbers are stripped of the context that makes them citable (which client, which platform, over what period) — that context only lives on the case-studies page. An AI citing the homepage alone would have to hedge the claim.

---

### AI Crawler Access

| Crawler | Status | Notes |
|---|---|---|
| GPTBot | Allowed | Explicit `Allow: /` block |
| OAI-SearchBot | Unknown → effectively Allowed | Not explicitly named, but inherits `User-agent: * / Allow: /` |
| ChatGPT-User | Allowed | Explicit `Allow: /` block |
| ClaudeBot | Allowed | Explicit `Allow: /` block |
| anthropic-ai | Allowed | Explicit `Allow: /` block |
| PerplexityBot | Allowed | Explicit `Allow: /` block |
| Amazonbot | Unknown → effectively Allowed | Not named, inherits wildcard rule |
| Google-Extended | Allowed | Explicit `Allow: /` block |
| Bytespider | Unknown → effectively Allowed | Not named, inherits wildcard rule |
| CCBot | Unknown → effectively Allowed | Not named, inherits wildcard rule |
| Applebot-Extended | Allowed | Explicit `Allow: /` block |
| FacebookBot | Unknown → effectively Allowed | Not named, inherits wildcard rule |
| Cohere-ai | Unknown → effectively Allowed | Not named, inherits wildcard rule |
| Bingbot | Allowed | Explicit `Allow: /` block (also feeds Bing Copilot) |

**Crawler Access Score: 100/100.** No blocks of any kind. `User-agent: * / Allow: /` covers every crawler not explicitly named, and `Sitemap: https://kseniiashermin.com/sitemap-index.xml` is correctly referenced.

Verified independently in this audit (not just robots.txt):
- **No meta `robots` tags** (noindex/nofollow or otherwise) found in the `<head>` of any of the 6 pages (home, about, case-studies, services, for-employers, contact).
- **No `X-Robots-Tag` HTTP header** on any of the 6 pages — all served via Cloudflare with only standard caching/NEL headers, no crawl-blocking header.
- No `Crawl-delay` directives present (none to slow AI indexing).

**Issues Found:**
- None critical. Minor completeness point: `OAI-SearchBot` and `Amazonbot`/`Bytespider`/`CCBot`/`FacebookBot`/`Cohere-ai` are not individually named — this doesn't currently block anything (wildcard covers them), but naming them explicitly removes any doubt for future robots.txt edits and signals intent clearly to auditors and AI-training-preference scrapers.

**Content Signals:** Absent. No `Content-Signal:` directive found in robots.txt. Recommendation: add one, e.g. `Content-Signal: search=yes, ai-train=yes, ai-personalization=yes, ai-retrieval=yes` at the top of the file (applies to `User-agent: *`), given the stated goal is maximum AI discoverability for a personal-brand/job-search site. See https://contentsignals.org/.

---

### llms.txt Status

**Status:** Present at `/llms.txt` (HTTP 200)
**Score:** 78/100

**What's right:**
- Correct format: H1 site name (`# Kseniia Shermin`), blockquote summary immediately after, `## Pages` section with proper `- [Title](url): Description` markdown links.
- All 6 sitemap URLs are represented with accurate, specific one-line descriptions — the Case Studies line even front-loads the actual stats (5X, 90-day, 25X, 36X), which is exactly what you want an LLM's first read of the site to contain.
- Content matches live page content (no drift detected between llms.txt claims and actual page text).

**What's missing (why it's not 90+):**
1. **No `/llms-full.txt`** (returns 404). For a 6-page site this is a low-cost addition — a single concatenated file with full page text (especially the four case studies and the FAQ) would let models that fetch it skip inference/summarization entirely and quote source text directly.
2. **No `## Optional` section.** Not strictly required, but the spec allows it for secondary resources (e.g. the LinkedIn profile, a resume/PDF if one exists) that shouldn't be prioritized reading but are still worth surfacing.
3. Minor: llms.txt correctly lists "For Employers" but doesn't flag it as the priority page for hiring-manager/recruiter-intent queries — worth a one-line addition since that's a primary business goal of the site (per the site's own stated purpose).

**Fix:** Generate `/llms-full.txt` concatenating full text of all 6 pages (roughly 2,000-3,000 words total based on what was fetched in this audit — small enough to be a single file), add an `## Optional` section linking the verified LinkedIn profile, and re-link to `/llms-full.txt` from `/llms.txt` per spec convention.

---

### Brand Mention Presence

**Brand Authority Score: 15/100**

This is the site's real gap. All on-page technical GEO work (schema, robots.txt, llms.txt) is close to best-practice, but AI models cross-check on-page claims against independent, third-party signals before trusting an entity — and for "Kseniia Shermin" those signals are almost entirely absent outside of one verified but under-surfaced LinkedIn profile.

| Platform | Status | Details |
|---|---|---|
| Wikipedia | Absent | Confirmed via direct MediaWiki API search (`en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Kseniia Shermin`) — 0 results. Expected for a personal-brand/freelance site; not a realistic near-term target, but worth naming as a ceiling on entity-recognition score. |
| Reddit | Absent | No discussion, no subreddit presence, no threads mentioning her by name found via search. |
| YouTube | Absent | No official channel. Search results return only unrelated people sharing the first name "Kseniia" (a dance/nutrition influencer, a Ukrainian war-story subject, etc.) — a namesake-collision problem, not a false negative. |
| LinkedIn | Present, verified, under-surfaced | `https://www.linkedin.com/in/kseniiashermin/` — fetched directly and confirmed: name "Kseniia Shermin," association with "P7 Ventures" visible in the public preview, which matches the site's own About-page career history exactly. This is real, correct, and matches schema.org `sameAs`. However, a plain web search for `"Kseniia Shermin" LinkedIn` does **not** surface this profile in top results — it is currently only reachable by someone who already has the exact URL. |
| Industry Sources | Minimal | One indirect hit: a Luma event listing ("Networking Hike - Marketing Walk & Talk") associated with her name, suggesting some in-person marketing-community activity. No presence found on G2/Trustpilot/Capterra (not directly applicable — she's a solo consultant, not a SaaS product) and no freelancer-directory presence (Clutch, UpCity, MarketerHire, etc.) despite that being a natural fit for the "for-employers"/consulting positioning. |

**Critical name-collision risk found:** A web search for "Sienna Shermin" (the nickname used internally per her own materials, and phonetically close to how "Kseniia" often gets rendered) surfaces a **different, real person** — `linkedin.com/in/siennashermin/`, "Senior PPC Manager" at Noetic Creative, also in paid search/Google & Bing Ads, also healthcare-adjacent. This is a same-name-plus-same-profession collision in her exact niche. If "Sienna Shermin" is ever used publicly (bylines, social handles, press) without the "Kseniia" anchor, AI systems doing entity resolution risk merging or confusing these two people's claims and results. The site itself is safe (it consistently uses "Kseniia Shermin" and correctly links to `/in/kseniiashermin/`), but this is a real external risk worth monitoring and actively countering with consistent naming.

---

### Priority Actions

1. **[HIGH] Fix the LinkedIn discoverability gap.** The verified profile (`linkedin.com/in/kseniiashermin/`) doesn't surface on a plain "Kseniia Shermin LinkedIn" search. Add the full LinkedIn URL as visible, crawlable text (not just an icon link) somewhere on the About and Contact pages, and consider a LinkedIn post or two that includes the exact string "Kseniia Shermin" plus "P7 Ventures" / "iHealthQuotes" / "Performance Marketing Manager" to reinforce the entity link search engines and AI crawlers pick up.
2. **[HIGH] Add full names/titles to testimonials, or at minimum LinkedIn profile links, on the About page.** Five 5-star quotes are currently anonymous ("LinkedIn recommendation, May 2026"). Even first name + last initial + title/company (if permission allows) would move these from citation-unlikely (~36/100) to genuinely citable social proof, and materially strengthens E-E-A-T signals AI models weigh for trust.
3. **[HIGH] Counter the "Sienna Shermin" name-collision risk directly.** Since another real PPC professional (Noetic Creative) is discoverable under a near-identical name in the same field, standardize all public-facing content, bylines, and social profiles on the unique full name "Kseniia Shermin" rather than "Sienna Shermin" alone, and keep the schema.org `Person` `sameAs` array as the single source of truth AI systems can cross-reference to disambiguate.
4. **[MEDIUM] Publish `/llms-full.txt`.** Low effort for a 6-page site — concatenate full page text (the case-studies stat blocks and services FAQ are the highest-value content to include verbatim) so AI crawlers that fetch it can quote directly instead of summarizing.
5. **[MEDIUM] Pursue 1-2 freelancer/industry-directory listings** (Clutch, UpCity, MarketerHire, or a niche PPC/insurance-marketing directory) to build independent third-party corroboration of the case-study claims — this is currently the single biggest lever available to move the Brand Authority Score, since Wikipedia/Reddit/YouTube presence isn't realistic or necessary for this site type.
6. **[LOW] De-duplicate the "How I Work" section** currently repeated verbatim on Home and About — keep the full version on About, shorten/vary the Home version, and consider adding one concrete example or number to each of the 3 principles to lift it out of "vague-methodology" citability territory.
7. **[LOW] Add a `Content-Signal:` directive to robots.txt** (e.g. `Content-Signal: search=yes, ai-train=yes, ai-personalization=yes, ai-retrieval=yes`) — costs nothing, and is an emerging signal some AI crawlers are starting to read as an explicit preference layer on top of robots.txt allow/disallow rules.
