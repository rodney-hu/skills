---
name: youtube-channel-scout
description: "Research and qualify YouTube channels in any niche that have built a real audience but lack conversion infrastructure — no email list, no lead magnet, no course, no community funnel, no owned audience capture of any kind. Use this skill whenever the user asks to find YouTube channels for prospecting, lead generation, or outreach — in any niche, any creator format (on-camera or faceless). Trigger on phrases like \"find YouTube channels\", \"scout YouTube for prospects\", \"find channels with no funnel\", \"YouTube channel research\", \"channels that aren't monetizing their audience\", or any request to build a YouTube prospect list. Also trigger when the user provides keywords, niches, or subscriber ranges and wants matching channels evaluated as potential clients for funnel or email list services.\n"
---

# YouTube Channel Scout

A research skill for finding and qualifying YouTube channels — in any niche, any format — that have built real audiences but lack conversion infrastructure. These are prime prospects for AgenticOS, email funnel installation, and lead gen services.

---

## Purpose

Find YouTube channels where creators have:
- ✅ A real, growing audience (10K–50K subscribers by default)
- ✅ Consistent content output in a relevant niche
- ✅ Long-form videos — channel must publish videos ≥7 minutes (not Shorts-only)
- ✅ Any creator format — on-camera, faceless, voiceover, brand channel, podcast-style, etc.
- ❌ Shorts-only format (no qualifying long-form content ≥7 minutes)
- ❌ No email list or newsletter opt-in
- ❌ No lead magnet, free resource, or download
- ❌ No course, product, or digital offer
- ❌ No community (Skool, Circle, Patreon, Discord, etc.)
- ❌ No "Work with me," "Book a call," or coaching CTA
- ❌ No mechanism to convert platform audience into owned audience

These are the gap channels — audience built, monetization potential untapped.

---

## Data Layer: VidIQ MCP

This skill uses the **VidIQ MCP** as the primary data source for channel discovery and metadata. Web search and web_fetch are still used for funnel detection (About tab, video descriptions) and contact lookup — VidIQ doesn't see funnels or emails.

### VidIQ tools used in this skill

| Tool | Purpose | Cost |
|---|---|---|
| `vidiq_balance` | Check credits before a run | 0 |
| `vidiq_keyword_research` | Optional niche validation (Step 0) | 5 |
| `vidiq_breakout_channels` | Primary channel discovery (Step 2) | 5 |
| `vidiq_similar_channels` | Expand pool from a seed channel (Step 2) | 5 |
| `vidiq_channel_videos` | Verify last upload date for recency (Step 3) | 5 |
| `vidiq_channel_stats` | Confirm sub count + growth on top candidates only (Step 3) | 5 |

### Credit budget per run

A typical 10-prospect run should cost ~60–100 credits:
- 1× `breakout_channels` (5) → returns 20–50 candidates with subs already attached
- 0–1× `similar_channels` (5) if pool is thin
- 10–15× `channel_videos` (50–75) → recency check on top candidates
- 0–5× `channel_stats` (0–25) → only when subscriber count or growth needs confirmation

**Always run `vidiq_balance` first** if credits are uncertain. If the run will exceed available credits, surface the budget tradeoff to the user before starting.

---

## Inputs

| Input | Default | Description |
|---|---|---|
| `keywords` | See defaults below | Search terms, niche topics, or creator type to target |
| `min_subs` | 10,000 | Minimum subscriber count threshold |
| `max_subs` | 50,000 | Maximum subscriber count threshold |
| `max_channels` | 10 | How many qualified channels to return |
| `niche` | Personal/spiritual development | Broad niche context for scoring relevance |
| `creator_format` | Any | Optional filter: "on-camera", "faceless", "brand", "podcast" — leave blank for all |
| `country` | (none) | Optional 2-letter country code (e.g. "US") to filter VidIQ discovery |

### Default Niches (use when no keywords provided)

