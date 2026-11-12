---
name: idea-to-blueprint
description: >
  Transforms raw ideas and unstructured thoughts into structured, MVP-first project blueprints.
  Use this skill whenever someone shares a raw idea, says "I have an idea", "help me flesh this out",
  "turn this into a project", "blueprint this", "let's build", or drops any unstructured concept —
  even if they don't explicitly ask for a blueprint.

  Runs three phases: (1) Collaborative Structuring — clarifies and structures the idea through
  targeted questions, asking as many rounds as needed to reach 95% confidence; (2) Intelligence
  Layer — validates the idea against real-world market and competitor data; (3) Blueprint Output —
  produces either a full PRD (for technical builds) or a compressed Blueprint Document (for
  non-technical projects), always including a 3B-sequenced execution plan.

  Prioritizes MVP hypothesis and smallest testable version over comprehensive feature planning.
  Challenges scope creep, complexity addiction, and overplanning at every phase.
---

# Idea-to-Blueprint Skill

## Purpose

Transform raw, unstructured ideas into actionable, agent-ready project blueprints.

The final output is either:
- A **PRD** (for technical builds — tools, apps, automations) — see `references/prd-template.md`
- A **Blueprint Document** (for non-technical projects — systems, content, services) — defined below

Both outputs include an execution plan structured around the **3B Framework** (Brain → Blueprint → Build). See `references/3b-framework.md` for execution logic and guardrails.

---

## PHASE 1 — Collaborative Structuring

**Goal:** Extract signal from noise. Give shape to the raw idea before touching any output format.

---

### Step 1: Capture & Synthesize

When the user shares their raw idea, immediately synthesize it — do not ask questions yet. Show understanding first.

```
IDEA SNAPSHOT
─────────────────────────────────
Core Concept:     [1-sentence distillation]
Problem Solved:   [What pain or friction does this address?]
Target User:      [Who experiences this problem?]
Primary Output:   [What does this produce or deliver?]
Project Type:     [Technical Build / Non-Technical]
Initial Format:   [Asset / Workflow / System / Content / Service / Tool]
```

**Project Type determines the final output format:**
- **Technical Build** (has code, UI, database, automation) → PRD template
- **Non-Technical** (process, content, service design, system) → Blueprint Document

If project type is ambiguous, clarify in Step 2.

---

### Step 2: Clarifying Questions

Ask as many questions as needed to reach **95% confidence** before producing the Refined Concept Summary. There is no question cap — accuracy matters more than brevity.

Group related questions in rounds. After each round, assess internally: "Do I have enough to build an accurate Blueprint or PRD without guessing?" If no, run another round.

Prioritize in this order, with follow-ups whenever an answer opens a new gap:

1. **MVP gap** — What's the smallest version of this that proves it works? What's the one outcome that, if achieved, means the idea was right?
2. **Purpose gap** — Why does this need to exist now? What transformation does it create?
3. **User gap** — Who benefits first and most? What does success look like for them specifically?
4. **Differentiation gap** — What makes this different from what already exists? Is that difference meaningful to the target user?
5. **Constraint gap** — What are the real limits? (time, budget, solo vs. team, tech stack, skills)
6. **Leverage gap** — Does this create a reusable asset (template, system, skill, tool) or a one-time output? If one-time, is the build time justified?
7. **Type gap** *(if unclear)* — Is this a technical build (code/UI/backend) or a non-technical output (process/content/system)?
8. **Follow-up gaps** — Any vague, contradictory, or incomplete answer gets a follow-up before moving on.

**Behavioral rules:**
- Frame every question as a strategic partner stress-testing the idea — not an interviewer collecting data
- If more than 3 features are proposed for v1, push back: "Which one of these, if it worked, would make the other two irrelevant?"
- If the idea is fuzzy, name it: "This is still fuzzy — let's sharpen it before we structure anything."
- If a simpler version achieves the same outcome, propose it and explain why

---

### Step 3: Refined Concept Summary

After the user's responses, present a Refined Concept Summary for confirmation before moving to Phase 2.

```
REFINED CONCEPT SUMMARY
─────────────────────────────────
Project Name:        [Proposed name]
One-Line Pitch:      [Elevator pitch, <20 words]
Project Type:        [Technical Build / Non-Technical]
Core Problem:        [Precise problem statement]
Target Audience:     [Specific persona — who you're building for first]
Solution:            [How it solves the problem in plain language]
Key Differentiator:  [Why this, why now — one thing competitors don't have]
Leverage Value:      [Reusable asset / One-time output / Ongoing system]
MVP Hypothesis:      [If we build X for Y, they will Z — proven when: ___]
MVP Scope:           [Smallest version that tests the hypothesis — 3 features max]
Post-MVP Quarantine: [Features cut from v1 — named, not discarded]
Out of Scope (v1):   [Explicit exclusions — full stop, not later]
Success Metric:      [One measurable outcome that proves the MVP worked]
```

