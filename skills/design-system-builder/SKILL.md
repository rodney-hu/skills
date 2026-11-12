---
name: design-system-builder
description: Build a new design system from scratch, or audit/evolve an existing one. Trigger on "design system", "component library", "design tokens", "style guide", "audit my design system", "compare design systems", "harden my design system", or when asked to build reusable UI infrastructure meant to span more than one project.
---

# Design System Builder

This is not a generic best-practices checklist. Every rule below exists because skipping it produced a real, shipped bug — most of them silent (no error, no failed build, just wrong in the browser). `references/bug-catalog.md` has the specific incident behind each one. Read it once before starting a system large enough to matter.

The through-line: **a rule that lives only in a comment or a doc will eventually be violated by accident, and the violation will not error.** Every phase below ends by asking "how does this get enforced automatically" — if the answer is "someone remembers," the phase isn't done.

Two entry points:
- **Building new** → Phases 1–7 in order.
- **Auditing or evolving an existing system** → Phase 8, which points back into 1–7 as needed.

## Phase 1 — Discover

Ask before building; guessing here produces a system nobody wanted, and by the time that's visible it's expensive to unwind.

- **Reference material as literal examples**, not adjectives. "Modern and clean" specifies nothing; three screenshots do.
- **Does color carry meaning, or is it just aesthetic?** If a palette has categorical values (element, status, brand line), decide up front whether each one is *also* a behavior (motion, shape, weight) or purely visual. Retrofitting meaning onto a color chosen for looks is much harder than deciding this first.
- **What does content sit on?** Don't assume a page background and a panel background are "close enough." Measure candidate combinations before committing — see Phase 2.3.
- **Scope**: new build, refine an existing system, or compare against a prior/sibling one? Routes to Phase 8 if it's not a clean new build.
- **Distribution**: one project, or reused across many? This single answer decides whether Phase 6 (packaging) applies at all. Get it wrong and you either over-engineer a one-off or under-engineer something that's about to drift across three repos.

## Phase 2 — Author tokens

In priority order — get these wrong and everything built on top inherits the wrong foundation.

**2.1 — Colors are authored once, as raw channel triplets, never as a bare hex.**
```css
--fire-rgb: 170 0 0;                          /* the only authored value */
--fire: rgb(var(--fire-rgb));                 /* derived */
--fire-soft: rgb(var(--fire-rgb) / 0.18);     /* derived */
```
This isn't stylistic. Tailwind (and most utility systems') opacity modifiers (`bg-fire/40`) cannot compose an alpha channel onto an opaque `var(--x)` hex value — the class silently resolves to nothing, no error, no warning. This exact bug is what started the hardening pass this pattern comes from. One authored number per color also means there's only ever one place to change it.

**2.2 — Every color that can render as text gets a `-text` variant, and glyphs use it, never the base.**
Verify contrast by computing WCAG relative luminance (formula in `assets/check-tokens.template.mjs`), not by eye. A tint that clears 4.5:1 against one surface can fail against another — which is exactly why 2.3 matters.

**2.3 — If there's more than one surface tier (page / panel / recessed), define it as a real elevation scale and measure the separation between tiers before committing.**
"A bit lighter" is not a decision, it's a guess. A real system reversed a whole elevation model (ink-as-page → void-as-page) after shipping it, purely because someone finally computed the actual composited contrast: 1.04:1 one way, 1.19:1 the other. Do that arithmetic *before* building on top of the choice, not after a stakeholder says "the cards feel flat."

Once there's a scale, every text-safe token needs contrast checked against **every tier it can appear on**, not just the one it was designed for.

**2.4 — Motion: one easing curve, a small fixed set of durations.**
If any JS animation (framer-motion, GSAP, a manual `requestAnimationFrame`) will consume these, export the curve and durations as JS constants alongside the CSS ones — a CSS variable is invisible to JavaScript, and a hand-typed bezier or duration drifts immediately and invisibly. Keep the CSS and JS versions checked against each other (Phase 4).

**2.5 — Numeric caps on anything glow/gradient-like must be real numbers, checked against the value actually shipped — including gradient stops, not just flat single-alpha colors.** "Subtle glow" with no enforced ceiling is how full-page ambient glow comes back, one component at a time, each one individually reasonable-looking.

**2.6 — Every token gets a one-line comment saying *when* to reach for it**, not just what it renders as.

## Phase 3 — Build primitives

