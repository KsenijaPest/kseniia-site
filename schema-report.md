# GEO Schema & Structured Data Report — kseniiashermin.com
Date: 2026-09-02
Pages audited: Home (/), About (/about/), Case Studies (/case-studies/), Services (/services/), For Employers (/for-employers/), Contact (/contact/)
Method: Raw HTML fetched via `fetch_page.py` (no JS execution — matches what AI crawlers like GPTBot/ClaudeBot/PerplexityBot see). Site is built on Astro (`data-astro-cid-*` attributes = static/server-rendered output).

## Schema Score: 53/100 — Fair

| Component | Points Possible | Points Earned | Why |
|---|---|---|---|
| Person/Organization schema present & complete | 15 | 10 | Person present on 2 pages but incomplete (no image, worksFor, alumniOf; About-page version has no sameAs/knowsAbout at all) |
| sameAs links (5+ platforms) | 15 | 3 | Only 1 platform linked (LinkedIn) |
| Article schema with author details | 10 | 0 | No Article/CreativeWork schema anywhere, including case studies |
| Business-type-specific schema (ProfessionalService) | 10 | 5 | Present but missing url, logo, sameAs, @id, address |
| WebSite + SearchAction | 5 | 0 | Absent site-wide |
| BreadcrumbList on inner pages | 5 | 0 | Absent on all 5 inner pages |
| JSON-LD format (not Microdata/RDFa) | 5 | 5 | 100% JSON-LD, no Microdata/RDFa found |
| Server-rendered (not JS-injected) | 10 | 10 | All JSON-LD present in raw HTML response, no JS execution needed |
| speakable property | 5 | 0 | Absent |
| Valid JSON + valid Schema.org types | 10 | 10 | All 7 blocks parse cleanly, all @types are real Schema.org types |
| knowsAbout property | 5 | 5 | Present on homepage Person schema (15 topics) |
| No deprecated schemas present | 5 | 5 | Clean — no HowTo, SpecialAnnouncement, or CourseInfo found |
| **Total** | **100** | **53** | |

---

## Detected Schemas

| Page | Schema Type | Format | Valid | Rich Result Eligible |
|---|---|---|---|---|
| / (Home) | Person | JSON-LD | Yes | N/A (Person doesn't independently trigger rich results, but feeds Knowledge Graph/entity understanding) |
| / (Home) | ProfessionalService | JSON-LD | Yes, but incomplete | No — missing address/telephone/openingHours required for LocalBusiness-family rich results |
| /about/ | Person | JSON-LD | Yes, but minimal | N/A |
| /case-studies/ | — none — | — | — | — |
| /services/ | FAQPage | JSON-LD | Yes | Rich result: **restricted** to govt/health authority sites since Aug 2023 (see note below); still valid for AI parsing |
| /services/ | Service ×3 | JSON-LD | Yes | No dedicated rich result type for generic Service |
| /for-employers/ | — none — | — | — | — |
| /contact/ | — none — | — | — | — |

**Total schema blocks found: 7** (2 on Home, 1 on About, 4 on Services, 0 on Case Studies/For Employers/Contact)
**Format used: 100% JSON-LD.** No Microdata or RDFa detected anywhere on the site.

---

## Validation Results

### Home (/) — Block 1: Person
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Kseniia Shermin",
  "jobTitle": "Performance Marketing Manager",
  "description": "...",
  "url": "https://kseniiashermin.com",
  "sameAs": ["https://www.linkedin.com/in/kseniiashermin/"],
  "knowsAbout": [ /* 15 topics */ ]
}
```
| Property | Status | Value/Issue |
|---|---|---|
| @context | OK | `https://schema.org` |
| @type | OK | `Person` |
| name | OK | "Kseniia Shermin" |
| jobTitle | OK | Present |
| description | OK | Present |
| url | OK | Absolute, matches canonical |
| sameAs | Present but thin | Only 1 URL (LinkedIn). No Wikidata, GitHub, personal-site cross-link, or X/Twitter |
| knowsAbout | OK, strong | 15 well-chosen topics — this is a genuine GEO strength |
| image | **Missing** | An `/kseniia-shermin.jpg` headshot exists on the About page but isn't referenced here |
| worksFor | **Missing** | Should reference the ProfessionalService/Organization entity on the same page |
| @id | **Missing** | No stable identifier for cross-referencing this Person across pages |

