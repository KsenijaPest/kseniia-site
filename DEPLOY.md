# Deploy this site

## What's already built
- 6 pages: Home, For Employers, Services (Work With Me), About, Case Studies, Contact
- JSON-LD schema (Person, ProfessionalService, Service x3, FAQPage) rendered statically
- robots.txt explicitly allowing AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot)
- Sitemap auto-generated on build

## Before you publish, fill in these placeholders (search for "TODO" and "REPLACE_ME" / "FILL IN"):
- `src/pages/index.astro` and `about.astro`: your real LinkedIn and Contra URLs (`sameAs` in schema)
- `src/pages/services.astro`: minimum budget, results timeline, NDA answer, solo/team answer
- `src/pages/case-studies.astro`: real case study data (budgets, actions, results)
- `src/pages/contact.astro`: your real Web3Forms access key (get one free at web3forms.com) and your real Cal.com link
- `astro.config.mjs`: confirm `site:` matches your final domain

## Deploy to Cloudflare Pages (free)
1. Push this project to a GitHub repo (private or public, your choice).
2. In the Cloudflare dashboard: Workers & Pages -> Create -> Pages -> Connect to Git -> select the repo.
3. Build settings:
   - Framework preset: Astro
   - Build command: `npm run build`
   - Build output directory: `dist`
4. Deploy. Cloudflare gives you a free `*.pages.dev` URL immediately.
5. Once `kseniiashermin.com` is purchased in the same Cloudflare account: Pages project -> Custom domains -> Add `kseniiashermin.com`. DNS connects automatically since domain and Pages are in the same account.

## After publishing
1. Submit the sitemap (`https://kseniiashermin.com/sitemap-index.xml`) to Google Search Console and Bing Webmaster Tools.
2. Add GA4, Cloudflare Web Analytics, and a cookie-consent banner (see commented-out placeholder in `src/layouts/Layout.astro`).
3. Set up the Web3Forms and Cal.com accounts referenced above.
