#!/usr/bin/env bash
# One-time import: copy Rodney's own skills into skills/.
# Sources: claude.ai account cache (creatorType=user) + ~/.claude/skills + 00 Foundations.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/skills"
if [ -n "$(ls -A "$DEST" 2>/dev/null)" ] && [ "${FORCE:-}" != 1 ]; then
  echo "skills/ is not empty. This repo is now the master copy; re-importing overwrites edits and the public scrub. Set FORCE=1 to do it anyway." >&2; exit 1
fi
CACHE_BASE="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"
MANIFEST="$(grep -l '"creatorType": *"user"' "$CACHE_BASE"/*/*/manifest.json 2>/dev/null | head -1 || true)"
[ -n "$MANIFEST" ] || MANIFEST="$(ls -t "$CACHE_BASE"/*/*/manifest.json | head -1)"
CACHE="$(dirname "$MANIFEST")/skills"

CLAUDE_AI=$(python3 -I -c '
import json,sys
d=json.load(open(sys.argv[1]))
print("\n".join(sorted(s["name"] for s in d["skills"] if s.get("creatorType")=="user")))' "$MANIFEST")
LOCAL="close-loop design-system-builder gtm-portfolio rodney-post-to-video spec-demo triage-inbox"

copy() { # src name
  rm -rf "$DEST/$2"; mkdir -p "$DEST/$2"
  rsync -a --exclude '.DS_Store' --exclude 'node_modules' "$1/" "$DEST/$2/"
  echo "  + $2"
}
echo "claude.ai account skills:"
for s in $CLAUDE_AI; do
  [ "$s" = rodney-writing-style ] && continue
  copy "$CACHE/$s" "$s"
done
echo "Foundations:"; copy "$HOME/Desktop/RodneyOS/00 Foundations/rodney-writing-style" rodney-writing-style
echo "Claude Code local:"
for s in $LOCAL; do copy "$(cd "$HOME/.claude/skills/$s" && pwd -P)" "$s"; done
echo "Total: $(ls "$DEST" | wc -l | tr -d ' ') skills"