**Status: Valid, but incomplete for GEO purposes.**

### Home (/) — Block 2: ProfessionalService
| Property | Status | Value/Issue |
|---|---|---|
| @context / @type | OK | Valid |
| name | OK | "Kseniia Shermin - Performance Marketing" |
| description | OK | Present |
| areaServed | OK | "Worldwide" |
| priceRange | OK | "$$$" |
| url | **Missing** | Required for most rich-result families |
| logo | **Missing** | No logo/headshot referenced |
| sameAs | **Missing** | No LinkedIn/social cross-link on this entity |
| address / telephone | Missing | Expected — this is a remote freelance service, not a physical LocalBusiness, so full address is optional. `PostalAddress` with just `addressCountry` (or omitted entirely) is the right call for a remote consultant; do not fabricate a street address. |
| provider / founder link to Person | **Missing** | Not connected to the Person schema above — these two entities aren't linked, so AI models can't tell "Kseniia Shermin" (Person) and "Kseniia Shermin - Performance Marketing" (ProfessionalService) are the same operator |

**Status: Valid, but the two homepage schemas are disconnected entities.** This is the single biggest structural gap — Person and ProfessionalService should reference each other via `@id`.

### About (/about/) — Person
| Property | Status | Value/Issue |
|---|---|---|
| @context / @type / name / jobTitle / description / url | OK | All valid |
| sameAs | **Missing** | The homepage Person has it, the About-page Person doesn't — inconsistent |
| knowsAbout | **Missing** | Same inconsistency |
| image | **Missing** | About page visibly displays `/kseniia-shermin.jpg` in HTML but it isn't in the schema |

**Status: Valid but duplicate/weaker version of the homepage Person.** Two different Person JSON-LD blocks for the same entity with different completeness levels is a minor conflicting-schema issue — recommend consolidating to one canonical, complete Person block (ideally via `@id` reuse) rather than two partial ones.

### Services (/services/) — FAQPage
5 Questions, each with a proper `acceptedAnswer`/`Answer` pair. **Syntactically and structurally valid — no errors.**

**Google rich-result note:** As of August 2023, Google restricts the FAQ rich result snippet to well-known government and health-authority sites. This site will not get the rich snippet, but the schema still has GEO value — it gives AI models (ChatGPT, Perplexity, AI Overviews) a clean, pre-extracted Q&A pairing they can lift directly into answers about Kseniia's services. **Recommendation: keep it, do not remove.**

### Services (/services/) — Service ×3
All three (`Audit`, `Consultation`, `Ongoing Management`) are valid but each nests `provider` as a bare `{"@type": "Person", "name": "Kseniia Shermin"}` with no `@id`/`url`/`sameAs` — again, disconnected from the fuller Person entity elsewhere on the site.

