---
name: research-prospects
description: Runs Step 3 (Research) of the Pre-Sold Protocol prospecting pipeline. Pulls all Qualified leads from the Notion CRM, fetches each prospect's website, extracts Company Intelligence and Audience Intelligence, writes both fields back to Notion, and advances Status to Researched. Use when Rodney says "run research", "research the leads", "research qualified leads", "Step 3", or any request to move Qualified leads forward in the pipeline. Always use this skill before any compose or pitch step — it produces the intelligence that powers the outreach email. Never run this step manually lead-by-lead when this skill can batch it.
---

# Research Prospects — Step 3

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

Batch research step for the Pre-Sold Protocol pipeline. One run processes every Qualified lead in the CRM: fetches their website, extracts intelligence, writes it back to Notion, and advances the status to Researched.

---

## Setup

**Notion CRM data source:** `{{CRM_DS}}`

**Target leads:** Status = "Qualified"

**Fields to write:** `Company Intelligence`, `Audience Intelligence`

**Status to set on completion:** `Researched`

**Fields already populated (do not overwrite):** `Trigger`, `First Name`, `Last Name`, `Email`, `Website`, `LinkedIn`

---

## The Loop

For each Qualified lead, run the following in sequence. Process leads one at a time — do not batch or skip.

### Step 1 — Fetch the website

Fetch these pages in parallel:
- `{Website}` (homepage)
- `{Website}/about`
- `{Website}/services` (or `/coaching`, `/work-with-me`, `/programs`)
- `{Website}/blog` (or `/articles`, `/resources`)

If the homepage returns no content, a dead domain, a maintenance page, or a redirect loop:
- Skip this lead
- Log it as `SKIPPED — dead/inaccessible site`
- Do NOT update Notion Status

If partial pages fail (about, services, blog) but the homepage returns content, proceed with what you have.

### Step 2 — Extract Company Intelligence

Company Intelligence is the briefing on the business itself. Write it as a dense paragraph (not bullets) covering:

- **Who:** Founder name, title, and primary identity (how they describe themselves)
- **What:** The niche they serve and what transformation they deliver
- **Offer stack:** Every named product or service, from free entry point to highest-ticket item
- **Brand voice:** 3–5 descriptors (e.g., "warm, nurturing, mentor-over-coach, accountability-forward")
- **Core mechanism:** Their named method or framework. If unnamed, infer from the content and label it in brackets (e.g., "[Transitional Identity Coaching]")
- **Proof signals:** Best 1–2 credibility markers — client count, testimonials, credentials, lived experience
- **CTA pattern:** Their primary conversion action (verb + destination), e.g., "Book Your Consultation Now → Calendly"
- **The gap:** What audience-capture infrastructure is missing — no email list, no lead magnet, no nurture sequence, etc. This is the pitch angle.

**Format:** One dense paragraph, plain prose, no headers. Max ~200 words.

**Example (Camika Jones — Vibrant Soul Life Coaching):**
> Certified Life Coach and Emerging Adulthood Mentor (self-styled "MOMentor"). Military spouse background — used global travel to build empathy across cultures. Four coaching tracks: Transition Coaching, Self-Care/Self-Reflection, College Prep, and Emerging Adulthood Coaching. Offer stack: free 15-min consult → 65-min strategy session → 50-min coaching sessions (single or 4-pack) → New College Graduate Program. Brand voice: warm, nurturing, mentor-over-coach, community-first, accountability-forward. Core mechanism: [Transitional Identity Coaching] — personalized self-discovery, goal setting, and resilience-building tailored to the client's specific transition. Proof: military spouse lived experience, Reviews section on About page (content not publicly rendered). CTA: "Book Your Consultation Now" → Calendly 15-min free consult. No email list, no lead magnet, no nurture layer — only path to conversion is the Calendly link.

### Step 3 — Extract Audience Intelligence

Audience Intelligence is the briefing on the people this coach serves. Write it as a structured paragraph covering all of the following. Every item is required.

