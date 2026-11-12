#!/usr/bin/env bash
# Zip each skill into dist/<name>.zip for upload at claude.ai > Settings > Capabilities > Skills.
# Includes config.local.md when present (zips stay private; they are git-ignored).
# Usage: scripts/package.sh [skill-name ...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/dist"
names=("$@"); [ ${#names[@]} -gt 0 ] || names=($(ls "$ROOT/skills"))
for n in "${names[@]}"; do
  rm -f "$ROOT/dist/$n.zip"
  (cd "$ROOT/skills" && zip -qr "$ROOT/dist/$n.zip" "$n" -x '*.DS_Store')
  echo "dist/$n.zip"
done
