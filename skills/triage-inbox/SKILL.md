---
name: triage-inbox
description: Process the Notion Idea Vault capture inbox. Reads every row with Status = Inbox, fills Type, Domain, Source, Summary (and Pillar only when content-relevant), then proposes exactly one destination per row for approval. Use whenever Rodney says "triage", "triage my inbox", "process my captures", "clear the inbox", "what's in my inbox", or "/triage-inbox", and on any scheduled inbox run. Never routes anything without approval.
---

# Triage the Inbox

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

Idea Vault is the only capture inbox. Three doors feed it: AudioPen via Zapier, the Notion Web Clipper, and `capture this` said to an agent. Policy lives in the Agent Front Door; this skill follows it.

Captures rot when sorting is manual and optional. This runs on a Sunday schedule and on demand.

## Read first

1. Fetch the Agent Front Door: {{AGENT_FRONT_DOOR_URL}}
2. Load the live Idea Vault schema: `{{IDEA_VAULT_DS}}`. Use only option values it returns.

If either fetch fails, do not write from memory. Return a clearly UNSAVED block with the proposed properties per row.

## Step 1 - Read the queue

Query every row where `Status = Inbox` or `Status` is empty. Oldest first.

Read the actual content: page body, `Raw Transcript`, `AudioPen`, `Summary`, `Primary Link`. Do not classify from the title alone. A voice dump's title is often the weakest signal in the row.

## Step 2 - Fill the metadata

Rodney never fills these at capture time. Inbox means not yet processed, not permission to leave basic metadata blank. Fix only unambiguous metadata, and leave anything already set alone.

| Property | How to set it |
| :--- | :--- |
| `Type` | Journal, Idea, Insight, Clip, Transcript, or Note (reference notes that fit none of the others) |
| `Domain` | Career, Business, or Personal. This is the Idea Vault list, not the one Templates and Agents use |
| `Source` | Only if empty. AudioPen if the AudioPen field is populated. Browser if Primary Link is set and the body is clipped material. Claude Code or Grokbot if that agent captured it. Agent only for other agents, naming the actual agent in the body. Otherwise Manual |
| `Summary` | Two lines maximum. What this is and why it was worth keeping. Leave as-is if populated |
| `Pillar` | Only when the item is relevant to content: Authority Amplifier, Personal Reflections, Healthcare Insights, or Tech & Tools. Otherwise leave blank |
| `Topic` | A short noun phrase, only when it adds retrieval value |

Leave `Insights` for entries that genuinely contain a reusable lesson. An empty field beats a padded one.

## Step 3 - Propose exactly one destination

One row, one route. Present the whole batch as a table and wait for approval. Search the destination for an existing match before proposing a new row.

| Route | When |
| :--- | :--- |
| **Journal** | Stream-of-consciousness, reflection, processing. Terminal destination |
| **Project task** | Contains a concrete commitment tied to an existing project. Propose the exact checklist item and its Done when for that Active Projects page. Add it only on approval and within Rodney's authorized scope, as Ready or Blocked. Never claim or start it from triage. Keep the capture in Idea Vault |
| **Project** | A named artifact a stranger could inspect. Rare. Propose a new Active Projects row with Deliverable and Definition of Done. Never create it unapproved |
| **Resource** | A tool, GPT, program, domain, or bookmark. Resource Library, new rows start Draft |
| **Template** | A reusable prompt, framework, or SOP. Templates, status Draft. Link the original source |
| **Evidence** | A single sourced stat, quote, pain point, objection, trend, or story worth independent reuse. Evidence Library, status Unverified. Do not split every sentence into a row |
| **Company** | Findings about a target company. Update the existing Ikigai Business Targets row; do not duplicate as a generic note |
| **Content candidate** | A publishable angle. Keep it in Idea Vault with `Pillar` set. Claude Code never creates Content HQ rows; Rodney or an authorized content agent promotes it |
| **Archive** | Dead, superseded, or never worth acting on. A valid and honest destination |

### Journal is terminal, not a staging state

Brain dumps stay in Idea Vault. Set `Type = Journal` and `Status = Processed`. They surface in the existing Journal view. Do not force a journal entry into another route just to clear the queue.

Summarize and type a journal entry. Do not mine it for action items unless it contains an explicit commitment. If a real next action is buried in one, propose it as a Project task **and** keep the entry as Journal.

### Skip parked rows

Rows captured with `park this` are deliberate not-now. Idea Vault has no field that marks them, so only skip a row whose body or Summary says it is parked. When unsure, ask.

## Step 4 - Execute on approval

After Rodney approves:

- Create or update the destination row. Match the destination's live schema and carry source links. Keep Evidence Unverified.
- Mark the Idea Vault row `Status = Processed` only after the summary, extraction, or filing is actually complete. Use `Archive` for dead items.
- Verify each write by reloading the row before reporting it.

**Nothing leaves Inbox without a destination.** Archive is a destination. Limbo is not.

## Rules

- Never auto-route. Propose, wait, then execute.
- Never create a Notion database or property.
- Never create Content HQ rows. Never activate a Template or verify Evidence.
- Search before creating. Preserve unrelated content.
- If a capture is genuinely ambiguous, say so and ask. Do not guess a Domain or invent a Pillar to fill the field.

## Finish

Report: how many rows were processed, the route split, how many remain, and the age of the oldest thing still in Inbox. One short block, no preamble.
