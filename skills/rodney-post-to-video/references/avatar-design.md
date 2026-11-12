# avatar-design system: video translation

Source of truth: the avatar-design repo at `~/Desktop/RodneyOS/01 Projects/avatar-design` (tokens in `design-system/tokens/`, live showcase avatar-design2.vercel.app). The Notion "Elemental Design System Reference" (`{{DESIGN_SYSTEM_NOTION_URL}}` in `config.local.md`) is the older write-up of the same system. Re-check the repo tokens if this file looks stale.

Every constant below is already defined in `lib/motion.py`. Use the names, not hex.

## Colors (dark default; `LIGHT[...]` = parchment)
| Role | Name | Dark | Light |
|---|---|---|---|
| Void (video bg) | `BG` | #0a0a0a | #f5f0eb |
| Base | `BASE` | #0d0d0d | #faf7f4 |
| Raised (cards) | `RAISED` | #1a1a1a | #ffffff |
| Elevated | `ELEV` | #252525 | #ffffff |
| Text / secondary / muted | `TEXT SEC MUTED` | #f0f0f0 / #a0a0a0 / #666666 | #1a1a1a / #555555 / #888888 |
| Border subtle / default / strong | `SUBTLE BORDER STRONG` | #1f1f1f / #2a2a2a / #3a3a3a | #e5e0db / #d4cec8 / #b0a99f |

Elements:
- Fire `FIRE` #aa0000: fills, primary.
- Fire 400 `FIRE4` #dd3333: any Fire TEXT on dark, because 500 fails contrast there.
- Fire glow `FIREG` #e01010.
- Water `WATER` #0088e0 · Earth `EARTH` #27ae34 · Air `AIR` #e6bf00.
- Avatar cyan `AVATAR` #00ffff: ONE hero moment per video, never body text.

## Type (bundled in `assets/fonts/`, licences in `assets/fonts/licenses/`)
- `head`: Inter ExtraBold for headlines, tracking about -20.
- `body` / `bodym` / `bodyb`: Inter Regular / Medium / Bold.
- `mono` / `monom`: JetBrains Mono for labels and numbers. Uppercase labels at tracking 60–100.
- `hero`: Cinzel 800, the one hero title only. No → glyph.
- `brush`: Avatar Airbender, for standalone headings only. Never body text. No → glyph.

## Brand mark
- `wordmark(x, y, width, theme)`: RODNEY HU in white letters with HU on a Fire block (`assets/rodney-hu-wordmark.png`, 1476×394). `theme="light"` switches to the parchment version (RODNEY in ink, HU stays white on Fire).
- Use it on the sign-off scene only, at least 360 px wide, with clear space of about half its height. Don't recolour it, outline it or put it on a Fire fill.

## Shape and motion
- Radius: 8 cards, 6 small, 12 modals, full for pills.
- Motion restraint: one reveal per block; hold finished states ~1–1.5 s.
- Fire is snappy, Water fluid, Earth grounded, Air springy.

## Text vs graphics colour
Text is white (`TEXT`) and red (`FIRE4`) only, with grey (`SEC`) for mono labels. Water, Earth, Air (and Fire) colour graphics: icon tiles, bars, dots, card top bars. Avatar cyan is optional: at most once, as a graphic. The starter doesn't use it (no underline under text).

## Video motifs that worked
Persistent gate/ring that a human "closes" after each step (`gate()`); element icon tiles per row (`tile()`); stat cards with counters; tinted element bars; four element dots; segmented progress footer. See `templates/build.py` and `~/Desktop/RodneyOS/01 Projects/videos/human-judgment/.tesseract-work/build.py`.
