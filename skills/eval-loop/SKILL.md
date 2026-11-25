---
name: eval-loop
description: Build to a goal contract and iterate until every check passes. Takes a goal, a named deliverable, pass/fail checks, files in scope, out of scope, approvals needed, deploy target, tier and round budget; builds, runs the checks, has the read-only eval-reviewer subagent grade the work against the contract, fixes only failing checks, and enforces a score ratchet so each version is no worse than the last. Use when Rodney or Claude Bot runs "/eval-loop", hands over an approved plan, build spec, or goal contract, or says "build until the checks pass", "run the eval loop", or "iterate to the goal".
---

# Eval loop

You are the builder. The contract defines done. A separate reviewer grades. You never grade your own work and never add work the contract did not ask for.

All loop state lives in `.eval/` at the project root:

| File | Committed | Purpose |
|---|---|---|
| `contract.md` | no | this task's contract |
| `rounds/<n>/` | no | evidence per round: check output, screenshots, verdict |
| `handoff.md` | no | 5-line handoff for the next session |
| `checklist.md` | yes | project checks added from Rodney's manual fixes |
| `scores.json` | yes | ratchet log, one entry per version |
| `golden.md` | yes | best example per artifact type |
| `parked.md` | yes | ideas raised during builds, never built without approval |

On first run, create `.eval/` and copy `${CLAUDE_SKILL_DIR}/assets/eval.gitignore` to `.eval/.gitignore`.

## 1. Load the contract

Input is `$ARGUMENTS`: a path to a contract, or a goal and plan inline. If inline, write it to `.eval/contract.md` using `${CLAUDE_SKILL_DIR}/assets/contract.template.md`.

A valid contract has these fields: goal, deliverable, checks, files in scope, out of scope, approvals needed, deploy target, tier, and round budget. Every check is pass/fail and names its evidence (command, screenshot, or reviewer). Deliverable must name an artifact, path, or URL. Approvals needed and deploy target may be `none`. If approvals needed includes `deploy`, deploy target cannot be `none`. If a field is missing or a check is vague ("looks good", "is clean"), stop and return the gap. Do not guess.

Then:
- Append every item in `.eval/checklist.md` that applies to the artifact type. These are standing checks.
- Run `python3 ${CLAUDE_SKILL_DIR}/scripts/scope_check.py --init` to record the starting point.
- Read the latest entry in `.eval/scores.json`. Those passed checks are the ratchet floor.
- If `.eval/golden.md` has an entry for this artifact type, the reviewer compares against it.

Check menus by category are in `${CLAUDE_SKILL_DIR}/references/checklists.md`. The contract already names its checks; use the menu only when the contract says "use the <category> menu".

## 2. Tier

| Tier | Use for | Checks | Reviewer | Rounds |
|---|---|---|---|---|
| Light | copy tweak, one-file fix | automated only | none | 1 |
| Standard | feature, page | automated + reviewer | eval-reviewer, 1 pass per round | up to 2 |
| Full | client-facing, spec demo, launch | full menus + ratchet + golden | eval-reviewer every round | 3 |

The contract's round budget wins if lower. Never exceed the tier cap.

## 3. Models

- Builder: the session model. Claude Bot starts loops with `--model sonnet`.
- Reviewer: `eval-reviewer` (pinned to Opus, read-only).
- Research, lookups, docs: spawn a subagent with `model: haiku`.
- Do not switch the builder to Opus mid-loop. If Sonnet fails the same check twice, stop (rule below) and say so.

## 4. Round loop

For round n = 1 to budget:

1. **Build.** Round 1 implements the plan. Later rounds touch only what the failing checks name. Edit only files in scope.
2. **Scope guard.** Run `python3 ${CLAUDE_SKILL_DIR}/scripts/scope_check.py .eval/contract.md`. It lists changed files outside scope. Revert any out-of-scope change with `git checkout -- <file>` (or delete a new file you created) before continuing.
3. **Automated checks.** Run every check that has a command. Save output to `.eval/rounds/<n>/`. Capture screenshots for design checks (375px and 1280px) with whatever the project uses (Playwright, the browser tool) and save them there.
4. **Review** (Standard, Full). Run the reviewer in the foreground (never in the background) and wait for its verdict before doing anything else or ending your turn; in headless `claude -p` runs a background subagent is killed when the run ends. Delegate to the `eval-reviewer` subagent: "Grade round <n>. Contract: .eval/contract.md. Evidence: .eval/rounds/<n>/." Save its verdict to `.eval/rounds/<n>/verdict.md`. If `eval-reviewer` isn't installed, spawn a general subagent with `model: opus`, tools limited to Read, Grep, Glob and Bash, and the body of `${CLAUDE_SKILL_DIR}/agents/eval-reviewer.md` as its instructions. Its verdict is final for that round. You may not overrule it, re-run it hoping for a different answer, or edit the evidence.
5. **Ratchet.** Any check that passed in the previous version and fails now is a regression. Revert the change that caused it before anything else.
6. **Stop** when any of these is true:
   - every check passes
   - the round budget is spent
   - the same check fails in two consecutive rounds
   - a real decision needs Rodney (scope, money, brand, a trade-off the contract doesn't settle)

   Otherwise go to round n+1 with only the failing checks.

**Ideas are not work.** Anything you or the reviewer think would be better but no check requires goes to `.eval/parked.md` as one line with the date. Never build it in this loop.

## 5. Record

1. Append to `.eval/scores.json` (format in `${CLAUDE_SKILL_DIR}/assets/scores.example.json`): version, date, goal, tier, rounds, models, passed check IDs, failed check IDs, artifact.
2. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/ratchet.py .eval/scores.json`. Report any regression it prints.
3. If every check passed on a Full tier and the reviewer rated it at or above the golden example, replace that `golden.md` entry with a pointer to this artifact (path or commit) and one line on why.

**Manual fixes become checks.** When Rodney says he fixed something by hand, or the next contract includes a fix to your last output, add a pass/fail check for it to `.eval/checklist.md` with the date and the artifact type. The bar only rises.

## 6. Context hygiene

- One contract per session. Start a fresh session for the next task.
- When context is heavy, run `/compact` with: "Keep the contract goal, the deliverable, every check ID with its current pass/fail, decisions made, files touched, and the current round number. Drop file contents and tool output."
- Re-read `.eval/contract.md` after any compaction before touching code.

## 7. Finish

1. Write `.eval/handoff.md`, exactly 5 lines: goal, result (passed/total), what changed, what's open, next step.
2. Run `/close-loop` if the project has a Notion row. If close-loop can't sync, say so; do not skip silently.
3. End with this block and nothing after it:

```
EVAL RESULT: <PASS | STOPPED: reason>
Goal: <one line>
Tier: <tier>  Rounds: <used>/<budget>  Models: builder <model>, reviewer opus
Score: <passed>/<total>  (last version <passed>/<total>, delta <+/-n>)
Checks:
- [PASS|FAIL] <id> <check> — <evidence path or command result>
Regressions: <none | ids, reverted>
Parked ideas: <none | one per line>
Needs Rodney: <none | the decision>
Artifact: <the deliverable: path, URL, or commit>
```

## Rules

- Never deploy, merge, push to main, delete data, spend money, or contact anyone unless that exact action is named under Approvals needed and Rodney has already given his yes, quoted, to Claude Bot. Approvals needed is not itself permission. If it is `none`, those actions stay forbidden.
- Never edit the contract to make a check pass. A check that's wrong is a "Needs Rodney" item.
- Never mark a check PASS without evidence you can point to.
