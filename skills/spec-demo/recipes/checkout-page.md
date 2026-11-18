# Recipe: checkout-page

**Status:** planned. Layout to build: `<kit>/recipes/checkout-page/` (`index.html`, `thanks.html`, `schema.json`).
**The link shows:** an offer page written for one audience type, ending in a mock checkout (order summary + a pay button that goes to a confirmation page). No real payment form, no processor, no card fields.
**Best for:** revenue, ecommerce and offer-owner roles whose current page talks to everyone at once.
**Structure to borrow:** the `landing-eec` and `funnel-architect` skills (offer stack, objections, guarantee wording).

## Steps
1. **Copy plan → `copy/offer.md`.** One audience type from the brief, their main objection (the whisper), the prospect's real offer as published (name, what's included, published price only), 3 to 5 outcome bullets in the audience's words, FAQ for the top objections.
2. **`demo.json`.** `"recipe": "checkout-page"`, shared slots plus `offer` (`name`, `includes[]`, `price` as published, `guarantee` only if published) and `checkout` (`button`, `summary_lines[]`).
3. Render, check, deploy, deliver.

## Done checks
- Price, guarantee and inclusions match the prospect's published page, with sources in `about.sources`; nothing invented.
- The pay button goes to `thanks.html`; the page makes no network calls and has no card inputs.
- The page names one audience type throughout.
- Banned-word grep passes; works at 390px.
