# Company research

Goal: real-world practice. Build on what the company actually sells, to whom, and how, from public sources.

## Recipe (Firecrawl CLI, run from the session scratchpad)

1. `firecrawl --status` once. Credits are limited (~1,000 per cycle): keep one project's research under ~25 credits. If not authenticated, use the keyless tier or tell Rodney.
2. Find pages with targeted maps, not a bare map (a bare map on a docs-heavy site returns docs noise):
   `firecrawl map <url> --search pricing --limit 3`, then the same for `customers`, `about`, `careers`.
3. Scrape at most 6 pages: home, pricing, customers or case studies, product/solutions, about, careers.
4. `firecrawl search` for:
   - recent news, funding, launches, leadership hires (last 6–12 months)
   - 3–5 live job postings: theirs first, or the target role at similar companies
5. Optional: their tech stack from job postings, the integrations page, or the site's footer and scripts.

Keep raw output in the scratchpad. Only the extracted facts go into Notion.

## Extract

| Field | What to capture |
|---|---|
| Niche | Category and sub-segment, in their words |
| Offer | Products, pricing model and tiers, free trial or PLG entry |
| ICP | Company size, industry, buyer and user personas, named customer logos |
| GTM motion | PLG, sales-led, inbound-heavy, outbound, partner. Evidence for each |
| Visible stack | CRM, MAP, enrichment, data tools named in postings or integrations |
| Signals | Funding, hiring surges, launches, expansion |
| Visible gaps | What a GTM system could fix: slow demo booking, generic forms, no routing, thin nurture |
| Role requirements | Recurring requirements across the postings |

## Provenance tags

Tag every fact and every payload field:

- **Real**: public, with source URL and access date.
- **Constructed**: a reasoned inference from real facts, with the reasoning ("~400 inbound signups/mo, inferred from 12k G2 reviews and a free tier").
- **Mock**: private or costly data. CRM records, contact names and emails, intent data, enrichment fields, internal metrics, conversion rates.

Use mock when the data is private, hard to find, or would burn credits (Clay is on the free plan). Say which in one line.

## Limits

- Company-level public data only. No scraping personal contact details. Named people appear only as public roles (e.g. "VP Sales, per LinkedIn"), and never in sample payloads; use mock personas instead.
- If the site blocks scraping or facts conflict, say so and mark the field unknown. Don't fill gaps with guesses tagged Real.
- If Ikigai Business Targets (`{{TARGET_COMPANIES_DS}}`) already has a row for the company, read it first and link it from B-00. Don't duplicate its research.
