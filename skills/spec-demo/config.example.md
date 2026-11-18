# Config for spec-demo

Copy this file to `config.local.md` (git-ignored) and fill in your values. A key may list one value per machine; the skill uses the one whose path exists.

- `SPEC_DEMO_OUTPUT_DIR`: <folder where each demo is saved, one subfolder per prospect; ideally a git repo shared by your agents>
  - e.g. Cloud: /home/user/spec-demos
- `SPEC_DEMO_KIT_DIR`: <folder holding the spec-demo kit (render.mjs, layouts, recipes/)>
  - e.g. Cloud: /home/user/foundations/templates/spec-demo/
- `SPEC_DEMO_REFERENCE`: <folder name of the finished reference demo inside the kit's examples/>
- `SPEC_DEMO_VERCEL_TEAM`: <Vercel team every demo deploys to>
