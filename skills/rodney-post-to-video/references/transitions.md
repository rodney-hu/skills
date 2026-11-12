# Fractal zoom transition

Prototype: `~/Desktop/RodneyOS/01 Projects/videos/fractal-zoom/.tesseract-work/build.py` (3 dives in, then a level-by-level pull-out).

## How it works
1. Put the current scene's content (with its full-frame bg rect) in a camera group: `cam = group("Camera", 0, None, layers + [bg])`.
2. Add a portal to it: `cam["layers"][:0] = portal("P", cx, cy, d, build_next_static(), NEXT_BG, stroke=EL[1])`.
   `build_next_static()` must be a fresh, un-animated build of the next scene's opening frame, without its bg rect.
3. Dive: `zoom_through(cam, cx, cy, d, t0, t1)` on the scene's clock, with `t1` = the scene's end.
4. The next scene starts at that moment with exactly the same static layout, then animates (text rises etc.).
5. Pull back: `zoom_through(cam, cx, cy, d, 0, dur, out=True)` on a scene that starts inside its portal.

## Rules
- Keep text outside `cam` and fade it before `t0`; the next scene's text rises after the cut.
- Don't `drift()` a camera group (it keys the same scale props).
- The portal can be off-centre; the camera tracks it to screen centre.
- Images (wordmark) blur when scaled up: keep them out of a camera that dives.
- No masks: the disc fill hides the copy's edges, so give the next scene a background that matches the disc fill.
- 3 beats per dive feels right at 125 bpm; 2 beats per level for a pull-out. Whoosh at t0, soft-impact on arrival.
