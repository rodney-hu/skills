---
name: prospect-intelligence
description: >
  Extract prospect intelligence from a YouTube channel URL or company/brand URL.
  Produces three outputs: (1) JSON brief with 13 variables covering outreach core,
  audience psychology, and messaging elements; (2) Free Consulting Brief with diagnostic,
  EEC concept, Loom script skeleton, and CTA block; (3) rendered outreach email.
  Disqualifies prospects with full funnel infrastructure. Use whenever Rodney needs
  to turn a qualified prospect into deployment-ready inputs for outreach, EECs, landing
  pages, and Notion CRM. Trigger on "build the prospect brief for [channel/brand]",
  "run prospect-intelligence on [URL]", "research this prospect", "extract outreach
  variables", "build intelligence for [company]", "what is their audience", or Stage 3
  of the youtube-to-notion workflow. Always use before writing any outreach copy or
  funnel assets for a prospect.
---

# Prospect Intelligence

One URL in. One JSON brief out. One Free Consulting Brief. One rendered email. Nothing else.

Supports two input types: **YouTube channel URL** and **Company/Brand URL**.
Auto-detects which path to run. Same variable set. Different signal sources.

---

## URL Router

```
INPUT URL
  |-- Contains youtube.com or youtu.be  -->  ROUTE A: YouTube Extraction
  +-- All other URLs (website, LinkedIn) -->  ROUTE B: Company Extraction
```

Declare route at the top of every run:

```
ROUTE DETECTED: [A: YouTube | B: Company]
INPUT: {url}
PROCEEDING WITH: {route name}
```

---

## Variable Set

All 13 variables apply to both routes. Signal sources differ per route below.

### Block 1 - Outreach Core (feeds email + Instantly)

| Variable | Definition |
|---|---|
| `name` | Creator or founder first name |
| `target_archetype` | Specific identity of their audience (1-4 words) |
| `audience_problem` | The painful bottleneck their audience is trying to escape |
| `quick_win` | The immediate result a 5-day EEC delivers (Rodney-designed) |
| `backend_offer` | Their core product or service, or inferred if absent |

### Block 2 - Audience Intelligence (feeds copy-eec, landing-eec, funnel-architect)

THIS IS THE HIGHEST-VALUE BLOCK. Extract with the most care.

| Variable | Definition |
|---|---|
| `audience_desires` | Top 2-3 things their audience is moving TOWARD |
| `audience_fears` | Top 2-3 things their audience is afraid of losing or never achieving |
| `activation_language` | 3-5 VERBATIM phrases their audience uses to describe their own situation |
| `transformation_statement` | Before to After: "From [old state] to [new state]" |
| `audience_identity_trigger` | The identity label that makes their audience lean in |

### Block 3 - Messaging Elements (feeds brand-intelligence, copy-eec, funnel-architect)

| Variable | Definition |
|---|---|
| `brand_voice` | 3-5 voice descriptors (e.g., "direct, no-fluff, practitioner-first") |
| `core_mechanism` | The named method or framework they use to get results |
| `proof_signals` | Best 1-2 social proof signals (numbers, testimonials, outcomes claimed) |
| `cta_pattern` | How they ask for action - the verb and destination they use most |

---

## Route A: YouTube Extraction

### `name`
1. YouTube About tab - "Hi, I'm [Name]"
2. Channel banner or handle if it is a personal name
3. Recent video intros - first 30 seconds
4. Web search: "{channel name}" founder OR creator

### `target_archetype`
1. Video titles - scan last 10 for "for [X]" patterns
2. Comments - self-identification language ("As a coach myself...", "I run a SaaS and...")
3. About tab - explicit "I help X do Y" statement
4. Channel tagline or banner copy

**Format rules:**
- 1-4 words in the audience's own language
- Specific enough to picture one person
- Never "viewers," "subscribers," "audience," "creators," "entrepreneurs"

Good: `agency owners`, `RevOps leads`, `healthcare AI founders`, `solo SaaS builders`
Bad: `people interested in marketing`, `business owners`, `creators`

### `audience_problem`
1. Recurring pain across last 10 video titles - same friction stated 3+ times
2. Comments - what bottleneck do commenters keep naming?
3. Pinned video or pinned comment - usually addresses the number 1 problem
4. Most-viewed video of last 90 days - highest engagement = highest pain resonance

**Format rules:**
- Plain-language sentence
- The thing they are trying to ESCAPE, not the thing they want
- Specific bottleneck, not aspirational outcome

### `audience_desires`
1. Comments - "I wish I could...", "I just want to...", "My goal is..."
2. Video titles framed as outcomes - "How to finally X", "The [outcome] method"
3. Community tab posts - what wins are they celebrating?

