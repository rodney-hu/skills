---
name: landing-eec
description: "Generate a brand-specific, audience-targeted landing page as a deployable React artifact. Supports multiple framing modes — challenge, course, sprint, bootcamp, workshop — with the same conversion architecture throughout. Takes a brand URL, Brand Profile, and/or Audience Intelligence profile and produces a fully populated page with real, on-brand, audience-specific copy. Use this skill whenever Rodney (or a client) needs to see what a finished offer page looks like. Trigger on 'build a landing page for [brand/client]', 'create a challenge page', 'create a course page', 'build a sprint landing page', 'show them what done looks like', 'generate a landing page from this brand profile', 'build the page for this client', 'turn this offer into a landing page', or any request to produce a ready-to-present offer landing page for a specific brand. Always use this skill before writing landing page copy by hand. Also trigger on 'landing-eec' or 'landing eec'."
---

# EEC / Offer Landing Page Generator

Produces a brand-specific, audience-targeted offer landing page as a deployable React `.jsx` artifact. Supports five framing modes — **challenge, course, sprint, bootcamp, workshop** — with identical conversion architecture. All template tokens are replaced with real copy derived from the brand's identity, offer, and audience intelligence.

---

## Input Contract

```yaml
# One of these input modes is required:

mode_1_full:
  brand_profile: string         # Output from brand-intelligence skill
  audience_intelligence: string # Output from audience-intelligence skill

mode_2_brand_only:
  brand_profile: string         # Output from brand-intelligence skill

mode_3_url_only:
  url: string                   # Any HTTPS URL
  brand_name: string | null     # Optional. Auto-extracted if absent.

# Optional overrides for any mode:
offer_context: string | null    # Specific offer title or brief if known
framing: challenge | course | sprint | bootcamp | workshop | null
  # If null or not specified, framing is auto-detected in Phase 0
```

**Priority order**: Full profiles → brand only → URL only. If profiles exist in the conversation, use them rather than re-extracting.

---

## Workflow

### Phase 0 — Select Framing Mode

> Load `references/framing-modes.md` first. It contains all vocabulary tables and detection rules.

**If framing is explicitly specified in the request** → use it. Skip detection.

**If not specified**, infer from brand signals:

| Brand Signal | Inferred Mode |
|---|---|
| Transformation, habit-building, community-driven content | `challenge` |
| Curriculum, expertise-first, credentials, B2B knowledge | `course` |
| Operator/builder audience, speed language, quick wins | `sprint` |
| High-ticket, intensive, "no excuses" voice | `bootcamp` |
| Done-with-you, creative, practitioner, skills-based | `workshop` |

**Default if still unclear:** `challenge`

Record the selected framing. Every Phase 3 copy decision pulls vocabulary from that mode's table in `references/framing-modes.md`.

---

### Phase 1 — Gather Brand + Audience Context

**Brand Profile + Audience Intelligence both present:**
Skip extraction. Use them directly. Proceed to Phase 2.

**Brand Profile only:**
Infer audience signals from voice samples, content pillars, and CTA strategy. Flag inferred fields with `(inferred)`.

**URL only:**
Run lightweight extraction:
1. `web_fetch` the URL — homepage + about page if accessible
2. Web search `"[brand name] [niche] target audience"` and `"[brand name] offer"`
3. Extract minimum required fields
4. Proceed to Phase 2

> Load `references/token-mapping.md` before Phase 2.

---

### Phase 2 — Map Signals to Template Tokens

Populate the token map. Every required token must have a value before Phase 3.

**Required tokens:**
- `OFFER_NAME`
- `NUMBER` (always 5)
- `DOING_TOPIC`
- `TANGIBLE_OUTCOME_1/2/3`
- `COMMON_FRUSTRATION`
- `DAY_1–5_TITLE`
- `DAY_1–5_TEASER`
- `SENDER_FIRST_NAME`, `SENDER_LAST_NAME`, `SENDER_TITLE`
- `SENDER_BIO`

