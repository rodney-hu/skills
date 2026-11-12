# Tracks and stack

GTM / RevOps is the default. The other tracks keep the same six gates; only the Gate 01–03 artifacts change shape.

## Artifact by track

| Gate | GTM / RevOps | Marketing Ops | Sales Ops | Engineering |
|---|---|---|---|---|
| 00 Brief | Motion: Inbound (capture → qualify → route) or Outbound (signal → enrich → score → engage) | Lifecycle stage or campaign that leaks | Handoff, territory or forecast that breaks | The GTM problem the tool solves |
| 01 Context | ICP hard bounds, signal taxonomy, tier rubric, LLM system prompt | Segment definitions, lifecycle stage rules, lead-score model | Territory and assignment rules, stage exit criteria, SLA matrix | Requirements, acceptance criteria, non-goals |
| 02 Process | State machine: trigger → enrich → AI decision → route, with SLAs and dead-letter queue | Lifecycle or campaign flow, with suppression and re-entry rules | Lead → opp → close handoffs, round-robin, escalations | Sequence or architecture diagram with failure paths |
| 03 Data | Field dictionary + webhook in/out payloads | UTM and attribution schema, event taxonomy | CRM object model, field ownership, stage definitions | API contract or DB schema + fixtures |
| 04 Build | Orchestration: ingest → enrich → reason → route | Automation + reporting view | Routing or hygiene automation + pipeline view | Working code + tests |
| 05 Package | Speed-to-lead or research hours saved | Attribution coverage or cycle time | Hours saved or data-quality score | Runtime, cost per run, coverage |

## Stack menu

Default **Claude Code**. Recommend one stack per project, with one line of why.

| Tool | Use when |
|---|---|
| Claude Code | Default. Scripts, LLM reasoning steps, glue, anything code-first |
| n8n | The proof is a visual, triggerable workflow a GTM team would own. Build with `n8n-builder` |
| Grokbot | An always-on agent or chat-surface step is part of the system |
| Vercel | The proof needs a live URL (form, demo, dashboard) |
| Supabase | The build needs a real database, auth, or edge functions |
| Python | Data cleaning, scoring models, batch jobs |
| HubSpot CRM | The system of record for CRM-type builds. Test records only, labeled |
| Clay | Optional enrichment step only. Free plan, limited credits: default to mock enrichment and show where Clay slots in |

Not used: Make. Notion is never a stack choice; it's the storage layer for every project.

Suggested defaults by track:
- GTM / RevOps → Claude Code + HubSpot (n8n if the role asks for workflow tools)
- Marketing Ops → n8n + HubSpot
- Sales Ops → HubSpot + Claude Code
- Engineering → Claude Code + Supabase, Vercel if it needs a URL
