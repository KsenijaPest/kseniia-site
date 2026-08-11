# Project: kseniiashermin.com — Personal site for a Performance Marketing Manager

## Context
This is an Astro static site for Kseniia Shermin, a Performance Marketing Manager
(10+ years, paid search + paid social, lead gen focus). The site serves two
audiences at once: hiring managers (full-time roles) and consulting clients
(audits, consultations, account management). Domain `kseniiashermin.com` is
already purchased via Cloudflare Registrar.

The project skeleton (layout, 6 pages, JSON-LD schema, robots.txt, sitemap
integration) already exists in this repo. Do not rebuild it from scratch —
extend and finish it.

## Non-negotiable technical requirements
1. **Everything must be statically rendered.** No content that only appears
   after client-side JS runs. This site is optimized for both traditional
   SEO and AI/LLM crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended),
   most of which do not execute JavaScript. Verify with `npx astro build`
   and grep the output HTML for any content that should be there.
2. **JSON-LD schema stays in sync with visible content.** If you edit a page's
   text, update its schema to match. Don't let them drift apart.
3. **Never invent facts.** Case study numbers, testimonials, certifications,
   and FAQ answers (minimum budget, results timeline, NDA policy) must come
   from Kseniia directly. Where a value is genuinely unknown, leave the
   `[FILL IN: ...]` placeholder in place and flag it in your summary at the
   end of the session, do not guess a plausible-sounding number.
4. **Keep the tone direct and specific, no filler.** No em dashes anywhere
   in any copy you write or edit, use commas, periods, or restructure the
   sentence instead. This applies to all text on the site, not just body copy.

## Priority-ordered task list

### P0 — Get it live
- [ ] Confirm `astro.config.mjs` `site:` value matches `https://kseniiashermin.com`
- [ ] Initialize a git repo if one doesn't exist, push to GitHub (ask Kseniia
      whether the repo should be public or private if not already decided)
- [ ] Walk through connecting the GitHub repo to Cloudflare Pages
      (Workers & Pages -> Create -> Pages -> Connect to Git). Build command
      `npm run build`, output directory `dist`, framework preset Astro.
- [ ] Add `kseniiashermin.com` as a custom domain on the Cloudflare Pages
      project (domain and Pages project are in the same Cloudflare account,
      so this should be a few clicks, not manual DNS).
- [ ] Verify the live site loads over HTTPS on the custom domain.

### P1 — Fill remaining placeholders (ask Kseniia for anything you don't have)
Search the repo for `TODO`, `REPLACE_ME`, and `FILL IN`, every instance
needs a real value before this is genuinely done. Known gaps as of this
handoff:
- [ ] Real LinkedIn and Contra URLs in `sameAs` schema fields
      (`src/pages/index.astro`, `src/pages/about.astro`)
- [ ] FAQ answers in `src/pages/services.astro`: minimum budget, results
      timeline, NDA policy, solo-vs-team answer
- [ ] Case study data in `src/pages/case-studies.astro`: real budgets,
      actions taken, results, and whether client/company names can be
      shown or need to stay as vertical labels only (health insurance,
      iHealthQuotes, mental health)
- [ ] Web3Forms access key in `src/pages/contact.astro` (free account at
      web3forms.com), test that a real submission actually arrives by email
- [ ] Real Cal.com booking link in `src/pages/contact.astro`
- [ ] Google Ads / Microsoft Advertising certification badges on the About
      page, if Kseniia has current ones

### P2 — Analytics and consent
- [ ] Add Cloudflare Web Analytics (cookie-free, no consent banner required,
      safe to add immediately), snippet placeholder is already commented
      out in `src/layouts/Layout.astro`
- [ ] Add GA4 and Microsoft Clarity, but gate both behind a cookie-consent
      banner (they use cookies, GDPR applies for EU/UK visitors). Use a
      lightweight open-source consent banner, default to declined/opted-out
      until the visitor accepts, per privacy-by-default.
- [ ] Set up Google Search Console and Bing Webmaster Tools, verify
      ownership, submit `https://kseniiashermin.com/sitemap-index.xml` to both.

### P3 — Content and polish
- [ ] Populate the blog section referenced in the site plan, starting with
      the 6 topics already drafted with Kseniia (ask her for the current
      list if not present in this repo)
- [ ] Replace placeholder reviews section on the About page once Kseniia
      has collected real LinkedIn recommendations / Upwork reviews, do not
      draft placeholder quotes attributed to real platforms
- [ ] Run a Lighthouse/PageSpeed pass, fix any Core Web Vitals issues,
      especially image weight on case study screenshots
- [ ] Add alt text to every image
- [ ] Double check heading hierarchy (one H1 per page) and that FAQ sections
      use question-phrased headings site-wide, not just on the Services page

### P4 — Nice to have, not blocking launch
- [ ] Add an `llms.txt` file at the site root summarizing key pages. Low
      confirmed impact as of mid-2026 (most major crawlers don't use it yet),
      treat as a cheap afterthought, not a priority.

## Working style
- Work through tasks in priority order (P0 before P1, etc.), but don't
  block on missing content, skip an item needing Kseniia's input and come
  back to it, rather than stalling the whole session.
- At the end of each session, summarize: what got done, what's still
  blocked on missing information from Kseniia, and any decisions you made
  that she should sanity-check.