Run these as `breakout_channels` queries until you have a candidate pool of 15–25 channels:
1. `spiritual awakening`
2. `shadow work`
3. `inner healing mindset`
4. `law of attraction`
5. `stoicism philosophy`
6. `conscious growth spiritual development`
7. `neuroscience`

When the user provides a keyword or niche, use it directly as the `breakout_channels` query — natural language works (e.g. "vegan cooking tutorials", "personal finance for millennials").

---

## Workflow

Follow these steps in order. Do not skip steps.

### Step 0: (Optional) Validate Niche Demand

When the user is exploring a new niche or you have low confidence in keyword strength, run `vidiq_keyword_research` on the seed term first. Look at:
- **Volume score** (0–100) — is anyone actually searching for this on YouTube?
- **Competition score** (0–100) — saturated or open?
- **Related keywords** — better adjacent niches to consider?

If volume is below 20, surface this to the user before continuing — the niche may be too small to build a prospect list from.

Skip this step when the user has already validated the niche or has a working list of clients in it.

### Step 1: Generate Search Queries

If the user provides keywords or a niche, use them directly as `breakout_channels` queries. Natural language is fine — VidIQ uses semantic search.

If no input is given, use the default niches list above.

### Step 2: Discover Channels (VidIQ-First)

For each niche query, call `vidiq_breakout_channels` with these parameters:

```
query: [niche query]
subscriberCountMin: [min_subs, default 10000]
subscriberCountMax: [max_subs, default 50000]
faceless: [only set if user requested format filter]
country: [only set if user provided one]
limit: 25
```

This returns channels already filtered by subscriber range — no manual filtering needed. Each result includes channel ID, handle, title, subscriber count, and growth metrics.

**If the candidate pool is thin (<10 channels):**
- Pick the strongest result as a seed
- Call `vidiq_similar_channels` with the niche and same subscriber range to expand the pool by 20–30 channels

**If the user provides a specific channel they want similar prospects to:**
- Skip `breakout_channels` entirely
- Go straight to `vidiq_similar_channels` with the niche or topic and subscriber bounds

Collect a candidate pool of 15–25 unique channels before moving to qualification. Web search is no longer needed for discovery — VidIQ replaces it.

### Step 3: Research Each Channel

For each candidate, gather the data needed to qualify them. Split this into two passes — VidIQ for stats + recency, web_fetch for funnel signals.

#### 3a. Recency check (VidIQ)

For each candidate, call `vidiq_channel_videos`:
```
channelId: [channel handle or ID from Step 2]
videoFormat: "long"
popular: false  ← important: this returns RECENT uploads, not popular
```

Look at the results:
- **If the tool returns no videos at all → DISQUALIFY immediately.** The channel posts only Shorts or has no long-form content — it does not meet the minimum format requirement.
- **If the latest long-form upload is more than 7 days ago → DISQUALIFY immediately.** Do not score, do not check funnel signals.
- **If the most recent long-form video is under 7 minutes** (check the video duration if surfaced) → DISQUALIFY. We require substantive long-form content.
- If within 7 days and long-form ≥7 min → continue to funnel check.

#### 3b. Subscriber count confirmation (VidIQ, only if needed)

`breakout_channels` already returns subscriber counts. Only call `vidiq_channel_stats` when:
- The channel came from `similar_channels` and you want growth trajectory data
- The subscriber count looks borderline (close to min_subs or max_subs)
- You need country/language/topic metadata for niche scoring

#### 3c. Funnel signal detection (web_fetch)

VidIQ does not detect funnels. For channels that pass the recency check, use `web_fetch` on the YouTube channel URL to read the About tab and 2–3 recent video descriptions.

Look for:
- **External links in About tab** — any URLs?
- **Description text** — product/funnel signals (see Funnel Signal Detection Reference below)
- **Linktree, Beacons, or website links** — what's behind them?
- **Pinned comments or community posts** — product announcements?

**Helpful URL patterns:**
- `https://www.youtube.com/@[handle]` — channel home / About tab
- `https://www.youtube.com/@[handle]/about` — direct About tab
- `https://www.youtube.com/@[handle]/videos` — video listing (already covered by VidIQ in 3a)

