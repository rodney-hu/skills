#!/usr/bin/env python3
"""List files changed since the loop started that fall outside the contract's scope.

Usage:
  scope_check.py --init            record the baseline (run once at loop start)
  scope_check.py .eval/contract.md  print out-of-scope files; exit 1 if any
"""
import fnmatch, pathlib, re, subprocess, sys

BASE = pathlib.Path(".eval/rounds/baseline.txt")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def changed():
    files = set()
    for line in git("status", "--porcelain", "--untracked-files=all").splitlines():
        path = line[3:].split(" -> ")[-1].strip('"')
        if not path.startswith(".eval/"):
            files.add(path)
    return files


def scope_globs(contract):
    text = pathlib.Path(contract).read_text()
    m = re.search(r"^## Files in scope\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        sys.exit("contract has no '## Files in scope' section")
    globs = [l.strip()[2:].strip().strip("`") for l in m.group(1).splitlines() if l.strip().startswith("- ")]
    if not globs:
        sys.exit("'## Files in scope' lists no globs")
    return globs


def in_scope(path, globs):
    for g in globs:
        if fnmatch.fnmatch(path, g) or fnmatch.fnmatch(path, g.replace("**/", "")):
            return True
        if g.endswith("/**") and path.startswith(g[:-3] + "/"):
            return True
    return False


def main():
    if sys.argv[1:] == ["--init"]:
        BASE.parent.mkdir(parents=True, exist_ok=True)
        head = git("rev-parse", "HEAD").strip()
        BASE.write_text(head + "\n" + "\n".join(sorted(changed())) + "\n")
        print(f"baseline {head[:7]}, {len(changed())} pre-existing changed files ignored")
        return
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    globs = scope_globs(sys.argv[1])
    lines = BASE.read_text().splitlines() if BASE.exists() else []
    head, pre = (lines[0], set(lines[1:])) if lines else (None, set())
    files = changed() - pre
    if head:
        files |= {f for f in git("diff", "--name-only", head, "HEAD").splitlines() if not f.startswith(".eval/")}
    out = sorted(f for f in files if not in_scope(f, globs))
    for f in out:
        print(f"OUT OF SCOPE: {f}")
    if not out:
        print(f"scope ok: {len(files)} changed files, all in scope")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
