# Data-Race Drill: Template and Question Design

Clay Cup's live elimination rounds use a fixed workbook of 30 numeric questions, tiered by difficulty, scored by points, built cold in Clay under a 20-minute clock. This is a speed/fundamentals drill, not a scenario exercise — no ICP, no messaging, just "can you get Clay to answer this fast and correctly."

## The template

```markdown
# Data Race: [Theme, e.g. "SaaS Landscape" or Notion's Competitive Set]

**Objective:** Score as high as possible in 20 minutes, using only Clay. Build
from a blank table — no pre-built templates, no Sculptor shortcuts.

**Scoring:** Easy = 100 pts each (×10 = 1000), Medium = 200 pts each (×10 =
2000), Hard = 300 pts each (×10 = 3000). Max score: 6000.

## Easy (100 pts each)
1. ...
2. ...
...(10 total)

## Medium (200 pts each)
11. ...
...(10 total)

## Hard (300 pts each)
21. ...
...(10 total)

**Do not look up the answers before building** — the exercise is the workflow,
not the trivia.
```

## Question design principles

- **Every question must be answerable via Clay enrichment** — a lookup, an AI column, a formula, or a chain of those. If it can't be answered by enriching a table, it doesn't belong in this drill.
- **Easy tier:** single-lookup facts about one company — headcount, follower count, founding year, funding raised, HQ location.
- **Medium tier:** a comparison or simple calculation across two entities — a difference, a ratio, a sum. E.g. "What is the difference between the founding years of X and Y?"
- **Hard tier:** chained lookups or multi-step calculations — requires combining 2–3 enriched data points, possibly across more than two companies, or a derived metric (e.g. "average headcount growth rate across these 3 companies over the last year").
- **Use real, enrichable companies** — either well-known ones (mirrors the actual competition's use of HubSpot, Airtable, Linear) or, if this drill is themed around a company Rodney gave you, that company plus its real competitors/peers.
- **Vary the data source implied per question** — don't make all 30 pull from the same single enrichment type (e.g. don't make every question a LinkedIn follower count). Mix firmographic, social, funding, and product-signal questions so the drill exercises different Clay integrations.

## After the drill

If Rodney asks you to check his answers, look them up then — not before. Compare his numbers against what you find and flag any mismatches by question number rather than just handing back a raw list, so it reads like feedback rather than an answer dump.

If he asks for a nudge on a specific question mid-drill instead of a full check, don't resolve it — point him at *which type of lookup or Clay primitive* would answer it (e.g. "that one needs a two-step waterfall, not a single enrichment") without giving the number itself.

If he asks for a harder or easier version, adjust the tier mix (e.g. more hards for a harder drill) rather than just raising point values.
