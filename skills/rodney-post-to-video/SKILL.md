---
name: rodney-post-to-video
description: "Rodney's post-to-video skill: turns an X or LinkedIn post (or a Content HQ row in Notion) into an editable Tesseract motion-graphic video, 1080x1350 MP4, in Rodney's avatar-design system with the RODNEY HU wordmark sign-off, timed to a music beat grid. Use when Rodney asks for a video or motion graphic from a post, or /rodney-post-to-video."
argument-hint: "<post text or Content HQ page URL> [design reference url/screenshot] [screenshot of real data]"
---

# rodney-post-to-video

Videos for Rodney's own brand (Rodney Hu / House of Hu). Every video uses the **avatar-design system** (dark by default) and signs off with the **RODNEY HU wordmark**. No third-party logos, CTAs or brand names on screen unless the post itself is about that product, and even then only as plain text, never their logo.

## Before step 1: load my context
Read `references/brand-profile.md`, `references/avatar-design.md` and `references/lessons.md` in this skill's directory. If the input is a Notion Content HQ URL, fetch it for the post (Draft), Hook, Angle and Source Project instead of asking for pasted text. After finishing, append new lessons to `references/lessons.md`, add a row to `references/catalog.md`, and (optionally) write the MP4 path back to the Content HQ row's Asset Link.

`templates/build.py` is the avatar-design dark starter (hook / list / stat card / wordmark sign-off); `templates/build-light.py` is the parchment variant (only when the brief asks for light). For a full worked example, read `videos/human-judgment/.tesseract-work/build.py`.

One post in, one finished video out: `videos/<slug>/<Name>.mp4` plus the editable `<Name>.tsrct`,
a `build.py` that generates every layer and keyframe, and a `NOTES.md`.

The pipeline is Python → editable JSON → `tsrct project commit` → `tsrct export`. All shared code
lives in `lib/motion.py`. Each video only writes scenes. This skill sits on top of
`tesseract-motion` (CLI install, schema, filmstrip review): read that skill's references only when
you need something the library doesn't cover.

## 0. Setup (once per machine)

Use this skill's own directory. When the skill loads, that directory is the "Base directory for this skill". It lives at `~/.claude/skills/rodney-post-to-video`. The `tsrct` install guide and schema come from the separate `tesseract-motion` skill (setup.sh points to it).

```bash
bash "<skill-dir>/scripts/setup.sh"    # checks pinned tsrct, creates the Python venv, checks Linux libraries
source "<skill-dir>/scripts/env.sh"    # sets $PY, $T, $POST_TO_VIDEO
"$T" --version                         # must match tesseract-motion/references/cli-version.txt
```

If `setup.sh` says `tsrct` is missing or the wrong version, follow `tesseract-motion/references/installation.md` (the skill installed beside this one). That guide downloads the pinned CLI zip, checks its checksum, and runs the official `install.sh`. Then run `setup.sh` again.

`setup.sh` does not download `tsrct` and does not use sudo. On Linux it also checks for a Vulkan driver and for `ffmpeg` with libx264. On macOS it warns when ffmpeg is missing (`brew install ffmpeg`; beats.py, music auto-length and the LUFS readout need it). If it prints an install command, run that command, then run `setup.sh` again. Later steps assume `env.sh` has been sourced.

## 1. Read the post

- Pull out the beats of the argument: hook → mechanism steps → proof → closing line + wordmark sign-off. One scene each; 5–8 scenes, **25–35 s total**.
- **Pacing:** hook ≈ 10 beats, most scenes 8–12 beats, one "hero" scene up to ~18. List items land every 1–2 beats, not 4. Staggered grids/tiles 40–110 ms apart. Hold a finished state ~1–1.5 s, then cut. No idle beats waiting for the next element. A cut near 48 s is too slow; about 28 s is the pace that works. Stay in 25–35 s.
- **Flag, don't silently fix**: likely typos in product or model names, numbers that don't match supplied data, and claims you can't support. Use the sensible reading on screen and list every change in the final message.
- Sign-off: the last scene ends on `wordmark()` (RODNEY HU). No product CTA, URL or third-party mark unless Rodney asks for one.
- If the user attaches a **screenshot of real data**, redraw it natively (read values off the pixels), state which values are exact vs. read off the chart, and keep the post's claim and the chart consistent or flag the gap.
- If the user names a **design reference** (URL or screenshot), that overrides the seed concept for the look. Read it (ask before opening a browser; Cloudflare sites block curl/WebFetch), match its type, colour, components and motion, and keep the RODNEY HU wordmark sign-off. Never put a third-party logo on screen.

## 2. Seed → concept

```bash
bash $POST_TO_VIDEO/scripts/seed.sh videos/<slug>-seed.txt 120    # prints palindromes, runs, doubles, hidden words, digit sums, factors
```

Look past the surface: hidden words/abbreviations, palindromes, a digit sum that also appears as a
substring, clusters, the length's factors (96 = 8×12 → a 12-column grid). Tie 2–4 findings to the
post's message and turn them into ONE visual system (a world + a signature motion + one persistent
element). Examples that worked: "007" → version numbers → a changelog; "p2"+"hde" → hide on page 2
→ a scrolling page with a rank ruler; "vOv" → a face → the bot avatar.

- **Never show the string**, or a recognisable chunk of it, on screen. Save it in `.tesseract-work/seed.txt`.
- Check `references/catalog.md` and pick a system that hasn't been used. Different from the last video, not a reskin.
- Tell the user in 2–4 lines which patterns you found and what they became.

## 3. Music

