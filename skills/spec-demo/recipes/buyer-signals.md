# Recipe: buyer-signals

**Status:** planned. Layout to build: `<kit>/recipes/buyer-signals/` (`index.html`, `schema.json`, `recipe.css`).
**The link shows:** a brand-themed table of **at most 10** named accounts likely in market for the prospect now, each with sourced signals, a score, the buyer title and a one-line "why now". Below it: the scoring rubric and method notes.
**Best for:** founders, sales and BD roles at B2B companies with a clear buyer title.
**Source to extract from:** `spec-demos/scanlab/research/signals/` (`scanlab-buyer-signals-prd.md` rubric and data model, `target-list.md` columns, `loom-script.md`).

## Steps
1. **Rubric → `research/signals/rubric.md`.** Adapt the ScanLab rubric to this industry: 6 to 9 signal types (hiring for the problem role, aged or reposted posts, agency or contractor use, new site or capacity, new leader, M&A, look-alike of a named customer), each with points. Tier 1 = direct evidence of the problem now.
2. **Pull → `research/signals/raw/`.** Firecrawl job boards, career pages, news and press. Public pages only. No Apollo, Clay or HubSpot without a yes.
3. **Score → `research/signals/target-list.md`.** Rank and keep the top 10 (fewer is fine; never pad). Mark each signal **V** (page opened and read) or **S** (snippet only, half points).
4. **`demo.json`.** `"recipe": "buyer-signals"`, shared slots (`company`, `mark`, `mark_accent`, `meta_description`, `hero`, `theme`) plus `accounts[≤10]` (`rank`, `org`, `where`, `signals[]` of `{tier, detail, url, date_seen, confidence: V|S}`, `score`, `buyer_title`, `why_now`), `rubric[]`, `method` notes, `as_of` date.
5. Render, check, deploy, deliver.

## Building the layout (first run only)
Header + short hero ("<N> <buyers> likely in market for <product> now", as-of date) + one responsive table (cards stacked below 720px) + rubric table + method notes + footer. Every signal renders as a link to its source with a V or S badge.

## Done checks
- 10 rows or fewer; `schema.json` sets `maxItems: 10`.
- Every signal has a working source URL and a date seen.
- No personal emails or phone numbers; buyer names only when public, and marked unverified if not confirmed.
- The table reads at 390px with no horizontal page scroll.
