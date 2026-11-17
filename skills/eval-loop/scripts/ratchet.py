#!/usr/bin/env python3
"""Compare the last two versions in scores.json. Exit 1 if a check that passed before fails now.

Usage: ratchet.py .eval/scores.json
"""
import json, sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
scores = json.load(open(sys.argv[1]))
if not scores:
    sys.exit("scores.json is empty")
cur = scores[-1]
total = len(cur["passed"]) + len(cur["failed"])
line = f"v{cur['version']}: {len(cur['passed'])}/{total}"
if len(scores) < 2:
    print(line + " (first version, no ratchet floor)")
    sys.exit(0)
prev = scores[-2]
ptotal = len(prev["passed"]) + len(prev["failed"])
delta = len(cur["passed"]) - len(prev["passed"])
print(f"{line}  vs v{prev['version']}: {len(prev['passed'])}/{ptotal}  delta {delta:+d}")
regressed = sorted(set(prev["passed"]) & set(cur["failed"]))
if regressed:
    print("REGRESSION: " + ", ".join(regressed))
    sys.exit(1)
print("no regressions")
