# Recipe: onboarding-eec

**Status:** planned. Layout to build: `<kit>/recipes/onboarding-eec/` (`index.html`, `schema.json`, optional `recipe.css`).
**The link shows:** one landing page where the onboarding or education content is readable on the page itself: hero, then 5 short lessons as on-page sections (tabs or accordions), then About and a closing band. No email capture, no Resend, no drip.
**Best for:** education, onboarding, training and customer-success roles; products where new users or students stall after week one.
**Source to extract from:** `spec-demos/corsmed-eec-demo/` (page + `site/emails/day-0..5.md` lesson content). Drop `site/api/`, `drip.config.json` and the Resend wiring.

## Steps
1. **Copy plan → `copy/lessons.md`.** Use `copy-eec` to plan 5 lessons for the prospect's new users (each: title, the mistake or confusion it removes, 3 to 5 short paragraphs or steps, one "try this today" action). Lesson 5 sits closest to the prospect's product.
2. **`demo.json`.** `"recipe": "onboarding-eec"`, shared slots (`company`, `mark`, `mark_accent`, `meta_description`, `hero`, `about`, `faq`, `cta`, `theme`) plus `lessons[5]` (`title`, `summary`, `body` paragraphs, `action`).
3. Render, check, deploy, deliver.

## Building the layout (first run only)
Start from `landing.html`: keep header, hero band, About, Questions, CTA band and footer. Replace the opt-in card with a lesson index (5 anchor links), and replace the What's inside accordion with 5 full lesson sections. The CTA band links to lesson 1. No form, no script beyond tab or accordion behavior.

## Done checks
- All 5 lessons are readable without any form or click-gate.
- Banned-word grep passes (no "email course", "day N", "drip").
- Reads well at 390px; lesson index links jump to the right sections.
