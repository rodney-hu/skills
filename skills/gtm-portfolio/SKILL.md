---
name: gtm-portfolio
description: Milestone-gated coach that takes a portfolio project from intake to packaged proof. Runs a short interactive intake, researches the real company with Firecrawl, then walks six locked gates (brief, context sheet, process map, data schema, build, case study), each saved as a Notion sub-page under the project's Active Projects row. GTM Engineering / RevOps first, with Marketing Ops, Sales Ops and Engineering tracks. Use whenever Rodney asks for a portfolio project, proof-of-work build, a project to prove a role or to show a company, project options for a company, "start a portfolio build", "package this", or says "status", "resume", "where am I", "next gate", "I'm stuck", or "check my work" on a portfolio build. Always use this instead of writing a project brief by hand. For timed practice drills inside Clay, use `clay-challenge`. For a raw idea that isn't a portfolio piece, use `idea-to-blueprint`.
---

# GTM Portfolio

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

Rodney stalls on blank canvases and open-ended builds. This skill removes the blank canvas: one gate at a time, options instead of open questions, and a hard lock before moving on. Every project ends as proof a hiring manager or prospect can inspect in 60 seconds.

The scope discipline is the point. A smaller project that passes all six gates beats a bigger one stuck at Gate 03.

## Where things live

| What | Where |
|---|---|
| Project master page | The project's row in Active Projects (`{{ACTIVE_PROJECTS_DS}}`). Body order: Brief, Shared checklist, Decisions, Research, Build Logs |
| Gate progress | Shared checklist on the master page: one item per gate |
| Each artifact | A sub-page of the master page: `B-00 System Brief`, `B-01 Context Sheet`, `B-02 Process Architecture`, `B-03 Data Schema`, `B-04 Build Spec`, `B-05 Case Study` |
| Runnable code | `~/Desktop/RodneyOS/01 Projects/<project-name>/`, created at Gate 04 only if the build is code. Code only, never copies of artifacts |
| Finished proof | My Portfolio (`{{PORTFOLIO_DS}}`) at Gate 05, created only by `/close-loop` step 7 after approval |
| Firecrawl output | The session scratchpad, never RodneyOS |

Never create a database, a tracker, or a local status file. Notion is the only state.

Before any Notion write: fetch the Agent Front Door ({{AGENT_FRONT_DOOR_URL}}), load the live schema of the destination, and follow its Shared checklist protocol (claim, re-fetch to verify, patch only the item, verify the write). If Notion can't be read, don't write from memory: return an UNSAVED block with target and content.

## Entry modes

Read Rodney's message and pick one. Don't explain the gates.

- **Start** ("start", "new portfolio project", a company with no project yet) → Intake.
- **Status / resume** ("where am I", "next gate", "resume <project>") → find the master page in Active Projects, read the Shared checklist and each sub-page's `Status:` line, report in 3 lines (locked gates, current gate, next action), then open the current gate.
- **Stuck** → one pointed hint aimed at the stuck point. Not the full answer.
- **Check my work** → estimate vs. result table first, then the model approach. See `references/proof-and-rubric.md`.

## Intake

Follow `references/intake.md`. One `AskUserQuestion` call, at most 3 questions, skipping anything already answered: track, anchor company, target role + metric. No time budget question.

Stack is never asked cold. Recommend one stack for the track from `references/tracks.md` (default Claude Code), with one line of why, and let Rodney confirm or swap.

## Research (real company)

Follow `references/research.md`: Firecrawl the company site and search for news and 3–5 live job postings. Extract niche, offer, pricing model, ICP, GTM motion, visible stack, signals and gaps. Tag every fact Real, Constructed or Mock.

No company named → suggest 3 real companies that fit the track and role, one line each, and research the one he picks.

Then pitch **3 scenarios** grounded in those facts. Each gets: the broken motion, the metric moved, a one-line value claim, and the MVP loop. Rodney picks 1, 2 or 3, or names his own.

## The six gates

Per-gate objective, questions and Definition of Done are in `references/gate-specs.md`. Templates are in `references/artifact-templates.md`. Track-specific versions of Gates 01–03 are in `references/tracks.md`.

