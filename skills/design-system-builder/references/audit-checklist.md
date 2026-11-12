# Audit checklist

Condensed scoring pass for Phase 8. Score each row honestly — "yes, but only in one place" is a no. For each "no," the fix is the linked phase in `SKILL.md`.

## Tokens (Phase 2)

- [ ] Every color is authored once as a raw channel triplet; derived values (solid, soft, glow) come from it, not hand-typed separately.
- [ ] Every color that renders as text has a dedicated `-text` variant, and components actually use it instead of the base.
- [ ] Contrast is computed (formula, not eyeballed) for every text-safe token against **every surface tier it can appear on**.
- [ ] If there's more than one surface tier, the separation between them has been measured, not assumed.
- [ ] Motion has exactly one easing curve and a small fixed set of durations, and if any JS animation is used, the same values exist as JS constants — checked against the CSS ones.
- [ ] Any glow/gradient token has a numeric cap that's actually enforced against the shipped value (including gradient stops), not just described in a comment.
- [ ] Every token has a one-line "when to use this" comment.

## Primitives (Phase 3)

- [ ] No component hand-types a hex code, an arbitrary value, or a `white/xx`-style literal.
- [ ] No opacity-modifier class (`bg-x/10`) targets a color that can't actually compose alpha.
- [ ] No component has a variant prop whose intended override collides at equal CSS specificity with a hardcoded base class.
- [ ] Nothing that looks clickable (cursor, hover state) is a non-interactive element with a styling prop standing in for real interactivity — check for a real `<a>`/`<button>` underneath, or a keyboard-accessible twin.
- [ ] Complex interactive components (modal, tabs, menu) lean on native elements/ARIA patterns where possible, and their keyboard behavior has been explicitly verified, not assumed.

## Guard script (Phase 4)

- [ ] A check script exists and actually runs (in CI, pre-commit, or at minimum `npm run check`).
- [ ] It covers: token existence, hand-typed literals, contrast, numeric caps, motion JS/CSS parity, and any system-specific structural rule (e.g. "no full-page glow").
- [ ] It can run against a consumer's source tree, not only the system's own repo.
- [ ] Every check has been negative-tested at least once (deliberately broken and confirmed to fail) — not just written and assumed to work.
- [ ] No rule can false-positive on prose/documentation text.

## Docs (Phase 5)

- [ ] Exactly three docs exist for why / what-to-do / what-was-decided — not zero, not four+.
- [ ] `foundations.md` maps roughly 1:1 to what the guard script actually enforces.
- [ ] `decisions.md` entries are newest-first, and superseded entries are marked superseded with reasoning, not deleted.
- [ ] The showcase/style guide renders real tokens and components (imports the actual source), not a hand-maintained second copy.
- [ ] If the showcase is deployable, it's deployed to a real URL and has been viewed at a real narrow viewport, not only opened as a local file.

## Distribution (Phase 6 — only if reused across projects)

- [ ] The system installs as a package with an exports map — there is no "copy these files into your project" instruction anywhere.
- [ ] If a Tailwind preset is distributed, its `content` globs are exported AND every piece of consumer-facing documentation shows them being spread into the consumer's own `content` array (not just declared in the preset and assumed to merge).
- [ ] Versions are tagged, not just branch-pinned.
- [ ] At least one consumer has been rebuilt from a clean install against the current tag, with `node_modules` checked to confirm the resolved version actually changed.

## Verification discipline (Phase 7)

- [ ] The last real fix was verified against a fresh install/clone, not the working directory.
- [ ] Build output was diffed, not just re-run and glanced at.
- [ ] At least one component has actually been rendered in a real consumer and visually inspected — not only typechecked.
- [ ] Any platform API used to verify a claim (font coverage, layout, timing) has itself been sanity-checked against a cheap alternate method at least once.
- [ ] Any timer/observer-driven effect (scroll reveal, replay animation) has an explicit fail-open path for the case where its trigger never fires.

## Evolving/retiring a prior system (Phase 8)

- [ ] Any claim that two systems are "unrelated" has been verified by reading actual source, not inferred from a name or a build artifact.
- [ ] Anything worth keeping from a retired system (specific values, curves, naming) has been extracted and the reasoning recorded in the new system's `decisions.md`.
- [ ] The retired system has an explicit, honest deprecation notice — not silent abandonment.
