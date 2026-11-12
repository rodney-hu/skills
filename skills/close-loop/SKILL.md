---
name: close-loop
description: Close out a build session by saving it to Notion. Use at the end of any session where something was built, shipped, fixed, decided, or packaged - and whenever Rodney says "close the loop", "close out", "log this session", "wrap up", or "/close-loop". Reconciles this session's Shared checklist items on the Active Projects page (check off with evidence, or mark blocked, or release the claim), appends a Build Log entry, records durable decisions, and flags whether the work is packageable into GTM Portfolio. A build session is not done until this has run.
---

# Close the Loop

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

Notion holds project memory and the Shared checklist. Claude Code executes and keeps command-level steps locally. This skill moves what a session claimed, shipped, and decided into the project row so the next session or agent can continue without Rodney retelling it. It implements the Front Door's Shared checklist protocol and Build Workflow stages 5 to 7.

## Read first

1. Fetch the Agent Front Door: {{AGENT_FRONT_DOOR_URL}} (see "Shared checklist protocol").
2. Fetch the Build Log Template: {{BUILD_LOG_TEMPLATE_URL}}
3. Load the live Active Projects schema (`{{ACTIVE_PROJECTS_DS}}`) before writing any property.
4. Fetch the project page again. Read the Brief, Shared checklist, Decisions, and latest Build Log as they are now, not as cached at session start.

If any read fails, do not write from memory or cached state. Return a clearly UNSAVED block with the target item, evidence, and proposed update, and report **COMPLETED LOCALLY, NOT SYNCED** for finished work.

## Steps

### 1. Establish what actually happened

Do not ask Rodney to summarize. Derive it from the session, then confirm.

- What shipped: the artifact that now exists and can be opened, run, sent, or inspected.
- What changed: files, commits, configs, records. Link them.
- Validation actually run, observed results, and what remains untested.
- Decisions made and why.
- Issues found but not fixed.

If nothing inspectable was produced, say so. Research and planning alone are not Done.

### 2. Find the project

Search Active Projects by artifact and purpose, not title alone. If none exists and the work is a named artifact a stranger could inspect, propose a new row (Project Name, Deliverable, Definition of Done, Domain, Lane) and wait for Rodney's approval. Never create one silently. If the work does not qualify as a project, write nothing to Notion and say so.

### 3. Reconcile this session's checklist items

For each item this session claimed:

- **Done when is true:** check the box. Record the actual completing agent (Claude Code), the actual time, an inspectable output or link, observed validation, and untested limits. Never invent a test, owner, date, or source.
- **Not finished:** leave unchecked. If blocked, state the dependency, approval, or verification needed. If pausing available work, return it to Ready with a short handoff. In both cases, explicitly release the claim.
- Re-read the page before each write. Patch only that item. Do not touch other agents' claims or items.
- Items needing Rodney's approval stay Blocked on him. Completing a draft does not authorize publication, outreach, pricing, template activation, or evidence verification.
- If no checklist exists or imported state is uncertain, reconcile authorized scope against actual artifacts first. Do not invent a checklist, and do not add items beyond the authorized scope without asking.

Do not mark the project Done because every box is checked. Set `Status = Done` only when the Definition of Done is true and the artifact opens, with validation evidence.

### 4. Append the Build Log

Under `## Build Logs`, one entry per session, newest last, using the Build Log Template:

```
## YYYY-MM-DD: shipped artifact or meaningful change
### Shipped or changed
### Validation
### Decisions
### Issues and handoff
### Provenance
```

- Link the affected checklist items. Do not duplicate the checklist.
- Provenance names the actual agent and execution context. Never invent a session URL.
- No raw command output, chat transcripts, or implementation backlogs.
- Never rewrite earlier entries.

### 5. Record durable decisions

Add each under `## Decisions`: the decision, reason, source or trade-off, date, and agent. Link it from the log.

### 6. Verify every write

Reload the page. Confirm the checkbox state, claim or release text, log entry, and links are as intended. Only then report success.

### 7. Package proof (canonical routine; the only place a My Portfolio row is created)

Active Projects is the private workroom. My Portfolio is the public showroom. One project has one row in each, linked both ways. Never merge them and never copy the workroom into the showroom.

Only when the Definition of Done is true, the artifact opens, and Lane = Proof. Pipeline and Personal lanes get no portfolio row. Spec demos never get their own row: on approval, add the demo as an anonymized example on the existing "Spec-Demo Email Course Funnel" row.

1. Ask whether to package. Do not package automatically.
2. Search My Portfolio by the Active Project relation first. Reuse a row if found.
3. On Rodney's yes, create one row from the "Portfolio Project Packaging (Before → System → After)" template ({{PORTFOLIO_PACKAGING_TEMPLATE_URL}}): Packaging Status = Drafted, Active Project = this row. Proof Metric is one plain sentence with no category prefix. Without a measured baseline, report demonstrated output, not invented improvement figures. Anonymize client names and strip private research, IDs and the self-score.
4. Set this row's Proof Project to the new row.
5. Add a checklist item "Package proof" here (Done when: Packaging Status = Packaged). Put leftovers (Loom, repo push, test-record cleanup) in the checklist too. Never use My Portfolio's Next Action or Tasks fields.
6. Extract reusable prompts or SOPs to Templates as Draft, and content angles to Idea Vault. Never create Content HQ rows.

## Rules

- Never write to the hidden legacy fields: Tasks, Goal, Progress, Due Date, Priority, Next Action.
- Never create a task row, tracker, database, or property.
- Preserve unrelated content. Smallest targeted change.
- Never take over another session's claim.
- Write to Notion, not chat. A summary pasted into chat is not a closed loop.

## Finish

One line naming what was written (items checked or released, log added) and where, with the project row URL.
