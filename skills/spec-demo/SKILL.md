---
name: spec-demo
description: Turns one prospect URL plus one role title into one free, brand-matched asset for that prospect's audience, deployed to one shareable link. Researches the company and the role (Firecrawl map, scrape and search), captures their site design, routes to the best-fit recipe (lead-magnet page, onboarding course page, buyer-signals table, interactive tool, or checkout page), builds it with the spec-demo kit, deploys it to Vercel and hands back the link, screenshots, a Loom script and a one-line note. Use whenever Rodney says "spec demo", "build a demo for [company]", "make something for this prospect", "build an asset for the [role] at [company]", "run the demo process on [URL]", or gives a prospect URL and wants a tangible asset to show them. Does not send anything to the prospect.
---

# Spec demo

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in. When a key lists several machines, use the value whose path exists here.

**Input:** one prospect URL + one role title (e.g. "Head of Clinical Education"). Optional: an audience segment.
**Done =** one live URL that opens with no login, screenshots of that live page, and `asset-card.md`, `loom-script.md` and `note.md` in `{{SPEC_DEMO_OUTPUT_DIR}}/<company-slug>/`.

Kit (templates and renderer): `{{SPEC_DEMO_KIT_DIR}}`. Read its `README.md` first; it holds the copy rules and the folder layout. This skill holds the process: `references/` and `recipes/`.

```
url + role → 1 research → 2 design → 3 route (asset card = THE gate) → 4 build → 5 deploy + deliver
```

## Before you start
- **Cloud session:** if the kit or output folder is missing, `add_repo` `rodney-hu/foundations` (kit) and `rodney-hu/spec-demos` (output), then clone them to `/home/user/`.
- Read the Notion Agent Front Door and the **Spec Demo Library** row in Active Projects. Add or claim `Demo: <Company>` per the Shared checklist protocol. Never file demos under Ghostwriting Offer, and never create a new Active Projects row per demo.
- Run the pull in **Save to the repo**, then look for an existing `<company-slug>/` folder. Reuse what is there.

## 1. Research → `research/brief.md`
1. `firecrawl map <url>` → `research/sitemap.txt`.
2. Scrape home, product, each audience or solution page, about, FAQ, pricing and case studies → `research/pages/<slug>.md` (usually 6 to 10).
3. 4 to 6 `firecrawl search` queries for the audience's own language (pains, mistakes, fears, skeptics, reviews, competitors) → `research/search/<topic>.json`.
4. 2 to 3 searches for the role's language, per `references/role-lens.md`.
5. Fill the kit's `brief-template.md`, including **Role lens**. Quote real language with its source. Keep the prospect's claims apart from verified facts.

## 2. Design capture → `design/`
If `design/` already holds the files, check them and move on. Otherwise:
- Scrape `branding,images` → `design/branding.json`, plus a full-page screenshot → `design/screenshot.png` (headless Chrome if Firecrawl fails, or ask Rodney).
- Download the logo → `design/logo.<ext>`. If none is usable, omit `about.logo`.
- Look at the screenshot, then write `design/tokens.json` with the `theme` keys from `demo.schema.json`. Match their light or dark. Never add automatic dark mode.

## 3. Route → `asset-card.md` (the only gate)
1. Score the recipes with `references/router.md`: role KPI fit × company gap × proof available × build cost.
2. Fill the kit's `asset-card-template.md`: chosen recipe and runner-up, observed signal, hypothesis, asset name, outline, done checks.
3. **Gate:** show Rodney the card. He approves or edits it. Record the decision on the card. Everything after this runs without stopping.

## 4. Build → `demo.json`, `site/`
Open `recipes/<recipe>.md` and follow it. Every recipe:
1. Writes its copy plan (the recipe names the file), then `demo.json` with `"recipe": "<recipe>"`, the copy and the `theme` from `design/tokens.json`.
2. Runs `node "<kit>/render.mjs" .` and fixes whatever it reports. Never hand-edit `site/`.
3. Passes the copy rules in the kit README and the banned-word grep:
   `grep -niE "email course|day [0-9]|rodney|drip|newsletter|sequence" site/*.html` returns only the footer line.
4. Passes the recipe's own done checks.

If the recipe's layout is not in the kit yet (status "planned" in the kit README), build it in the kit first (`recipes/<recipe>/`), following the recipe doc. Never fork a layout inside one demo.

## 5. Deploy + deliver
1. Deploy `site/` per `references/deploy.md` to `https://<company-slug>-demo.vercel.app` (always this name). Write the URL to `demo.json` (`live_url`) and `asset-card.md`.
2. `node "<kit>/shoot.mjs" .` (or Playwright on the live URL), desktop + mobile. Look at them: theme matches their site, nothing overflows on mobile, logo shows.
3. Write `loom-script.md` and `note.md` per `references/delivery-pack.md`.
4. Send Rodney the link and screenshots, plus a short note: role, recipe, asset name, open claims.

## Save to the repo
If `{{SPEC_DEMO_OUTPUT_DIR}}` is a git repo, other agents share it:
- **Before starting:** `git -C "{{SPEC_DEMO_OUTPUT_DIR}}" pull --rebase`.
- **After each stage** (brief, design, approved card, rendered site, deploy + delivery), from inside `{{SPEC_DEMO_OUTPUT_DIR}}`:
  ```bash
  git add "<company-slug>/"
  git commit -m "<company-slug>: <stage>"
  git push
  ```
- Stage only this demo's folder. Never force-push or rewrite history. If the push is rejected, `git pull --rebase` and push once more; if it still fails, stop and report.

## Hand-off
Give Rodney: the live URL, `screenshots/`, `asset-card.md`, `loom-script.md`, `note.md`, and the repo link to the folder. Offer, and do none without a yes:
- send the note (Rodney's call, his channel)
- record the Loom (Rodney's)
- add real email capture (kit README, "Going further")

Never create a My Portfolio row per demo. Packaging means adding the demo, anonymized, to the existing "Spec-Demo Email Course Funnel" portfolio row, only on Rodney's approval via `/close-loop` step 7. Then run `/close-loop`.

## Rules
- One card → one recipe → one live URL. No Resend, no drips, no live payments, no backend.
- Edit `demo.json` and re-render. Never hand-edit `site/`. Layout changes go in the kit, for every future demo.
- Never reproduce the prospect's copy as your own. Their claims go only in About (or the recipe's credit block), attributed. Record each claim's page in `about.sources`.
- No "demo" wording on the page except the footer disclaimer. Buttons, headings and fine print use normal offer copy.
- Nothing goes to the prospect without Rodney's yes. Deploying is not sending: the URL is noindex and unlisted.