### `audience_fears`
1. Comments - expressions of dread, worry, "what if I never..."
2. Video titles framed as threats - "Stop doing X", "Why you're failing at Y"
3. Most-watched content - high views + fear-framed title = confirmed fear signal

Fears and desires must mirror each other. Fear = loss of desire. Re-align if they do not map.

### `activation_language`
- Pull EXACT phrases from comments - VERBATIM, never paraphrased
- Look for repeated wording patterns across 20+ comments from 3 recent videos
- These are the words that go directly into copy

### `transformation_statement`
- Synthesize from titles, comments, and About tab
- Format: "From [specific struggle] to [specific outcome]"

### `audience_identity_trigger`
- Who does this audience believe they are or want to become?
- Sources: About tab language, comment self-identification, video title framing

### `backend_offer`
1. Pinned video - usually pitches the offer
2. About tab links - Skool, Patreon, course URLs, "Work with me"
3. Community tab posts - recent product or cohort announcements
4. Video descriptions, last 3 uploads

**Decision logic:**
- Offer detected + full audience-capture infrastructure active (email list, lead magnet, funnel, community all present) --> DISQUALIFY. No gap to fill. Tell Rodney.
- Offer detected + audience-capture gap present (no email list, no lead magnet, no EEC, no opt-in) --> Proceed. The offer is the backend. The gap is the pitch angle.
- No offer detected --> Proceed. Infer what their backend should be based on content, archetype, and problem.

When proceeding with an offer detected, note the gap explicitly in `backend_offer.value` and set `status` to `DETECTED_WITH_GAP`.

### `brand_voice`
- Watch or read 3 recent videos for tone, pacing, language register
- Note: formal vs. casual, practitioner vs. theorist, direct vs. nurturing

### `core_mechanism`
- The named system, method, or framework they teach
- If unnamed, infer from content pattern and label in brackets

### `proof_signals`
- Subscriber count and view velocity (from VidIQ)
- Any stated results, case studies, or testimonials in descriptions or outros

### `cta_pattern`
- The action they ask viewers to take most often
- Example: "subscribe and comment", "DM me", "join the community"

---

## Route B: Company URL Extraction

Signal sources shift from video/comment to web pages, sales copy, and content assets.

### `name`
1. About or Team page - founder or primary POC
2. Contact page
3. LinkedIn company page - founder listed
4. Web search: site:{domain} founder OR CEO

### `target_archetype`
1. Homepage hero copy - "We help X do Y"
2. Sales or services page - who is this for?
3. Blog post bylines or category labels
4. Case study client descriptions

### `audience_problem`
1. Homepage above-the-fold copy - the problem framed in the first headline
2. Services or solutions page - what pain does each offer solve?
3. FAQ section - what do customers keep asking about?
4. Testimonials - what problem did clients have before hiring this company?

### `audience_desires`
1. Outcome language in sales copy - "Finally achieve X", "Imagine having Y"
2. Testimonials - what result did clients celebrate?
3. Case study headlines - the outcome framed as the story lead

### `audience_fears`
1. Sales page agitation copy - what does it cost them NOT to solve this?
2. FAQ framing - questions that reveal anxiety ("Will this work for...", "What if I...")
3. Blog titles framed as risks - "The X mistake that costs you Y"

### `activation_language`
- Pull exact phrases from testimonials, case study quotes, and blog comments
- Customer's own words about their situation - verbatim only, never paraphrased

### `transformation_statement`
- Read 2-3 case studies or testimonials for the before/after arc
- Format: "From [specific struggle] to [specific outcome]"

### `audience_identity_trigger`
- Who does this brand's customer believe they are or want to become?
- Sources: homepage positioning, testimonials, blog content themes

### `backend_offer`
1. Pricing page (if public)
2. Services or solutions page - named packages or deliverables
3. CTA buttons - what is the primary conversion action?

**Decision logic for company route:**
- Offer exists + audience-capture gap present (no email list, no lead magnet, no EEC, no opt-in) --> Proceed. The offer is the backend. The gap is the pitch angle. Set `status` to `DETECTED_WITH_GAP`.
- Offer exists + full-stack infrastructure active (email list, lead magnets, nurture sequences, funnel all present) --> DISQUALIFY. No gap to fill. Tell Rodney.
- No offer detected --> Proceed. Infer what their backend should be. Set `status` to `INFERRED`.

### `brand_voice`
- Read homepage, About page, and 1-2 blog posts
- Note: corporate vs. founder-led, polished vs. raw, case-study-heavy vs. philosophy-heavy