### Case Studies, For Employers, Contact
**Zero structured data blocks on all three pages.** This is the largest coverage gap, particularly:
- **Case Studies** — page contains four+ quantified results (5X lead-gen growth, #24 Inc. 5000, 90-day scale-up, 25X vertical growth, 36X order growth) with zero machine-readable markup. This is high-value, highly citable proof content that AI models currently have to parse from raw prose.
- **For Employers** — the page explicitly targeting hiring managers has no Person/JobTitle/CV-adjacent markup at all.
- **Contact** — no schema; low priority (contact forms rarely warrant schema), but a `ContactPage`/`ContactPoint` reference would help.

---

## GEO-Critical Schema Assessment

| Schema | Status | GEO Impact | Notes |
|---|---|---|---|
| Person (Kseniia Shermin) | Present, Partial | Critical | Two inconsistent versions across Home/About; missing image, worksFor, @id; sameAs has only 1 platform |
| Organization/ProfessionalService | Present, Partial | Critical | Disconnected from Person; missing url, logo, sameAs, @id |
| Review/Testimonial (About page) | **Missing** | High | 5 testimonials rendered as plain HTML (star rating + quote + context) with zero Review/AggregateRating markup — see detail below |
| FAQPage (Services page) | Present, Valid | Medium (High for AI parsing, Low for Google rich results) | Correctly structured; rich-result eligibility restricted per Google policy, not a site issue |
| Article/CreativeWork (Case Studies) | **Missing** | High | 4+ quantified case-study results with no schema at all |
| BreadcrumbList | **Missing** | Low-Medium | Absent on all 5 inner pages |
| WebSite + sameAs | **Missing** | Medium | No WebSite entity anywhere; no site-level sameAs |
| speakable | Missing | Low-Medium | No content marked for AI/voice extraction |

### Testimonial detail (About page)
Found 5 testimonials in plain HTML (`.testimonial-card`), each with a 5-star rating (`★★★★★`), a quote, and a context label — but **no reviewer names** are shown (only role/context, e.g. "LinkedIn recommendation, November 2024" or "PPC expert for ongoing agency work"). This matters for the generated template below: Schema.org's `Review.author` technically requires a name, and per your own instruction not to invent facts, the templates below use `[FILL IN: reviewer name or "LinkedIn connection"]` placeholders rather than guessing identities. If the underlying LinkedIn recommendations have public names attached, pull them in; otherwise consider whether an anonymized `author` (e.g., "Verified LinkedIn Recommendation") is acceptable, since fabricating names would violate both Schema.org guidelines (reviews should represent real, attributable feedback) and your own no-invented-facts rule.

---

## sameAs Entity Linking

**Current sameAs links found: 1** (LinkedIn, and only on the homepage Person block)

| Platform | Linked | URL |
|---|---|---|
| Wikipedia | No | Not applicable at this career stage — skip |
| Wikidata | No | Not applicable at this career stage — skip |
| LinkedIn | Yes (Home only) | https://www.linkedin.com/in/kseniiashermin/ |
| YouTube | No | Not found — likely N/A |
| Crunchbase | No | Not found — likely N/A for an individual freelancer |
| Twitter/X | No | Not found on site |
| GitHub | No | Not found — worth adding if you have a public GitHub for the AI-agent work mentioned on the About page |
| Cal.com (booking) | Not standard sameAs, but present | https://cal.com/kseniiashermin/15min — worth adding via `ContactPoint`/`potentialAction`, not `sameAs` |

**Assessment:** Weakest part of the site's structured data. A solo consultant's entity graph is realistically built from LinkedIn (already linked) plus whatever else is real and active — GitHub if public, X/Twitter if used professionally, a Google Scholar/Crunchbase-equivalent doesn't apply here. Wikipedia/Wikidata are not realistic for an individual at this stage and should not be forced. **Priority fix: make sure the one real link (LinkedIn) is present consistently on every Person/ProfessionalService block, and add any other genuinely active professional profiles** — do not fabricate placeholder platforms just to hit a count.

---

## Deprecated/Restricted Schemas

| Schema | Status | Recommendation |
|---|---|---|
| FAQPage | Restricted (not deprecated) — rich results limited to govt/health sites since Aug 2023 | **Keep.** Still valid for AI parsing; no harm from having it. |

No deprecated schemas (HowTo, SpecialAnnouncement, CourseInfo) were found. Clean on this front.

---

## JavaScript Rendering Risk

**Schema delivery method: Server-rendered.** All 7 JSON-LD blocks were found in the raw HTML returned by a plain HTTP GET (no JavaScript execution, via `requests`/BeautifulSoup) — the same access pattern used by GPTBot, ClaudeBot, and PerplexityBot, none of which execute JavaScript. This confirms the site is statically generated (Astro build output, evidenced by `data-astro-cid-*` attributes) and **all current schema is fully visible to AI crawlers with zero delay risk.** This is a genuine strength — whatever gaps exist are about coverage/completeness, not delivery risk.

---

## Recommended JSON-LD Templates

### 1. Unified Person schema — HIGHEST PRIORITY
Replace both the Home and About Person blocks with this single, complete version (same content on both pages, using `@id` so they're recognized as the same entity). This fixes the missing image, sameAs consistency, and links to the ProfessionalService entity.

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
  "worksFor": {
    "@id": "https://kseniiashermin.com/#professionalservice"
  },
  "sameAs": [
    "https://www.linkedin.com/in/kseniiashermin/"
    ,"[FILL IN: GitHub profile URL, if public]"
    ,"[FILL IN: X/Twitter profile URL, if actively used professionally]"
  ],
  "knowsAbout": [
    "Google Ads",
    "Microsoft Ads",
    "Meta Ads",
    "Paid Search",
    "PPC",
    "SEM",
    "Health Insurance (ACA)",
    "Health Insurance (U65)",
    "Medicare (O65)",
    "Life & Final Expense Insurance",
    "Auto & Home Insurance",
    "Mental Health & Behavioral Health Treatment",
    "Telecom & Internet Service Providers",
    "E-commerce (Home Appliances & Consumer Goods)",
    "B2B SaaS",
    "AI Agents for Marketing Operations"
  ]
}
```
**Implementation:** Place on Home and About (and ideally For Employers) inside `<script type="application/ld+json">` in `<head>`. Remove `[FILL IN]` lines entirely if the profile doesn't exist rather than leaving a placeholder live.

### 2. Enhanced ProfessionalService — linked to Person — HIGH PRIORITY
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
  "founder": {
    "@id": "https://kseniiashermin.com/#person"
  },
  "provider": {
    "@id": "https://kseniiashermin.com/#person"
  },
  "sameAs": [
    "https://www.linkedin.com/in/kseniiashermin/"
  ]
}
```
Note: Deliberately omitting `address`/`telephone` — this is a remote consultancy, and fabricating a physical address or phone number would violate the "never invent facts" rule. If there's a business phone/email meant to be public, add it via `ContactPoint`; otherwise leave it out.

### 3. WebSite schema (Home page) — MEDIUM PRIORITY
No on-site search exists, so `SearchAction`/`potentialAction` is omitted rather than fabricated — add it only if a search feature is ever built.
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://kseniiashermin.com/#website",
  "url": "https://kseniiashermin.com",
  "name": "Kseniia Shermin",
  "description": "Performance Marketing Manager — lead generation at scale across Google Ads, Microsoft Ads, and Meta Ads.",
  "publisher": {
    "@id": "https://kseniiashermin.com/#person"
  },
  "inLanguage": "en-US"
}
```

### 4. BreadcrumbList — one per inner page — MEDIUM PRIORITY
Example for /case-studies/ (repeat the pattern for /about/, /services/, /for-employers/, /contact/, adjusting `name`/`item`):
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://kseniiashermin.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Case Studies",
      "item": "https://kseniiashermin.com/case-studies/"
    }
  ]
}
```

