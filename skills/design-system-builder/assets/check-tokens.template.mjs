#!/usr/bin/env node
/**
 * DESIGN SYSTEM GUARD — TEMPLATE
 *
 * Zero dependencies, on purpose — this should never be blocked by an
 * install failure. Run with `node check-tokens.mjs` or wire to `npm run
 * check`.
 *
 * Every check below exists because skipping it produced a real bug once.
 * See ../references/bug-catalog.md for the specific incident behind each
 * numbered section. Read that file before deleting a check you think is
 * unnecessary — it probably isn't.
 *
 * TODO markers show where a new system's specific names/paths need to be
 * filled in. Everything else is meant to run as-is.
 *
 * IMPORTANT: negative-test every check before trusting it. Deliberately
 * break each rule in a scratch copy and confirm this script actually fails
 * on it. A check that has never been observed to fail is unverified.
 */

import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join, dirname, extname } from "node:path";
import { fileURLToPath } from "node:url";

// ---------------------------------------------------------------------------
// CONFIG — TODO: fill these in for your system
// ---------------------------------------------------------------------------

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

const CONFIG = {
  tokensCssPath: "tokens/tokens.css", // TODO: path to your token source
  presetPath: "tokens/tailwind-preset.cjs", // TODO: path to your Tailwind preset, or null
  motionJsPath: "motion/motion.ts", // TODO: path to JS motion constants, or null
  componentDirs: ["components"], // TODO: directories to scan for hand-typed literals

  // Every surface a text-safe token can render on. TODO: fill in your real
  // elevation tiers. A tint that clears AA on one tier can fail on another —
  // check ALL of them, not just the one it was designed for.
  contrastSurfaces: [
    // ["--surface-page-rgb", "page"],
    // ["--surface-raised-rgb", "panel"],
  ],
  contrastMinimum: 4.5, // WCAG AA for normal text. Use 7 if you support small/thin text.

  // Numeric alpha caps for glow/gradient-style tokens. TODO: fill in the
  // real token names and their documented ceilings. Keys are matched as
  // `--{key}:` in the token source.
  alphaCaps: {
    // "aura-fire": 0.06,
    // "halo-fire": 0.3,
  },
};

const read = (relPath) => readFileSync(join(ROOT, relPath), "utf8");
const exists = (relPath) => existsSync(join(ROOT, relPath));

const failures = [];
const fail = (check, msg) => failures.push(`${check}: ${msg}`);

function stripComments(src) {
  return src.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
}

// ---------------------------------------------------------------------------
// 1. Every token a preset/component references actually exists
//    (bug-catalog.md #1, #5 — a class referencing a nonexistent or
//    non-composable token resolves to nothing, silently)
// ---------------------------------------------------------------------------
if (exists(CONFIG.tokensCssPath) && CONFIG.presetPath && exists(CONFIG.presetPath)) {
  const tokensCss = read(CONFIG.tokensCssPath);
  const preset = read(CONFIG.presetPath);

  const defined = new Set(
    [...tokensCss.matchAll(/^\s*(--[\w-]+):/gm)].map((m) => m[1]),
  );
  const used = new Set(
    [...preset.matchAll(/var\((--[\w-]+)\)/g)].map((m) => m[1]),
  );
  for (const v of used) {
    if (!defined.has(v)) {
      fail("token-existence", `preset reads ${v}, which is not defined in ${CONFIG.tokensCssPath}`);
    }
  }

  // Any color exposed with <alpha-value> must read a bare RGB triplet, not
  // a derived hex var — that is the exact bug in bug-catalog.md #1.
  for (const [, name, value] of preset.matchAll(
    /"?([\w-]+)"?:\s*"([^"]*<alpha-value>[^"]*)"/g,
  )) {
    if (!/rgb\(var\(--[\w-]+-rgb\)\s*\/\s*<alpha-value>\)/.test(value)) {
      fail(
        "token-existence",
        `color "${name}" uses <alpha-value> but does not read a --*-rgb triplet: ${value}`,
      );
    }
  }
} else {
  fail("config", "tokensCssPath / presetPath not found — fill in CONFIG at the top of this script");
}