### Step 4: Qualify Each Channel

Score each channel against the qualification criteria:

#### ✅ PASS Criteria (must meet ALL)
- Subscriber count within range (default 10K–50K) — confirmed via VidIQ
- Channel is actively creating original content (not just clip compilations or reposts)
- Content is in the target niche
- Channel has posted at least once within the last 7 days — confirmed via `vidiq_channel_videos`
- Creator has built genuine audience trust (comments, engagement signals)

#### ❌ DISQUALIFY Criteria (any one = remove)
- Has a link to a course, coaching program, or product page
- Has a Patreon, Skool, Circle, or community platform link
- Has an email list opt-in or lead magnet link
- Has a Gumroad, Teachable, Kajabi, or digital product storefront link
- Has a newsletter (Substack, ConvertKit page, Beehiiv, etc.)
- Subscriber count outside range
- Channel has not posted within the last 7 days (automatically disqualified — no exceptions)
- Channel publishes only Shorts — `vidiq_channel_videos` with `videoFormat: "long"` returns no results (no long-form content at all)
- Most recent long-form video is under 7 minutes (Shorts-adjacent, not substantive enough for email funnel pitch)
- Channel is purely a clip/compilation account (no original voice or perspective)

#### 🟡 PARTIAL (note it, include with caveat)
- Has a free app but no email funnel
- Has affiliate links but no owned list or product
- Has a vague "DM me" CTA but no formal funnel
- Has a Linktree that only links social profiles (no product behind it)
- Is slightly over/under subscriber threshold but otherwise a strong fit
- Has a newsletter mentioned in passing but no visible opt-in on channel

### Step 5: Score Each Qualified Channel

For every channel that passes, assign a **Prospect Score** from 1–10 based on:

| Factor | Weight | Notes |
|---|---|---|
| Audience size | 20% | Sweet spot = 10K–30K. Higher = more leverage, harder sell. |
| Content quality signal | 20% | High view counts relative to subs = good engagement. Comments = trust signals. |
| Niche alignment | 20% | How closely does content match the service offer (education, transformation, expertise)? |
| Funnel gap severity | 30% | Zero funnel = 10. Newsletter only = 6. Partial (app/community) = 4. |
| Growth trajectory | 10% | Growing > flat > declining. Use `vidiq_channel_stats` 30-day delta when needed. |

**Creator format note:** Record whether the channel is on-camera (named host), faceless/voiceover, brand channel, or podcast-style. This affects pitch angle — not the score.

### Step 6: Build the Prospect List

Output a formatted table with one row per qualified channel. Include:

| Field | Description |
|---|---|
| Channel Name | Display name |
| Channel URL | Full direct YouTube link — **required, always include** (e.g. `https://www.youtube.com/@handle`) |
| Subs | Confirmed via VidIQ |
| Last Upload | Date or "X days ago" — confirmed via `vidiq_channel_videos`, must be within 7 days |
| Creator Format | On-camera / Faceless / Brand / Podcast-style |
| Niche | 2–3 word content descriptor |
| Funnel Status | "None detected" / "Partial: [what they have]" |
| Prospect Score | X/10 |
| Pitch Angle | One-sentence positioning for outreach |
| Contact Info | Email / DM method found (see Step 7) |
| Notes | Any context, caveats, or flags |

---

### Step 7: Find Contact Information

For every qualified channel, run the contact lookup sequence below in order. Stop as soon as you find a usable contact method. Record what you found and where.

**No API keys required. VidIQ does not surface contact info — all lookups use web_search and web_fetch on publicly available data.**

#### Lookup Sequence (run in order, stop when found)

**1. YouTube About Tab — check first**
Use `web_fetch` on `https://www.youtube.com/@[handle]` or the channel URL.
Look for: "View email address" button content, any email address in the About/Details section, or external links listed under the channel.

