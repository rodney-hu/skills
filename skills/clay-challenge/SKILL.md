---
name: clay-challenge
description: Generates Clay Cup-style GTM engineering practice challenges for sharpening skills in Clay (clay.com) — either a full business-problem brief (scenario, ICP, deliverables, rubric) or a timed data-race drill (30 tiered numeric questions), modeled directly on how Clay's own Clay Cup competition packages problems for competitors. Use this skill any time Rodney asks for a Clay practice challenge, a GTM engineering problem to build, wants to sharpen his Clay skills, mentions "Clay Cup", "practice problem", or "business problem to solve in Clay" — and especially when he gives a company name or website and wants a challenge built around it. Also use it when he returns to check his work, asks for a hint, or is stuck mid-build on a challenge this skill produced. Always use this skill instead of writing a challenge by hand, even for a quick one-off request.
---

# Clay Cup-Style Challenge Generator

## Why this exists

Clay Cup (Clay's live GTM engineering competition) packages real business problems into a tight, repeatable structure: a scenario, one objective, a hard time box, a fixed set of deliverables, and a rubric. That structure is *why* it works as a training tool — it forces the same reps (define the ICP, pick validation signals, build a scored list, write a message that doesn't sound copy-pasted) over and over on different material, which is exactly what sharpens Clay fluency.

This skill produces that same structure so Rodney can generate a fresh, realistic problem on demand and go build it live in Clay — the way a Clay Cup competitor would, minus the bracket.

## Step 1: Figure out what to generate

Two independent choices need to be made before you can write the challenge: **format** and **subject**. If Rodney's message already answers both (e.g. "give me a hiring-themed data race" or "build me a lead-gen challenge for notion.so"), skip straight to Step 2/3 — don't make him click through questions he's already answered.

If either choice is genuinely ambiguous, ask using a quick-select tool (e.g. `ask_user_input_v0`) rather than a wall of prose questions — this mirrors how Clay Cup itself is a fast, low-friction pick:

- **Format:**
  - *Build-a-GTM-system brief* — a scenario + 4 deliverables, ~20–30 min build (see `references/scenario-categories.md`)
  - *Data-race drill* — 30 tiered numeric questions, 20-minute timed sprint (see `references/data-race-question-bank.md`)
- **Subject:**
  - *Fictional company* (default, no research needed)
  - *Real company* — Rodney gives a name or URL; ground the scenario in what you find (Step 2)
- **Category** (build-a-system only, if not implied by subject): Lead-gen & prospecting / Hiring & recruiting / Market research & competitive intel / Event ops & partnerships — see `references/scenario-categories.md` for what each implies. Rotate away from whatever category was used last in this conversation rather than repeating it.

## Step 2: If a real company is named, research it first

When Rodney gives a company name or URL, treat it as the seed for a grounded scenario — this is what makes the practice transfer to real prospecting/outreach work, not just generic trivia.

1. `web_search` / `web_fetch` the company: what they do, funding/stage signals, hiring page or recent news, competitors, anything that suggests a real ICP.
2. Use real facts for the *setup* (industry, stage, product, a real signal like a funding round or open role). Invent only what the exercise needs and doesn't exist publicly (e.g. an exact internal objective) — and say so plainly in the brief so Rodney knows what's real vs. constructed.
3. **State clearly in the brief that this is a practice exercise** — any outreach message drafted is for skill-building only and isn't meant to be sent to the real company. Don't imply the exercise involves actually contacting real people.

If Rodney gives a company but not a category, pick the category that fits what you find (e.g. a company mid-hiring-spree → recruiting; a company with no visible outbound motion → lead-gen) and say why in one line.

## Step 3: Write the challenge

Use the matching template from `references/scenario-categories.md` (build-a-system) or `references/data-race-question-bank.md` (data race). Both share the same discipline Clay Cup uses:

- **One page.** If the brief is sprawling, it's not a Clay Cup-style brief anymore — it's a spec document. Cut it back. This also keeps it fast to read under a live clock, which is the point.
- **One concrete objective**, not a bundle of goals.
- **A stated time box.** Default 20 minutes for a warm build, 30 for a first attempt at a new category — say which and let Rodney adjust.
- **"Build only in Clay"** stays the default constraint (matches the actual competition and forces real reps instead of pre-built templates/Sculptor shortcuts). Only relax this if Rodney asks for an easier on-ramp.

For a **data-race drill**, do not resolve the answers as part of generating the challenge — the entire point is that Rodney builds the Clay workflow to find them himself. Only look answers up afterward if he explicitly asks you to check his results.

## Step 4: Always include the self-scoring rubric

This is what Clay Cup judges actually score on — attach it verbatim (adapt tense/wording minimally) to every build-a-system brief:

> **Self-score each build, 1–5 on:**
> - **Problem framing** — did you nail the *ideal* profile, not just "a good" one?
> - **Logical structure** — clear ICP → validation signals → scored list → output, in that order?
> - **Effective use of Clay primitives** — waterfalls, AI columns, Claygent, formulas chosen deliberately, not just thrown at the prompt?
> - **Execution speed** — visible progress inside the time box, not stalled on setup?
> - **Ability to explain decisions** — could you defend every column to a judge who knows exactly where it'll break?
> - **Personalization standout** — would the final message be obviously non-generic to the recipient?

For a data-race drill, swap the rubric for: raw score out of 6000 (10×100 + 10×200 + 10×300), plus a note on which tier slowed you down most.

## Step 5: Deliver it

Output the finished challenge as an artifact (markdown) — it's a standalone reference document Rodney will keep open while building in Clay, not something to bury in chat prose. Keep the tone like an actual competition brief: crisp, a little high-stakes, no hedging or meta-commentary about how it was generated.

Mention in passing that a way to check his work exists once he's built something — don't dump it in the same breath as the challenge, and don't ask a generic "want another?" either. If natural, offer the specific next lever (e.g. "next one could hit the market-research category, or I can run the same scenario as a data race instead").

## Step 6: Prepare a way to self-check — but keep it withheld until asked

Rodney wants to know if he's doing well, or get unstuck, without the challenge being spoiled before he's attempted it. That means: build the checking material, but never surface it in the same turn as the challenge itself. Only produce it when he actually asks — for a check, a hint, or because he's stuck.

There are two tiers. Read the ask and give the right one:

- **A nudge** — he's mid-build and stuck on one piece (e.g. "what am I missing on validation signals?"). Give one pointed hint, not the full reference. This is closer to what a competitor would get from a coach mid-round than a graded rubric.
- **A full reveal** — he's done, or wants to check everything. Give the complete reference below.

**For a build-a-system brief:** the reference is a **model solution**, not a single correct answer — these scenarios don't have one. Write, for the same 4 deliverables: an example strong ICP statement, an example set of 3–5 validation signals with a one-line reason each is high-signal, the scoring logic that would rank the list, and one example message that demonstrates real (not generic) personalization. Frame it explicitly as *one* strong approach: "check whether your reasoning holds up against this, not whether you matched it exactly."

**For a data-race drill:** don't pre-resolve all 30 answers when you first generate the drill — that's wasted work if he never asks, and the questions should stay unresolved so the exercise is real. When he does ask to check results, look up the actual answers at that point (all 30, or just the ones he flags) and compare against what he got.