// ---------------------------------------------------------------------------
// 2. No hand-typed hex or literal opacity color in component source
//    (bug-catalog.md #5 — a token existed and nothing enforced using it)
// ---------------------------------------------------------------------------
{
  const sources = [];
  for (const dir of CONFIG.componentDirs) {
    if (!exists(dir)) continue;
    for (const f of readdirSync(join(ROOT, dir))) {
      if ([".tsx", ".ts", ".jsx", ".js"].includes(extname(f))) {
        sources.push(`${dir}/${f}`);
      }
    }
  }

  for (const file of sources) {
    const src = stripComments(read(file));

    for (const m of src.matchAll(/#[0-9a-fA-F]{3,8}\b/g)) {
      fail(file, `hand-typed hex "${m[0]}" — add it to your token source instead`);
    }

    // TODO: adjust this list to your own "escape hatch" literals, e.g.
    // "white" or "black" used directly instead of a neutral token.
    for (const m of src.matchAll(/\b(?:bg|border|text|ring)-(?:white|black)\/[\w[\].]+/g)) {
      fail(file, `hardcoded "${m[0]}" — use a neutral token instead`);
    }
  }
}

// ---------------------------------------------------------------------------
// 3. Contrast — every -text token against every configured surface
//    (bug-catalog.md #2, #3 — contrast eyeballed instead of computed,
//    and only checked against one surface instead of all of them)
// ---------------------------------------------------------------------------
if (exists(CONFIG.tokensCssPath) && CONFIG.contrastSurfaces.length > 0) {
  const tokensCss = read(CONFIG.tokensCssPath);

  const srgb = (c) => {
    const n = c / 255;
    return n <= 0.03928 ? n / 12.92 : Math.pow((n + 0.055) / 1.055, 2.4);
  };
  const lum = ([r, g, b]) => 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b);
  const ratio = (a, b) => {
    const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x);
    return (hi + 0.05) / (lo + 0.05);
  };

  const triplet = (varName) => {
    const m = tokensCss.match(new RegExp(`${varName}:\\s*(\\d+)\\s+(\\d+)\\s+(\\d+)`));
    return m ? [+m[1], +m[2], +m[3]] : null;
  };

  const surfaces = CONFIG.contrastSurfaces
    .map(([varName, label]) => [label, triplet(varName)])
    .filter(([, rgb]) => rgb);

  for (const m of tokensCss.matchAll(/--([\w-]+)-text-rgb:\s*(\d+)\s+(\d+)\s+(\d+)/g)) {
    const fg = [+m[2], +m[3], +m[4]];
    for (const [label, bg] of surfaces) {
      const r = ratio(fg, bg);
      if (r < CONFIG.contrastMinimum) {
        fail(
          "contrast",
          `--${m[1]}-text is ${r.toFixed(2)}:1 on ${label} — below the ${CONFIG.contrastMinimum}:1 floor`,
        );
      }
    }
  }
}

// ---------------------------------------------------------------------------
// 4. Alpha caps for glow/gradient tokens, enforced as numbers
//    (bug-catalog.md — caps that live only in a comment get exceeded)
// ---------------------------------------------------------------------------
if (exists(CONFIG.tokensCssPath) && Object.keys(CONFIG.alphaCaps).length > 0) {
  const tokensCss = read(CONFIG.tokensCssPath);
  for (const [name, cap] of Object.entries(CONFIG.alphaCaps)) {
    const m = tokensCss.match(
      new RegExp(`--${name}:\\s*rgb\\(\\s*var\\(--[\\w-]+\\)\\s*/\\s*([\\d.]+)`),
    );
    if (!m) {
      fail("alpha-cap", `token --${name} referenced in CONFIG.alphaCaps but not found in ${CONFIG.tokensCssPath}`);
    } else if (parseFloat(m[1]) > cap) {
      fail("alpha-cap", `--${name} is ${m[1]}, above its documented cap of ${cap}`);
    }
  }
}

// ---------------------------------------------------------------------------
// 5. Motion JS constants must mirror the CSS tokens
//    (bug-catalog.md #4 — a CSS variable is invisible to JS; hand-typed
//    bezier curves and durations drift immediately and invisibly)
// ---------------------------------------------------------------------------
if (CONFIG.motionJsPath && exists(CONFIG.motionJsPath) && exists(CONFIG.tokensCssPath)) {
  const tokensCss = read(CONFIG.tokensCssPath);
  const motionJs = read(CONFIG.motionJsPath);

  // TODO: adjust these variable/export names to match your own token and
  // constant naming.
  const cssEase = tokensCss.match(/--ease-\w+:\s*cubic-bezier\(([^)]+)\)/);
  const jsEase = motionJs.match(/export const ease\w* = \[([^\]]+)\]/);

  if (cssEase && jsEase) {
    const norm = (s) => s.split(",").map((n) => parseFloat(n.trim()));
    const a = norm(cssEase[1]);
    const b = norm(jsEase[1]);
    if (a.length !== b.length || a.some((n, i) => n !== b[i])) {
      fail("motion", `JS easing constant [${b}] does not match CSS --ease [${a}]`);
    }
  } else if (!cssEase) {
    fail("motion", "no --ease-* cubic-bezier found in token source");
  } else if (!jsEase) {
    fail("motion", `no matching easing export found in ${CONFIG.motionJsPath}`);
  }
}

// ---------------------------------------------------------------------------
// 6. Structural rules — TODO: fill in your system's own hard-to-violate-
//    accidentally rules. Two examples, adapt or replace:
// ---------------------------------------------------------------------------
{
  for (const dir of CONFIG.componentDirs) {
    if (!exists(dir)) continue;
    for (const f of readdirSync(join(ROOT, dir))) {
      if (![".tsx", ".jsx"].includes(extname(f))) continue;
      const src = stripComments(read(`${dir}/${f}`));

      // Example: a background-tinting utility must never land on a
      // page-level element — that is how full-page ambient glow returns.
      // TODO: replace "aura" / "halo" with your own glow-namespace names.
      for (const m of src.matchAll(
        /<(section|main|body)\b[^>]*className={?["'`][^"'`]*\baura\b/g,
      )) {
        fail(`${dir}/${f}`, `background-tint utility applied to <${m[1]}> — should be object-scoped, not page-scoped`);
      }

      // Example: a variant prop whose base component hardcodes the thing
      // it's meant to override (bug-catalog.md #6) — hard to grep for in
      // general; the reliable check is a code-review habit ("is this
      // variant a lookup table, or a base class plus an expected
      // override at equal specificity?"), not a regex. Leaving this here
      // as a reminder rather than a working check.
    }
  }
}

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------
if (failures.length) {
  console.error(`\n✕ Design system guard — ${failures.length} problem(s):\n`);
  for (const f of failures) console.error(`  • ${f}`);
  console.error("");
  process.exit(1);
}

console.log("✓ Design system guard passed");
