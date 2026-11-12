---
name: brand-intelligence
description: Extract brand intelligence from any source URL — website, YouTube channel, or LinkedIn company page. Routes to the appropriate extraction path based on URL type and produces a unified Brand Profile covering identity, niche, voice, content architecture, mechanism, authority signals, and CTA strategy. Use whenever someone provides a URL and wants to understand who a brand or creator is, how they sound, what they offer, or how they position themselves. Trigger on "research this company", "analyze [URL]", "extract brand voice from [company]", "what does this brand do", "tell me about this YouTube channel", "what's their positioning", or any request that involves studying a brand's identity from a single URL. Replaces the older `company-research` and `youtube-brand-persona` (Asset A) skills with one URL-aware skill. For audience-side intelligence (ICA, fears, desires, activation), use the separate `audience-intelligence` skill — they're designed to chain.
---

# Brand Intelligence

## Overview

A **URL-aware brand research skill**. Detects the type of URL provided and routes to the appropriate extraction path. All paths produce the same unified output: a **Brand Profile** describing who the brand is, how they sound, what they offer, and how they position themselves.

| URL Type | Extraction Path | Backed By |
|---|---|---|
| Website (any `https://` URL not matching below) | `references/website-extraction.md` | Python scripts in `scripts/` |
| YouTube channel (`youtube.com/@...`, `youtube.com/c/...`, `youtube.com/channel/...`) | `references/youtube-extraction.md` | Markdown workflow, public page fetches |

This is **brand-side only**. It does not extract audience intelligence (ICA, pains, fears, activation moments). For that, run `audience-intelligence` — it can take this skill's output as input or run from the same URL standalone.

---

## Input Contract

```yaml
url: string                    # Required. Any HTTPS URL.
brand_name: string | null      # Optional. Extracted automatically if absent.
```

---

## Workflow

### Step 1: Detect URL Type

```python
import re

def detect_url_type(url: str) -> str:
    url = url.strip().lower()
    if re.search(r"youtube\.com/(@|c/|channel/|user/)", url):
        return "youtube"
    if url.startswith("http://") or url.startswith("https://"):
        return "website"
    raise ValueError("Invalid URL — must be HTTPS")
```

For ambiguous cases (e.g. `youtu.be/...` for video URLs), normalize first or abort with a clear message.

### Step 2: Route to the Correct Extraction Path

Each path is documented in detail in `references/`:

- **Website** → load `references/website-extraction.md`. This path uses the Python scripts in `scripts/` (`scrape_website.py`, `extract_voice.py`, `audit_content.py`, `format_output.py`). Inherits the original `company-research` extraction logic.
- **YouTube** → load `references/youtube-extraction.md`. Public page fetches plus web search, no API key.

### Step 3: Populate the Unified Brand Profile

Every path writes to the same template: `references/brand-profile-template.md`.

The template has 7 sections. Sections that don't apply to a particular source mark fields as `N/A — [reason]` rather than omitting them. This keeps downstream skills consuming a stable shape.

### Step 4: Quality Check

Set the quality flag in the deliverable header:

- **PASS** — All required sections populated. Brand voice has real samples (not summaries). Niche and offer clearly stated. At least 2 authority signals identified.
- **THIN_DATA** — Some sections required heavy inference. List which.
- **INSUFFICIENT_DATA** — Cannot extract minimum required data. Abort.

---

## Unified Output Structure

The deliverable is a markdown document with this structure:

```
# [Brand Name] — Brand Profile

> Source: [url] | Type: [website/youtube/linkedin] | Quality: [PASS/THIN_DATA]

## 1. 🪪 Brand Identity
## 2. 🎯 Niche & Core Offer
## 3. 🎙️ Brand Voice & Tone
## 4. 🧩 Content Architecture
## 5. 🧬 Proprietary Mechanism / Framework
## 6. 🏛️ Authority Signals & Positioning
## 7. 🧲 CTA & Lead Gen Strategy
```

See `references/brand-profile-template.md` for the full structure with field-level guidance.

---

## Abort Conditions

- URL is invalid (not HTTP/HTTPS)
- Cannot detect URL type and no obvious match
- Site is broken (404), placeholder ("under construction"), or auth-walled
- After all extraction attempts, fewer than 200 words of content captured
- Brand name cannot be extracted or inferred

---

## Quality Standards

For `PASS`:
- ✅ Brand name extracted or strongly inferred
- ✅ Niche / industry identified
- ✅ Core offer stated in 1–2 sentences
- ✅ Brand voice has at least 2 real sample lines (not summaries)
- ✅ At least 3 messaging themes or content pillars identified
- ✅ Brand archetype assigned with reasoning (use `references/brand-archetypes.md`)
- ✅ At least 2 authority signals captured
- ✅ At least 1 CTA / opt-in mechanism identified

---

## Integration

| Downstream Skill | What This Feeds |
|---|---|
| `audience-intelligence` | Takes this output as optional input to skip redundant extraction |
| `rodney-writing-style` | Brand Voice & Tone → ghostwriting tone match |
| `pga-eec` | Niche, content pillars, mechanism → EEC topic angles |
| `icebreaker-eec` | Brand voice + CTA strategy → personalized icebreakers |
| `funnel-architect` | Niche + mechanism + offer → funnel positioning brief |

---

## Troubleshooting

### URL type ambiguous
- `youtu.be/...` is a video URL → extract the channel from the video page first

### Web fetches return thin content
- **Website**: Try `/about`, `/services`, `/products` directly; fall back to root if all fail
- **YouTube**: JS-heavy. Try `/about` specifically; supplement with web search of cached metadata; fetch a video URL for description text
- **LinkedIn**: Company pages often gated. Use web search for cached "About" content; check for the company's external website link

### Mechanism not visible
- Most brands don't have a named methodology. Mark mechanism as `(none stated)` or `(inferred)` and lean on positioning + content pillars instead.

### Voice samples generic
- If the only language extracted is "we help businesses succeed" type filler, mark `quality_flag: THIN_DATA`. The brand likely doesn't have a strong voice — that's a finding, not a failure.

---

## References

- `references/brand-profile-template.md` — Unified output template (used by both extraction paths)
- `references/website-extraction.md` — Website extraction workflow
- `references/youtube-extraction.md` — YouTube extraction workflow
- `references/brand-archetypes.md` — 7 brand archetypes for assignment
- `references/voice-dimensions.md` — Voice analysis criteria (5 dimensions)
- `references/content-patterns.md` — Content infrastructure patterns
- `references/industry-signals.md` — Industry classification heuristics
- `scripts/` — Python utilities for the website extraction path
