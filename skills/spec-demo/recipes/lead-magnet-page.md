# Recipe: lead-magnet-page

**Status:** live (kit root: `landing.html`, `thanks.html`, `demo.schema.json`).
**The link shows:** a Biggest Mistakes opt-in page for the prospect's audience. The form validates the address and goes to the thank-you page. Nothing is sent.
**Best for:** marketing, growth and demand-gen roles; companies with a defined audience and no free entry point.

## Steps
1. **Copy plan → `copy/offer.md`.** Use the `copy-eec` skill's Biggest Mistakes formula and the Notion "EEC Offers and Outlines Framework", filling the kit's `offer-template.md`: asset name (audience + golden word), hook, 5 mistakes (each with an outcome and a fix), the whisper, 3 to 4 About bullets, 4 to 6 FAQs. Use the audience's words from the brief. Put the mistake closest to the prospect's product last.
2. **`demo.json`.** Copy `examples/{{SPEC_DEMO_REFERENCE}}/demo.json`, set `"recipe": "lead-magnet-page"`, and replace every value from the copy plan, brief and tokens. Optional slots: `tag`, `about.logo`, `about.logo_artwork`, `about.eyebrow`, a bullet `url` (only when a claim must be visibly attributed).
3. Render, check, deploy, deliver (SKILL.md steps 4 and 5).

## Done checks
- The banned-word grep returns only the footer line. "email" appears only in the form.
- The page talks only to the prospect's audience and names no format.
- Hero card is balanced with the text; nothing overflows at 390px; the logo shows.
- Every About claim has its page in `about.sources`.
