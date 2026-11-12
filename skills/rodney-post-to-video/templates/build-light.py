"""__NAME__: generates .tesseract-work/editable.json for this post video.

Concept: <one line: what the seed patterns became, and the visual system>
Look: avatar-design parchment (light) theme. Use only when the brief asks for light.
Run: $PY .tesseract-work/build.py   (rebuild.sh does this, then commits)
"""
import os, sys
sys.path.insert(0, "__SKILL_LIB__")
from motion import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT, SEC, MUTED = LIGHT["TEXT"], LIGHT["SEC"], LIGHT["MUTED"]
BG, RAISED, BORDER = LIGHT["BG"], LIGHT["RAISED"], LIGHT["BORDER"]
setup(ROOT, ink=TEXT)                           # 1080x1350; Inter / JetBrains Mono / Cinzel ("hero") / brush
L, R = 80, 1000                                 # content margins (keep single text lines <= 900 px)
ACC = FIRE                                      # Fire 500 passes contrast on parchment

# ---------- timing: beat grid from scripts/beats.py ----------
MUSIC_SRC0 = 28131                              # source ms of the in-point (lift lands on beat 4)
B = Beats(469.8, [0, 10, 24, 36, 48])           # scene boundaries in beats; last = end
S, D = B.S, B.D
scenes = []


def head(lab, l1, l2=None, y0=250):
    """Section label + one or two headline lines (each <= 900 px)."""
    out = []
    lab_ = text("Label", "", L, y0 - 70, "monom", 21, ACC, 100); typing(lab_, lab, 60, cps=70); out.append(lab_)
    a = text("Headline 1", l1, L, y0, "head", fit(l1, "head", 72, 900, -20), TEXT, -20); rise(a, 120, dy=22); out.append(a)
    if l2:
        b = text("Headline 2", l2, L, y0 + 84, "head", fit(l2, "head", 72, 900, -20), ACC, -20); rise(b, 260, dy=22); out.append(b)
    return out


# ---------- scene 0: hook (the drop lands on beat 4) ----------
s = []
h1 = text("Hook 1", "first line of the hook", L, 520, "head", fit("first line of the hook", "head", 84, 900, -20), TEXT, -20)
h2 = text("Hook 2", "the line on the drop.", L, 616, "head", fit("the line on the drop.", "head", 84, 900, -20), ACC, -20)
rise(h1, B.lb(0, 1)); rise(h2, B.lb(0, 4) - 60)
sfx("soft-impact", B.pt(0, 4), 0.6)
s += [h1, h2]
g = group("0 · Hook", S[0], D[0], s); exit_scene(g, D[0]); scenes.append(g)

# ---------- scene 1: example list that builds on the beats ----------
s = head("STEP 01 · EXAMPLE", "a list that builds", "on the beat.")
for i, item in enumerate(["first item", "second item", "third item"]):
    y = 470 + i * 110
    t = B.lb(1, 2 + i)
    bg = rect(f"Row {i} card", L, y, R - L, 90, RAISED, r=8, stroke=BORDER, sw=1.5)
    ck = check(f"Row {i} check", L + 28, y + 30, 28, ACC)
    tx = text(f"Row {i}", item, L + 76, y + 57, "bodym", 32, TEXT)
    rg = group(f"Row {i}", 0, None, [ck, tx, bg])
    key(rg, "opacity", t, 0); key(rg, "opacity", t + 180, 100, EO)
    key(rg, "positionX", t, 30); key(rg, "positionX", t + 380, 0, EO)
    sfx("soft-tap", S[1] + t, 0.4)
    s.append(rg)
g = group("1 · Example", S[1], D[1], s); enter_scene(g); exit_scene(g, D[1]); scenes.append(g)

# ---------- scene 2: proof / payoff ----------
s = head("RESULT", "a number that counts up.")
n = text("Counter", "0", L, 640, "head", 200, TEXT, -40)
counter(n, B.lb(2, 2), B.lb(2, 6), 1000, fmt="${n}")
fade(n, B.lb(2, 2), 200)
s.append(n)
g = group("2 · Proof", S[2], D[2], s); enter_scene(g); exit_scene(g, D[2]); scenes.append(g)

# ---------- scene 3: closing line + RODNEY HU sign-off (ink-letter wordmark) ----------
s = head("THE POINT", "the one line", "to remember.", y0=420)
mark = group("Wordmark", 0, None, [wordmark((W - 600) / 2, 820, 600, theme="light")]); fade(mark, B.lb(3, 4), 400)
sfx("soft-pop", B.pt(3, 4), 0.45)
s.append(mark)
g = group("3 · Sign-off", S[3], D[3], s); enter_scene(g); scenes.append(g)

# ---------- chrome (persistent, sits on top of scenes) ----------
ch = [line("Footer rule", L, 1240, R, 1240, BORDER, 1.5),
      text("Footer left", "HOUSE OF HU", L, 1284, "mono", 18, ACC, 80),
      text("Footer right", "AVATAR DESIGN", R, 1284, "mono", 18, MUTED, 80, just="right")]
chrome = group("Chrome", 0, B.TOTAL, ch)
for b in S[1:]:
    sfx("air-whoosh", b - 220, 0.22)

write_doc("__NAME__", [chrome] + scenes[::-1], B.TOTAL, BG,
          music_layer=music(MUSIC_SRC0, B.TOTAL, vol=0.45))