**2. Channel Description / Video Descriptions**
Scan the channel description and 2–3 recent video descriptions.
Look for: email addresses written out (e.g. `hello@domain.com`), contact links, or "for business inquiries" text.

**3. Linked Website**
If the About tab lists a website URL, use `web_fetch` on that URL.
Look for: Contact page, About page, or footer with an email address.
Also try `web_fetch` on `[domain]/contact` if the homepage doesn't surface an email.

**4. Instagram Bio**
Search `"[channel name]" Instagram` — many creators list a business email in their IG bio even when it's absent from YouTube.
Use `web_fetch` on the Instagram profile URL if found.
Look for: email address in bio, or "Email: [address]" text.

**5. Hunter.io Domain Search**
If you found the creator's website domain, search `site:hunter.io "[domain]"` or `"[domain]" email contact`.
This surfaces likely email format patterns (e.g. `firstname@domain.com`) even when no address is explicitly listed.

**6. LinkedIn**
Search `"[creator name]" LinkedIn`.
Look for: professional email, DM option, or contact details on their profile.

**7. Twitter/X Bio**
Search `"[channel name]" Twitter OR X`.
Look for: email in bio, or a Linktree/Beacons link that may surface contact info.

#### Contact Status Labels

Use these labels in the output table:

| Label | Meaning |
|---|---|
| ✅ Email confirmed | Direct email address found and recorded |
| 🔗 Website contact form | No email found, but contact form available at [URL] |
| 📸 Instagram DM | No email found, Instagram handle available for DM |
| 🐦 Twitter/X DM | No email found, Twitter handle available |
| ⚠️ Not found | No contact method located — manual search needed |

#### Contact Lookup Priority Notes
- Always check YouTube About tab first — many creators add a business email specifically for partnership inquiries
- Instagram bios catch a large percentage of creators who don't expose email on YouTube
- If a creator has a website but no visible email, note the contact form URL — that's still a usable path
- Never fabricate or guess email addresses — only record what is explicitly found
- If contact info is completely absent across all channels, flag for manual outreach via YouTube comment or community post

---

## Output Format

After the table, include:

**Summary block:**
- Total channels researched
- Total qualified
- Contacts found vs. not found
- Top 3 prospects with brief rationale
- Recommended next action
- **VidIQ credits consumed** (estimated based on tool calls made)

**Verification reminder:**
Always note that funnel status should be manually confirmed before outreach — VidIQ confirms subs and recency, but funnel detection relies on web scraping which can miss recently-added links. Recommend the user:
1. Visit each channel's About tab directly and confirm no links were recently added
2. Check the /videos tab to confirm a post within the last 7 days (already verified by VidIQ but worth a sanity check on top prospects)

---

## Funnel Signal Detection Reference

Use this reference when scanning channel descriptions, About tabs, and video descriptions via `web_fetch`.

### Strong Funnel Signals (DISQUALIFY)
- "Join my course" / "Enroll now" / "Buy now"
- Links to Teachable, Kajabi, Thinkific, Podia, Gumroad, or similar
- "Join our community" + link to Skool, Circle, Mighty Networks, Patreon
- "Download my free guide" / "Get the free resource" + link

### Partial/Weak Funnel Signals (FLAG, don't disqualify)
- "Follow me on [social]" (no product behind it)
- Generic app link (wellness/community app, not a funnel per se)
- Affiliate links in descriptions (not owned list)
- Patreon mentioned but no active tiers / very low patron count
- "DM me for info" (informal, no system)

### No Funnel Signals (IDEAL)
- Description ends with subscribe CTA only
- About tab has zero external links
- No links of any kind in video descriptions
- Only monetization is YouTube AdSense (estimated low earnings)
- No pinned community post or product announcement

---

## Example Prospect Entries