- Components reference tokens exclusively. No hex, no arbitrary values, no `white/10`-style literals — these are exactly what Phase 4's guard checks for, so writing them now just means failing the check later.
- Any opacity-modifier usage (`bg-x/10`) must target a token that's actually alpha-composable per 2.1 — checkable, so check it, don't eyeball it.
- **Don't hardcode a variant into a component's base classes if a prop is meant to override it.** `className="shadow-lg"` baked into every card, with a prop meant to swap in `shadow-root-earth`, produces two box-shadow utilities at equal specificity — the winner is decided by source order in the generated stylesheet, silently. Make the variant a lookup table keyed by the prop (`Record<Variant, string>`), never a base class plus an expected override.
- **A styling prop is not a substitute for a real interactive element.** A card that looks clickable (`cursor-pointer`, hover lift) via an `interactive` prop, but is a `<div>`, gives a mouse user an affordance a keyboard user never gets — no focus ring, no role, no activation. If something is meant to be clicked, render an `<a>` or `<button>` (a `CardLink`/`CardButton` twin), not a styling toggle on the passive version.
- **For genuinely complex interactive components (modal, tabs, toast), lean on the platform.** Native `<dialog>` gives a focus trap and Escape-to-close for free; hand-rolled versions reliably get one of those wrong. Roving tabindex for tabs is the single most common thing hand-rolled tab implementations get wrong (every inactive tab stays a Tab stop) — verify it explicitly (tabindexes move `[0,-1,-1,-1] → [-1,0,-1,-1]` on arrow-key nav), don't assume.
- If the system needs custom icon/mark assets, fix the drawing rules up front (grid, stroke weight, cap style) and enforce them the same way as color rules — this is Phase 4's job too.

## Phase 4 — Guard it

Write a small, ideally zero-dependency, check script. This is the single highest-leverage artifact in the whole process — every bug in `references/bug-catalog.md` was a rule that existed only in prose until someone encoded it here.

Minimum coverage (adapt `assets/check-tokens.template.mjs`):
- Every token a component or preset references actually exists.
- No hand-typed hex or literal opacity color in component source.
- WCAG contrast for every text-safe token against every surface tier it can appear on (2.3).
- Documented numeric caps enforced as numbers on the actual shipped value — including the brightest stop of a gradient, not just simple colors (2.5).
- JS motion constants match their CSS token counterparts (2.4).
- Structural rules that are easy to violate by accident — e.g., "no full-page background glow": check that a glow utility is never applied to a page-level element, not just that the token's alpha is capped.
- Scope any rule that could match ordinary prose (e.g. a rule about "a second easing curve") to actual code contexts — class attributes, CSS values — not arbitrary text. A linter that flags your own documentation gets disabled, which defeats the point.

**The check must eventually run against consuming projects, not just the system's own repo.** This is the single biggest lesson available here: in one real system, every rule violation that ever actually happened — eleven type sizes under 24px, three different `<h2>` sizes on one site, five competing letter-spacing values, a second easing curve, invented durations — happened in a project *consuming* the system, and the internal check never looked there. It was, for a long time, guarding code that had never broken a rule. Ship the checker so it's runnable against arbitrary source (`npx your-check ./src`), and give it a scoped escape hatch for genuine exceptions (a `your-check-allow: <rule> — <reason>` comment convention) rather than making people disable the whole check.

**Negative-test every check before trusting it.** Deliberately break each rule in a scratch copy and confirm the script actually fails on it. A check that has never been observed to fail is unverified — you don't know if it works or is silently inert.

## Phase 5 — Document

Three files, split by audience — resist the urge to add a fourth. A fourth doc (an aggregated "design.md", a second style-guide-as-doc) is a second place for the same values to drift; three that each own a distinct question (why / what-to-do / what-was-decided) is enough.

- **`philosophy.md`** — the why, the identity, the meaning behind choices. Read once, rarely re-read.
- **`foundations.md`** — the operational rules. What someone checks before building something new. Should map roughly 1:1 to what Phase 4's guard enforces — if a rule is in one and not the other, pick which is missing and fix it.
- **`decisions.md`** — a running log, newest entry first, of specific judgment calls and why. **Never delete a superseded entry.** Mark it superseded and explain what changed and why. Reversing a real decision (an elevation model, an accent hierarchy) without a paper trail forces the next person — often future-you — to re-derive the reasoning from scratch, or worse, silently re-break what the original decision fixed.
- **A living showcase that renders the real tokens and components** — not a description of them. If it can't literally `import` the package (a static single-file HTML doc, say), it's carrying a second inlined copy of every value, and that copy *will* drift: one real system's showcase silently fell two versions behind its own tokens before anyone rebuilt it as something that imports the actual package. The fastest fix, if a static showcase is unavoidable for a while, is Phase 4 guarding the inlined copy against the real source — but plan to retire that as soon as the system is stable enough to have a real consumer.
- If the showcase is deployable, **deploy it to a real URL and view it at a real, narrow viewport.** A layout bug that only appears when a specific section is narrower than its content (an intentionally-overflowing decorative element widening the whole document, say) is invisible to every static check — not a token violation, not a contrast failure, not a lint error. It only exists in an actual browser at an actual width. One such bug shipped and survived three versions because the only place the system was ever viewed was a local file.
- Write down a versioning policy and the order to read the docs in, once there's more than one doc. Costs one paragraph, saves someone re-deriving it.

