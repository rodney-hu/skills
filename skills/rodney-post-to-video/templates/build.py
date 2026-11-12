"""__NAME__: generates .tesseract-work/editable.json for this post video.

Concept: <one line: what the seed patterns became, and the visual system>
Look: avatar-design dark. Text is white (TEXT) + red (FIRE4) only; element colours go on graphics
(icon tiles, bars, dots). Fire approval gate motif from human-judgment. Avatar cyan is optional (once, as a graphic).
Run: $PY .tesseract-work/build.py   (rebuild.sh does this, then commits)
"""
import os, sys
sys.path.insert(0, "__SKILL_LIB__")
from motion import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup(ROOT)                                     # 1080x1350 (LinkedIn 4:5); Inter / JetBrains Mono / Cinzel / brush
L, R = 80, 1000                                 # content margins (keep single text lines <= 900 px)
EL = [c for _, c in ELEMENTS]                   # FIRE4, WATER, EARTH, AIR: graphics only, never text

# ---------- timing: beat grid from scripts/beats.py ----------
MUSIC_SRC0 = 11748                              # source ms of the in-point (lift lands on beat 4)
B = Beats(481.1, [0, 10, 22, 36, 48])           # scene boundaries in beats; last = end
S, D = B.S, B.D
P = B.P
scenes = []


def head(lab, l1, l2=None, y0=250):
    """Mono section label (grey) + white headline + red second line (each <= 900 px)."""
    out = []
    lab_ = text("Label", "", L, y0 - 70, "monom", 21, SEC, 100); typing(lab_, lab, 60, cps=60); out.append(lab_)
    a = text("Headline 1", l1, L, y0, "head", fit(l1, "head", 72, 900, -20), TEXT, -20); rise(a, 120, dy=22); out.append(a)
    if l2:
        b = text("Headline 2", l2, L, y0 + 84, "head", fit(l2, "head", 72, 900, -20), FIRE4, -20); rise(b, 260, dy=22); out.append(b)
    return out


# ---------- scene 0: hook (the gate closes on the drop, beat 4) ----------
s = []
lab = text("Hook label", "", L, 300, "monom", 21, SEC, 100); typing(lab, "TOPIC · CONTEXT · NUMBER", 60, cps=45)
h1 = text("Hook 1", "first line of the hook", L, 400, "head", fit("first line of the hook", "head", 92, 900, -20), TEXT, -20)
h2 = text("Hook 2", "the line on the drop.", L, 500, "head", fit("the line on the drop.", "head", 92, 900, -20), FIRE4, -20)
rise(h1, B.lb(0, 1)); rise(h2, B.lb(0, 4) - 60)
g0 = gate("Gate", 540, 860, 280, B.lb(0, 4))
key(g0[-1], "opacity", B.lb(0, 1), 0); key(g0[-1], "opacity", B.lb(0, 1) + 400, 100, EO)   # ring fades in first
orbit = []                                      # four element dots settle around the gate after the drop
for k, col in enumerate(EL):
    a = math.radians(-90 + 90 * k)
    d_ = circle(f"Orbit {k}", 540 + 210 * math.cos(a), 860 + 210 * math.sin(a), 18, fill=col)
    show(d_, B.lb(0, 5) + k * 90); pop(d_, B.lb(0, 5) + k * 90, a=0, dur=260)
    orbit.append(d_)
sfx("soft-impact", B.pt(0, 4), 0.6)
s += [lab, h1, h2] + orbit + g0
g = group("0 · Hook", S[0], D[0], s); drift(g, D[0]); exit_scene(g, D[0]); scenes.append(g)

# ---------- scene 1: list; each row gets an element tile, then a human closes its gate ----------
s = head("STEP 01 · EXAMPLE", "a list that builds", "on the beat.")
rows = [("doc", "first item"), ("bolt", "second item"), ("user", "third item")]
for i, (kind, item) in enumerate(rows):
    y = 430 + i * 150
    t = B.lb(1, 2 + 2 * i)
    ta = t + P                                  # approval one beat after the row lands
    card = rect(f"Row {i} card", L, y, R - L, 120, RAISED, r=8, stroke=BORDER, sw=1.5)
    hl = rect(f"Row {i} active", L, y, R - L, 120, CLEAR, r=8, stroke=FIRE4, sw=2.5)
    key(hl, "opacity", 0, 0, HOLD); key(hl, "opacity", t, 100, HOLD); key(hl, "opacity", ta + 120, 100); key(hl, "opacity", ta + 600, 0, EO)
    tl = tile(f"Row {i} tile", kind, L + 20, y + 20, 80, EL[i % 4], t=t + 80)
    tx = text(f"Row {i}", item, L + 130, y + 72, "bodym", fit(item, "bodym", 32, 680), TEXT)
    gt = gate(f"Row {i} gate", R - 60, y + 60, 48, ta)
    rg = group(f"Row {i}", 0, None, gt + [tl, hl, tx, card]); rise(rg, t, dy=26, dur=380)
    sfx("soft-tap", S[1] + t, 0.4); sfx("soft-pop", S[1] + ta, 0.35)
    s.append(rg)
