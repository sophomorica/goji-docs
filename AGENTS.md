# AGENTS.md — goji-docs

This repository (`sophomorica/goji-docs`) is the **workspace coordination / documentation
repo** for the Goji product. Start with `CLAUDE.md`, `PARENT_APP_PRODUCT.md`, and `TODO.md`.

## Cursor Cloud specific instructions

- **This repo contains no application code.** It is docs-only: `CLAUDE.md`,
  `PARENT_APP_PRODUCT.md`, `TODO.md`, `.gitignore`, and this file. There is nothing to
  install, lint, build, or run here, and no dev server or test suite.
- **The three product subrepos are NOT present in a fresh Cloud VM.** `goji_computer/`,
  `goji_cloud/`, and `goji_learner_app/` are listed in `.gitignore` as separate git repos
  and are intentionally not vendored here. As of this writing they are also not reachable
  on the `sophomorica` GitHub org: `goji_computer` does not exist there, and per `TODO.md`
  `goji_cloud` and `goji_learner_app` are "local-only — no backup." A Cloud Agent cannot
  clone them, so the actual product environment (Flask+SQLite backend, Svelte 5 kiosk
  frontend, sync agent, Supabase cloud, Flutter parent app) cannot be set up from this
  checkout alone.
- **To do product development in Cloud**, the subrepos must first be made available in the
  VM (e.g. pushed to GitHub and cloned into `/workspace/goji_computer`, `/workspace/goji_cloud`,
  `/workspace/goji_learner_app`, or added to the Cloud environment). Once present, use the
  commands already documented in `CLAUDE.md` (e.g. backend `cd goji_computer/backend &&
  python -m pytest tests/`, frontend `cd goji_computer/frontend && npm run test:run`,
  e2e in `frontend/e2e/`) plus each subrepo's own README for run/build steps.
- **Runtimes available in the base image:** Python 3.12, Node 22. Not preinstalled:
  Flutter/Dart (needed by `goji_learner_app`) and the Supabase CLI (needed by `goji_cloud`);
  install these only after the corresponding subrepo is available.
