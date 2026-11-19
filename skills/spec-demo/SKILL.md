---
name: spec-demo
description: Turns one prospect URL plus one role title into one free, brand-matched asset for that prospect's audience, deployed to one shareable link. Researches the company and the role (Firecrawl map, scrape and search), captures their site design, routes to the best-fit recipe (lead-magnet page, onboarding course page, buyer-signals table, interactive tool, or checkout page), builds it with the spec-demo kit, deploys it to Vercel and hands back the link, screenshots, a Loom script and a one-line note. Use whenever Rodney says "spec demo", "build a demo for [company]", "make something for this prospect", "build an asset for the [role] at [company]", "run the demo process on [URL]", or gives a prospect URL and wants a tangible asset to show them. Also runs batches: a list of URL + role pairs with one combined approval gate ("batch these", "run the batch"). Does not send anything to the prospect.
---

# Spec demo

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in. When a key lists several machines, use the value whose path exists here.

**Input:** one prospect URL + one role title (e.g. "Head of Clinical Education"). Optional: an audience segment. For a list, see **Batch mode**.
**Done =** one live URL that opens with no login, screenshots of that live page, and `asset-card.md`, `loom-script.md` and `note.md` in `{{SPEC_DEMO_OUTPUT_DIR}}/<company-slug>/`.

Kit (templates and renderer): `{{SPEC_DEMO_KIT_DIR}}`. Read its `README.md` first; it holds the copy rules and the folder layout. This skill holds the process: `references/` and `recipes/`.

```
url + role → 1 research → 2 design → 3 route (asset card = THE gate) → 4 build → 5 deploy + deliver
```

## Before you start
- **Cloud session:** if the kit or output folder is missing, `add_repo` `rodney-hu/foundations` (kit) and `rodney-hu/spec-demos` (output), then clone them to `/home/user/`.
- Read the Notion Agent Front Door and the **Spec Demo Library** row in Active Projects. Add or claim `Demo: <Company>` per the Shared checklist protocol, in the format under **Save to GitHub and Notion**. Never file demos under Ghostwriting Offer, and never create a new Active Projects row per demo.
- Run the pull in **Save to GitHub and Notion**, then look for an existing `<company-slug>/` folder. Reuse what is there.

## 1. Research → `research/brief.md`
1. `firecrawl map <url>` → `research/sitemap.txt`.
2. Scrape home, product, each audience or solution page, about, FAQ, pricing and case studies → `research/pages/<slug>.md` (usually 6 to 10).
3. 4 to 6 `firecrawl search` queries (run Firecrawl calls one after another, not in parallel: the free tier allows about 12 a minute; Reddit pages can't be scraped, so quote search snippets and mark them as such) for the audience's own language (pains, mistakes, fears, skeptics, reviews, competitors) → `research/search/<topic>.json`.
4. 2 to 3 searches for the role's language, per `references/role-lens.md`.
5. Fill the kit's `brief-template.md`, including **Role lens**. Animated stat counters often scrape as `0+` or `0%`: never quote a number from a scrape that shows 0; find it in a press release or leave it out. Quote real language with its source. Keep the prospect's claims apart from verified facts.

## 2. Design capture → `design/`
If `design/` already holds the files, check them and move on. Otherwise:
- Scrape `branding,images` → `design/branding.json`, plus a full-page screenshot → `design/screenshot.png` (headless Chrome if Firecrawl fails, or ask Rodney). If the full page comes out blank (sites that animate sections in on scroll), take a 1440×900 viewport screenshot instead and note it.
- Download the logo → `design/logo.<ext>`. If none is usable, omit `about.logo`.
- Check the logo's size. If it is under 200px wide, or icon-only (a symbol with no wordmark), flag it to Rodney and look for a higher-res or full-wordmark version first (the site's header or footer SVG, `og:image`, press or brand page, or the `images` scrape). Do this before you build the page. If nothing better exists, say so, and let Rodney decide between that logo and omitting `about.logo`. If the SVG can't be downloaded (TLS errors, blocked hosts; Firecrawl won't fetch `.svg` files), try the `images` scrape and `og:image`, then crop the logo from `design/screenshot.png` at 2x. Note which one you used. Write what you found to `design/logo-check.md` (file, size, wordmark or icon, options) and add the logo question to the asset card.
- Look at the screenshot, then write `design/tokens.json` with the `theme` keys from `demo.schema.json`. Match their light or dark. Never add automatic dark mode.

## 3. Route → `asset-card.md` (the only gate)
1. Score the recipes with `references/router.md`: role KPI fit × company gap × proof available × build cost.
   - **buyer-signals seed pass:** if buyer-signals is the default or scores within one point of the leader, run 2 or 3 Firecrawl searches for the rubric's Tier 1 signals first and open the best hits. Score proof 3 only with at least 3 accounts confirmed from opened pages (V), 2 with 1 or 2, and 1 with snippets only. List the seed accounts on the card so Rodney approves real names, not a promise.