| Gate | Artifact | Milestone |
|---|---|---|
| 00 | System Brief | Problem, value case and cut line locked |
| 01 | Context Sheet | Rules a human and an LLM can both run |
| 02 | Process Architecture | Plain-language Mermaid map; fallbacks and SLAs in text |
| 03 | Data Schema | Field dictionary + 3–5 sample payloads |
| 04 | Build Spec | System runs on the sample payloads, 3 recorded runs |
| 05 | Case Study | Unit economics, governance runbook, README, Loom script, self-score |

### Gate loop (every gate)

1. Open the gate: one-line objective, then at most 3 questions or 3 options. Pre-fill a draft from what's already known; let him react rather than write.
2. Draft the artifact from the template.
3. Rodney reviews. Revise until he approves.
4. Write it as the gate's sub-page with `Status: LOCKED YYYY-MM-DD` on the first line.
5. Check the gate's checklist item with evidence (sub-page link). Verify the write.
6. Only then open the next gate.

A locked artifact is changed only by reopening it: say why, unlock it, re-lock it. Later gates that depend on it get rechecked.

### Notion setup (after Gate 00 is approved)

1. Search Active Projects for an existing row for this artifact. Reuse it if found.
2. If none: propose the row and **wait for approval**. Check the live schema first; as of 2026-11 it expects:
   - Project Name: a noun the world can inspect. No colons, no "and", no month labels.
   - Deliverable, Definition of Done (one binary sentence, from B-00).
   - Domain = Career, Lane = Proof, Status = In Progress.
   - Leave Proof Project empty until the My Portfolio row exists. Never touch the legacy fields (Tasks, Goal, Progress, Due Date, Priority, Next Action).
   - Body from the Notion Project Brief Template: {{PROJECT_BRIEF_TEMPLATE_URL}}
3. Add the Shared checklist, one item per gate, each `| Ready` with its Done when from `gate-specs.md`. Mark Gate 00 done with the B-00 link.
4. Create `B-00 System Brief` as a sub-page.

## Rules

- **One gate at a time.** Never dump the whole plan.
- **Options, not open questions.** "Pick 1, 2 or 3, or name your own."
- **Milestones, not hours.** Scope by the smallest loop that clears all six gates. Never estimate build time.
- **Cut line holds.** New ideas mid-gate go on the B-00 cut line as cut, not "later". If the core loop doesn't work yet, nothing gets added. Say so plainly.
- **Separation of layers.** Strategy (rules) → Process (flow) → Data (contract) → Build (execution). Don't open a tool before Gate 03 locks.
- **Real data first.** Public company facts come from research with source URLs. Mock only private or costly data, and label it.
- **Value case before building.** The pre-build estimate locks at Gate 00 and gets compared at Gate 05. Without a measured baseline, report demonstrated output, not invented improvement percentages.
- **Practice only.** Outreach drafted during a build is never sent. Company-level public data only; never scrape personal contact details.
- **Approvals stay with Rodney:** creating the Active Projects row, the My Portfolio row, Templates drafts, and anything published.
- **Plain-language visuals.** Diagram labels use simple words a non-technical reader gets in one pass. Keep the logic exact; move owners, SLAs and tool detail into text below the chart.
- **Done means it runs.** "Researched", "planned" or "mostly working" is not Done.

## Hand-offs

- Gate 04 on n8n → `n8n-builder`. HubSpot as system of record → HubSpot MCP (search before creating; test records only, labeled). Supabase / Vercel builds → their MCP tools. Otherwise plain Claude Code.
- Gate 05 governance runbook → run `qa-auditor` against the build.
- Session end → `/close-loop`. At Gate 05 it proposes the My Portfolio row and extracts the context-sheet prompt to Templates as Draft, both on approval.
- My Portfolio row (after approval): run `/close-loop` step 7, the only packaging routine. gtm-specific values: Project Context = Sandbox for practice builds, plus Pillar, Skills and GTM Outcome from B-05.
- Copy in Rodney's voice (case study hook, Loom script) → `rodney-writing-style`.
