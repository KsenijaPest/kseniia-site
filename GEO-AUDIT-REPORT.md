# GEO + SEO Audit — kseniiashermin.com

**Date:** September 2, 2026
**Site type:** Personal brand / consultant portfolio (Kseniia "Sienna" Shermin, freelance Performance Marketing Manager)
**Pages audited:** 6 of 6 (Home, About, Case Studies, Services, For Employers, Contact)

---

## Composite GEO Score: 61 / 100 (Fair, leaning Good)

| Category | Weight | Score | Weighted |
|---|---|---|---|
| AI Citability & Visibility | 25% | 88 | 22.0 |
| Brand Authority Signals | 20% | 15 | 3.0 |
| Content Quality & E-E-A-T | 20% | 60 | 12.0 |
| Technical Foundations | 15% | 86 | 12.9 |
| Structured Data | 10% | 53 | 5.3 |
| Platform Optimization | 10% | 56 | 5.6 |
| **Composite** | | | **60.8 → 61** |

**The pattern:** everything the site controls directly (technical setup, on-page schema, content quality, citability of the actual copy) is good-to-excellent. The score is pulled down almost entirely by one thing outside the page itself — **third-party brand authority is nearly absent.** No Wikipedia, no Reddit, no YouTube, and the one real signal that exists (a verified LinkedIn profile) doesn't surface on a plain name search. There's also a name-collision risk worth acting on directly (see below).

This is a good problem to have: the fixes are mostly additive (add dates, link testimonials, publish a privacy page, expand `sameAs`) rather than structural rebuilds. Nothing found blocks AI crawlers or hides content from them.

---

## What's already working well

- **robots.txt explicitly allow-lists every major AI crawler by name** — GPTBot, ChatGPT-User, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot — on top of a wildcard `Allow: /`. Most sites don't do this.
- **llms.txt already exists and is well-formed** (correct format, all 6 pages linked with accurate, stat-forward descriptions).
- **Fully server-rendered (Astro static build)** — every page ships complete text in the raw HTML before any JS runs, so AI crawlers that don't execute JavaScript see exactly what a human sees. This is the single strongest technical asset on the site.
- **Case studies are genuinely citation-ready.** The stat-callout format ("Grew monthly orders by 36x and reduced cost per order by 2.5x," "#24 on the Inc. 5000 list") is close to the ideal shape AI answer engines lift verbatim. Citability scored 86/100 — the best-performing category on the whole site.
- **Person + ProfessionalService + FAQPage JSON-LD schema is already implemented** on Home/About/Services — not every consultant site bothers with this at all.
- **Voice is authentically human and specific** — named clients, real tools, hard numbers, no AI-boilerplate phrasing, no em dashes. Matches your own writing standard.

---

## The five biggest gaps, in priority order

### 1. [CRITICAL] No privacy policy, despite an active data-collecting contact form
`/contact/` collects name, email, budget, and free text. `/privacy-policy` returns a 404, and there's no privacy or terms page anywhere on the site. This is the single biggest trust gap found — fix it before anything else on this list.

### 2. [CRITICAL] Brand authority is the real ceiling on the score
- Wikipedia, Reddit, YouTube: confirmed absent (checked directly, not just assumed).
- Your verified LinkedIn profile (`linkedin.com/in/kseniiashermin/`) is real and matches your site's career history exactly — but it does **not** surface in a plain "Kseniia Shermin LinkedIn" search. It's only reachable if someone already has the URL.
- **Name-collision risk:** searching "Sienna Shermin" surfaces a *different* real person — a Senior PPC Manager at Noetic Creative, same profession, healthcare-adjacent. Same name, same niche. Worth actively standardizing on "Kseniia Shermin" (not "Sienna") in every public-facing byline, social profile, and piece of content going forward, so AI entity-resolution doesn't conflate the two of you.
- Fix: make the LinkedIn profile independently discoverable (link it as visible crawlable text, not just an icon, on About and Contact), and consider 1–2 freelancer/industry directory listings (Clutch, UpCity, MarketerHire) — currently your only realistic lever to move this score, since Wikipedia/Reddit presence isn't a near-term target for a solo consultant site.

### 3. [HIGH] Testimonials are anonymous — and it's costing you on two fronts
Five 5-star testimonials on `/about/` are attributed only as "LinkedIn recommendation, [month/year]" with no reviewer name or title. This scores ~36/100 for citability (AI systems weigh named social proof far more than anonymous quotes) and blocks proper Review schema markup. If the underlying LinkedIn recommendations show real names (they typically do), pull them in.

