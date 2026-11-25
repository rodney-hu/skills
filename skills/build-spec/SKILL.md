---
name: build-spec
description: >
  Turns a rough ask into a structured build spec that Claude Bot can paste into an eval-loop contract with little rewriting. Use when Rodney or a project lead wants a brief for a build, says "write a build spec", "brief Claude Bot", "turn this into a contract", or hands over a rough ask that needs a goal, a named deliverable, pass/fail checks, scope, tier, approvals, and a deploy target before a build starts. Not for fleshing out a raw product idea (use idea-to-blueprint), not for launching the build (that is eval-loop), and not for Notion project memory (use the Project Brief).
---

# Build spec

Turn a rough ask into a filled build spec. The output is the contract Claude Bot pastes into `.eval/contract.md`, plus a short Context / Inputs section.

You write the spec. You do not start the build, deploy, or invent a deliverable or an approval.

## Anti-jobs

- Do not write a PRD or run market research. If the ask is still a raw idea that needs shaping, point to `idea-to-blueprint` and stop.
- Do not launch eval-loop, edit the repo, commit, push, or deploy.
- Do not create or update Notion project memory. That stays in the Project Brief on the Active Projects row.

## Output

Write the spec using `${CLAUDE_SKILL_DIR}/assets/build-spec.template.md`. Headings under the contract must match `eval-loop`'s `assets/contract.template.md` exactly so the file pastes into `.eval/contract.md` with little rewriting.

Filled examples are in `${CLAUDE_SKILL_DIR}/references/examples.md`.

## Steps

### 1. Capture

Restate the ask in one or two sentences: the outcome, the named artifact if one was given, and any approval or deploy already stated. Do not add work the ask did not include.

### 2. Fill what you can

Map the ask onto every field below. Suggest a tier, a round budget, check IDs from the menus, and files in scope. Leave a field blank rather than guess the deliverable or the approvals.

### 3. Ask once for gaps

If a required field is empty or a check is vague, ask only for the missing items, in one short list. Do not interview. Do not produce a finished spec until those gaps are closed.

Required fields:

- **Goal.** One line. The outcome, not the activity.
- **Deliverable.** A named artifact, path, or URL. Never invent this. If the ask is "fix the headline" and the new copy was not given, ask for it.
- **Checks.** Each is `ID | pass/fail check | evidence`. Use IDs from eval-loop `references/checklists.md` (Copy C, Design D, Backend B, Product P). Add a gated check only when no menu ID fits, with a unique ID such as G1, and named evidence. Reject vague checks such as "looks good" or "is clean".
- **Files in scope.** One glob per line.
- **Out of scope.** What not to touch or add. Write `none` only when that is truly true.
- **Tier.** Light, Standard, or Full. You may suggest a default from the table below.
- **Round budget.** An integer that does not exceed the tier cap.
- **Approvals needed.** The exact actions that need Rodney's yes: push, deploy, merge, delete, spend, contact. Or `none`. Never invent an approval. If the ask says "redeploy", list `deploy`, and list `push` if the change has to land on the remote first. If the ask is silent, ask once.
- **Deploy target.** Platform, project, scope, and live URL, or `none`. If Approvals needed includes `deploy`, this cannot be `none`.

Context / Inputs is recommended: repo, existing brief, constraints, and known inputs. It is not a required contract field. Plan is optional when the steps are obvious from the checks.

### 4. Return the spec

Return the filled template and nothing after it, except a one-line note on any assumption that is not a required field, such as a suggested tier the sender can override.

## Field notes

Keep the prose short. Name the problem the change answers, the visible output, how it could fail silently, and the decision that stays with Rodney. The checks, not the prose, define done.

### Check selection

Read eval-loop `references/checklists.md` and copy the rows that apply. Do not rewrite a menu check's meaning.

- Always include B7 when the work is in a git repo.
- Include B1 when a build command exists.
- Include P1 and P4 on Standard and Full.
- Include copy, design, or backend menu rows that the change can fail.

### Tier defaults

| Tier | Use for | Default budget | Default checks |
|---|---|---|---|
| Light | copy tweak, one-file fix | 1 | the automated checks the change touches, usually B1, B7, and C5 when copy changes |
| Standard | feature or page | 2 | the relevant category menu, plus B1, B7, P1, P4 |
| Full | client-facing work, a spec demo, or a launch | 3 | every menu that applies |

Suggest a tier. The sender can pick a lower budget. Do not exceed the cap.

### Spec demo deploys

When the deliverable is a prospect demo page on Vercel, use this deploy target unless the sender gives a different one:

- Command, run from the demo's `site/` folder: `vercel deploy --prod --yes --scope house-of-hu --project <slug>-demo --non-interactive --verify`
- Live URL: `https://<slug>-demo.vercel.app`

Approvals needed in that case include `push` and `deploy` unless the sender says the operator will deploy after the run.

## Rules

- Do not guess a deliverable, an approval, or a live URL.
- Do not add work the ask did not include. Default menu checks for the chosen tier are the exception.
- Do not start the build.
