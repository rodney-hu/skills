# YouTube Extraction Path

> *Used when `detect_url_type(url) == "youtube"`. Markdown-driven workflow, no API key required. Public page fetches plus web search supplementation.*

---

## Workflow

### Step 1: Normalize URL

Accept any of these formats and normalize to canonical channel URL:

- `https://www.youtube.com/@handle` ✅ canonical
- `https://youtube.com/c/channelname`
- `https://youtube.com/channel/UCxxxxxx`
- `@handle` (prepend `https://www.youtube.com/`)
- `youtu.be/...` (video URL — extract channel from video page first)

### Step 2: Fetch Channel Pages

Use `web_fetch` in priority order:

```
Priority 1 (Required):
  {channel_url}        → Featured content, banner tagline, About bio
  {channel_url}/about  → Channel description, links, keywords

Priority 2 (High value):
  {channel_url}/videos → Recent video titles
  {channel_url}/playlists → Content pillars
```

YouTube is JS-heavy. If `web_fetch` returns thin HTML (<500 chars visible text), supplement aggressively with web search.

### Step 3: Supplement with Web Search

Always run at least two:

```
Search 1: "{channel name}" YouTube about audience
Search 2: site:youtube.com "{channel name}" (for cached titles)
Search 3 (if creator has site/community): "{channel name}" newsletter OR course OR community
```

Fetch any individual video URLs that surface — video pages render description text more reliably than channel pages.

### Step 4: Extract Brand Profile Fields

Map observable channel data to the unified template:

| Brand Profile Field | YouTube Signal |
|---|---|
| §1 Name | Channel name |
| §1 Handle/Domain | `@handle` |
| §1 Tagline / Bio | About-page first line / banner tagline |
| §1 Brand Archetype | Apply `references/brand-archetypes.md` (use signals across video titles + bio + tone) |
| §2 Niche | Inferred from channel keywords + content categories |
| §2 Core Offer | What the channel sells/teaches/promotes — pull from About-page links and recurring CTAs |
| §2 Value Proposition | Outcome promised in About bio |
| §2 Target Customer | Direct address in titles ("If you're a...", "For founders who...") |
| §2 Messaging Themes | 3–5 themes that recur across video titles and About bio |
| §2 External Properties | Links from About page (newsletter, course, community, product) |
| §3 Voice Dimensions | Title phrasing, description style, About copy, banner |
| §3 Voice Samples | Pull 3 actual lines — best from video titles (highest signal density) |
| §4 Content Pillars | Group recurring video themes into 4–5 pillars; use playlists as shortcut |
| §4 Title Formula | Pattern observed across video titles |
| §4 Hook Style | How videos open (from descriptions) |
| §4 Content Infrastructure | Use YouTube row of the table — playlists, posting cadence, video length avg |
| §5 Mechanism | Look for branded frameworks: named methodologies in titles, recurring terminology, named curriculum in linked communities |
| §5 Mechanism Source | Mark `(stated)` if explicit, `(inferred)` if synthesized from patterns |
| §6 Differentiators | What makes this creator distinct in their niche |
| §6 Authority Signals | Subscriber count, named clients, press, third-party validation |
| §6 Gaps | Visibility into testimonials, case studies, proof |
| §7 Core CTA | What every video pushes — subscribe / download / book / apply / join |
| §7 CTA Copy Pattern | Pull or reconstruct from video descriptions |
| §7 Friction Level | Free download = low. Paid community = medium. Application/coaching = high |
| §7 Opt-in Mechanisms | Pull from About-page links + video description CTAs |

---

## Source-Specific Notes

### What YouTube gives you well
- Brand voice in titles and descriptions (high signal density)
- Content pillars from video patterns and playlists
- Hook style — every title is a hook
- Audience direct-address language
- Mechanism — creators often name and brand their methodology

### What YouTube gives you poorly
- Subscriber-level demographics (estimates only)
- Visual identity (thumbnails are surface-level signal)
- Comments are often hidden from `web_fetch`
- Channel-page content is JS-rendered and frequently sparse

### When to supplement with web search
- Always — at minimum to surface cached titles
- Priority when About-page bio is empty
- Priority when channel name appears multiple times across creators

---

## Failure Modes

### Channel page returns thin HTML
1. Try `/about` specifically
2. Use `web_search` for `youtube.com/@{handle}` → grab cached metadata
3. Fetch a specific video URL (from search results) → video pages render description text reliably

### Channel name extraction unclear
- Multiple creators may share a name (e.g. several "Katie Clarke" accounts)
- Use the @handle as the disambiguator, never just the name
- Always include channel URL in the deliverable header

### Sparse content
- Fewer than 3 videos visible → return `INSUFFICIENT_DATA`
- Fewer than 5 video titles in cache → mark `THIN_DATA`, note in `inferred fields`

### Private or deleted channel
Return: `"This channel appears to be private, deleted, or unavailable. Unable to extract brand data."`

---

## Quality Flag

- **PASS**: Channel description extracted, ≥5 video titles analyzed, mechanism named, archetype assigned, ≥2 voice samples
- **THIN_DATA**: Some sections required heavy inference (especially mechanism or external properties)
- **INSUFFICIENT_DATA**: Channel not found, private, or fewer than 3 videos
