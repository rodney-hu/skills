---
name: copy-eec
description: Write high-converting email copy and funnel copy using Premium Ghost Writing Academy methodology. Use when the user needs to build EECs (Educational Email Courses), email sequences, broadcast emails, nurture flows, opt-in page copy, bridge page copy, sales page copy, or any funnel copywriting. Takes minimal input (topic + audience + outcome) and produces complete, deployment-ready copy assets. Triggers on requests like "write email copy", "create an email course", "build an EEC", "write funnel copy", "write a landing page", "opt-in page copy", "bridge page copy", "sales page copy", "email sequence", "5-day email series", "write this funnel", or any request to produce persuasive copy for a funnel or email system. Always use this skill before writing any email or funnel copy by hand.
---

# Copy-EEC: Email Copy + Funnel Copy

Produce high-converting, deployment-ready copy for email sequences and funnels using PGA methodology.

**Two modes:** Email Copy (EECs, broadcasts, nurture) · Funnel Copy (opt-in, bridge, thank you, sales pages) · Combinable.

---

## Quick Start

```
Topic: [what the content covers]
Audience: [specific person, not "people"]
Outcome: [tangible result they get]
Mode: [Email Copy / Funnel Copy / Both]
```

Optional: brand voice sample, paid offer to promote, competitor context, funnel stage.

---

## Mode 1: Email Copy

**EEC types:** Crash Course · Step-by-Step · **Biggest Mistakes (DEFAULT)** · Easy Templates

**Offer formula (Biggest Mistakes default):**
`"Top [N] Mistakes [Exact Audience] Make With [Topic] (And How To Fix Them)"`
Golden words: Roadmap, Blueprint, Playbook, System, Method → Full 6-step build: `references/offer-templates.md`

### 5-Section Email Structure (Days 1–5)

1. **The Reminder** — Callback to opt-in promise
2. **The Mistake** — Name it + tangible consequences
3. **The Reason** — Why smart people still fall into this
4. **How To Fix It** — Action steps with real detail
5. **Check Tomorrow** — Preview that creates anticipation

Each section: 1/3/1 rhythm + 3–5 detailed bullets.

### The 1/3/1 Writing Rhythm

Every prose block = 1 opener + 3 explanation sentences + 1 conclusion.

Opener types: strong declarative · question · controversial opinion · moment in time · vulnerable statement · **weird unique insight (most common)**

Full email templates + Day 0 welcome structure: `references/email-templates.md`

### Email Use Cases

**EEC:** Build offer → Day 0 welcome → Days 1–5 (one mistake/day) → PS monetization on Days 3–5 if promoting paid offer.

**Broadcast:** One opener type → insight or story lead → bridge to offer → one CTA only.

**Nurture:** Map goal (onboard/re-engage/convert) → one belief shift per email → soft or hard CTA by stage.

---

## Mode 2: Funnel Copy

### Capture / Opt-in Page (most common — built inline)

1. **Headline** — Specific outcome + audience + timeframe if possible
2. **Subheadline** — Mechanism or proof statement
3. **Bullets (3–5)** — Benefit-led, not feature-led
4. **CTA Button** — Action verb + outcome ("Send My Free Blueprint")
5. **Trust line** (optional) — "Join 1,200+ [audience] already inside"

**Headline formulas:**
- "How [Audience] [Achieve Outcome] Without [Common Frustration]"
- "The [Golden Word] For [Audience] Who Want [Outcome]"
- "Stop [Painful Problem]. Start [Desired Outcome]."

**Bridge/VSL · Thank You · Sales Page** structures + examples: `references/examples.md`

---

## Copy Principles (Both Modes)

**Tangibility over vague language:**
- ❌ "Waste time" → ✅ "20 hours/week on unqualified leads"
- ❌ "Nobody takes you seriously" → ✅ "$0 raised after 6 months"

**One CTA per asset.** Never split attention.
**Specific audience.** Never "people" or "business owners." Name the exact person.
**Under 1000 words per email.** Funnel pages: match length to temperature (cold = shorter).
**No jargon.** No "leverage," "synergy," "game-changer" unless it's in the brand voice.

---

## Decision Tree + Tools

| Need | Load |
|---|---|
| Full EEC build | `references/offer-templates.md` → `references/email-templates.md` |
| PS monetization | `references/ps-templates.md` |
| Bridge/VSL, Thank You, Sales page | `references/examples.md` |
| Quality check | `references/checklists.md` |
| Automate offer/email generation | `scripts/generate_offer.py` + `scripts/generate_email.py` |
| Package for client delivery | `scripts/package_eec.py` (outputs Notion MD, ConvertKit CSV, JSON) |

**Pairs with:** `funnel-architect` (renders copy as React SPA) · `packaging-eec` (Notion delivery) · `rodney-writing-style` (brand voice layer)