```bash
$PY $POST_TO_VIDEO/scripts/beats.py $POST_TO_VIDEO/assets/music/<track>.mp3 --need 50
$PY $POST_TO_VIDEO/scripts/beats.py $POST_TO_VIDEO/assets/music/<track>.mp3 --zoom 31.2    # confirm a drop
```

Choose from `references/music.md` (prefer an unused track/section). Put the quiet part under the
first line of the hook and the drop on beat 3–4 (≈2 s) under the key line. All scene boundaries are
beats. Weak-grid tracks (strength < 1.25) are out.

## 4. Build

```bash
bash $POST_TO_VIDEO/scripts/new.sh <slug> <CamelName> <track>     # claims videos/<slug> (fails if it exists), copies fonts/sfx/wordmark/music, writes template build.py + rebuild.sh
cp videos/<slug>-seed.txt videos/<slug>/.tesseract-work/seed.txt && rm videos/<slug>-seed.txt
```

Edit `videos/<slug>/.tesseract-work/build.py` (the template shows hook / list / stat counter / wordmark sign-off):

- `setup(ROOT)`, then `B = Beats(period, [scene beats…])`, `MUSIC_SRC0 = <in-point ms>`. The avatar-design palette is already in `motion`: `BG BASE RAISED ELEV TEXT SEC MUTED SUBTLE BORDER STRONG FIRE FIRE4 FIREG WATER EARTH AIR AVATAR`, `LIGHT[...]` for parchment, `hx("#rrggbb")` for anything else.
- Scene groups: `group(name, S[i], D[i], layers)` + `enter_scene` / `exit_scene`. Times inside a scene use `B.lb(i, beat)`; SFX use project time `B.pt(i, beat)`.
- Library: `text rect circle path_shape line polyline check image group pivot shadow`,
  `key fade rise pop show hide snap_in typing counter stepped scramble redact`,
  `pill offset tokens_line wordmark Thread bubble`, `icon tile gate draw_on drift`, `portal zoom_through zoom_keys` (fractal zoom transition), `sfx music write_doc`. Read `lib/motion.py` docstrings.
- Starter look (`templates/build.py`): text is white `TEXT` + red `FIRE4` only (labels `SEC`). Element colours (`ELEMENTS`)
  go on graphics: `tile()` icon tiles (kinds in `ICONS`: spark bolt user chart doc loop target eye), tinted bars, dots.
  Prefer an icon/graphic next to a claim over text alone. Motion stays subtle: `drift()` per scene, icons `draw_on`,
  `gate()` closes on approvals, progress footer fills one segment per scene.
- Fractal zoom transition (`references/transitions.md`): `portal()` plants a tiny copy of the next scene in a disc;
  `zoom_through(cam, cx, cy, d, t0, t1)` dives into it and the next scene hard-cuts in; `out=True` pulls back.
- Fonts (avatar-design defaults): `head` Inter ExtraBold, `body` Inter, `bodym` Inter Medium, `bodyb` Inter Bold,
  `mono`/`monom` JetBrains Mono, `hero` Cinzel 800 (one hero title only), `brush` Avatar Airbender (standalone headings).
  Extras: `geist geistr gmono gmonom outfit outfitm jbmono type typeb`. Remap with `setup(ROOT, fonts={"head": FONT_FILES["geist"]})`.
- `wordmark(x, y, width=480, theme="dark")`: RODNEY HU image, top-left at (x, y); `theme="light"` on parchment. Keep it ≥ 360 px wide.
- **Rules that bite** (`references/quirks.md`): fade Shapes through a group; keep text lines ≤ 900 px;
  `layers[0]` is on top; text y is the baseline; no ✓ glyph (use `check()`); 1 ms offsets for
  coincident HOLD keys.
- Default 1080x1350, avatar-design dark, Fire as the lead accent, Avatar cyan for one hero moment. Parchment light only if the brief/reference calls for it.
- Mock content (sample names, counts, code) is fine; real-looking numbers that are not from the user must be listed as illustrative in the final message.

```bash
videos/<slug>/.tesseract-work/rebuild.sh                     # ~15 s; prints WARN lines, fix them
bash $POST_TO_VIDEO/scripts/check.sh videos/<slug>             # 20 evenly spaced frames -> checks/fs-a.png, fs-b.png
bash $POST_TO_VIDEO/scripts/check.sh videos/<slug> 1500 2400 …  # or specific ms
```

Open both filmstrips (Read) and fix: overlaps, text wrapping, empty halves of the frame, things
appearing before/after they should, colours on colours (an orange stamp on an orange card
disappears), labels colliding. Use `"$T" preview --project … --time <s> --output x.png` for a
full-size frame. Iterate until clean. Usually 1–3 passes.

## 5. Export and deliver

```bash
bash $POST_TO_VIDEO/scripts/export.sh videos/<slug>            # run in background: ~60-80 s; prints streams, LUFS, peak; writes Previews/Filmstrip.png
```

Then:
1. Write `videos/<slug>/.tesseract-work/NOTES.md`: brief, seed patterns → concept, look, music + in-point
   + beat (estimated, not listened), scene beats, real vs. illustrative data, copy changes.
2. Add a row to `references/catalog.md` (and `music.md` "Used by").
3. Send the MP4 with SendUserFile (display: render).
4. Final message: the concept in 2–4 lines, scene-by-scene list, audio numbers, and a **flag list**:
   copy changes, claim/data gaps, illustrative content, "beat sync not confirmed by ear".

Revisions: copy the current mp4 + build.py into `Versions/` before a redesign, then edit build.py
and re-run rebuild → check → export.