### 5. Review schema for testimonials (About page) — HIGH PRIORITY
Modeled as reviews of the ProfessionalService entity. Reviewer names are placeholders since none are shown on the page — fill in real names only if you have permission to publish them (LinkedIn recommendations typically do show the recommender's name on LinkedIn itself, so these can likely be pulled in accurately rather than left blank).
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@id": "https://kseniiashermin.com/#professionalservice"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "5",
    "bestRating": "5"
  },
  "author": {
    "@type": "Person",
    "name": "[FILL IN: reviewer name from LinkedIn recommendation, Nov 2024]"
  },
  "reviewBody": "Meeting Kseniia was a great pleasure. She's extremely knowledgeable...[FILL IN: full quote text]",
  "datePublished": "2024-11-01"
}
```
Repeat for each of the 5 testimonials (adjust `datePublished` to `2026-05` for the May 2026 recommendation; for the three testimonials without dates/names, either source the missing name/date or represent them without a `Review` wrapper — an unattributed star rating alone doesn't meet Schema.org's intent for `Review.author`). Wrap all 5 in an `AggregateRating` on the ProfessionalService entity once compiled:
```json
{
  "@type": "AggregateRating",
  "ratingValue": "5",
  "reviewCount": "5",
  "bestRating": "5"
}
```
(add this as an `aggregateRating` property on the ProfessionalService block from template #2, only once real review count/value is confirmed).

### 6. Article/CreativeWork per case study — HIGH PRIORITY
Case studies aren't blog-style articles, so a straight `Article` type is a slight mismatch — this uses `Article` anyway since it's the type both Google and AI platforms parse most reliably for "written, attributed, dated content with a headline and result." Example for the iHealthQuotes.com case study; replicate for the other 3+ case studies on the page:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "5X Lead Gen Growth in 2 Years — Health Insurance (iHealthQuotes.com)",
  "author": {
    "@id": "https://kseniiashermin.com/#person"
  },
  "publisher": {
    "@id": "https://kseniiashermin.com/#professionalservice"
  },
  "about": "Health Insurance Paid Search Lead Generation",
  "description": "As Director of Marketing at P7 Ventures, led multi-channel paid search strategy for this health insurance brand, scaling the lead gen program 5X in 2 years and helping the brand reach #24 on the Inc. 5000 list in 2025.",
  "mainEntityOfPage": "https://kseniiashermin.com/case-studies/",
  "datePublished": "[FILL IN: date this case study was added/last updated]",
  "dateModified": "[FILL IN: last update date]",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".result-stat", ".case-study-result"]
  }
}
```
**Implementation note:** `datePublished`/`dateModified` are required for Article schema but no dates currently exist on the case-studies page in visible content — add real dates rather than fabricating them (per your no-invented-facts rule), even if that means adding a visible "Last updated" line to the page first.