**Optional tokens (degrade gracefully):**
- `NUMBER_OF_SUBSCRIBERS`
- `SPECIFIC_AUDIENCE`
- `TESTIMONIAL_*` (leave placeholder if none available)

> Full token definitions and signal-to-token mapping: `references/token-mapping.md`

---

### Phase 3 — Write the Copy

Using the selected framing mode's vocabulary table from `references/framing-modes.md`, write all copy.

> Full copy rules per framing mode: `references/copy-principles.md`

**Offer naming:**
The framing word (Challenge / Course / Sprint / Bootcamp / Workshop) appears in the topbar and eyebrow — not necessarily in the offer title itself. Name the offer by its transformation.
- Good: "The Pipeline Fix Sprint"
- Good: "The 5-Day Email Sequence Course"
- Avoid: "The GTM Stack Sprint", "The Email Marketing Course"

**Headline:** Pull the pattern from the selected mode's vocabulary table.

**Subheadline:** Use the mode's opener as the starting point. Fill in three outcomes following the arc: clarity → asset/system → confidence.

**Day titles:** Action-oriented across all modes. Verb choice adapts to the mode (see Day Label Variants in `references/framing-modes.md`), but all titles describe what the participant *does*, not what they *learn*.

**Success state:** Use the mode's exact `success title` and `success subtitle` from `references/framing-modes.md`. Do not improvise.

---

### Phase 4 — Assemble the Page

1. Load `assets/template.jsx` as the base
2. Replace the `CONTENT` object with all populated tokens, using mode-specific strings for:
   - `hero.eyebrow`
   - `primaryCta.buttonLabel` and `microcopy`
   - `whatToExpect.label` and `whatToExpect.intro`
   - `socialProof.label`
   - `author.label`
   - `secondaryCta.label`, `secondaryCta.supporting`, `secondaryCta.buttonLabel`
   - `trustSignals` array
   - Success state strings in the `CtaForm` component (edit JSX directly)
   - Topbar label string in JSX
3. Apply brand color overrides if hex values are in the Brand Profile
   - `--gold` → brand primary accent (warm, high-contrast)
   - `--bg` → brand background (keep dark unless brand is explicitly light)
   - Light-theme: see color swap table in `references/token-mapping.md`
4. Update `author.initials` to actual initials
5. Output file: `/mnt/user-data/outputs/[brand-slug]-[mode]-page.jsx`
6. Present the file to the user

---

### Phase 5 — Present + Summary

```
Brand: [name]
Framing: [mode] — [one-line reason if auto-detected]
Audience: [ICA in one line]
Offer name: [title]
Transformation arc: [pain] → [outcome]
Tokens inferred: [list or "none"]
Next step: [what needs to be done before it goes live]
```

---

## Decision Tree

```
Input received
│
├── Framing specified?
│   ├── YES → use it
│   └── NO → detect from brand signals → default: challenge
│
├── Brand Profile + Audience Intel in context?
│   └── YES → Phase 2
│
├── Brand Profile only?
│   └── YES → infer audience → Phase 2
│
└── URL only?
    └── YES → web_fetch + search → Phase 2
```

---

## Quality Standards

Before outputting the final file, verify:

- [ ] No `{{PLACEHOLDER}}` tokens remain in required fields
- [ ] Framing mode is consistent throughout — no mixing of vocabulary across modes
- [ ] Day titles are action-oriented (verb-first where possible)
- [ ] Subheadline uses outcome language, not learning language
- [ ] CTA button label matches selected mode
- [ ] Success state matches selected mode exactly
- [ ] Topbar label matches selected mode
- [ ] Author initials match actual sender name
- [ ] File named `[brand-slug]-[mode]-page.jsx`

---

## Reference Files

| File | When to Load |
|---|---|
| `references/framing-modes.md` | Phase 0 — load first |
| `references/token-mapping.md` | Before Phase 2 |
| `references/copy-principles.md` | Before Phase 3 |
| `assets/template.jsx` | Phase 4 — base file |
