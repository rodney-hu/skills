# Rodney Hu: Agent Skills

25 skills I built to run GTM, copy and operations work with AI agents. Each one is a folder with a `SKILL.md` in the open [Agent Skills](https://agentskills.io) format, so it runs in Claude (Code, chat, Cowork), Google Antigravity, Gemini CLI, Cursor and any agent that reads `SKILL.md`.

This repo is the master copy. Every tool I use links to or installs from it.

## Install

| Where | How |
|---|---|
| Any agent, any machine | `npx skills add rodney-hu/skills` (pick the skills and agents you want) |
| Claude Code / Antigravity on my Mac | `scripts/link.sh` symlinks every skill into `~/.claude/skills` and `~/.gemini/config/skills` (Antigravity's global folder). Edit once, every tool sees it |
| claude.ai (chat, Cowork) | `scripts/package.sh <name>` builds `dist/<name>.zip`; upload it at Settings → Capabilities → Skills |
| A server (Grokbot, cron agents) | `git clone https://github.com/rodney-hu/skills` and point the agent at `skills/`. Keep it current with a `git pull` cron |

Some skills read workspace IDs (Notion pages, databases) from a `config.local.md` in their folder. Copy `config.example.md` to `config.local.md` and fill it in. It is git-ignored.

## Catalog

### Copy and funnels
| Skill | What it does |
|---|---|
| [rodney-writing-style](skills/rodney-writing-style) | Writes persuasive posts, emails and funnel copy in my voice, with a quality check per format |
| [copy-eec](skills/copy-eec) | Builds Educational Email Courses, sequences and funnel page copy from topic + audience + outcome |
| [hypnotic-copy](skills/hypnotic-copy) | Layers presuppositions, pacing/leading and open loops into posts, pages and emails |
| [landing-eec](skills/landing-eec) | Generates a brand-matched offer landing page (challenge, course, sprint, workshop) as a React artifact |
| [funnel-architect](skills/funnel-architect) | Builds a working funnel prototype for any goal as a React or HTML artifact |
| [offer-build](skills/offer-build) | Designs a productized offer: script, package, pricing, anchoring and tiers |

### Prospecting and outreach
| Skill | What it does |
|---|---|
| [value-first-outreach](skills/value-first-outreach) | Turns a target company into a signal, an asset spec and ready-to-send DM, email and Loom script |
| [cold-email-writer](skills/cold-email-writer) | Writes cold emails to a deliverability-aware SOP |
| [spec-demo](skills/spec-demo) | Builds a free brand-matched landing page and thank-you page for a prospect from one URL |
| [prospect-intelligence](skills/prospect-intelligence) | Turns a YouTube channel or company URL into an outreach brief and a free consulting brief |
| [brand-intelligence](skills/brand-intelligence) | Extracts a full brand profile from a website, YouTube channel or LinkedIn page |
| [audience-intelligence](skills/audience-intelligence) | Builds an audience report: ICA, fears, desires, activation moments, language |
| [youtube-channel-scout](skills/youtube-channel-scout) | Finds YouTube channels with a real audience and no funnel to capture it |
| [qualify](skills/qualify) | Pipeline step 2: pass/fail qualifies new leads in a Notion CRM with a written trigger |
| [research-prospects](skills/research-prospects) | Pipeline step 3: writes company and audience intelligence back to each qualified lead |

### GTM engineering
| Skill | What it does |
|---|---|
| [gtm-portfolio](skills/gtm-portfolio) | Coaches a portfolio project through six gates, from intake to packaged case study |
| [clay-challenge](skills/clay-challenge) | Generates Clay Cup-style practice briefs and timed data-race drills |
| [n8n-builder](skills/n8n-builder) | Plans, builds, debugs and reviews n8n workflows |
| [qa-auditor](skills/qa-auditor) | Audits workflows, apps and pipelines for reliability, data integrity and error handling |

### Build and design
| Skill | What it does |
|---|---|
| [design-system-builder](skills/design-system-builder) | Builds a design system from scratch or audits and hardens an existing one |
| [rodney-post-to-video](skills/rodney-post-to-video) | Turns a post into a beat-synced 1080×1350 motion-graphic video (needs Graphed's `tesseract-motion`) |
| [idea-to-blueprint](skills/idea-to-blueprint) | Turns a raw idea into an MVP-first project blueprint |

### Operating system
| Skill | What it does |
|---|---|
| [close-loop](skills/close-loop) | Ends a build session by logging shipped work, decisions and checklist state to Notion |
| [triage-inbox](skills/triage-inbox) | Classifies every Inbox capture in a Notion vault and proposes one destination each |
| [asymmetric-execution](skills/asymmetric-execution) | Accountability mentor: vision → milestones → time-blocked days, with Notion as task state |

## Repo layout

```
skills/<name>/SKILL.md     the skill (plus references/, scripts/, assets/ as needed)
scripts/link.sh            symlink skills into local agent folders
scripts/package.sh         zip skills for claude.ai upload
scripts/import.sh          one-time import used to build this repo
```

## License

MIT. See [LICENSE](LICENSE). Third-party credits in [NOTICE.md](NOTICE.md).