### `core_mechanism`
- Named methodology, framework, or proprietary process on the website
- If unnamed, infer from positioning and label in brackets

### `proof_signals`
- Client logos, case study results, revenue or growth stats claimed
- Best 1-2 with specificity ("Helped X achieve Y in Z timeframe")

### `cta_pattern`
- Primary CTA verb and destination - "Book a call", "Start your free trial", "Download the guide"

---

## Output Format

Three outputs in sequence. Never skip one. Never reorder.

1. JSON Brief (intelligence layer)
2. Free Consulting Brief (pitch layer)
3. Rendered Outreach Email (send layer)

---

### Output 1: JSON Brief

Return this JSON block first.

```json
{
  "prospect": {
    "input_url": "",
    "route": "youtube | company",
    "brand_slug": "",
    "run_date": ""
  },
  "outreach_core": {
    "name": { "value": "", "confidence": "HIGH | INFERRED" },
    "target_archetype": { "value": "", "confidence": "HIGH | MEDIUM | INFERRED" },
    "audience_problem": { "value": "", "confidence": "HIGH | MEDIUM | INFERRED" },
    "quick_win": { "value": "", "confidence": "RODNEY_DESIGNED" },
    "backend_offer": { "value": "", "status": "DETECTED_WITH_GAP | INFERRED | DISQUALIFIED", "confidence": "HIGH | INFERRED" }
  },
  "audience_intelligence": {
    "audience_desires": { "value": ["", ""], "confidence": "" },
    "audience_fears": { "value": ["", ""], "confidence": "" },
    "activation_language": { "value": ["", "", ""], "confidence": "VERBATIM" },
    "transformation_statement": { "value": "", "confidence": "" },
    "audience_identity_trigger": { "value": "", "confidence": "" }
  },
  "messaging_elements": {
    "brand_voice": { "value": ["", ""], "confidence": "" },
    "core_mechanism": { "value": "", "confidence": "NAMED | INFERRED" },
    "proof_signals": { "value": ["", ""], "confidence": "" },
    "cta_pattern": { "value": "", "confidence": "" }
  },
  "disqualified": false,
  "disqualification_reason": null,
  "handoff": {
    "copy_eec": ["target_archetype", "audience_problem", "quick_win", "backend_offer", "audience_desires", "audience_fears", "activation_language"],
    "landing_eec": ["target_archetype", "audience_problem", "quick_win", "transformation_statement", "activation_language"],
    "funnel_architect": ["target_archetype", "audience_problem", "audience_fears", "audience_desires", "brand_voice", "core_mechanism"],
    "notion_crm": "all_variables"
  }
}
```

---

### Output 2: Free Consulting Brief

Run this after the JSON. Uses the extracted variables to build a deterministic pitch package.
Four blocks. Fill every field. No vague language. No hedging.

---

#### BLOCK A — DIAGNOSTIC

Purpose: Name the problem category and surface missed opportunities Rodney will point out on the Loom.

**Problem Category** (pick exactly one):

| Category | Signal |
|---|---|
| `SOCIAL_TRAFFIC_NO_OPTIN` | Active social audience, no email capture anywhere |
| `WEBSITE_TRAFFIC_NO_OPTIN` | Website gets traffic, no opt-in form or lead magnet |
| `NEWSLETTER_WEAK_OPTIN` | Has a newsletter but it's buried or generic ("subscribe for updates") |
| `NO_PRE_CALL_EDUCATION` | High-ticket offer, no nurture sequence before the sales call |
| `NO_ONBOARDING_SEQUENCE` | Community or SaaS with no structured onboarding/welcome flow |

Output format:

```
PROBLEM CATEGORY: {category}
WHY: {1-2 sentences naming the specific evidence that confirms this — e.g., "No opt-in above the fold. Newsletter signup buried in footer. Current lead magnet is a generic PDF with no delivery sequence."}
```

**Missed Opportunities** (2-4 items, not in the problem category — bonus observations):

Pull from what you saw during extraction. These are gaps or weaknesses Rodney can mention to demonstrate depth of research. Use short, specific bullets.

Format rules:
- Each bullet names one specific thing: what it is, why it costs them
- No vague observations ("their content could be better")
- Pull specific evidence ("Day 1 email goes straight to a sales pitch — no trust built first")

Examples of strong missed opportunities:
- "Opt-in CTA says 'Join my newsletter' — no outcome promise. Likely under 5% conversion."
- "No follow-up sequence after lead magnet download. Traffic captured, then abandoned."
- "YouTube description links go to homepage, not a dedicated capture page. Leaking thousands of monthly views."
- "Calendar booking page has zero pre-call education. Prospects arrive cold."
- "Social proof exists (testimonials on website) but never referenced in content or email."

