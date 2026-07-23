# AGENTS.md — goji-docs

This repository (`sophomorica/goji-docs`) is the **workspace coordination / documentation
repo** for the Goji product. Start with `CLAUDE.md`, `PARENT_APP_PRODUCT.md`, and `TODO.md`.

## Cursor Cloud specific instructions

- **This repo contains no application code.** It is docs-only: `CLAUDE.md`,
  `PARENT_APP_PRODUCT.md`, `TODO.md`, `.gitignore`, and this file. There is nothing to
  install, lint, build, or run here, and no dev server or test suite.
- **The three product subrepos are NOT present in a fresh Cloud VM.** `goji_computer/`,
  `goji_cloud/`, and `goji_learner_app/` are listed in `.gitignore` and live in separate
  GitHub repos (see the table in `CLAUDE.md`): `goji_computer/` → `sophomorica/kodi-computer`,
  `goji_cloud/` → `sophomorica/goji-cloud`, `goji_learner_app/` → `sophomorica/goji-learner-app`.
  A Cloud Agent cannot set up the actual product environment (Flask+SQLite backend, Svelte 5
  kiosk frontend, sync agent, Supabase cloud, Flutter parent app) until those repos are
  cloned into this workspace as siblings.
- **The Cloud Agent GitHub token is scoped to `goji-docs` only.** Cloning the three product
  repos fails with "repository not found" because the Cursor GitHub App / Cloud Agent access
  does not include them (they may be private or not yet created). To do product development in
  Cloud, either (a) grant the Cursor Cloud Agent access to those repos and use a multi-repo
  Cloud environment with all four selected, or (b) push them so they are reachable and clone
  into `/workspace/goji_computer`, `/workspace/goji_cloud`, `/workspace/goji_learner_app`.
- Once the subrepos are present, use the commands documented in `CLAUDE.md` (e.g. backend
  `cd goji_computer/backend && python -m pytest tests/`, frontend
  `cd goji_computer/frontend && npm run test:run`, e2e in `frontend/e2e/`) plus each subrepo's
  own README for run/build steps.
- **Runtimes available in the base image:** Python 3.12, Node 22. Not preinstalled:
  Flutter/Dart (needed by `goji_learner_app`) and the Supabase CLI (needed by `goji_cloud`);
  install these only after the corresponding subrepo is available.
