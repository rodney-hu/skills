# Gate specs

Each gate: objective, what to ask (max 3 questions or 3 options), Definition of Done. The Done when line is copied verbatim into the master page's Shared checklist.

## Gate 00: System Brief

**Objective:** lock one company, one broken motion, one metric, and the cut line.

**Ask:** usually nothing new. Intake + research + the picked scenario fill it. Confirm only the value-claim number and the cut line.

**Value case (locked here, compared at Gate 05):**
- Metric: pipeline, retention, CX, or cost.
- Value claim, one sentence with a fitting verb: "Reduces [time/cost/errors] by ~Y for a [role] at a [company type]", "Increases [meetings/conversion] by ~Y…", "Improves [speed to lead/data quality] by ~Y…". Accelerates, recovers, eliminates are fine when they fit.
- 2–4 assumptions, each with a baseline number and a source or reasoning.
- Most sensitive to: the one assumption that breaks the claim if wrong.
- Pre-build estimate: the number, locked. If it can't be justified, widen the range and say so.

**Cut line:** an explicit list of what's out. V2 features go here as cut, not "later". Sanity check: does the MVP loop pass all six gates as scoped? If unsure, cut a feature.

**Done when:** B-00 sub-page is LOCKED with Real/Constructed/Mock tags, a value claim with sourced assumptions and a locked estimate, a cut line, and a checkable Definition of Done for the whole project.

## Gate 01: Context Sheet

**Objective:** turn vague personas into deterministic rules a human operator and an LLM can both run without guessing.

**Ask:** draft from research first, then ask at most 3 boundary questions, e.g. "Is a 10-person agency in-ICP or out?", "Does a pricing-page visit outrank a webinar signup?".

**Done when:** B-01 is LOCKED with hard bounds and exclusions, a signal taxonomy (high vs. low intent), a boolean tier rubric (Tier 1 high touch / Tier 2 automated / Tier 3 disqualify, or the track's equivalent), and a production system prompt that returns strict JSON. The prompt has been run on at least 2 sample records with the output pasted in.

## Gate 02: Process Architecture

**Objective:** draw the operational flow across teams before touching a tool.

**Ask:** 3 options for the main design choice (e.g. route on tier only vs. tier + territory vs. tier + account owner), then fallbacks and SLA timers.

**Done when:** B-02 is LOCKED with a Mermaid flowchart in plain language that renders, showing the entry trigger, a fallback when data is missing, the decision, routing splits, and an error path. Below it, plain-language sections give each branch's owner (system or team), deadlines (SLAs), and failure handling. Chart labels use simple words: no acronyms or tool names.

## Gate 03: Data Schema

**Objective:** design the data contract before building, so the CRM doesn't bloat.

**Ask:** which fields are worth storing vs. computing on the fly. Offer a lean field list and let him cut.

**Done when:** B-03 is LOCKED with a field dictionary (Field | Type | Source | Transformation | Destination property | Provenance), one input and one output JSON payload shape, and 3–5 sample records. Company attributes come from research (Real); private fields are Mock and labeled. The samples cover the happy path, a missing-data case, and a disqualify case.

## Gate 04: Build

**Objective:** make it run on the Gate 03 samples in the chosen stack.

**Micro-steps, one at a time, each tested before the next:**
1. Ingestion (webhook, form, scraper, CSV)
2. Enrichment and normalization (waterfall or mock enrichment, formatting)
3. AI reasoning (B-01 prompt + JSON parser + retry on bad JSON)
4. Routing and action (CRM upsert, Slack alert, sequencer push, or the track's equivalent)

Create `01 Projects/<project-name>/` here if the build is code. Commit as it goes.

**Done when:** B-04 is LOCKED with node or module configs, API calls used, and 3 recorded runs (raw input → transformed output) covering the three sample cases, plus the repo or workflow link. The system runs end to end with no manual steps.

## Gate 05: Case Study

**Objective:** turn the build into proof someone who wasn't there understands in 60 seconds.

**Ask:** nothing new until the draft is ready. Then confirm the hook and the estimate-vs-result explanation.

**Done when:** B-05 is LOCKED with estimate vs. result, a unit-economics ledger, a governance runbook (rate limits, bad JSON, duplicates, missing data) checked by `qa-auditor`, a README, the Loom script, and the rubric self-score. `/close-loop` has run and the My Portfolio row is proposed.
