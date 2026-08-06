# Goji — workspace guide (goji_learner/)

Goji is a family learning product by Narrow Road Studios: a self-contained
Raspberry Pi learning computer for kids ("the Goji computer", on-device brand
"Codi" for now), a parent phone app, and a small cloud that connects them.

**This repo (`goji-docs`) is docs/coordination only** — product SoT markdown for
agents and humans. The three product codebases are separate GitHub remotes.
Clone them as siblings under a local `goji_learner/` folder (or use a Cursor
multi-repo Cloud Agent environment with all four selected).

| Local path | GitHub remote | What it is | Read first |
|------------|---------------|------------|------------|
| *(this repo)* | [`sophomorica/goji-docs`](https://github.com/sophomorica/goji-docs) | Product SoT + agent entry (`PARENT_APP_PRODUCT.md`, `TODO.md`, this file) | this file, `PARENT_APP_PRODUCT.md`, `TODO.md` |
| `goji_computer/` | [`sophomorica/kodi-computer`](https://github.com/sophomorica/kodi-computer) | Device: Flask+SQLite backend, Svelte 5 kiosk, sync agent, deployment | `goji_computer/CLAUDE.md`, `docs/ARCHITECTURE.md`, `docs/CLOUD_SYNC_PLAN.md` |
| `goji_cloud/` | [`sophomorica/goji-cloud`](https://github.com/sophomorica/goji-cloud) | Supabase-as-code: migrations, RLS, edge functions | `README.md`, **`SYNC_API.md`** (wire contract SoT), `HUMAN_CHECKLIST.md` |
| `goji_learner_app/` | [`sophomorica/goji-learner-app`](https://github.com/sophomorica/goji-learner-app) | Flutter parent app (`goji_parent`): school-day remote + trust dashboard | `PARENT_APP_PRODUCT.md` (product SoT), `README.md`, `BRANDING.md` |

```bash
# Typical local layout after cloning all four:
mkdir -p goji_learner && cd goji_learner
git clone git@github.com:sophomorica/goji-docs.git .
git clone git@github.com:sophomorica/kodi-computer.git goji_computer
git clone git@github.com:sophomorica/goji-cloud.git goji_cloud
git clone git@github.com:sophomorica/goji-learner-app.git goji_learner_app
```

**Parent-folder coordination:** product decisions that span computer + app + cloud land here (`PARENT_APP_PRODUCT.md`, `TODO.md`, this file). Agents should read those first, then work in the child repos in parallel without drifting.

**Curriculum / pedagogy planning (K–12, teaching animations, quizzes, tools map):**
[`curriculum/README.md`](./curriculum/README.md) + **[`curriculum/VISION.md`](./curriculum/VISION.md)** — start here for Goji computer curriculum, lesson plans, objectives, Claude Design animations, Virginia skills coverage, Gutenberg/Kiwix reading, or parent “where does my child stand.”  
**Paradigm:** three pillars — **reading** (access), **writing** (think), **math** (think straight); teach → practice → comprehension; child’s pace; vehicle+data on device; parent metrics + school day; optional Grok co-pilot cloud-side.  
Curriculum lead may be a non-engineering family member — keep answers in this folder’s language; don’t invent structure inside `goji_computer/` seed without updating `curriculum/` first.

## Cross-repo rules (apply to all work here)

1. **The sync contract lives in `goji_cloud/SYNC_API.md`.** Any change to what
   crosses the wire (tables, endpoints, payload shapes, signing) is edited THERE
   first, then implemented on both sides. Never let the Pi and cloud drift.
2. **Offline-first is the product.** Every kid-facing feature must work with no
   cloud. Sync is opportunistic; the Pi talks to exactly ONE server (the family
   Supabase project) and NEVER calls third-party APIs. AI generation happens
   cloud/parent-side only.
3. **Nothing cloud- or app-related goes back into `goji_computer/`** — that repo
   is the flashable SD image source. `cloud/` or `parent-app/` reappearing at
   its root is a regression (it happened once; see git history).
4. **No secrets in any repo.** Supabase keys live in local `.env` files only.
   The flashed image contains no secrets; device identity is generated on first
   boot (see pairing design in `docs/CLOUD_SYNC_PLAN.md` §3).
5. **Env vars:** `GOJI_*` only (`GOJI_CLOUD_URL`, `GOJI_SYNC_MODE`, …). No
   `CODEBOX_*` fallback — see `goji_computer/NAMING.md` and `env_goji()` in
   `goji_computer/backend/sync/cloud.py`.
6. **Naming:** product = Goji. Kid-facing hub uses the Goji wordmark/seal (not
   "Codi" as the primary brand mark). Internal DB/module identifiers may still
   carry legacy names until a deliberate rename pass — don't rename
   opportunistically beyond what `NAMING.md` already locked.
7. Workspace-level TODOs / feature list: `TODO.md` next to this file.
   Repo-specific engineering TODOs stay in `goji_computer/TODO.md`.
8. **Parent app product SoT:** `PARENT_APP_PRODUCT.md`. Do not re-litigate School Mode,
   wizard scope, or dashboard shape in a child repo without updating that file.
9. **One brand across phone and kiosk.** Parent app must use Goji seal/wordmark assets and
   tokens from `goji_computer/PRODUCT_DESIGN.md` + `docs/BRAND.md` (canonical SVGs in
   `goji_computer/frontend/src/assets/brand/`; app copies in `goji_learner_app/assets/brand/`).
   No parallel palette or logo treatment.
10. **Owned curriculum planning** lives in `curriculum/` (objectives, lesson plans, animation
    registry, quiz strategy, tools inventory). Maximize existing Goji apps first; track gaps
    in `curriculum/TOOLS.md`. Large animation binaries stay out of git — see `curriculum/ANIMATIONS.md`.

## Working here (for Claude sessions)

- goji_computer follows Narrow Road standards via `../narrow-road-hq/standards/`
  (operating manual, code standards, `/review` PASS = done). The other two repos
  follow the same spirit: tests green, no orphaned code, escalate rather than
  invent architecture, label guesses `ASSUMED:`.
- Tests: `cd goji_computer/backend && python -m pytest tests/` ·
  `cd goji_computer/frontend && npm run test:run` (one known pre-existing
  MyApps.test.js flake) · e2e in `frontend/e2e/` (import `test` from
  `./fixtures`, never `@playwright/test` directly).
- Flutter app has no platform folders until `flutter create` is run locally
  (Dart sources only in git).
- Live cloud state: see `goji_cloud/HUMAN_CHECKLIST.md` for what has to be done
  by a human in the Supabase dashboard vs what is code.