g = group("1 · Example", S[1], D[1], s); drift(g, D[1]); enter_scene(g); exit_scene(g, D[1]); scenes.append(g)

# ---------- scene 2: proof (two stat cards + element bar chart) ----------
s = head("RESULT", "a number that", "counts up.")
for k, (val, lab_t, col, kind) in enumerate([(65, "ILLUSTRATIVE", EL[0], "chart"), (93, "ILLUSTRATIVE", EL[1], "target")]):
    x, t0 = L + k * 480, B.lb(2, 2 + 2 * k)
    card = rect(f"Stat {k} card", x, 410, 440, 380, RAISED, r=8, stroke=BORDER, sw=1.5)
    bar = rect(f"Stat {k} bar", x, 410, 440, 6, col, r=3)
    tl = tile(f"Stat {k} tile", kind, x + 340, 446, 64, col, t=t0 + 200)
    n = text(f"Stat {k}", "0", x + 36, 660, "head", 200, TEXT, -40)
    counter(n, t0 + 60, t0 + 60 + 3 * P, val); fade(n, t0, 200)
    lb_ = text(f"Stat {k} label", lab_t, x + 36, 746, "monom", 24, SEC, 60); fade(lb_, t0 + 200, 300)
    gr = group(f"Stat {k}", 0, None, [tl, lb_, n, bar, card]); rise(gr, t0, dy=24, dur=380)
    sfx("soft-tap", S[2] + t0, 0.4); sfx("clear-ping", S[2] + t0 + 60 + 3 * P, 0.28)
    s.append(gr)
base = line("Chart base", L, 1160, R, 1160, BORDER, 2)
s.append(base)
for k, (hgt, col) in enumerate(zip([120, 190, 150, 250], EL)):
    t = B.lb(2, 8 + k)
    b_ = rect(f"Chart bar {k}", L + 20 + k * 236, 1160 - hgt, 180, hgt, [*col[:3], 0.18], r=6, ay=hgt, stroke=col, sw=2)
    key(b_, "scaleY", t, 0); key(b_, "scaleY", t + 520, 100, EO)
    sfx("soft-pop", S[2] + t, 0.25)
    s.append(b_)
g = group("2 · Proof", S[2], D[2], s); drift(g, D[2]); enter_scene(g); exit_scene(g, D[2]); scenes.append(g)

# ---------- scene 3: closing line + RODNEY HU sign-off ----------
s = head("THE POINT", "the one line", "to remember.", y0=420)
mark = group("Wordmark", 0, None, [wordmark((W - 600) / 2, 760, 600)]); fade(mark, B.lb(3, 4), 400)
dots = []
for k, col in enumerate(EL):
    d_ = circle(f"Sign-off dot {k}", W / 2 - 60 + k * 40, 1040, 14, fill=col)
    show(d_, B.lb(3, 6) + k * 110); pop(d_, B.lb(3, 6) + k * 110, a=0, dur=240)
    dots.append(d_)
sfx("soft-pop", B.pt(3, 4), 0.45)
s += dots + [mark]
g = group("3 · Sign-off", S[3], D[3], s); drift(g, D[3]); enter_scene(g); scenes.append(g)

# ---------- chrome: progress footer (one segment per scene fills while it plays) ----------
ch = [text("Footer left", "HOUSE OF HU", L, 1284, "mono", 18, FIRE4, 80)]
cnt = text("Footer right", "", R, 1284, "mono", 18, SEC, 80, just="right")
stepped(cnt, [(S[i], f"{i + 1:02d} / {len(S):02d}") for i in range(len(S))])
ch.append(cnt)
gap = 12
sw_ = (R - L - gap * (len(S) - 1)) / len(S)
for i in range(len(S)):
    x = L + i * (sw_ + gap)
    fl = rect(f"Progress {i}", x, 1238, sw_, 4, FIRE4, r=2)
    key(fl, "scaleX", S[i], 0); key(fl, "scaleX", S[i] + D[i], 100)
    ch += [fl, rect(f"Progress {i} track", x, 1238, sw_, 4, STRONG, r=2)]
chrome = group("Chrome", 0, B.TOTAL, ch)
for b in S[1:]:
    sfx("air-whoosh", b - 220, 0.22)

write_doc("__NAME__", [chrome] + scenes[::-1], B.TOTAL, BG,
          music_layer=music(MUSIC_SRC0, B.TOTAL, vol=0.45))
