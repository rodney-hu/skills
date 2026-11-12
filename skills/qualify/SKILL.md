---
name: qualify
description: >
  Runs Step 2 of the Pre-Sold Protocol prospecting pipeline: pulls all Status = New leads
  from the Notion CRM, fetches each prospect's homepage, applies a pass/fail
  qualification check, writes a precise Trigger observation, and updates each record to
  Qualified or Disqualified. Use this skill whenever Rodney says "run Qualify", "qualify
  the leads", "qualify batch", "run step 2", or any request to process New leads from the
  CRM. Always run after Block A (Curate) and before Step 3 (Research).
---

# Step 2: Qualify

> **Config:** values in `{{DOUBLE_BRACES}}` come from `config.local.md` in this skill's folder. If it is missing, copy `config.example.md` to `config.local.md` and fill it in.

## What This Step Does

Pulls every lead with Status = New from the Notion CRM, fetches their homepage, and
applies a pass/fail check. Pass → Status = Qualified + Trigger written. Fail → Status =
Disqualified + Trigger written. Make every call autonomously — no per-lead review needed.

**Queue:** Status = New
**Output:** Status = Qualified or Disqualified, Trigger field populated
**Tool stack:** Notion MCP + web fetch
**Batch size:** All New leads per run (fetch URLs in parallel, max 10 at a time)

---

## Execution

### Step 1 — Pull the Queue

Query the Notion CRM and collect all Status = New leads.

- CRM data source: `{{CRM_DS}}`
- Master view: `{{CRM_MASTER_VIEW}}`

Collect per lead: First Name, Last Name, Company, Website URL, Notion page ID.

If a lead has no Website URL → mark Disqualified immediately.
Trigger: "no website on record"

If more than 10 New leads exist, process in batches of 10.

### Step 2 — Fetch All Homepages in Parallel

Fire all web fetches simultaneously within each batch. Use https:// prefix.

Treat as Disqualified if the fetch:
- Returns empty content
- Times out
- Returns a maintenance/error/placeholder page
- Redirects to a domain registrar or unrelated platform (e.g. ClickFunnels homepage)

### Step 3 — Apply Pass/Fail Logic

#### PASS → Status = Qualified

The prospect has an audience but sends traffic directly to a booking page or contact form
with no capture layer in between.

Qualifying signals (any one is sufficient):
- Only CTA is a Calendly, booking link, or scheduling tool — no email opt-in anywhere
- Contact/inquiry form is the sole conversion action
- Coaching services listed but no lead magnet, quiz, challenge, or email course

#### FAIL → Status = Disqualified

| Signal | Examples |
|--------|---------|
| Email opt-in on page | "Subscribe for updates", "Join my list", newsletter form |
| Lead magnet | Free PDF, free meditation, free guide, free training download |
| Email/challenge funnel | 5-day challenge, email course, free masterclass |
| Quiz or assessment | "Take the quiz", assessment CTA |
| Gated nav content | Kajabi/Teachable links in nav requiring email signup |
| Newsletter in nav or footer | "Newsletter" as a nav item or prominent footer link |
| Wrong ICP | Local physical service, financial/accounting coaching, B2B enterprise only, family business consulting |
| Dead/empty domain | Empty fetch, registrar redirect, HTTP error |
| Maintenance mode | Site temporarily unavailable page |
| No high-ticket coaching signal | Pure product store, no coaching offer |

### Step 4 — Write Trigger (10–12 words max)

State only what you observed. Do not explain what's missing.

**Qualified examples:**
- "only CTA is a Calendly link; no email capture"
- "booking form is only CTA; no lead magnet or opt-in"
- "all CTAs route to booking portal; no pre-sell layer"

**Disqualified examples:**
- "email subscribe opt-in above the fold on homepage"
- "free PDF guide download on homepage"
- "newsletter in nav; executive corporate coaching, wrong ICP"
- "dead domain, no content"
- "Mailchimp email capture for mini masterclass on homepage"
- "two Kajabi email-gated products in nav"

### Step 5 — Update Notion in Parallel

Fire all Notion page updates simultaneously using `notion-update-page` with
`command: update_properties`.

Qualified: `{"Status": "Qualified", "Trigger": "<trigger text>"}`
Disqualified: `{"Status": "Disqualified", "Trigger": "<trigger text>"}`

### Step 6 — Report

Output a summary table after all updates are confirmed:

```
Batch complete. X leads processed.

| Lead | Company | Result |
|------|---------|--------|
| ... | ... | ✅ Qualified / ❌ [reason] |

X/Y qualified (Z%). X New leads remain in queue.
```

---

## Decision Rules

**When in doubt, fail.** A false positive wastes Research and Compose cycles. A false
negative costs nothing — the lead stays in the CRM.

**Check nav links, not just the hero.** Newsletters, email courses, and gated content
often live in nav items (e.g. "Free Training", "Subscribe", "Private Podcast") even
when the hero CTA looks clean.

**A passive blog notification is not a lead magnet.** A single "get notified of new
posts" link in the footer, clearly not promoted as a freebie, does not disqualify. Use
judgment — if it's clearly a low-key notification, pass.

**Fail fast on capture, then check ICP.** If capture infrastructure exists, mark
Disqualified immediately. Only evaluate ICP if the site would otherwise pass.

---

## Known Patterns

- ~25% of leads have dead/broken domains — Apollo data quality issue.
- ~40% already have capture infrastructure.
- Expected pass rate: 15–25% depending on Apollo filter quality.
- Common pass format: Calendly-only, Dubsado booking form, direct booking portal.
- Common fail formats: free meditation download, PDF guide, newsletter, Kajabi gated content,
  Mailchimp mini masterclass, book excerpt opt-in.
