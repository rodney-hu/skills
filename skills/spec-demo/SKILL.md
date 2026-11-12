---
name: spec-demo
description: Build a free spec-demo landing page and thank-you page for a prospect from one URL. Researches the company (Firecrawl map, scrape and search), captures their site design, drafts a Biggest Mistakes offer and outline for their audience, then renders a brand-matched local HTML page with the spec-demo kit. Use whenever Rodney says "spec demo", "build a demo for [company]", "make a landing page for this prospect", "run the demo process on [URL]", or gives a prospect URL and wants a tangible asset to show them. Does not write the emails, set up Resend or deploy, unless Rodney asks.
---

# Spec demo

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

Kit: `{{SPEC_DEMO_KIT_DIR}}`. Read its `README.md` first. It holds the SOP, the copy rules and the folder layout. The finished reference is `examples/{{SPEC_DEMO_REFERENCE}}/`.

Input: one prospect URL, plus an optional audience segment. Work in `~/Desktop/RodneyOS/01 Projects/spec-demos/<company-slug>/`.

## Before you start
- Read the Notion Agent Front Door and the **Spec Demo Library** row in Active Projects (the standing home for every spec demo). Add or claim the checklist item `Demo: <Company>` per the Shared checklist protocol. Do not file demos under Ghostwriting Offer, and do not create a new Active Projects row per demo.
- Search for an existing folder in `spec-demos/` first. Reuse what is there.
- Nothing is sent to the prospect. Outreach, deploys and DNS need Rodney's approval.

## 1. Research → `research/brief.md`
1. `firecrawl map <url>`, saved to `research/sitemap.txt`.
2. Scrape the home, product, each audience or solution page, about, FAQ, pricing and case studies to `research/pages/<slug>.md`, usually 6 to 10 pages.
3. Run 4 to 6 `firecrawl search` queries for the audience's own language: pains, mistakes, fears, the category's skeptics, reviews and competitors (Reddit, forums, review sites). Save each to `research/search/<topic>.json`.
4. Fill `brief-template.md`. Quote real language with its source. Separate the prospect's claims from verified facts.
5. **Gate:** recommend one segment and why, then ask Rodney to pick. Record his choice in the brief.

## 2. Design capture → `design/`
Follow the `firecrawl-website-design-clone` skill's collection step:
- Scrape `branding,images` to `design/branding.json`, and take a full-page screenshot to `design/screenshot.png`.
- If the screenshot fails, use headless Chrome, or ask Rodney for one.
- Download the logo from `branding.logo` to `design/logo.<ext>`. If none is usable, omit `about.logo` and the layout drops the logo card.
- Look at the screenshot, then write `design/tokens.json` with the `theme` keys from `demo.schema.json`: their background, text, primary, tint, border, hero band (gradient or solid), font (closest Google Font) and radius.
- Match light or dark to their site. Never add automatic dark mode.

## 3. Offer and outline → `copy/offer.md`
- Use the `copy-eec` skill's Biggest Mistakes formula and the Notion "EEC Offers and Outlines Framework", and fill `offer-template.md`.
- Build the asset name from the audience plus a golden word, the hook, 5 mistakes (each with an outcome and a fix), the whisper, 3 to 4 About bullets and 4 to 6 FAQs.
- Use the audience's words from the brief. Put the mistake closest to the prospect's product last.
- **Gate:** Rodney approves or edits. Don't write the page before this.

## 4. Page → `demo.json`, `site/`, `screenshots/`
1. Copy `examples/{{SPEC_DEMO_REFERENCE}}/demo.json`, then replace every value from the offer, brief and tokens.
2. Check every copy rule in the README. The page talks only to the prospect's audience. It never mentions Rodney, email courses or drips, and it names no format.
3. `node "<kit>/render.mjs" .`, then fix whatever it reports.
4. `grep -niE "email course|day [0-9]|rodney|drip|newsletter|sequence" site/*.html` must return only the footer line. "email" may appear only in the form.
5. `node "<kit>/shoot.mjs" .`. Look at all three screenshots: the theme matches their site, the hero card is balanced with the text, nothing overflows on mobile, and the logo shows.
6. Send Rodney the screenshots, then add a short note: the audience, the asset name and any open claims.

## Hand-off
List the local paths: `site/index.html`, `screenshots/`, `research/brief.md` and `copy/offer.md`. Offer these next steps, and do none of them without a yes:
- deploy (README, "Going further")
- write the emails
- record a Loom (Rodney's)

Never create a My Portfolio row per demo. Packaging means adding the demo, anonymized, as an example on the existing "Spec-Demo Email Course Funnel" portfolio row, only on Rodney's approval via `/close-loop` step 7.

Then run `/close-loop`.

## Rules
- Edit `demo.json` and re-render. Never hand-edit `site/`.
- To change the layout for every future demo, edit the kit. Don't fork the layout in a single demo.
- Never reproduce the prospect's copy as your own. Their claims go only in About, attributed with a source link.