Output format:

```
MISSED OPPORTUNITIES:
- {Opportunity 1}
- {Opportunity 2}
- {Opportunity 3}
```

---

#### BLOCK B — EEC CONCEPT

Purpose: Design the specific EEC Rodney would build for this prospect. This is the "vision" shown at the end of the Loom.

**Working Headline** (use Biggest Mistakes format by default):

Formula: `"The [N] Biggest Mistakes [target_archetype] Make With [topic] (And How To Fix Them)"`

Alternative formulas if Biggest Mistakes doesn't fit:
- `"The [N]-Step [Outcome] Blueprint For [target_archetype]"`
- `"How [target_archetype] [Achieve Outcome] Without [Common Frustration]"`

Pick the formula that best matches the prospect's brand voice. Do not use all three.

**5-Day Outline**:

Each day = one sentence. Format: `Day [N]: [Mistake or Topic] — [What They Learn or Fix]`

Days must follow this arc:
- Day 1: Problem awareness (name the mistake they don't know they're making)
- Day 2: Reframe (why the standard approach fails)
- Day 3: New approach (introduce the mechanism)
- Day 4: Proof or application (show it working)
- Day 5: CTA (call to action toward the backend offer)

Use `audience_problem`, `audience_desires`, `core_mechanism`, and `backend_offer` from the JSON to make each day specific to this prospect.

Output format:

```
EEC HEADLINE: {headline}

Day 1: {topic} — {what they learn}
Day 2: {topic} — {what they learn}
Day 3: {topic} — {what they learn}
Day 4: {topic} — {what they learn}
Day 5: {topic} — {what they learn}
```

---

#### BLOCK C — LOOM SCRIPT SKELETON

Purpose: Give Rodney a punchy talking-points skeleton he can record against. Not a word-for-word script. Short sentences. Rodney's voice. Reads like how he actually talks.

Voice rules (same as rodney-writing-style):
- Short sentences. Active voice. No em dashes.
- No "leverage," "optimize," "streamline," or any business jargon.
- Direct. Specific. No hedging.
- Every line is a thing Rodney would actually say.

Structure: Five beats. Each beat = 2-4 talking points (not paragraphs — bullets he can riff from).

```
BEAT 1 — WHAT I NOTICED (15-20 sec)
Context: Open by naming exactly what you saw on their channel/site. Be specific — not "I was checking out your stuff," but "I went through your last 8 videos and noticed X."
Talking points:
- {Specific observation tied to problem category}
- {One number or detail that proves you actually looked}

BEAT 2 — WHAT IT'S COSTING THEM (20-30 sec)
Context: Quantify the gap. Real numbers where possible. Make the cost feel tangible.
Talking points:
- {Specific cost — traffic, leads, or revenue leaking}
- {Missed opportunity #1 from Block A}
- {Missed opportunity #2 from Block A — optional, only if it reinforces the cost}

BEAT 3 — WHAT I'D BUILD (30-45 sec)
Context: Show the EEC concept. Walk through the headline and 2-3 days. Don't read all 5 — tease enough that they want to see the rest.
Talking points:
- {EEC headline}
- {What Day 1 does for their audience}
- {What Day 3-5 sets up — the backend offer connection}
- {One sentence on why this format works for their specific audience}

BEAT 4 — THE OUTCOME (15-20 sec)
Context: Paint the after state. Specific result, not vague promise.
Talking points:
- {transformation_statement from JSON}
- {One concrete metric — opt-in rate, call quality, pipeline volume}

BEAT 5 — THE ASK (10-15 sec)
Context: Binary ask. Permission to proceed, not a commitment.
Talking points:
- {CTA line — see Block D}
```

---

#### BLOCK D — CTA BLOCK

Purpose: The exact line Rodney says at the end of the Loom (and repeats in the follow-up email).

Rules:
- One ask only
- Binary — "yes" or "no thanks" are the only possible answers
- No pressure language ("no obligation," "totally fine if not")
- Offer to send the full outline, not to "hop on a call" — that comes later

Default CTA template (fill in the blanks):

```
"If this looks useful, I'd love to put the full 5-day sequence together for you — for free.
Just reply and I'll send over the complete outline so you can see exactly what it looks like.
No strings. I just think [target_archetype] deserve better than what most [their niche] are giving them."
```

Adjust the last line to match the prospect's brand voice. If they're more formal, remove the last line entirely and end at "No strings."

Output format:

```
LOOM CTA:
"{filled CTA}"
```

---

### Output 3: Rendered Outreach Email

After the Free Consulting Brief, render the short outreach email.
This is the ping that goes before (or alongside) the Loom.