## Phase 6 — Package and distribute

Only if Phase 1 said "reused across projects."

- **Ship as an installable package** (`package.json` with an `exports` map). Never "copy these files into your project" — copying has no path for a downstream fix to flow back upstream, which is how a system's own source of truth quietly becomes the more-broken of two copies. This was the root cause of the very first bug in this whole lineage.
- **If distributing a Tailwind preset: a preset's `content` array is NOT merged by Tailwind.** A consumer's own `content` array replaces the preset's outright. This is the second-most costly bug in the catalog, and the "obvious" fix — declare the globs in the preset and assume they combine — does not work; the build comes back byte-identical, which is the tell. The preset must export its globs, and every piece of onboarding (README, a scaffold command if one exists) must show consumers spreading them explicitly: `content: [...preset.content, ...yourGlobs]`. Verify this with the bundler's own config-resolution API, don't assume — an unchanged build artifact after a "fix" is a bug signal, not a coincidence.
- **Version with tags, not just branches.** A branch pin moves silently under a consumer the moment the source repo's branch advances — which is exactly how a consumer can end up shipping an untested version without anyone deciding that. If a consumer needs to move to a new tag, remember lockfiles can pin the exact resolved commit independent of what the tag in `package.json` says — force re-resolution and verify `node_modules` actually reports the new version before trusting a rebuild.
- If the package offers a scaffold/init command for new consumers, have it emit the *correct*, spread-in content config from day one — don't rely on every consumer's README-reading discipline for a footgun serious enough to have its own decision-log entry.

## Phase 7 — Verify

Applies continuously, not just once at the end.

- **Test against a fresh install or clone, not the working directory.** A working directory hides missing exports, uncommitted fixes, and stale caches that a real consumer will hit on day one.
- **An unchanged build artifact after a "fix" is a signal the fix didn't work, not a coincidence.** Diff the actual output before believing anything changed.
- **Typechecking is not verification.** The most serious bug in this catalog — a font rendering in completely the wrong typeface — passed every static check available and was only caught by rendering the component in a real consumer and looking at it. Render everything at least once in something real before calling it done.
- **Distrust convenient-looking platform APIs for verification claims.** `document.fonts.check()` looks like exactly the right tool for "does this font actually contain this glyph" and lies (it reports availability of a matching font *face*, not the specific glyph). Measuring rendered width against a fallback font is what actually works. General lesson: if an API's claim can be checked by a cheap alternate method, check it before relying on it for anything load-bearing.
- **Effects driven by timers or animation frames need a fail-open path.** A `requestAnimationFrame`-driven replay silently never fires while a tab is backgrounded; an `IntersectionObserver`-driven reveal never fires on a zero-area element (a collapsed container, a hidden ancestor, a headless/backgrounded viewport reporting 0×0) — and if the entrance state is `opacity: 0` until observed, the content is invisible forever with no error anywhere. Guard both: default to visible/settled when the trigger can't fire, and prefer explicit state (a counter, a flag) over relying on frame timing for anything that has to be correct.
- **CSS-specificity ties are a silent-failure class of their own** — two classes at equal specificity on the same element, and the "loser" is whichever the bundler happened to emit second. If a component is designed to be overridden, make the override structurally win (a lookup table selecting one class, not two competing ones), not "usually wins because of source order."

## Phase 8 — Audit or evolve an existing system

Use `references/audit-checklist.md` — Phases 2–5 condensed into a scoring pass.

- **Before dismissing something as unrelated, verify — don't trust a name collision or a stale artifact.** A build folder's leftover generic scaffold title once caused a real, related prior system to be wrongly written off as noise; the actual project files, one directory up, told a completely different story. Read the actual source before concluding two things aren't connected.
- **When comparing to a prior/sibling system, extract what's worth keeping** — a specific hex value, an easing curve, a naming convention — even while retiring the system itself, and record *why* in `decisions.md` on the new system. Don't let institutional memory live only in a repo nobody opens again.
- **Reversing a shipped decision**: supersede in the log (Phase 5), never silently edit.
- **Retiring a system**: leave an explicit, honest deprecation notice — what carried over, what was actually wrong with it, why it was retired — rather than deleting it or abandoning it with no explanation. The next person (including future-you) needs to know it was a deliberate call, not neglect.

## Reference material

- `references/bug-catalog.md` — every real bug behind the rules above, as a lookup table. Skim before starting something large.
- `references/audit-checklist.md` — condensed scoring checklist for Phase 8.
- `assets/tokens.template.css` — the triplet → derived pattern, an elevation-scale skeleton, motion tokens with the JS-parity comment.
- `assets/tailwind-preset.template.cjs` — preset skeleton with the `content` export and the spread-it-in warning.
- `assets/check-tokens.template.mjs` — a generalized guard script covering Phase 4's minimum checklist, with TODOs marking where a new system's specific token names need to be filled in.
