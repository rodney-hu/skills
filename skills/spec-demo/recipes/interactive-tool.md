# Recipe: interactive-tool

**Status:** planned. Layout to build: `<kit>/recipes/interactive-tool/` (`index.html`, `schema.json`, `recipe.css`, inline JS).
**The link shows:** one working tool for the prospect's audience (a cost or ROI calculator, a readiness self-assessment, or a scorecard) on its own page, with a copy-paste embed snippet below it so the prospect could put it on their site.
**Best for:** marketing and product-marketing roles whose buyers justify a purchase with numbers or a readiness check.

## Steps
1. **Tool plan → `copy/tool.md`.** Pick one type:
   - **Calculator:** 3 to 6 inputs the audience knows (with defaults), one formula, one result line plus a short "what this means". Every assumption is shown and editable. No invented benchmarks; cite the brief or let the user enter them.
   - **Self-assessment / scorecard:** 6 to 10 yes/no or 1-5 questions, 3 result bands, one next step per band.
   Write the formula or scoring in plain words in the plan before coding.
2. **`demo.json`.** `"recipe": "interactive-tool"`, shared slots plus `tool` (`type`, `inputs[]` or `questions[]`, `formula` or `bands[]`, `result_copy`).
3. Render, check, deploy, deliver. The embed snippet is an `<iframe>` pointing at the live URL's `?embed=1` view (no header or footer).

## Done checks
- The tool works with only the defaults, and changes results when inputs change.
- Results never claim savings for the prospect's product; they describe the audience's own numbers.
- The embed snippet, pasted into a blank HTML page, shows the tool.
- No network calls; works at 390px.
