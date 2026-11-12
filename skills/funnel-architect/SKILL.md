---
name: funnel-architect
description: >
  Builds a fully functional, deployable funnel prototype as a React JSX or HTML artifact — adapted to any funnel goal. Use this skill whenever someone says "build a funnel", "create a funnel for [brand/goal]", "funnel architect", "make a landing funnel", "build me an opt-in funnel", "build a sales funnel", "create a booking funnel", "build a challenge funnel", "build a course launch funnel", "mock up a funnel", or any request to produce a working funnel prototype. Also trigger when someone drops a company URL and wants a funnel built from it. ALWAYS use this skill before building any funnel by hand — even if the request seems simple.
---

# Funnel Architect

## Purpose

Build a deployable, conversion-architecture-correct funnel prototype for any goal. The funnel category and type are determined by the user's objective and inferred from brand research — not assumed upfront. All copy lives in a single `CONTENT` object so re-branding is a one-block edit.

---

## Phase 1 — Intake Interview

Before building anything, run a short intake. Ask all questions in **one message — never stagger them**.

**4 questions, always asked together:**

1. **Goal** — What should this funnel accomplish? *(e.g. collect emails, book calls, sell a course, launch a challenge)*
2. **Offer** — What is the visitor getting or being asked to do? *(e.g. free guide, strategy call, $97 course, 5-day challenge)*
3. **URL** — Drop the company/brand URL — I'll pull goal signals, brand voice, audience language, and proof from it.
4. **Output format** — React JSX (Claude artifacts / React setups) or plain HTML (no build step, opens in browser)?

**Do not build until all 4 are answered.** If the user drops a URL with a brief description, extract what you can and ask only for what's genuinely missing.

---

## Phase 2 — Brand Research + Auto-Detection

Once the URL is provided, fetch the homepage and extract:

| Signal | What to look for |
|---|---|
| Brand name + tagline | Logo text, H1, meta title |
| Core offer / mechanism | Hero section, above-the-fold CTA |
| Primary CTA pattern | Button text — "Book a call", "Download", "Buy now", "Join free" |
| Target audience language | Exact words used to describe who they serve |
| Primary pain point | Problem framing in hero/subhead |
| Proof signals | Testimonials, stats, logos, case studies |
| Tone | Formal / conversational / bold / minimal |
| Price signals | Any visible pricing, "free", "$X", "investment" |

**Auto-detect funnel category from CTA pattern:**

| Primary CTA signal | → Inferred category |
|---|---|
| "Book a call", "Schedule", "Apply" | → **Sales** (high-touch) |
| "Download", "Get free", "Join challenge", "Register" | → **Leads** |
| "Buy now", "Get instant access", "Enroll", "Start today" | → **Sales** (direct) |
| "Watch", "Learn", "Get the training", "Free workshop" | → **Educational** |

State the inferred category and the CTA signal that triggered it. If ambiguous, ask.

Use extracted context to pre-populate the `CONTENT` object with real brand language. Placeholders only for what's genuinely missing.

---

## Phase 3 — Funnel Category + Type Selection

### Three categories, clear purpose:

**LEADS** — Goal is audience capture. Psychology: friction reduction.
| Type | Pages | Use when |
|---|---|---|
| Opt-in / Lead Magnet | Capture → Thank You | Free resource, list building |
| Challenge Registration | Registration → Daily → Upsell | 5–30 day challenges |
| Webinar / Live Training | Registration → Confirmation → Replay | Live or evergreen events |

**EDUCATIONAL** — Goal is belief change before the sell. Psychology: worldview shifting.
| Type | Pages | Use when |
|---|---|---|
| VSL Bridge | Opt-in → Bridge (VSL) → CTA | Warm traffic, pre-sell before offer |
| Mini-Training | Opt-in → Training Page → Pitch | Short video series or email course |
| Case Study Sequence | Opt-in → Story Page → Offer | Proof-first indoctrination |

**SALES** — Goal is direct conversion. Psychology: objection demolition.
| Type | Pages | Use when |
|---|---|---|
| Booking / Discovery | Capture → Bridge → Calendar | High-touch, service offers |
| Long-form Sales Page | Sales → Checkout → Thank You | Low/mid-ticket direct offer |
| Course / Program Launch | Opt-in → Indoctrination → Sales → Checkout | High-ticket or deadline-driven |

### Category mismatch warning

Flag a mismatch when the offer and selected category are misaligned:

- High-ticket offer ($1k+) → **Sales** funnel without an **Educational** layer → warn: cold traffic won't convert without indoctrination; suggest VSL Bridge or Mini-Training before the Sales page
- Free offer → **Sales** funnel selected → warn: unnecessary friction; suggest **Leads** category instead
- Cold traffic + direct **Sales** funnel → warn: consider an Educational layer first

State the warning clearly, give the recommendation, then let the user decide. Never block the build.

### Funnel type rationale

After selecting, state in one sentence why: *"Booking funnel — your primary CTA is 'Schedule a call' and the offer is a high-touch service, so the funnel needs a VSL bridge before the calendar to pre-sell."*

---

## Phase 4 — CONTENT Object Assembly

