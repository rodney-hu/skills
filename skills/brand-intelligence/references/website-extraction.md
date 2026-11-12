# Website Extraction Path

> *Used when `detect_url_type(url) == "website"`. Inherits the original `company-research` extraction logic. Backed by Python scripts in `scripts/`.*

---

## Workflow

### Step 1: Validate and Plan Fetches

```python
from scripts.scrape_website import get_urls_to_fetch, validate_url

if not validate_url(url):
    abort("Invalid URL — must be HTTP or HTTPS")

urls_to_fetch = get_urls_to_fetch(url)
# Returns: [homepage, /about, /services, /solutions, /products, /pricing, /blog]
```

### Step 2: Fetch Each URL

You must call `web_fetch` directly — the Python scripts expect content passed in, they don't fetch.

```python
fetched_pages = {}
for u in urls_to_fetch:
    try:
        result = web_fetch(u)
        if result and result.content:
            fetched_pages[u] = result.content
    except Exception:
        continue  # Skip individual failures, keep going
```

### Step 3: Run the Extraction Pipeline

```python
from scripts.scrape_website import scrape_website
from scripts.extract_voice import extract_voice
from scripts.audit_content import audit_content
from scripts.format_output import format_output

scrape_result = scrape_website(url, fetched_pages)
if not scrape_result['success']:
    abort(scrape_result['error'])

scraped_pages = scrape_result['pages']
voice_analysis = extract_voice(scraped_pages)
content_audit = audit_content(scraped_pages)

# format_output produces the legacy CompanyData JSON shape — use it as a data source, then map to brand-profile-template
data = format_output(brand_name or "", url, scraped_pages, voice_analysis, content_audit)
```

### Step 4: Map JSON → Brand Profile Template

The Python scripts return a JSON contract from the original company-research skill. Map it to the unified template:

| Brand Profile Field | Source from JSON |
|---|---|
| §1 Name | `company.name` |
| §1 Handle/Domain | URL domain |
| §1 Tagline | First H1 or hero header (extract from `scraped_pages[homepage]`) |
| §1 Brand Archetype | Assign from `references/brand-archetypes.md` based on overall content |
| §2 Niche | `company.industry` |
| §2 Core Offer | `company.offer` |
| §2 Value Proposition | `company.value_prop` |
| §2 Target Customer | `company.target_customer` |
| §2 Messaging Themes | `company.messaging_themes` |
| §3 Voice Dimensions | `brand_voice` (formality, complexity, energy, pov, sentence_length) |
| §3 Voice Samples | `brand_voice.voice_samples` |
| §4 Content Pillars | Synthesize from messaging_themes + observed page categories (e.g. blog topic clusters, service categories) |
| §4 Content Infrastructure | `content_audit.blog_present`, `newsletter_signup`, `lead_magnets`, `educational_gaps` |
| §5 Mechanism | Inferred — websites rarely name a proprietary framework explicitly. Look for repeated branded terms in copy. Mark `(none)` if absent |
| §6 Differentiators | `positioning.differentiators` |
| §6 Authority Signals | `positioning.authority_signals` |
| §6 Gaps | Inferred from `content_audit.educational_gaps` + your own observation |
| §7 Core CTA | First item in `lead_gen.ctas` |
| §7 Friction Level | `lead_gen.friction_level` |
| §7 Opt-in Mechanisms | `lead_gen.opt_in_mechanisms` |

### Step 5: Quality Flag

The JSON from `format_output` includes its own `quality_flag` (`PASS / GENERIC_VOICE / INSUFFICIENT_DATA`). Map it to the unified flag:
- `PASS` → `PASS`
- `GENERIC_VOICE` → `THIN_DATA` (note "voice samples are generic" in `inferred fields`)
- `INSUFFICIENT_DATA` → `INSUFFICIENT_DATA` (abort, return error message)

---

## Source-Specific Notes

### What websites give you well
- Clear offer + value prop in hero / above-the-fold
- Lead gen mechanisms (forms, CTAs, lead magnets)
- Authority signals (testimonials, logos, case studies)
- Service / product structure

### What websites give you poorly
- Brand voice often filler-heavy ("we help businesses succeed")
- Mechanism rarely explicit
- Audience archetype obscured by SEO copy

### When to supplement with web search
- If site has fewer than 500 words extracted
- If voice samples are too generic to be useful
- If offer is unclear → search for `[brand] reviews OR pricing OR alternatives`

---

## Failure Modes

### All web_fetch calls failing
- Check if site requires JavaScript rendering (most are SPAs now)
- Try fetching root URL only
- Use web_search for cached snippets: `site:[domain]`

### Site is a placeholder / under construction
- Return `INSUFFICIENT_DATA` with a clear message
- Do not fabricate a brand profile from a placeholder site

### Site is auth-walled
- Return `INSUFFICIENT_DATA` — cannot extract from gated content
- Suggest user provides public alternative source (LinkedIn, YouTube)
