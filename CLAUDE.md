# Goji — workspace guide (goji_learner/)

Goji is a family learning product by Narrow Road Studios: a self-contained
Raspberry Pi learning computer for kids ("the Goji computer", on-device brand
"Codi" for now), a parent phone app, and a small cloud that connects them.
This folder is the whole product; each subfolder is its own git repo.

| Repo | What it is | Read first |
|------|-----------|------------|
| `goji_computer/` | Everything on the device: Flask+SQLite backend, Svelte 5 kiosk frontend, sync agent, deployment | `goji_computer/CLAUDE.md` (role-based context rules), `docs/ARCHITECTURE.md`, `docs/CLOUD_SYNC_PLAN.md` |
| `goji_cloud/` | Supabase-as-code: migrations, RLS, edge functions | `goji_cloud/README.md`, `SYNC_API.md` (**the sync contract — source of truth**), `HUMAN_CHECKLIST.md` |
| `goji_learner_app/` | Flutter parent app (`goji_parent`): school-day remote + trust dashboard | `PARENT_APP_PRODUCT.md` (product SoT), `goji_learner_app/README.md`, `goji_learner_app/BRANDING.md` |

**Parent-folder coordination:** product decisions that span computer + app + cloud land in this repo (`PARENT_APP_PRODUCT.md`, `TODO.md`, this file). Agents should read those first, then work in the child repos in parallel without drifting.

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
5. **Env vars:** canonical names are `GOJI_*`; `CODEBOX_*` is accepted as legacy
   fallback (`env_goji()` in `goji_computer/backend/sync/cloud.py`). New code
   documents only `GOJI_*`.
6. **Naming:** product = Goji. Internal code identifiers, DB names, and the
   kid-facing "Codi" hub branding are NOT yet renamed — that's a deliberate
   deferred pass. Don't rename opportunistically.
7. Workspace-level TODOs / feature list: `TODO.md` next to this file.
   Repo-specific engineering TODOs stay in `goji_computer/TODO.md`.
8. **Parent app product SoT:** `PARENT_APP_PRODUCT.md`. Do not re-litigate School Mode,
   wizard scope, or dashboard shape in a child repo without updating that file.
9. **One brand across phone and kiosk.** Parent app must use Goji seal/wordmark assets and
   tokens from `goji_computer/PRODUCT_DESIGN.md` + `docs/BRAND.md` (canonical SVGs in
   `goji_computer/frontend/src/assets/brand/`; app copies in `goji_learner_app/assets/brand/`).
   No parallel palette or logo treatment.

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