**Faceless channel:**
```
Channel: Psychomystic
Handle: youtube.com/channel/UCY7yhiXwkZ6jgjCOM_l6PQA
Subs: 47K (confirmed via VidIQ)
Last Upload: 3 days ago (confirmed via vidiq_channel_videos)
Creator Format: Faceless / voiceover narration
Niche: Shadow work / Jungian psychology / spiritual awakening
Funnel Status: None detected — description ends with "Subscribe to begin your journey within." Zero external links.
Prospect Score: 8/10
Pitch Angle: "You've built an audience of seekers. We can build the system that turns that attention into a list of pre-qualified leads — without changing what makes your content work."
Contact Info: ⚠️ Not found — no email on About tab, no website linked, no Instagram bio email. Recommend YouTube community post or comment outreach.
Notes: Faceless narration format, high-quality production, consistent posting.
```

**On-camera creator:**
```
Channel: [Example Creator]
Handle: youtube.com/@example
Subs: 42K (confirmed via VidIQ, +8% growth in last 30 days)
Last Upload: 1 day ago (confirmed via vidiq_channel_videos)
Creator Format: On-camera — named host, personal brand
Niche: Breathwork / nervous system regulation / somatic healing
Funnel Status: None detected — 3 video descriptions checked, no links. About tab has only Instagram link.
Prospect Score: 8.5/10
Pitch Angle: "42K people trust your face, your voice, your methods. Right now they watch and leave. A smart audit that captures them into a 5-day email course turns viewers into warm pipeline — without you doing anything differently on camera."
Contact Info: ✅ Email confirmed — hello@[domain].com found on website contact page via About tab link.
Notes: On-camera personal brand = higher trust, stronger pitch opportunity. Confirm no email list exists before outreach.
```

---

## Notes for Claude

- **VidIQ MCP is the data layer.** Use `vidiq_breakout_channels` and `vidiq_similar_channels` for discovery. Use `vidiq_channel_videos` for recency. Use `vidiq_channel_stats` for confirmation only when needed. Use web_fetch only for funnel detection and contact lookup — VidIQ doesn't see funnels or emails.
- **Run `vidiq_balance` first** if credit headroom is uncertain. Surface budget tradeoffs to the user before kicking off a large run.
- **ALWAYS include the full YouTube channel URL** in the output table. Format: `https://www.youtube.com/@handle` or `https://www.youtube.com/channel/[ID]`.
- **7-day recency is a hard disqualifier.** `vidiq_channel_videos` with `popular: false` returns recent uploads — use the publish date of the most recent one. No exceptions.
- **Shorts-only is a hard disqualifier.** Always call `vidiq_channel_videos` with `videoFormat: "long"` — if zero results come back, the channel has no qualifying long-form content and must be removed from the list. Do this check before scoring anything.
- **Minimum video length is 7 minutes.** If VidIQ surfaces video duration and the most recent long-form video is under 7 minutes, disqualify. The offer (lead magnet + email automation) is best pitched to creators whose audience sits and watches — not swipe-past Shorts viewers.
- **Don't waste credits.** `breakout_channels` already returns subscriber counts — don't call `channel_stats` on every candidate. Only call it when you need 30-day growth data or when subs are borderline.
- Creator format (on-camera vs. faceless) does NOT affect qualification — what matters is whether they have infrastructure to convert their audience into owned contacts. The `faceless` filter on `breakout_channels` is only used when the user explicitly wants format filtering.
- Always disclose which data points were confirmed (VidIQ) vs. inferred (web_fetch).
- Do not fabricate funnel status — if you can't access the About tab data, mark as "Unverified — manual check needed".
- Do not fabricate or guess email addresses — only record contact info that is explicitly found on a public page.
- Run discovery in batches — collect candidates first (Step 2), recency-check second (Step 3a), funnel-check third (Step 3c), score fourth, find contacts fifth.
- On-camera creators with no funnel are often BETTER prospects than faceless ones — they have a personal brand and a loyal audience, making the "you should own this relationship" pitch even more compelling.
- For contact lookup: YouTube About tab → website → Instagram bio → Hunter domain search → LinkedIn → Twitter/X — stop at first confirmed hit.
