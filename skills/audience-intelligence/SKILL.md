---
name: audience-intelligence
description: Build deep audience intelligence for a brand — who their audience is, what activates them, how to write to them. Produces an Audience Intelligence Report (ICA, demographics, psychographics, fears, desires, activation moments, old-vs-new model, transformational statement, messaging assets) and a Strategic Insight Bridge naming what the brand uniquely understands about their audience. Use when someone wants to understand a brand's audience, build a persona, reverse-engineer messaging, or generate audience-targeted content. Trigger on "build a persona for [brand]", "who is their audience", "build an audience intelligence for [URL]", "what activates their audience", "give me audience intelligence for [brand]", or any audience-focused request. Designed to chain with `brand-intelligence` — consumes a Brand Profile if available, otherwise runs from a URL alone.
---

# Audience Intelligence

## Overview

Builds the **audience-side** intelligence for a brand or creator. Produces an **Audience Intelligence Report** — the foundational asset for any audience-targeted content (sales pages, EECs, outreach, ads, posts).

Designed to chain with `brand-intelligence`:
- **Chained mode**: If a Brand Profile exists in the conversation, consume it directly. Skip redundant extraction.
- **Standalone mode**: If only a URL is provided, run a lightweight brand extraction first, then build the audience profile.

The output structure is the same in both modes.

---

## Input Contract

```yaml
# One of these is required:
brand_profile: string | null   # Output from brand-intelligence skill (markdown)
url: string | null              # Source URL (any type — same as brand-intelligence)
```

If both are provided, use the brand_profile as primary context and the URL only for supplementary signal (comments, recent content, etc.).

---

## Output

A markdown deliverable with two parts:

```
# [Brand Name] — Audience Intelligence

> Source: [url or "chained from brand-intelligence"]
> Quality: PASS | THIN_DATA

═══ AUDIENCE INTELLIGENCE REPORT ═══
[Full sales-copy-blueprint-template.md, populated]

═══ 🌉 STRATEGIC INSIGHT BRIDGE ═══
[2-4 sentences: what does this brand uniquely understand about their audience?]
```

See `references/sales-copy-blueprint-template.md` for the full Report structure.

---

## Workflow

### Step 1: Determine Mode

If a Brand Profile is already in context, use it directly — skip URL fetching. Otherwise, do a lightweight brand extraction first: fetch the URL, pull voice, niche, mechanism, and content pillars, then proceed. You don't need a full Brand Profile — just enough to anchor the audience analysis.

### Step 2: Extract Audience Intelligence

Map source signals to the Audience Intelligence Report:

| Report Section | Source Signal |
|---|---|
| **Ideal Client Avatar** | "If you're a [X]" framing, direct address in bio, audience archetype from `references/audience-archetypes.md` |
| **Demographics** | Inferred from content sophistication, pricing, language complexity |
| **Audience Archetype** | Match 3+ signals from `references/audience-archetypes.md` |
| **Psychographics VOC** | For each emotion (frustration, insecurity, overwhelm, skepticism, ambition, longing) — find or synthesize a quote in audience voice. Mark synthesized lines `(synthesized)` |
| **Goals** | What outcomes does the brand promise? Those = audience goals |
| **Surface Pains** | Symptoms the audience names out loud — "stop doing X", "why X isn't working" |
| **Deep Fears** | Stakes language — "before it's too late", "don't make this mistake". Usually: irrelevance, wasted time, looking foolish, being stuck |
| **Secret Desires** | Aspirational identity language — "become the kind of person who…", "what successful X do differently" |
| **Activation Moments (3–5, DYNAMIC)** | Specific moments when this audience says "now I need help." Build from what the brand's content actually addresses — not generic categories. E.g. "first failed launch", "watched a peer get the role", "month 6 with no growth" |
| **Old Way → New Way** | Old: "stop doing X" content. New: "do this instead" content |
| **Transformational Statement** | *"I help [audience] achieve [outcome] using [mechanism]—without [frustration]."* |
| **Swipe-Ready Hooks (5–8)** | Highest-impact lines from titles, taglines, banner copy |
| **Messaging Framework** | How this brand executes Hook → Truth → Mechanism → Proof → CTA |

### Step 3: Write the Strategic Insight Bridge

A single tight section. 2–4 sentences. Answers one question:

> **What does this brand uniquely understand about their audience that competitors don't see?**

Format: state the insight directly, then explain how it shows up in their content.

Example structure:
> *"[Brand] sees that their audience isn't actually struggling with [surface problem] — they're struggling with [deeper insight]. That's why their content consistently [pattern] instead of [what competitors do]."*

This is the highest-leverage paragraph in the deliverable. It names the underlying thesis the brand has about its audience. Get this right and every downstream piece of copy is anchored.

### Step 4: Quality Check

Set the quality flag in the deliverable header:

- **PASS** — All checklist items met:
  - ✅ Archetype assigned with reasoning
  - ✅ All 6 emotion VOC quotes populated (`(synthesized)` marker where inferred)
  - ✅ 3–5 activation moments — specific events, not generic categories
  - ✅ Old vs New Activity has 2+ rows each side
  - ✅ Transformational Statement uses the formula
  - ✅ Strategic Insight Bridge in 2–4 sentences
- **THIN_DATA** — Some sections heavily inferred. List which.
- **INSUFFICIENT_DATA** — Cannot extract enough signal even with web search. Abort.

---

## Integration

| Downstream Skill | What This Feeds |
|---|---|
| `pga-eec` | ICA + Pains/Fears/Desires + Old→New → EEC topic and angle selection |
| `icebreaker-eec` | Psychographics VOC + Swipe Hooks → personalized icebreakers |
| `funnel-architect` | Strategic Insight Bridge + Activation Moments + Transformational Statement → funnel copy brief |
| `copy-eec` | Full Audience Intelligence Report → copy brief for any funnel asset |

---

## Troubleshooting

- **Sparse VOC quotes** — Synthesize each emotion-quote in the audience's voice from the pain points the brand addresses. Mark all with `(synthesized)`.
- **Activation moments feel generic** — If they could apply to any audience, they're wrong. Rewrite using actual events from the brand's content: *"Hit month 6 with no growth"*, *"Watched a peer land the role"*, *"Lost a deal because their LinkedIn looked unfinished."*
- **Sparse URL / thin source** — Run `brand-intelligence` first, then chain into this skill. Chained mode always produces stronger output than standalone on thin sources.

---

## References

- `references/sales-copy-blueprint-template.md` — Full audience deliverable template
- `references/audience-archetypes.md` — 7 audience archetypes for assignment