All copy in one block at the top of the output file. Never hardcode strings in components.

### Universal slots (all funnel types)

```js
const CONTENT = {
  brand: {
    name: '',          // Brand name from research
    tagline: '',       // One-line positioning
    accentColor: '',   // Hex from brand (fallback: '#6366f1')
  },
  meta: {
    audience: '',      // ICP label — "For [who]"
    hook: '',          // H1 — Promise + Pivot + Exclusion formula
    subhead: '',       // Supporting sentence using their language
    cta: '',           // Primary button text
    reassurance: '',   // Below-CTA trust line
  },
  proof: [],           // [{ type: 'stat'|'quote'|'logo', value, label? }]
  footer: {
    copyright: '',
    links: ['Terms', 'Privacy', 'Contact'],
  }
}
```

### Category extensions

**LEADS — Opt-in** adds:
```js
leadMagnet: { title, tagline, pills: [] },
thankYou: { headline, steps: [] }
```

**LEADS — Challenge** adds:
```js
challenge: { name, duration, dailyTopics: [], startDate, registrationCta, upsellHeadline }
```

**EDUCATIONAL — VSL Bridge** adds:
```js
bridge: { alertBanner, vslTitle, vslRuntime, nextStepCta, caseStudies: [] }
```

**EDUCATIONAL — Mini-Training** adds:
```js
training: { seriesTitle, episodes: [{ title, duration, takeaway }], pitchCta }
```

**SALES — Booking** adds:
```js
bridge: { alertBanner, vslTitle, vslRuntime, bookingCta, caseStudies: [] },
calendar: { headline, subhead, calendarEmbed: '[CALENDAR_EMBED_URL]' }
```

**SALES — Long-form** adds:
```js
sales: { problemStatement, mechanism, benefits: [], price, priceAnchor, guarantee, faq: [], checkoutCta }
```

**SALES — Course Launch** adds:
```js
course: { name, modules: [], bonuses: [], price, priceAnchor, closingDate, salesCta }
```

### Copy quality rule

If brand research yields enough context (brand name, audience language, pain point, CTA pattern), attempt real first-draft copy for `hook`, `subhead`, `cta`, and `reassurance` using their exact language — do not default to brackets. Brackets only for slots where context is genuinely absent.

---

## Phase 5 — Build the Funnel

### JSX implementation rules

- Single `.jsx` file
- Pages as conditional views — `page` state variable controls which renders
- Navigation via state, never `<a href>` routing
- Tailwind utility classes only
- All strings sourced from `CONTENT` — zero hardcoded copy in JSX
- Available: React, Tailwind, lucide-react
- No `<form>` tags — use `onClick` handlers
- Functional components + hooks only
- **Include a one-line comment at each page transition explaining the psychological purpose:**
  ```js
  // Pattern interrupt: redirect attention before they leave
  // Belief bridge: shift worldview before the pitch
  // Commitment anchor: micro-yes before the big ask
  ```

### HTML implementation rules

- Single `.html` file — CSS in `<style>`, JS in `<script>`
- No external dependencies except CDN Tailwind Play
- Multi-page via `display: none` toggle
- All copy in `CONTENT` JS object at top of `<script>`
- Same psychological transition comments apply

### Mobile-first rules

Every layout must hold at 375px viewport:
- Font sizes: hero H1 min `text-3xl`, body min `text-base`
- CTA buttons: full width on mobile (`w-full md:w-auto`)
- Stack all flex rows on mobile (`flex-col md:flex-row`)
- Viewport meta tag required in HTML output
- No horizontal scroll at any breakpoint

### Design system defaults

```
Background:   zinc-950 / #09090b
Surface:      zinc-900 / #18181b
Border:       zinc-800 / #27272a
Primary text: zinc-50  / #fafafa
Muted text:   zinc-400  / #a1a1aa
Accent:       From brand research → fallback indigo-500 (#6366f1)
CTA button:   Accent bg + white text + hover:brightness-110
```

Brand color overrides accent only — zinc dark system is fixed.

---

## Phase 6 — Output + Handoff

Save to `/mnt/user-data/outputs/[brand-slug]-[funnel-type]-funnel.[ext]`

Call `present_files`. Handoff note includes:

1. **Category + type selected** — one sentence rationale
2. **Any mismatch warning** that was surfaced
3. **Slots populated** from brand research (real copy)
4. **Placeholders remaining** — what still needs input
5. **Production TODOs:**
   - Wire CTA to email platform (ConvertKit, Beehiiv, etc.)
   - Replace `[CALENDAR_EMBED_URL]` with Calendly / TidyCal link
   - Swap video placeholders with real VSL / case study embeds
   - Replace proof snippets with real screenshots
   - Remove prototype step-nav before client delivery

Keep it short. The file is the deliverable.

---

## Constraints

- **Never build before intake is complete.** 4 questions, one message, wait for answers.
- **Never invent copy.** Real language from URL research, or a placeholder. Never hallucinated copy.
- **Never restructure CONTENT.** One block at the top, always.
- **Never multi-file.** One JSX or one HTML.
- **Placeholders over hallucination.** Every time.
- **Never block on a mismatch warning.** Warn, recommend, build anyway.
