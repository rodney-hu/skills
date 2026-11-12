# Proof layer, rubric, and coaching modes

## B-05 sections

**Estimate vs. result**
| | Value |
|---|---|
| Pre-build estimate (from B-00) | |
| Result on sample data | |
| Gap | |
| Explained by | [which assumption moved, and why] |

**Unit economics ledger.** Cost per 1,000 runs (LLM tokens, API calls, enrichment credits) vs. human hours replaced. Show the math. Every input tagged Real/Constructed/Mock. Label the result an estimate. Without a measured baseline, report demonstrated output (e.g. "3/3 sample records routed in under 40 s"), not invented improvement percentages.

**Governance runbook.** How the system handles rate limits, bad JSON, duplicates, missing data, and API failure. Run `qa-auditor` on the build and fold in its findings.

**README**, six short sections:
- The problem (2–3 sentences)
- The value claim and its key assumption
- The approach and why (decisions, not a file list)
- How to run it
- Estimate vs. result
- What I'd do differently

**Architecture.** The B-02 diagram redrawn to match what was actually built.

**Loom script** (recorded after Done, one take, ≤3 min):
- `0:00` The bottleneck
- `0:45` The architecture
- `1:30` Live run
- `2:30` Unit economics and impact

Write hook and script in Rodney's voice via `rodney-writing-style`.

Adapt the proof to the role: a RevOps project may be better shown by a dashboard or documented workflow than a repo.

## Rubric (self-score 1–5, include verbatim)

> - **Problem framing:** is the problem sharp enough that the solution is obviously the right shape?
> - **Approach quality:** could you defend every architecture and tooling choice to someone who knows where it breaks?
> - **Shipped completeness:** does it meet the Definition of Done end to end, without you standing next to it?
> - **Scope discipline:** did you hold the cut line, or did it sprawl?
> - **Legibility:** could a hiring manager understand the value in 60 seconds without your narration?
> - **Role relevance:** does this map to real requirements in real job postings?
> - **Value case:** is the claim specific, are the assumptions sourced, do you know which one breaks it, and how did the result compare to the estimate?

## Coaching modes

**Stuck (nudge).** One pointed hint aimed at the exact stuck point, like a colleague over the shoulder. Don't hand over the section that resolves it.

**Check my work.** Open with the estimate-vs-result table. Then a model approach:
- Example problem definition
- Example approach decisions, each with reasoning and trade-off
- What Done looks like
- Example README opener

Frame it as one strong approach, not the answer. Don't produce the model approach unless asked.

After Gate 05, offer the single natural next lever if there is one (e.g. "the same build could target Sales Ops at the same company"), not a generic "want another?"
