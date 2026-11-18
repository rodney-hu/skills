# Deploy: one static site → one link

Every recipe renders a static `site/` (HTML, CSS, JS, assets, and a `vercel.json` noindex header written by `render.mjs`). Deploy it the same way every time.

- **Team:** `{{SPEC_DEMO_VERCEL_TEAM}}`. Never Rodney's personal account. Find the team ID with the Vercel MCP `list_teams`.
- **Naming (fixed, every demo):** project `<company-slug>-demo`, link `https://<company-slug>-demo.vercel.app` (e.g. `vista-ai-demo.vercel.app`). One project per company, never per recipe. `<company-slug>` is the demo's folder name in spec-demos.
- **Before deploying,** `list_projects` with `search: "<company-slug>-demo"`. If it exists, deploy into it (a new recipe for the same company replaces the old page; say so on the card). If the `.vercel.app` name is taken outside the team, stop and ask Rodney; never accept a suffixed URL.
- **Target:** production, so the short URL is assigned.

## With the Vercel MCP (default, works in cloud sessions)
1. Build the `files` array with a script, never by retyping file contents (a retyped payload drifts from the rendered files):
   `python3 -c "import json,os,base64;print(json.dumps([{'file':os.path.relpath(p,'site'),**({'data':open(p,encoding='utf-8').read(),'encoding':'utf-8'} if p.endswith(('.html','.css','.js','.json','.svg','.txt')) else {'data':base64.b64encode(open(p,'rb').read()).decode(),'encoding':'base64'})} for d,_,fs in os.walk('site') for p in [os.path.join(d,f) for f in fs]]))"`
   Collect every file under `site/`. Text files go in as `encoding: "utf-8"`, binaries (png, jpg, avif, webp, woff2, ico, and svg if unsure) as `base64`. Paths are relative to `site/` (e.g. `index.html`, `assets/logo.svg`).
2. `create_deployment` with `teamId`, `requestBody: { name, project: name, target: "production", files, projectSettings: { framework: null, buildCommand: null, outputDirectory: null } }`, and `skipAutoDetectionConfirmation: "1"`.
3. Poll `get_deployment` until `readyState` is `READY`. On `ERROR`, read the build logs, fix, redeploy.
4. Check the live URL returns 200 with no login (Firecrawl scrape with `maxAge: 0` works when the sandbox network blocks `*.vercel.app`). If Vercel Deployment Protection blocks it, turn protection off for this project only (ask Rodney if the MCP cannot).

## With the CLI (on a machine that has it)
`cd site && vercel deploy --prod --yes --scope <team-slug> --name <project>`

## After deploy
- Write the URL to `demo.json` (`live_url`) and to `asset-card.md`.
- Screenshot the live URL, not the local file.
- Editing later: change `demo.json`, re-render, deploy again to `<company-slug>-demo`. The URL stays the same.
- Deploying is not sending. The page is noindex and unlisted. Sharing it with the prospect needs Rodney's yes.
