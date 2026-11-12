/**
 * TAILWIND PRESET TEMPLATE
 *
 * ⚠️ READ THIS BEFORE COPYING THE content BLOCK ANYWHERE ⚠️
 *
 * Tailwind does NOT merge a preset's `content` array with a consumer's own
 * `content` array. A consumer's `content` REPLACES the preset's outright —
 * verify this yourself with `resolveConfig` before trusting otherwise; it
 * is the single most counterintuitive fact in this whole template, and the
 * "obvious" fix (just declare content here and assume it combines) does
 * not work. See ../references/bug-catalog.md #10 and #11.
 *
 * The correct pattern, which MUST be documented for every consumer:
 *
 *   // consumer's tailwind.config.js
 *   const preset = require("your-design-system/tailwind");
 *   module.exports = {
 *     presets: [preset],
 *     content: [...preset.content, "./src/**\/*.{ts,tsx}"],  // <- spread required
 *   };
 *
 * Skip the spread and every utility class used ONLY inside this package's
 * own components is never generated downstream — silently. No error, no
 * warning, just missing styles in the consumer's build.
 */

const path = require("node:path");

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class", // or "media" — pick one, don't support both silently

  // This package's OWN component files only. Absolute paths (via
  // __dirname) so they resolve correctly wherever the package ends up
  // installed (node_modules, a workspace, a file: link).
  content: [
    path.join(__dirname, "..", "components", "**", "*.{js,cjs,mjs,jsx,ts,tsx}"),
  ],

  theme: {
    extend: {
      colors: {
        // Every color that needs opacity-modifier support (bg-x/40) MUST
        // read the raw channel triplet with <alpha-value>, never the
        // derived hex var — see tokens.template.css and bug-catalog.md #1.
        "{{surface-page}}": "rgb(var(--{{SURFACE_PAGE}}-rgb) / <alpha-value>)",
        "{{surface-raised}}": "rgb(var(--{{SURFACE_RAISED}}-rgb) / <alpha-value>)",
        "{{category-1}}": "rgb(var(--{{CATEGORY_1}}-rgb) / <alpha-value>)",
        "{{category-1}}-text": "rgb(var(--{{CATEGORY_1}}-text-rgb) / <alpha-value>)",

        // Fixed-alpha tokens (soft fills, glows) stay as authored tokens —
        // they are NOT meant to be alpha-composable further.
        "{{category-1}}-soft": "var(--{{CATEGORY_1}}-soft)",
      },

      borderColor: {
        line: "var(--line)",
        "line-strong": "var(--line-strong)",
      },

      fontSize: {
        // Override Tailwind's own scale rather than adding alongside it,
        // so existing call sites (text-sm, text-lg, ...) pick up your
        // scale with zero component changes.
        xs: ["var(--text-xs)", { lineHeight: "var(--leading-normal)" }],
        sm: ["var(--text-sm)", { lineHeight: "var(--leading-relaxed)" }],
        base: ["var(--text-base)", { lineHeight: "var(--leading-relaxed)" }],
      },

      borderRadius: {
        DEFAULT: "var(--radius-sm)",
        md: "var(--radius-md)",
        lg: "var(--radius-lg)",
      },

      transitionTimingFunction: {
        DEFAULT: "var(--ease-standard)",
      },

      transitionDuration: {
        fast: "var(--duration-fast)",
        DEFAULT: "var(--duration-default)",
        slow: "var(--duration-slow)",
      },
    },
  },

  plugins: [],
};
