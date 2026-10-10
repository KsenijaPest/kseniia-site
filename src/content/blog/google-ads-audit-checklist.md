---
title: "Google Ads and Microsoft Ads Audit Checklist (2026)"
description: "A 12-point checklist for auditing a Google Ads or Microsoft Ads account in 2026, from conversion tracking to AI Max and competitors, with red flags for each check."
publishDate: 2026-10-09
image: "/blog/google-ads-audit-checklist/og-audit-checklist.png"
faq:
  - q: "What does a Google Ads audit include?"
    a: "A Google Ads audit reviews twelve areas: conversion tracking, account settings and structure, campaign settings, keywords and search terms, ads and ad extensions (assets), Quality Score, landing pages, performance metrics, audience targeting, budget and bidding, change history, and competitors."
  - q: "What should you check first in a Google Ads audit?"
    a: "Conversion tracking. Bidding systems optimize toward whatever the account counts as a conversion, so if tracking is wrong, every other finding rests on unreliable data."
  - q: "How do you audit search terms when AI Max or Performance Max is on?"
    a: "Use the search terms report for both. For AI Max, filter the Match type column by AI Max to see the queries it added. Performance Max has its own search terms report. Add irrelevant terms as negatives, and use brand exclusions and URL exclusions where they fit."
  - q: "Is a Microsoft Ads audit different from a Google Ads audit?"
    a: "The checks are mostly the same. Check whether a scheduled import from Google Ads is running, because depending on its options it can overwrite changes made directly in Microsoft Ads, and review imported settings and the quality of the traffic."
  - q: "What do I need to give someone who audits my ad account?"
    a: "Access to the advertising account. Implementation of the findings is discussed separately."
---

A Google Ads or Microsoft Ads audit reviews twelve areas: conversion tracking, account settings and structure, campaign settings, keywords and search terms, ads and ad extensions (assets), Quality Score, landing pages, performance metrics, audience targeting, budget and bidding, change history, and competitors. Conversion tracking comes first, because every other finding depends on whether the data can be trusted.

This checklist works for accounts of any size and any goal, whether the account drives leads, sales, or calls. It is updated for how both platforms work in 2026, including AI Max for Search, Performance Max search terms, and enhanced conversions. Each section lists what to check and what usually signals a problem.

## The checklist at a glance

1. **Conversion tracking:** only meaningful actions counted, enhanced conversions and consent set up.
2. **Account settings and structure:** auto-applied recommendations reviewed, campaigns organized logically.
3. **Campaign settings:** locations, networks, bidding, AI Max, and campaign overlap.
4. **Keywords and search terms:** relevance, match types, negatives, AI Max and Performance Max queries.
5. **Ads and ad extensions (assets):** ad strength, asset performance, automatically created assets.
6. **Quality Score:** expected CTR, ad relevance, and landing page experience per keyword.
7. **Landing pages:** relevance, speed, mobile, clear call to action.
8. **Performance metrics:** CTR, CPC, conversion rate, cost per conversion, ROAS or cost per lead, trends.
9. **Audience targeting:** observation vs targeting, remarketing and customer lists.
10. **Budget and bid strategy:** budget goes where results come from, lost impression share.
11. **Change history:** what changed, who changed it, including auto-applied changes.
12. **Competitors:** auction insights.

![The 12-point paid search audit checklist: conversion tracking first, then settings and structure, campaign settings, keywords and match types, ads and extensions, Quality Score, landing pages, performance metrics, audience targeting, budget and bidding, change history, and competitors](/blog/google-ads-audit-checklist/01-audit-checklist.svg)

## 1. Is conversion tracking set up correctly?

Bidding systems optimize toward whatever the account counts as a conversion. If the wrong actions are counted, the account gets better at the wrong thing.

| Check | What good looks like | Red flag |
|---|---|---|
| Types of conversions | Actions that matter to the business, such as purchases, form submissions, and qualified calls | Page views or clicks counted as conversions |
| Meaningful metrics | Conversion numbers match what the business actually receives | Many reported conversions, few real customers |
| Duplicates and conversion window | Each lead or sale is counted once, and the window fits the buying cycle | Double counting, or a window shorter than the sales cycle |
| Enhanced conversions | Turned on and sending data | Off, so conversions that cookies alone miss are not measured |
| Consent mode | Set up where consent is required, with all required signals passed | Conversions drop for visitors who decline cookies and nobody knows why |
| Offline conversions | Sales or qualified leads from the CRM imported back when the sale happens offline | The platform optimizes to form fills it cannot tell apart |
| Attribution model | A deliberate choice between data-driven and last click | Nobody knows which model the account uses |

## 2. Are account settings and structure organized logically?

| Check | What good looks like | Red flag |
|---|---|---|
| Auto-applied recommendations | Each auto-applied type is a deliberate choice, and the History tab is reviewed | Recommendations changing keywords, assets, or bidding with nobody reviewing them |
| Account-level controls | Account-level negative keywords and brand lists in place where needed | The same exclusions copied by hand into every campaign, or missing |
| Campaigns and ad groups | Clear split by product, intent, or location | Different offers mixed in one campaign |
| Keyword grouping within ad groups | Tight themes, so ads can match the keywords | Unrelated keywords sharing the same ads |

## 3. Are campaign settings correct?

| Check | What good looks like | Red flag |
|---|---|---|
| Locations and languages | Match the real service area and customers, with the location option ("presence" or "presence or interest") chosen on purpose | People outside the target area trigger ads |
| Networks | Search, Search Partners, Display, and YouTube are on only when intended | Networks left on by default |
| Bidding strategy | Fits the goal and the amount of conversion data | An automated target set with very little data behind it |
| Bid limits | Any limits are still sensible | Old limits holding back good traffic |
| AI Max and broad match settings | You know which campaigns use AI Max or campaign-level broad match, and why | AI Max running without anyone checking the queries it adds |
| Campaign overlap | Search and Performance Max campaigns do not compete for the same queries without a reason, and brand exclusions are used where needed | Performance Max taking brand searches meant for a brand Search campaign |