### 4. [HIGH] Structured data exists but isn't connected or complete
Person and ProfessionalService schema are on the site, but they're **disconnected entities** — nothing tells an AI model that "Kseniia Shermin" (Person) and "Kseniia Shermin - Performance Marketing" (ProfessionalService) are the same operator. The About-page Person block is also a thinner, inconsistent duplicate of the Home version. Case Studies, For Employers, and Contact carry zero schema — meaning your strongest proof content (5X, 25X, 36X, #24 Inc. 5000) has no machine-readable markup at all. Ready-to-use JSON-LD templates for all of this are in the [Structured Data Detail](#structured-data-detail) section below.

### 5. [HIGH] No certifications listed, despite 10+ years of platform expertise
Nothing on the site names a Google Ads or Microsoft Advertising certification. This is a free, easy, independently verifiable trust signal that's currently missing entirely.

---

## Full category breakdowns

### AI Citability & Visibility — 88/100 (component scores: Citability 86, Crawler Access 100, llms.txt 78)
The case-studies page is near-ideal AI-citation format (stat callout + Context/Platforms/What I did/Result). Weakest citability spot: testimonials (~36/100, anonymous) and the "How I Work" section duplicated verbatim on Home and About with no supporting numbers. llms.txt is solid but missing an `/llms-full.txt` companion for a 6-page site this size.

### Brand Authority Signals — 15/100
Covered above — this is the score to focus on. See the full findings in `ai-visibility-report.md` (saved alongside this report) for the complete platform-by-platform breakdown.

### Content Quality & E-E-A-T — 60/100
| Dimension | Score /25 |
|---|---|
| Experience | 18 |
| Expertise | 16 |
| Authoritativeness | 9 |
| Trustworthiness | 13 |

Experience and voice are strong (real named clients — iHealthQuotes.com, Riverhouse Wellness, E-techno; real tools — n8n, Power BI, Tableau, CallTrackingMetrics; correct, nuanced industry terminology). Authoritativeness and Trustworthiness are the weak dimensions: no external citations/press/awards, the missing privacy policy, no direct email/phone on Contact, and each case study is only ~150 words — strong specifics but not enough elaboration to fully substantiate its own headline numbers (36X, 25X). Also flagged: no content anywhere addresses regulatory/compliance fluency in health insurance and mental health advertising, despite those being named specialty verticals with real regulatory complexity — a specific, addressable authority gap.

### Technical Foundations — 86/100
Excellent SSR (100/100 — full text in raw HTML, no JS dependency), strong meta tags and crawlability (92/100, 90/100). The one real weak point: **security headers (45/100)** — `http://kseniiashermin.com/` doesn't redirect to HTTPS (serves the identical page over plain HTTP), and HSTS/CSP/X-Frame-Options/etc. are all absent. Everything's on Cloudflare, so these are dashboard config changes, not code changes. Also: the homepage hero photo is an unoptimized 800×800 native iPhone JPEG displayed at 140px — a quick LCP win via Astro's built-in Image component.

### Structured Data — 53/100
Detailed above and in the templates section. Bottom line: what's there is valid JSON-LD, server-rendered, zero delivery risk — it just needs to be consolidated (one Person entity, not two inconsistent ones), connected (`@id` links between Person and ProfessionalService), and extended to Case Studies (Article schema) and About (Review schema for testimonials).

### Platform Optimization — 56/100
| Platform | Score |
|---|---|
| Bing Copilot | 75 |
| Google AI Overviews | 58 |
| ChatGPT Web Search | 58 |
| Perplexity | 56 |
| Google Gemini | 33 |

Bing Copilot is strongest (Bing Webmaster Tools verified, deep Microsoft Ads content, /for-employers/ already reads like a direct answer to "should I hire her" queries). Gemini is weakest — no YouTube presence, and the `sameAs` schema that feeds Google's Knowledge Graph is thin and inconsistent across pages. One fix (consistent, expanded `sameAs`) helps ChatGPT, Gemini, and Perplexity simultaneously.

---

## Prioritized Action Plan

**Do first (high impact, low effort):**
1. Publish a privacy policy and link it in the footer — closes the biggest trust/compliance gap on the site.
2. Add real names/titles to the 5 About-page testimonials (or link to the source LinkedIn posts) if permission allows.
3. Consolidate Person schema into one `@id`-based entity used consistently on Home/About/For Employers, and link it to ProfessionalService via `@id` (templates below).
4. Make the LinkedIn profile independently discoverable — visible crawlable link text on About and Contact, not just an icon.
5. Enable Cloudflare "Always Use HTTPS" + HSTS, and add the missing security headers via Transform Rules — a same-session dashboard fix.
6. List any real Google Ads / Microsoft Advertising certifications you hold; if none current, that's fine to skip rather than invent.

