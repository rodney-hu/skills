---
name: job-to-demo
description: "Turns a job post Rodney found into a built demo and outreach pack for the hiring manager: fit gate, asset game plan, Claude Code build spec, Loom script, DMs, email, follow-up. Use when Rodney shares a job post, job URL, or role he wants to apply to with a demo, or asks for proof-of-work, value-first, or permissionless job outreach. Not for company-signal prospecting or plain cold emails; use cold-email-writer for those."
---

# Job to Demo

Takes one job post and produces one working demo plus one outreach pack. The job post is
the signal: the company has said in public that it is hiring someone to own a specific
problem. Instead of sending a resume into the pile, Rodney shows he already understands the
problem and has built something toward it. Relevance earns the reply, not polish.

**Done =** a built demo that opens from a link with no login, plus
`outreach-brief-[company].md`. Not "researching," not "planning." If the verdict is PARK,
done = a one-line reason.

**Roles:** Claude plans and builds the demo. Rodney does QA and records the Loom.

## Inputs

- **Job post:** a URL or pasted text. Required. This skill does not search for job posts;
  Rodney supplies them.
- **Lane (optional):** if Rodney does not say, infer it in Phase 2.

## Phase 1: Decode the post

Fetch the post. Record the URL, the date it was posted or seen, and whether it is still open.
Then extract:

- **Company:** name, site, rough size and stage
- **Role:** title and who it reports to
- **Outcome they are hiring for:** one sentence, in their words where possible
- **Top 3 responsibilities:** quoted or closely paraphrased
- **Tools named:** CRM, automation, data, and outreach tools
- **Owner clues:** hiring manager, founder, or team lead named in the post or findable on LinkedIn

Add company context only as far as the demo needs it: what they sell, to whom, and the
public customer journey (homepage, pricing, signup or booking flow). Do not hunt for extra
signals. The post is the signal.

## Phase 2: Gate (build or park)

Build only if all five are true:

1. **Lane fit:** one of the three lanes below
2. **Size fit:** SMB or startup (founder-led or under about 200 people). Enterprise is a PARK.
3. **Role fit:** GTM engineering, RevOps, GTM systems, marketing or sales ops, or automation ownership
4. **Demo-able:** a useful piece of the outcome can be shown in one build, with public or synthetic data and no internal access
5. **Owner:** one identifiable person to send it to

**Lanes:**

- **Lane 1:** founder-led SMBs and startups, including coaching, consulting, and agency businesses
- **Lane 2:** MRI- or imaging-adjacent companies (imaging software, MRI safety, equipment, staffing). Nonclinical roles and demos only.
- **Lane 3:** wildcard, any company Rodney flags as interesting

If any check fails, the verdict is **PARK**. Write one line on why and stop. Do not invent a
reason to build. A skipped post costs nothing; a forced demo costs trust.

Keep three statements separate, because blending them is how outreach starts to sound like an accusation:

- **Observation:** what the post actually says
- **Hypothesis:** the problem underneath it, stated with its uncertainty
- **Demonstration:** what the demo shows (not what it proves about results)

## Phase 3: Pick one asset

Choose exactly one type, using what the post emphasizes most:

| The post emphasizes | Asset |
|---|---|
| Workflows, automation, CRM hygiene, enrichment, routing, data | **A. Working automation:** an n8n workflow (JSON) run against synthetic data, with a screen-recordable result |
| Demand gen, funnels, landing pages, lifecycle, onboarding, conversion | **B. Funnel or page mockup:** a deployed landing page or flow written for their actual buyer |
| "Own or build our GTM stack," first GTM hire, systems strategy, architecture | **C. System package:** an architecture diagram, a spec, a README, and supporting visuals |

If two types tie, pick the one Rodney can explain fastest on camera. One asset per post.

## Phase 4: Game plan and build spec

Write the plan as a handoff Claude Code can execute without guessing:

- **Problem from the post:** the responsibility it answers, quoted
- **Demo outcome:** what the hiring manager will see working, in one sentence
- **Input:** the synthetic or public data used, with a sample
- **Process:** steps, tools, and key decisions with reasons
- **Visible output:** what appears on screen
- **Labels:** what is mocked or simulated, stated on the asset itself
- **Link plan:** where it is hosted; it must open with no login
- **Acceptance criteria:** 3 to 5 checks that mean the demo works
- **Failure conditions:** where it could break silently, and what to check
- **Human judgment kept:** what stays Rodney's call (tone, claims, whether to send)