| Variable | What to extract |
|---|---|
| **Target archetype** | 1–4 words in the audience's own language. Specific enough to picture one person. Never "people," "clients," "entrepreneurs." |
| **Core problem** | The painful bottleneck they're trying to escape — specific friction, not an aspiration |
| **Desires** | Top 2–3 things they're moving toward |
| **Fears** | Top 2–3 things they're afraid of losing or never achieving. Must mirror the desires. |
| **Activation language** | 3–5 VERBATIM phrases pulled directly from the site copy, testimonials, or blog — never paraphrased |
| **Transformation statement** | "From [specific struggle] to [specific outcome]" |
| **Identity trigger** | Who does this audience believe they are or want to become? |
| **Quick win** | A Rodney-designed concept for a 5-day email course that delivers one concrete result — design it from the data, never extract it from the site |

**Signal sources for Route B (company website):**
- Target archetype → homepage hero copy, services page "who this is for" language
- Core problem → above-the-fold headline, services page pain framing, FAQ
- Desires → outcome language in sales copy, testimonial wins, case study headlines
- Fears → agitation copy, FAQ anxiety framing, risk-framed blog titles
- Activation language → verbatim phrases from testimonials, case study quotes, services copy — exact words only
- Transformation → before/after arc in case studies or testimonials
- Identity trigger → positioning language, testimonial self-identification

**Format:** Dense prose paragraph followed by a clearly labeled "Quick win:" line. Max ~250 words total.

**Example (Camika Jones — Vibrant Soul Life Coaching):**
> Target archetype: young adults in transition (post-college graduates, emerging adults 18–25, high school seniors). Core problem: hit a major life change — graduation, career pivot, relocation, independence — with no clarity on who they are or where to go, so they stall out instead of moving forward. Desires: clarity and direction, confidence to make big decisions, a future they actively designed. Fears: falling behind peers by staying stuck too long, making the wrong life decision and wasting years, losing their identity in the chaos of transition. Activation language (verbatim): "dealing with life transitions" / "discovering their identity" / "seeking direction" / "navigating uncertainty" / "tap into their full potential." Transformation: From paralyzed and lost in a major life transition → to confident, clear, and moving forward with purpose. Identity trigger: the emerging adult who refuses to drift — wants to become the person who shows up for their own life with intention.
>
> Quick win: 5-day "Your Next Chapter" email course — one identity-clarifying exercise per day to name core values, map the transition gap, and write one specific first move for the week.

### Step 4 — Write to Notion

Update the lead's Notion page with:
- `Company Intelligence` → the paragraph from Step 2
- `Audience Intelligence` → the paragraph + quick win from Step 3
- `Status` → `Researched`

Do not modify any other field.

### Step 5 — Log the result

After each lead, output one line:

✅ Researched: [First Name] [Last Name] — [Company] ([Website])

or

⚠️ Skipped: [First Name] [Last Name] — [Company] (dead/inaccessible site)

---

## Run Summary

After all leads are processed, output:

Research complete.
✅ Researched: N leads
⚠️ Skipped: N leads

Researched:
- [Name] — [Company]
- ...

Skipped (needs manual review):
- [Name] — [Company] — [reason]

---

## Quality Checks

Before writing any field to Notion, verify:

- Target archetype is 1–4 words, specific enough to picture one person
- Audience problem is friction being escaped — not an aspiration
- Fears mirror the desires (Fear = loss of desire)
- Activation language contains verbatim phrases only — not paraphrased
- Transformation statement follows "From X to Y" with specifics
- Quick win is a concrete 5-day course concept, Rodney-designed, not extracted from the site
- Company Intelligence names the gap (what's missing from their funnel)
- Both fields are dense prose — no bullet points, no headers inside the field

If activation language cannot be found verbatim (site has no testimonials, no quotes, no client voice), pull the closest direct phrasing from services copy and mark it "(inferred from copy)" rather than presenting it as a verbatim client phrase.

---

## Notes

- **Thin sites are common in this niche.** Many prospects have GoDaddy or Squarespace one-pagers with almost no copy. Work with what you have — infer where needed, label inferences clearly.
- **Instagram and Facebook links** on the site can provide additional audience signal if the web pages are thin. Attempt to fetch them, but treat failure as acceptable — these are supplements, not required sources.
- **Do not disqualify leads here.** Disqualification happened in Step 2. If a lead is Qualified in the CRM and has a live website, research them regardless of niche fit concerns.
- **The gap is always the pitch angle.** Every Company Intelligence field must name what's missing. If the site has no email list, no lead magnet, and no nurture layer — that's the gap. Name it explicitly.