**Do next (medium impact):**
7. Add Article schema to each case study, and hyperlink the "#24 on the Inc. 5000 (2025)" claim to its actual source.
8. Add a consistent, expanded `sameAs` array (LinkedIn + any other genuinely active professional profiles) to every Person schema block — single biggest lever for ChatGPT/Gemini/Perplexity entity recognition.
9. Add visible "Updated: [month year]" dates to Home, About, and For Employers (already done on Services and Case Studies).
10. Compress/resize the hero photo via Astro's Image component.
11. Publish `/llms-full.txt` with full page text (case studies + FAQ especially) — low effort for a 6-page site.
12. Standardize public naming on "Kseniia Shermin" (not "Sienna") to counter the name-collision with a different PPC professional under a near-identical name.

**Lower priority / longer-term:**
13. Pursue 1–2 freelancer/industry directory listings (Clutch, UpCity, MarketerHire) for independent third-party corroboration.
14. Consider a short YouTube video (methodology walkthrough or case study explainer) — the single highest-impact fix available for Gemini specifically.
15. Add a comparison table to /services/ (Audit vs. Consultation vs. Account Management) for AI Overview extraction.
16. Add content addressing regulatory/compliance fluency in health insurance and mental health advertising — a specific, ownable authority gap.
17. Add WebSite schema + BreadcrumbList to inner pages.
18. Fix the placeholder Cloudflare Analytics token (`REPLACE_ME`) — not SEO, but analytics currently aren't being collected.

---

## Structured Data Detail

Ready-to-use JSON-LD (full versions and 4 more templates in `schema-report.md`, saved alongside this file). The two below are the highest-priority fixes — they consolidate and connect your existing Person/ProfessionalService schema.

**1. Unified Person schema** (replace both Home and About versions):
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://kseniiashermin.com/#person",
  "name": "Kseniia Shermin",
  "jobTitle": "Performance Marketing Manager",
  "description": "Performance Marketing Manager with 10+ years of experience in paid search and paid social, specializing in lead generation at scale across Google Ads, Microsoft Ads, and Meta Ads.",
  "url": "https://kseniiashermin.com",
  "image": "https://kseniiashermin.com/kseniia-shermin.jpg",
  "worksFor": { "@id": "https://kseniiashermin.com/#professionalservice" },
  "sameAs": [
    "https://www.linkedin.com/in/kseniiashermin/"
  ],
  "knowsAbout": [
    "Google Ads", "Microsoft Ads", "Meta Ads", "Paid Search", "PPC", "SEM",
    "Health Insurance (ACA)", "Health Insurance (U65)", "Medicare (O65)",
    "Life & Final Expense Insurance", "Auto & Home Insurance",
    "Mental Health & Behavioral Health Treatment",
    "Telecom & Internet Service Providers",
    "E-commerce (Home Appliances & Consumer Goods)", "B2B SaaS"
  ]
}
```

**2. Enhanced ProfessionalService, linked to Person:**
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://kseniiashermin.com/#professionalservice",
  "name": "Kseniia Shermin - Performance Marketing",
  "url": "https://kseniiashermin.com",
  "description": "Lead generation focused paid search and paid social consulting for B2C, B2B, and service businesses. Google Ads, Microsoft Ads, and Meta Ads audits, consultations, and account management.",
  "image": "https://kseniiashermin.com/kseniia-shermin.jpg",
  "areaServed": "Worldwide",
  "priceRange": "$$$",
  "founder": { "@id": "https://kseniiashermin.com/#person" },
  "provider": { "@id": "https://kseniiashermin.com/#person" },
  "sameAs": [
    "https://www.linkedin.com/in/kseniiashermin/"
  ]
}
```

Note: physical address/phone deliberately omitted — this is a remote consultancy, and neither exists to report. Do not add placeholder values for these.

Full templates for Review/testimonial schema, Article schema per case study, WebSite schema, and BreadcrumbList are in `schema-report.md`.

---

## Supporting detail files
Full per-category subagent reports (with complete evidence, page-by-page findings, and additional recommendations) are saved alongside this report in the same folder:
- `ai-visibility-report.md` — citability, crawler access, llms.txt, brand mentions
- `platform-report.md` — per-platform (Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot) breakdown
- `technical-report.md` — full technical SEO audit
- `content-report.md` — E-E-A-T and content quality detail
- `schema-report.md` — complete structured data audit + all JSON-LD templates