2. Fill the kit's `asset-card-template.md`: chosen recipe and runner-up, observed signal, hypothesis, asset name, outline, done checks.
3. **Gate:** show Rodney the card. He approves or edits it. Ask for a reply that names every choice, plus "deploy" (for example `approve card: lead-magnet, shield icon, deploy`); a bare "go" or "yes" is not enough for an agent to record approval or publish a page. Record the decision on the card. Everything after this runs without stopping.

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
2. `node "<kit>/shoot.mjs" . --url https://<company-slug>-demo.vercel.app` (shoots the live site; layouts without a thanks page skip it), desktop + mobile. Look at them: theme matches their site, nothing overflows on mobile, logo shows.
3. Write `loom-script.md` and `note.md` per `references/delivery-pack.md`.
4. Send Rodney the link and screenshots, plus a short note: role, recipe, asset name, open claims.

## Batch mode (several companies, one approval stop)
Use when Rodney gives a list instead of one URL ("batch these", "run the batch", a table of companies). Input: a numbered list of `URL + role` pairs, at most 5 per batch.

**A. Prep, per company, one company at a time.** Run stages 1 to 3 (research, design, route) and fill each asset card, but do not stop at the gate. Sync GitHub and Notion after each stage as usual. Run Firecrawl calls one after another across the whole batch (free tier, about 12 a minute). If a company fails (site blocks scraping, no usable signal), mark it `Blocked: <reason>` in Notion, drop it from the table below and keep going.

**B. One gate for the whole batch.** Set every company's Notion status to `Blocked: Rodney to approve the batch`, then show Rodney one table:

| # | Company | Role | Recipe (runner-up) | Asset name | Signal it answers | Open questions |
|---|---|---|---|---|---|---|

Put each card's open questions (logo, icon, claims to confirm) in the last column, with a default for each. Link each `asset-card.md`. Ask for a reply that spells out the decision and ends with "deploy", for example:
- `approve all, defaults ok, deploy`
- `approve 1, 3, 4 with defaults; drop 2; 5 use lead-magnet; deploy`

A bare "go", "yes" or "approve all" without "deploy" is not enough: ask once more for the full phrase. Record the decision on each card. Dropped companies get `Blocked: dropped at batch gate` and keep their files.

**C. Build and ship, no more stops.** For each approved company in order: stage 4, stage 5, sync after each. If one fails a done check you can't fix, mark it `Blocked: <reason>` and move on; never stop the batch for one company.

**D. One report.** A single table: company, recipe, live link, screenshots folder, status. Then the blocked ones and why. Same hand-off offers as one demo; nothing goes to a prospect.

Done when every company in the batch is either live with screenshots and synced, or marked Blocked with a reason, and Rodney was asked exactly once.

## Save to GitHub and Notion after every stage
Every demo lives in two places so other agents (Grokbot included) see the same state: the files in GitHub, the status in Notion. Sync both after **each** stage: brief, design, approved card, rendered site, deploy + delivery. In a batch, sync each company after each of its stages, not once at the end.

**Before starting:** `git -C "{{SPEC_DEMO_OUTPUT_DIR}}" pull --rebase`, then read the Spec Demo Library row. If another agent holds the `Demo: <Company>` claim, stop and ask.

**1. GitHub first.** From inside `{{SPEC_DEMO_OUTPUT_DIR}}` (repo `rodney-hu/spec-demos`):
```bash
git add "<company-slug>/"
git commit -m "<company-slug>: <stage>"
git push
```
Commit before you pull: `git pull --rebase` fails with uncommitted changes. Stage only this demo's folder. Never force-push or rewrite history. If the push is rejected, `git pull --rebase` and push once more; if it still fails, stop and report.

**2. Then Notion.** On the Spec Demo Library row (Active Projects), each company has a row in the **Demo roster** table and a toggle (`<toggle heading="h4">`, titled with the company) under **Shared checklist → Demos**. On the first stage, add both. After each stage, update that company's roster row and the `Demo: <Company>` item inside its toggle. Patch only those. Confirm the write by checking the update result for that company's row and item. Re-fetch the whole page only on the first write of a run, at a gate, and at the end (the page is large; re-reading it after every stage is wasted context). The item always carries:
```markdown
- [ ] Demo: <Company> | <status>: <agent>; claim: <session or "released">; stage <n>/5 <stage name>; updated: <ISO time>
  - Done when: live link, screenshots, asset card, Loom script and note are in the folder, and Rodney has reviewed them.
  - Role: <role title> · Recipe: <recipe or "not routed yet">
  - GitHub: [spec-demos/<company-slug>](https://github.com/rodney-hu/spec-demos/tree/main/<company-slug>) (last commit `<short sha>`)
  - Live: [<company-slug>-demo.vercel.app](https://<company-slug>-demo.vercel.app), or "not deployed"
```
`<status>` is `In progress`, `Blocked: <what is needed>` or `Ready: review needed`. Write file names in code formatting (`brief.md`) and links as `[label](url)`; Notion turns bare file names and URLs into links, which breaks later find-and-replace edits.

At the gate, set the status to `Blocked: Rodney to approve the asset card`. After stage 5, set it to `Ready: review needed` and release the claim. Only check the box after Rodney's review.

If the Notion write fails, the stage is not done: report `COMPLETED LOCALLY, NOT SYNCED` with the item text you meant to write. Never let Notion point at a commit that was not pushed.

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