## 4. Are keywords, match types, and search terms working?

| Check | What good looks like | Red flag |
|---|---|---|
| Keyword relevance to ads | The ad text reflects the keywords in the group | Generic ads for specific keywords |
| Irrelevant or low-performing keywords | Found and handled | Spend going to terms that never convert |
| Match types | Chosen on purpose | Broad and phrase match without a solid negative list |
| Negative keywords | Layered lists that stay current | None, or lists nobody updated in a long time |
| Search terms report | Real queries reviewed, good ones added as keywords, bad ones as negatives | Report never opened |
| AI Max and Performance Max queries | AI Max terms reviewed by filtering the Match type column, Performance Max search terms reviewed in its own report | Only keyword-matched terms reviewed, while AI-matched spend grows |

## 5. Do the ads and ad extensions (assets) do their job?

Google now calls ad extensions "assets". They are the extra parts of the ad, such as sitelinks, callouts, calls, and structured snippets.

| Check | What good looks like | Red flag |
|---|---|---|
| Ad copy quality | Relevant, compelling headlines and descriptions | Generic copy that could belong to any advertiser |
| Responsive search ads | Ad strength and asset performance ratings reviewed, weak assets replaced, pinning used only when needed | Low-rated assets left running for months |
| Automatically created assets | Turned on or off on purpose, with generated text checked against brand and policy rules | Generated headlines making claims the business would not make |
| Ad extensions (assets) | Every useful type is set up and approved | Missing or disapproved assets |

## 6. What does Quality Score show?

Quality Score is a 1 to 10 diagnostic for each keyword in Google Ads and Microsoft Ads. It summarizes expected click-through rate, ad relevance, and landing page experience. It is a diagnostic, not a direct input into the auction.

| Check | What good looks like | Red flag |
|---|---|---|
| Quality Score by keyword | Reviewed regularly, with the three components visible as columns | Never looked at |
| Low-scoring keywords | Listed with the weak component identified | Low scores ignored |

## 7. Do the landing pages match the ads?

| Check | What good looks like | Red flag |
|---|---|---|
| Relevance | The page delivers what the keyword and ad promise | Ad promises one thing, the page shows another |
| Speed and appearance | Loads fast and looks right on desktop and mobile. Test it with [PageSpeed Insights](https://pagespeed.web.dev/) | Slow load or a broken mobile layout |
| Calls to action | One clear next step | The button or form is hard to find |
| Landing pages report | Reviewed for pages the platform chose on its own | AI Max or Performance Max sending traffic to pages that should not get it |

## 8. What do the performance metrics say?

| Check | What good looks like | Red flag |
|---|---|---|
| Key metrics | CTR, CPC, conversion rate, cost per conversion, and ROAS (or cost per lead) reviewed together | Judging the account on one metric |
| Trends and sudden changes | The cause of each shift is known | Unexplained drops or spikes |

## 9. Is audience targeting used well?

| Check | What good looks like | Red flag |
|---|---|---|
| Observation vs targeting | Audiences on Search added as observation unless narrowing reach is intended | Targeting mode set by accident, cutting reach |
| Audience types | Demographics, affinity, in-market, remarketing, and customer lists used where they help | Audiences added and never checked |
| Audience performance | Segments compared | Decisions made without audience data |

## 10. Are budget and bid strategy effective?

| Check | What good looks like | Red flag |
|---|---|---|
| Budget across campaigns | Money goes where results come from | The best campaigns are limited by budget while weak ones are not |
| Lost impression share | Search impression share lost to budget and to rank both reviewed | High loss to budget on campaigns that hit their targets |
| Bid strategy | Results compared with the targets | Strategy never reviewed after launch |

## 11. What does the change history show?

| Check | What good looks like | Red flag |
|---|---|---|
| Recent changes | It is clear who changed what and what happened afterward, including auto-applied recommendations | A performance drop that follows an undocumented change |

## 12. How do competitors compare?

| Check | What good looks like | Red flag |
|---|---|---|
| Auction insights | Impression share, overlap rate, position above rate, and top of page rate against competitors are understood | Losing impression share and no plan for it |

## What should you fix first after an audit?

Fix tracking problems first, because they distort everything else. Then fix anything that wastes spend or blocks good traffic, such as irrelevant search terms, wrong locations, and campaigns limited by budget. Leave refinements like ad testing and audience layering for last.

## Is the audit different for Microsoft Ads?

The checks are mostly the same, and Microsoft Ads also reports Quality Score and search terms. Two things need extra attention:

- **Google imports.** Many Microsoft Ads accounts are built by importing campaigns from Google Ads. Check whether a scheduled import is still running, because depending on its options it can overwrite changes made directly in Microsoft Ads, and review settings that were copied over without a decision.
- **Traffic quality.** The smaller auction needs closer review of where clicks come from. The full comparison is in [Microsoft Ads vs Google Ads: Cost, Competition, and Bot Traffic](/blog/microsoft-ads-vs-google-ads/).

## Want a second pair of eyes?

I offer a [paid search audit](/services/#audit) for Google Ads and Microsoft Ads accounts. It covers account structure and settings, conversion tracking, budget and bidding, and ends in a written report with findings and a recommended order of fixes. I need access to the ad account, and any implementation is discussed separately after the findings. [Request an audit](/contact/?interest=Audit).