---

## Implementation Notes

- Place all JSON-LD in `<head>` inside `<script type="application/ld+json">` tags — this site is already server-rendered (Astro), so there's no JS-injection risk to worry about; keep it that way.
- Consolidate the Home and About Person blocks into the single `@id`-based version (Template #1) to remove the current inconsistency (About page's Person is missing sameAs/knowsAbout/image that Home's has).
- Link Person ↔ ProfessionalService via `@id` references (Templates #1 and #2) — this is the fix with the single biggest structural payoff, since right now AI models see two disconnected "Kseniia Shermin" entities on the same domain.
- Do not fabricate: physical address, phone number, reviewer names/dates you don't have, or case-study publish dates that don't exist yet. Every `[FILL IN: ...]` placeholder above should be replaced with a real value or the property dropped.
- After implementation, validate with Google's Rich Results Test (https://search.google.com/test/rich-results) and Schema.org Validator (https://validator.schema.org/) — expect FAQPage to pass validation but show "not eligible" for the rich-result feature specifically, which is expected per Google's 2023 policy change, not an error.

---

## Priority Actions

1. **[CRITICAL]** Consolidate Person schema to one complete `@id`-based entity (Template #1) used consistently on Home, About, and For Employers — currently two inconsistent partial versions exist.
2. **[CRITICAL]** Link the Person and ProfessionalService schemas together via `@id` (Templates #1 + #2) so AI models recognize them as the same operator, not two disconnected entities.
3. **[HIGH]** Add Review schema for the 5 About-page testimonials, sourcing real reviewer names from the underlying LinkedIn recommendations rather than leaving them anonymous (Template #5).
4. **[HIGH]** Add Article schema to each Case Studies entry — this is the site's strongest citable proof content (5X, 25X, 36X, #24 Inc. 5000) and currently has zero machine-readable markup (Template #6).
5. **[MEDIUM]** Add WebSite schema to the homepage and BreadcrumbList to all 5 inner pages (Templates #3, #4).
6. **[LOW]** Expand sameAs beyond LinkedIn only if there's a genuinely active GitHub or X/Twitter profile — do not add platforms that don't exist.