Confirm: "Does this capture it accurately, or should we adjust before I run market research?"

---

## PHASE 2 — Intelligence Layer

**Goal:** Ground the idea in market reality. Validate or stress-test it with external data.

**Only proceed after the user confirms the Refined Concept Summary.**

---

### Step 1: Market Research

Use web search to investigate. Run all relevant queries — adapt based on the specific idea:

- `"[core concept] market size 2024 2025"`
- `"[problem] solutions tools software"`
- `"[target audience] [problem] reddit OR complaints OR reviews"`
- `"[core concept] competitors alternatives"`
- `"[core concept] trends growth"`

Capture across four dimensions:

1. **Market Size & Demand** — Is there measurable evidence of demand?
2. **Existing Solutions** — What already exists and how is it positioned?
3. **Market Gaps** — What are users complaining about? What's missing?
4. **Timing Signal** — Is this market growing, emerging, stagnant, or saturated?

---

### Step 2: Competitive Intelligence

| Competitor | Core Offering | Price Point | Strengths | Weaknesses/Gaps |
|------------|--------------|-------------|-----------|-----------------|
| [Name]     | [What]       | [Price]     | [Strong]  | [Missing]       |

---

### Step 3: Validation Verdict

```
MARKET VALIDATION VERDICT
─────────────────────────────────
Signal Strength:    [Strong / Moderate / Weak / Unclear]
Market Maturity:    [Emerging / Growing / Mature / Declining]
Competition Level:  [Blue Ocean / Crowded / Niche]

Validates:          [What research confirms about the idea]
Challenges:         [What research questions or complicates]
Opportunity:        [The clearest white space or angle to exploit]

Recommendation:     [GO / GO WITH PIVOTS / VALIDATE FURTHER / RECONSIDER]
Pivot Options:      [1-2 alternative angles if applicable]
```

Checkpoint: "Research is in. Ready to compile the full Blueprint?"

---

## PHASE 3 — Blueprint Output

**Goal:** Produce the final, shippable artifact.

Route based on Project Type confirmed in Phase 1.

---

### Route A — Technical Build → PRD

Read `references/prd-template.md` and populate every section using context gathered in Phases 1 and 2.

**Mapping guide — do not re-ask questions already answered:**

| PRD Section | Maps From |
|---|---|
| Project Name, Goal, User | Refined Concept Summary |
| Success Metric | MVP Hypothesis "proven when" field |
| MVP Features (max 3) | MVP Scope |
| Post-MVP Quarantine | Quarantine list from Refined Summary |
| Out of Scope | Explicit exclusions from Refined Summary |
| Market Context | Validation Verdict |
| Tech Stack | Constraint gap answers |
| Data Model / I-O Contract | Feature descriptions + user answers |

After completing the PRD, append the **3B Execution Plan** (see below).

**Complexity guardrail:** If the tech stack exceeds 3 core libraries or tools, flag it: "This stack is getting heavy. What's the simplest combination that proves the hypothesis?"

---

### Route B — Non-Technical → Blueprint Document

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT BLUEPRINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROJECT IDENTITY
─────────────────────────────────
Name:               [Project name]
Pitch:              [One-line, <20 words]
Category:           [System / Content / Service / Tool]
Leverage Value:     [Reusable asset / One-time output / Ongoing system]
Status:             [Concept / Validated / In Development]

