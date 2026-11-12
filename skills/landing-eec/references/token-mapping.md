# Token Mapping Reference

Maps fields from Brand Profile and Audience Intelligence outputs to landing page template tokens. Read this before Phase 2 of the skill workflow.

---

## Required Token Map

| Template Token | Source (Brand Profile) | Source (Audience Intelligence) | Fallback if Missing |
|---|---|---|---|
| `CHALLENGE_NAME` | `Brand Identity > Offer/Mechanism` + `Niche` | `ICA > Primary Pain` | Construct: "[Niche] [Transformation] Challenge" |
| `NUMBER` | Always `5` | — | — |
| `DOING_TOPIC` | `Brand Identity > Niche` or `Content Pillars` | `ICA > Primary Context` | Required — extract from URL if absent |
| `TANGIBLE_OUTCOME_1` | `Offer > Primary Promise` | `Sales Copy Blueprint > Desires` (top desire) | Required — must be specific, measurable |
| `TANGIBLE_OUTCOME_2` | `Offer > Secondary Promise` | `Sales Copy Blueprint > Desires` (2nd desire) | Required |
| `TANGIBLE_OUTCOME_3` | `Offer > Tertiary Promise or Feature` | `Sales Copy Blueprint > Activation Moments` | Required |
| `COMMON_FRUSTRATION` | `Brand Voice > Pain Points addressed` | `Sales Copy Blueprint > Frustrations` (top) | Required — must be what they're avoiding, not just a problem |
| `DAY_1_CHALLENGE_TITLE` | `Content Pillars` (pillar 1 or top mistake) | `Sales Copy Blueprint > Old vs New Model` (old belief 1) | Construct from niche + audience pain |
| `DAY_2_CHALLENGE_TITLE` | `Content Pillars` (pillar 2) | `Old vs New Model` (old belief 2) | Construct |
| `DAY_3_CHALLENGE_TITLE` | `Content Pillars` (pillar 3) | `Old vs New Model` (old belief 3) | Construct |
| `DAY_4_CHALLENGE_TITLE` | `Mechanism` or `Offer feature` | `Desires` (desire 3) | Construct |
| `DAY_5_CHALLENGE_TITLE` | `Offer CTA or final transformation` | `Transformational Statement` | Construct — should feel like a win/arrival |
| `DAY_1–5_ONE_LINE_TEASER` | Derived from day title | Audience voice samples | Write fresh — see copy rules |
| `SENDER_FIRST_NAME` | `Brand Identity > Founder/Author name` | — | Required |
| `SENDER_LAST_NAME` | `Brand Identity > Founder/Author name` | — | Required |
| `SENDER_TITLE` | `Brand Identity > Role or Descriptor` | — | Construct from niche + outcome (e.g., "GTM Systems Architect") |
| `SENDER_BIO` | `Authority Signals` + `Brand Voice` | — | 2–3 sentences: what they've done, what they help people do |

---

## Optional Token Map

| Template Token | Source | Behavior if Missing |
|---|---|---|
| `NUMBER_OF_SUBSCRIBERS` | Not extractable from URL — leave blank or use social proof count | Remove sentence or use: "Built for {{SPECIFIC_AUDIENCE}} who are done guessing." |
| `SPECIFIC_AUDIENCE` | `ICA > Avatar description` (1-line) | Infer from niche + content signals |
| `TESTIMONIAL_QUOTE_1–3` | Not extractable unless explicitly provided | Leave `{{TESTIMONIAL_QUOTE_N}}` placeholder — note in debrief |
| `TESTIMONIAL_NAME_1–3` | — | Leave placeholder |
| `TESTIMONIAL_TITLE_1–3` | — | Leave placeholder |
| `TESTIMONIAL_INITIALS` | First letter of first + last name | Derive if name is known |

---

## Day Title Construction Rules

Day titles must be **action-oriented** — they describe the move the participant makes, not the concept they learn.

**Pattern:** `[Verb] + [Specific Object] + [Optional: in/within time/context]`

Examples by niche:

| Niche | Weak (Concept) | Strong (Action) |
|---|---|---|
| GTM / RevOps | "Understanding Your ICP" | "Define Your ICP in One Sitting" |
| Email Marketing | "The Problem with Your Welcome Sequence" | "Write a Welcome Sequence That Actually Converts" |
| Content / Brand | "Why Your Content Isn't Getting Traction" | "Audit Your Last 10 Posts in 15 Minutes" |
| Coaching / Consulting | "Pricing Mistakes Coaches Make" | "Price Your Offer Without Apologizing for It" |
| SaaS / Product | "What's Wrong with Your Onboarding" | "Map Your User's First 7 Days in 30 Minutes" |

Day 5 should always feel like arrival — the participant has done something complete.
- ❌ "Keeping the Momentum Going"
- ✅ "Ship Your First Automated Follow-Up Sequence"
- ✅ "Send Your First Outreach Message with Confidence"

---

## Teaser Construction Rules

Each teaser = one sentence. Hints at the fix, doesn't give it away.

**Pattern:** `You'll [verb phrase] so that [mini-outcome].`

Variants:
- `By the end of this one, you'll finally know [specific thing].`
- `This is the one most people skip — and it's why [problem persists].`
- `One [timeframe] task that changes how [audience does thing].`

**Tone:** Conversational, not instructional. Should feel like a friend giving a heads up, not a course description.

---

## Challenge Name Construction

When no explicit offer name exists, construct using:

```
[Transformation Verb] + [Specific Result] + "Challenge"
```

Examples:
- "Fix Your Follow-Up Challenge"
- "Map Your GTM in 5 Days Challenge"
- "Launch Your First Email Sequence Challenge"
- "Close Your First Client Challenge"

Avoid:
- Generic words: "Growth", "Success", "Level Up", "Transform"
- Mechanism names: "The CRM Challenge", "The Funnel Challenge"
- Internal jargon the ICA wouldn't use

---

## Color Mapping

If brand hex values are available in the Brand Profile, apply these overrides in the template's `:root` block:

| CSS Variable | Default | Override Rule |
|---|---|---|
| `--gold` | `#c9a84c` | Brand primary accent (if warm/high-contrast) |
| `--gold-light` | `#e8c97a` | Lighten brand accent by ~15% |
| `--gold-dim` | `rgba(201,168,76,0.12)` | Brand accent at 12% opacity |
| `--bg` | `#0d0d0b` | Keep dark unless brand is explicitly light |
| `--border` | `rgba(212,185,120,0.15)` | Brand accent at 15% opacity |

**Light-theme brands:**
If the brand's primary aesthetic is light/white, swap the entire palette:

```css
:root {
  --bg: #fafaf8;
  --surface: #f2f1ed;
  --surface2: #eae9e4;
  --border: rgba(0,0,0,0.08);
  --text: #1a1a18;
  --text-muted: #6b6760;
  --text-dim: #b0ada6;
  --white: #1a1a18;    /* headline color — inverted */
}
```
Keep `--gold` as-is or override with brand accent.

---

## Sender Bio Formula

```
[Credential or credibility signal] + [What they've built or done] + [Who they help and how].
```

Example:
> "Former cardiac MRI technologist turned systems architect. I've spent the last three years building AI-powered operating systems for B2B teams that are tired of duct-taping their GTM stack together. Now I help founders and RevOps leads replace chaos with infrastructure that actually compounds."

Rules:
- Lead with the thing that earns the right to teach this, not a job title
- Middle sentence = proof of work, not aspiration
- End sentence = who you help (ICA mirror)
- Max 3 sentences, no filler phrases like "passionate about" or "dedicated to"
