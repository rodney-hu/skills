# Check menus

Pick the checks a task needs and copy them into the contract with an ID. Each is pass/fail. The evidence column says what proves it.

## Copy (C)

| ID | Check | Evidence |
|---|---|---|
| C1 | A reader gets the point in 5 seconds: the headline states the outcome | reviewer reads headline only |
| C2 | Written in the buyer's words; no jargon ("leverage", "seamless", "unlock") | reviewer + grep for banned words |
| C3 | One call to action per page or section | reviewer counts CTAs |
| C4 | Every claim is backed by a number, example, or source; no invented stats | reviewer lists each claim and its backing |
| C5 | No AI tells (unslop pass, or `rodney-writing-style` verify script) | script output |
| C6 | Tight: no sentence that doesn't move the reader forward | reviewer flags cuttable lines |

## Design (D)

| ID | Check | Evidence |
|---|---|---|
| D1 | 375px wide: no horizontal scroll | screenshot + `scrollWidth <= 375` |
| D2 | Hierarchy reads headline, then proof, then CTA | 375px and 1280px screenshots |
| D3 | Text contrast meets WCAG AA; body text >= 16px | Lighthouse a11y or axe output |
| D4 | Spacing, type and colors match the brand kit or design tokens | reviewer vs tokens; `check-tokens` if present |
| D5 | Mobile and desktop screenshots saved this round | files in `.eval/rounds/<n>/` |
| D6 | Lighthouse performance >= 90 and accessibility >= 90 | Lighthouse JSON |

## Backend (B)

| ID | Check | Evidence |
|---|---|---|
| B1 | Build passes | build command exit 0 |
| B2 | No new console or server errors | console log diff vs last round |
| B3 | Happy path works end to end with a real submit and the real result | command or test output showing the stored/returned result |
| B4 | Edge cases handled: empty input, bad input, double submit, timeout | one test or scripted call per case |
| B5 | No secrets in source; inputs validated at the boundary | grep for key patterns + reviewer |
| B6 | qa-auditor: no CRITICAL or ALERT findings | reviewer's qa-auditor report |
| B7 | Only files in scope changed | `scope_check.py` output |

## Product (P)

| ID | Check | Evidence |
|---|---|---|
| P1 | Does the one job in the goal | reviewer walks the goal step by step |
| P2 | A stranger can use it without help | reviewer follows only on-screen text |
| P3 | Rodney can verify it in under 2 minutes | the 2-minute steps written in the final block |
| P4 | Nothing extra was built; extras are in `parked.md` | diff vs plan |

## Defaults by tier

- Light: the automated checks the change touches (usually B1, B7, C5).
- Standard: the relevant category menu plus B1, B7, P1, P4.
- Full: every menu that applies plus all standing checks in `.eval/checklist.md`.
