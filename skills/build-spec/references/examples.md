# Build spec examples

Two filled specs. Use them as a shape check, not as copy-paste for a different ask.

## 1. Spec demo landing page deploy

Ask: "Change the NeoSoft demo hero h1 to 'See wall motion in minutes, not a delayed report' and redeploy."

```
# Build spec

## Context / Inputs
- Repo: rodney-hu/spec-demos, folder `neosoft/`
- Kit: foundations/templates/spec-demo (render.mjs, shoot.mjs)
- Current hero lives in `neosoft/demo.json` and is mirrored in `neosoft/copy/offer.md`
- After editing, re-render and reshoot before deploy

## Goal
Replace the NeoSoft demo hero headline with the approved line and ship it to the live demo URL.

## Deliverable
The live NeoSoft demo page at https://neosoft-demo.vercel.app, with the hero h1 "See wall motion in minutes, not a delayed report", plus the matching `neosoft/demo.json`, `neosoft/copy/offer.md`, rendered `neosoft/site/`, and screenshots.

## Plan
1. Set the hero h1 in `neosoft/demo.json` to the approved line. Mirror it in `neosoft/copy/offer.md`.
2. Re-render: `node ../foundations/templates/spec-demo/render.mjs neosoft`.
3. Reshoot: `node ../foundations/templates/spec-demo/shoot.mjs neosoft`.
4. Commit only `neosoft/**` and push to main.
5. From `neosoft/site/`, deploy with the command in Deploy target.

## Checks
- C1 | A reader gets the point in 5 seconds: the headline states the outcome | reviewer reads headline only
- C2 | Written in the buyer's words; no jargon ("leverage", "seamless", "unlock") | reviewer + grep for banned words
- C4 | Every claim is backed by a number, example, or source; no invented stats | reviewer lists each claim and its backing
- C5 | No AI tells (unslop pass, or `rodney-writing-style` verify script) | script output
- D1 | 375px wide: no horizontal scroll | screenshot + `scrollWidth <= 375`
- D2 | Hierarchy reads headline, then proof, then CTA | 375px and 1280px screenshots
- D5 | Mobile and desktop screenshots saved this round | files in `.eval/rounds/<n>/`
- B7 | Only files in scope changed | `scope_check.py` output
- P1 | Does the one job in the goal | reviewer walks the goal step by step
- P4 | Nothing extra was built; extras are in `parked.md` | diff vs plan
- G1 | The rendered hero h1 is exactly "See wall motion in minutes, not a delayed report" | `rg` or DOM read of `neosoft/site/` and the live URL
- G2 | The live URL serves the new headline after deploy | `curl` or browser read of https://neosoft-demo.vercel.app

## Files in scope
- neosoft/**

## Out of scope
- Every other company folder
- The spec-demo kit and skills
- Offer body, FAQ, and CTAs other than the hero h1
- New claims, stats, or regulatory language

## Approvals needed
push, deploy

## Deploy target
Vercel, team house-of-hu, project `neosoft-demo`. From `neosoft/site/`: `vercel deploy --prod --yes --scope house-of-hu --project neosoft-demo --non-interactive --verify`. Live at https://neosoft-demo.vercel.app

## Tier
Full

## Round budget
3
```

Tier note: a hero change on a live prospect demo is Full because it is client-facing. The sender can drop the budget to 2, not above 3.

## 2. Small backend or script change

Ask: "In sirona-demo-request-router, skip the Claude call when enrich.ts already found a HubSpot company from the last 30 days. Do not deploy."

```
# Build spec

## Context / Inputs
- Repo: rodney-hu/sirona-demo-request-router
- Duplicate detection already lives in `src/enrich.ts` and is logged. A later HubSpot write also no-ops on duplicates. The Claude call in `src/tier.ts` still runs today and costs about one request per duplicate.
- Run tests with `npm test`. Sample fixtures are in `data/samples/`.

## Goal
A request that already has a HubSpot company from the last 30 days does not call Claude, and still ends as a logged duplicate with no new CRM record.

## Deliverable
A passing change in `src/` plus tests that prove a known duplicate skips the Claude call, with `npm test` exiting 0. No live deploy.

## Plan
1. When enrich marks a duplicate, skip `src/tier.ts` and the draft call. Keep the existing log and the no-op HubSpot write.
2. Add a test that replays a known duplicate fixture, asserts zero Claude calls, and asserts no new company record.
3. Re-run the existing sample suite and keep the other four fixtures unchanged.

## Checks
- B1 | Build passes | `npm test` exits 0
- B3 | Happy path works end to end with a real submit and the real result | test output showing the stored/returned result
- B4 | Edge cases handled: empty input, bad input, double submit, timeout | one test or scripted call per case that this change can affect, including the duplicate path
- B5 | No secrets in source; inputs validated at the boundary | grep for key patterns + reviewer
- B7 | Only files in scope changed | `scope_check.py` output
- P1 | Does the one job in the goal | reviewer walks the goal step by step
- P4 | Nothing extra was built; extras are in `parked.md` | diff vs plan
- G1 | A known-duplicate fixture makes zero Claude API calls | test or mock call count
- G2 | A first-time request still goes through enrich, tier, draft, and the HubSpot write as before | existing sample tests still pass

## Files in scope
- src/**
- tests/**
- data/samples/**

## Out of scope
- Deploy, hosting, and environment changes
- Prompt or schema changes in the tier or draft calls
- HubSpot property setup
- Non-US routing or new sample fixtures beyond what the duplicate test needs

## Approvals needed
none

## Deploy target
none

## Tier
Standard

## Round budget
2
```

This ask named a behavior change and said not to deploy, so approvals and deploy target are `none`. A one-file toggle with an existing test might be Light. This one changes control flow and needs a new test, so Standard is the default.