Rules for the demo: public or synthetic data only. No logins to their systems, no test
messages to their customers, no implied affiliation. Use their real buyer and product in
the content so it reads as made for them.

## Phase 5: Build

Build the demo by default. In Claude Code, build it directly. Elsewhere, run the parts that
need no repo, and hand the code parts to Claude Code with the Phase 4 spec.

- Put all files in `demos/[company]/`, with a README covering what it is, how to run it, and what is simulated
- Deploy or export to a link that opens with no login
- Check every acceptance criterion before calling the build finished

Then stop for Rodney's QA. Apply his feedback and check the criteria again. Keep iterating
until he approves the demo.

## Phase 6: Outreach pack

Read `references/templates.md` for copy format, DM rhythm, and a worked example. Produce:

- **Owner and channel:** the hiring manager or founder; LinkedIn if they are active there, otherwise a public professional email. One person, never a blast.
- **Loom script** (under 2:30, 4 beats):
  1. **Noticed:** "saw you're hiring a [role] to [outcome]." Show the post.
  2. **Understood:** the problem underneath it, framed as a hypothesis ("my guess is...")
  3. **Built:** run the demo. Show the result before you explain the tools.
  4. **Offer:** say what is simulated, invite a correction, give one easy next step, then stop.
- **Cover message (DM):** 2 to 3 separate short messages: (1) the demo and the link, (2) how it maps to the role, with one or two concrete uses, (3) the offer, on its own
- **Cover message (email):** one message, with at most one short line about Rodney
- **Follow-up:** one only, sent 4 to 7 business days later, adding something new (a screenshot or a takeaway). Never "bumping this."
- **Application note:** if there is a formal application, submit it too and put the demo link in the first line of any free-text field

Copy rules:

- All copy is lowercase except the letter I, including I'm, I'll, names, company names, acronyms, subject lines, and sign-offs. "lmk" stays lowercase. This is how Rodney writes, and it reads like a person, not a template. The brief's own headings stay in normal case.
- Plain words and short sentences, like a text to a colleague. No hype words, no em dashes, and no bold in the messages.
- Lead with the role and the demo. No mission praise, no resume summary, no tool list.
- Name the actual buyer, product, or workflow, not "your pipeline" or "your buyers."
- Describe what the demo could do, using "could" or "might." Share what was seen; never diagnose what is broken.
- No claims about saved hours, conversion, or revenue unless measured. Unmeasured numbers undo the trust the demo earned.
- DMs go out as separate messages, staggered rather than fired at once. Email stays one message.
- The first touch links to the demo or video on purpose, because the demo is the value.
- One ask only. No meeting request in the first touch. Pick one offer line: "happy to walk you through how I built it," "lmk if you want more info," or "lmk if it's relevant."

## Phase 7: Self-check before delivering

- The post is live, and its URL and date are recorded
- The gate passed on all 5 checks
- Observation, hypothesis, and demonstration are kept apart
- The demo meets every acceptance criterion and opens with no login
- Simulated parts are labeled on the asset
- Rodney has approved the demo after QA
- The Loom script runs under 2:30, and its first 5 seconds name the person and the role
- The DM is 2 to 3 short messages, with the offer last and on its own
- All copy is lowercase except the letter I
- There are no unmeasured claims, one owner, and one ask
- Would a busy hiring manager watch this past the first 10 seconds?

Fix anything that fails, then save the brief.

## Brief format

```
# [Company] / [Role] Outreach Brief
**Verdict:** BUILD | PARK (one line why)
**Lane:** 1 | 2 | 3
**Job post:** [URL, date posted or seen, still open Y/N]
**Outcome they're hiring for:**
**Owner / channel:**
**Observation:** / **Hypothesis:** / **Demonstration:**
**Asset type:** A | B | C, and why
**Build spec:** [Phase 4 fields]
**Demo link:** [no-login link] | **Files:** demos/[company]/
**QA status:** pending | approved
**Loom script:**
**Cover message (DM):**
**Cover message (email):**
**Follow-up:**
**Application note:**
**Next action:** [the one thing Rodney does next]
```