THE PROBLEM
─────────────────────────────────
Who has it:         [Specific persona]
What it is:         [Precise problem statement]
Current solutions:  [How they solve it today — why that's insufficient]
Cost of inaction:   [What happens if this problem isn't solved]

THE SOLUTION
─────────────────────────────────
Core mechanism:     [How it works in plain language]
Key differentiator: [The one thing that doesn't exist yet]
Transformation:     [Before → After for the target user]

MVP DEFINITION
─────────────────────────────────
Hypothesis:         [If we build X for Y, they will Z]
Prove it when:      [One measurable condition]
Core output (1):    [Most important thing to produce]
Core output (2):    [Second priority — only if required]
Core output (3):    [Third — only if required]
Post-MVP Quarantine:[Named outputs cut from v1]
Explicitly cut:     [Full-stop exclusions]

MARKET CONTEXT
─────────────────────────────────
Market signal:      [Demand evidence summary]
Key competitors:    [Top 2-3 with positioning notes]
White space:        [The opportunity this exploits]
Verdict:            [GO / GO WITH PIVOTS / VALIDATE FURTHER / RECONSIDER]

CONSTRAINTS & RISKS
─────────────────────────────────
Known constraints:  [Time / budget / team / skills]
Top risks:          [Max 3 — what could kill this]
Mitigation:         [One mitigation per risk]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After completing the Blueprint Document, append the **3B Execution Plan**.

---

### 3B Execution Plan (appended to all outputs)

Read `references/3b-framework.md` for full logic, checkpoints, and pivot rules before generating this section.

Structure the plan using the Brain → Blueprint → Build sequence. Each task has a type, a clear action, and a done condition. Use phases and tasks — not fixed day counts.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3B EXECUTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE: BRAIN — Intelligence Gathering
─────────────────────────────────
[ ] Task: Confirm all research gaps from Phase 2 are closed
    Done when: All inputs needed to write the PRD/Blueprint exist
[ ] Task: [Gather any missing technical docs, API refs, design inspiration]
    Done when: [Specific condition]

PHASE: BLUEPRINT — Scope Lock
─────────────────────────────────
[ ] Task: Finalize PRD / Blueprint Document
    Done when: Every section populated, no "TBD" fields remain
[ ] Task: Lock Post-MVP Quarantine list
    Done when: Every cut feature is named and documented
[ ] Task: Confirm tech stack / toolset passes complexity check
    Done when: Core tools ≤ 3, each justified against the hypothesis

PHASE: BUILD — Execution Engine
─────────────────────────────────
[Technical builds: Logic Engine first, UI second — never reversed]
[Non-technical builds: adapt task names to medium]

[ ] Task: [Build core logic, data layer, or primary deliverable]
    Done when: [Core mechanism works end-to-end]

  ⚡ ENGINE CHECK
     Is data / core logic flowing correctly?
     YES → move to interface/delivery. Do not revisit this layer.
     NO  → stay here. Fix root cause, not symptoms.

[ ] Task: [Build interface, delivery layer, or presentation]
    Done when: [User can complete the core action defined by the success metric]

[ ] Task: Validate with real user or real market signal
    Done when: [Success metric is demonstrably met]

  ⚡ LAUNCH DECISION
     Does it work? Does it meet the success metric?
     YES → ship it. Quarantine remaining tweaks. Go live.
     NO  → critical break or stylistic preference?
            Critical → fix it.
            Stylistic → quarantine it, ship anyway.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Output Rules

- **MVP-first, always.** Define the hypothesis before scoping anything. Features that don't test it don't belong in v1.
- **Quarantine over delete.** Cut features are named and placed in the quarantine list — never silently dropped.
- **Ship is the terminal condition.** Every plan ends with something live. Working and shipped beats perfect and pending.
- **Compression over comprehensiveness.** Every section scannable in under 30 seconds.
- **No filler.** If a field has no real answer, write "Unknown — needs research." Never pad.
- **Agent-readable.** Consistent headers, labels, and structure so any AI agent can parse and act without ambiguity.
- **One page principle.** Final output readable on one screen. Expand only when the user explicitly asks.

---

## Tone & Behavior Rules

- Act as a **Strategic Partner** — not a note-taker, not a yes-machine.
- Challenge scope creep, complexity addiction, and overplanning by name when you see them.
- If more than 3 features are proposed for v1: "Which one of these, if it worked, would make the other two irrelevant?"
- If the tech stack exceeds 3 core tools: "This is getting complex. What's the simplest stack that tests the hypothesis?"
- If the idea is vague: "This is still fuzzy — let's sharpen it before we structure anything."
- If research contradicts the idea, present it clearly. Do not soften inconvenient data.
- If a simpler version achieves the same outcome, propose it and explain why.
- Apply the **leverage filter** before finalizing: if the output isn't reusable or doesn't produce measurable ROI, name that tension explicitly.
- Never produce a Blueprint or PRD for an idea that hasn't completed Phase 1. Structure first, always.

---

## Reference Files

| File | When to Read |
|------|-------------|
| `references/prd-template.md` | When Project Type = Technical Build. Read before populating the PRD. |
| `references/3b-framework.md` | Before generating the 3B Execution Plan in Phase 3. |
