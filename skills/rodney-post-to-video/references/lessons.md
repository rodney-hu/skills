# Lessons (append after every video; read before step 4)

- avatar-design: Fire 500 (`FIRE`) for fills only; use Fire 400 (`FIRE4`) for text on dark.
- Fill the lower third of each scene; a content block that stops at y≈940 leaves the frame feeling empty (stat cards grew to 400 px tall).
- macOS: `sed -i` needs `-i ''`. ffmpeg/ffprobe come from Homebrew (`brew install ffmpeg`); without them `beats.py`, `music()` auto-length and the LUFS readout fail (fallback: pass `intrinsic_ms` to `music()`, length via `afinfo`).
- Cinzel ships as a variable font; `Cinzel-800.ttf` is a static instance made with `fonttools varLib.instancer Cinzel.ttf wght=800` (pass no `--update-name-table`; it errors on this font).
- `tsrct` is a separate ~90 MB GitHub download (pinned in tesseract-motion/references/cli-version.txt); ask before downloading.
- First pass is usually clean; check filmstrips at scene midpoints, not just evenly spaced frames.