Subject: your {target_archetype} audience

Hey {name},

You do an incredible job drawing in {target_archetype} and getting straight to the core of their {audience_problem}.

To help them actually solve this, I built a custom 5-Day Email Course for your brand. It gives them a structured quick win and primes them for your {backend_offer}.

Attached is the Day 1 outline and landing page to use for free. Want me to send over the fully built 5-day sequence?

---

## Definition of Done

- [ ] Route declared at top of run (A or B)
- [ ] All 13 variables filled with confidence labels
- [ ] backend_offer status confirmed - disqualify if applicable
- [ ] JSON is the first output block - valid, complete, no empty required fields
- [ ] activation_language contains at least 3 verbatim phrases - not paraphrased
- [ ] audience_desires and audience_fears contain at least 2 values each and mirror each other
- [ ] transformation_statement follows "From X to Y" format with specifics
- [ ] Free Consulting Brief has all 4 blocks - Diagnostic, EEC Concept, Loom Script, CTA
- [ ] Problem category is one of the 5 named categories - not invented
- [ ] Missed opportunities are specific - each names a thing and why it costs them
- [ ] EEC headline uses one of the 3 approved formulas
- [ ] EEC 5-day outline follows the awareness → reframe → mechanism → proof → CTA arc
- [ ] Loom script skeleton is 5 beats with talking points - not paragraphs
- [ ] CTA block is one binary ask - no meeting request, no pressure language
- [ ] Rendered email matches template exactly - no extra paragraphs, no em dashes
- [ ] All downstream handoff variables are usable as-is

---

## Failure Points

| Failure | Fix |
|---|---|
| target_archetype is generic | Re-extract from comments or testimonials - find self-identification language |
| audience_problem is aspirational | Reframe as friction being escaped, not outcome desired |
| quick_win is vague | Make it a concrete deliverable and outcome |
| activation_language is paraphrased | Pull verbatim phrases only - exact words from the source |
| audience_desires and fears do not mirror | Fears = loss of desires. Re-align. |
| transformation_statement is generic | Rewrite with specific before and after states |
| backend_offer detected with full funnel stack and no gap | Stop. Not a prospect. Tell Rodney. |
| backend_offer detected but audience-capture gap exists | Proceed. Set status DETECTED_WITH_GAP. Name the gap in the value field. |
| Problem category doesn't match one of the 5 | Re-read the evidence. Force it into the closest category. Add specifics in the WHY field. |
| Missed opportunities are vague | Each one must name a specific thing observed + the cost. "Content could be better" is not a missed opportunity. |
| EEC days don't follow the arc | Days 1-2 must set up the problem. Days 3-4 must shift the belief. Day 5 must bridge to the backend offer. |
| Loom script beats are paragraphs | Convert to short bullets. Rodney riffs from these - they are not a script to read. |
| CTA asks for a meeting | The first ask is always permission to send the outline. Meeting request comes after they reply. |
| Rendered email has em dashes or hedging | Strip. Voice must stay flat and forwardable. |
| Variables do not describe one coherent person | Pause. Re-extract. All 13 must describe the same human. |
| JSON is missing or malformed | JSON is primary output. Fix before rendering anything else. |

---

## Notes for Claude

- **Route B audience variables live in the copy, not comments.** Read sales pages, testimonials, and case studies. That is where the customer's voice is.
- **Activation language is verbatim only.** Never paraphrase. Pull the exact phrase a real person used.
- **Desires and fears are a mirror pair.** Fear = "I'll never achieve X." Desire = "I want X." Re-extract if they do not map.
- **Block 2 is the highest-value output.** Do not rush it. Sample widely before synthesizing.
- **Block 3 is the creative briefs layer.** core_mechanism and brand_voice go directly into copy-eec and funnel-architect as style inputs.
- **quick_win is always RODNEY_DESIGNED.** Never extract it. Design it from the data.
- **JSON is primary output.** Free Consulting Brief is second. Email is third. This order is fixed.
- **VidIQ is primary for Route A.** For Route B, web_fetch is primary - fetch homepage, services page, About page, and 1-2 case study pages.
- **Do not run a full brand report.** That is brand-intelligence. This skill is 13 variables + free consulting brief + 1 rendered email. Anything else is scope creep.
- **The Free Consulting Brief is deterministic.** Fill the templates. Do not invent new formats. The structure is the process.
- **The Loom skeleton is talking points, not a script.** Short bullets Rodney can riff from. If a beat has more than 4 bullets, cut it.
- **The CTA is always about sending the outline.** Never suggest a call in the first touch. That comes after they reply yes.
