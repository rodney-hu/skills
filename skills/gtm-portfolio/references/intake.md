# Intake

Goal: gather project context in one round so no gate starts from a blank page.

## Before asking

Read Rodney's message. Fill whatever he already gave (a company, URL, role, tool, metric). Ask only what's missing. If everything is answered, skip straight to research.

## The one AskUserQuestion call (max 3 questions)

**1. Track** (header: "Track")
- GTM / RevOps (Recommended): inbound routing, signal-based outbound, enrichment, lead scoring, CRM hygiene
- Marketing Ops: lifecycle, attribution, campaign ops, segmentation
- Sales Ops: territory and routing, pipeline hygiene, forecasting, handoffs
- Engineering: an internal tool, API integration, or data pipeline that solves a GTM problem

**2. Anchor** (header: "Company")
- Pitch me 3 companies (Recommended when none was named)
- I have one (they type the name or URL via Other)

**3. Role + metric** (header: "Prove")
Offer the 3 likeliest combos for the track, e.g. for GTM:
- GTM Engineer: pipeline
- RevOps / GTM Systems: cost (manual hours removed)
- Solutions / Forward-Deployed Engineer: CX (speed to lead)

## After the answers

1. Recommend one stack from `tracks.md`, one line of why. Default Claude Code. He confirms or swaps.
2. Note any skill he wants to stretch (SQL, APIs, prompt design). Make it load-bearing: the build should break without it.
3. If a tool is new to him, cut scope elsewhere to pay for learning it, and say so in the brief.
4. Run research (`research.md`), then pitch 3 scenarios.

## Seed rules (carried over)

- **Company** sets the data and context. Default anchor.
- **Role** sets what the project proves. Map it to 2–3 recurring requirements from live postings.
- **Skill** sets what gets stretched.
- **Tool** sets how it's built.
- When seeds conflict (a tool that doesn't fit the role's real workflow), resolve toward the role and say so in one line.
- A company-anchored project doubles as outreach leverage. If that's in play, say so in the brief: it raises the bar on the proof layer.
