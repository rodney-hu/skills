#!/usr/bin/env bash
# Symlink every skill in this repo into each agent's global skill folder.
# Existing real folders are moved to ~/Desktop/RodneyOS/_Archive/skills-pre-repo/ (never deleted).
# Usage: scripts/link.sh            (Claude Code + Antigravity global skills folder)
#        TARGETS="$HOME/.claude/skills" scripts/link.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ARCHIVE="${ARCHIVE:-$HOME/Desktop/RodneyOS/_Archive/skills-pre-repo}"
TARGETS="${TARGETS:-$HOME/.claude/skills $HOME/.gemini/config/skills}"
for T in $TARGETS; do
  mkdir -p "$T"
  for src in "$ROOT"/skills/*/; do
    name="$(basename "$src")"; dest="$T/$name"
    if [ -L "$dest" ]; then rm "$dest"
    elif [ -e "$dest" ]; then
      tag="$(echo "${T#$HOME/}" | tr -d . | tr / -)"
      mkdir -p "$ARCHIVE/$tag"; mv "$dest" "$ARCHIVE/$tag/$name"
      echo "archived $dest"
    fi
    ln -s "${src%/}" "$dest"
  done
  echo "linked $(ls "$ROOT/skills" | wc -l | tr -d ' ') skills into $T"
done
# Claude Code subagents bundled with a skill (skills/<name>/agents/*.md) go to ~/.claude/agents.
AGENTS="${AGENTS:-$HOME/.claude/agents}"
mkdir -p "$AGENTS"
for src in "$ROOT"/skills/*/agents/*.md; do
  [ -e "$src" ] || continue
  dest="$AGENTS/$(basename "$src")"
  [ -L "$dest" ] && rm "$dest"
  [ -e "$dest" ] && { echo "skipped $dest (real file exists)"; continue; }
  ln -s "$src" "$dest"; echo "linked agent $(basename "$src" .md) into $AGENTS"
done
