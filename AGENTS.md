# AGENTS.md — goji-docs

This repository (`sophomorica/goji-docs`) is the **workspace coordination / documentation
repo** for the Goji product. Start with `CLAUDE.md`, `PARENT_APP_PRODUCT.md`, and `TODO.md`.

## Cursor Cloud specific instructions

### Repo layout (multi-repo)
- `goji-docs` (this repo) is **docs only** — no app code lives here.
- The product code is in **three separate GitHub repos**, gitignored here and cloned as
  siblings inside this workspace (see the table in `CLAUDE.md`):
  - `goji_computer/`   → `sophomorica/kodi-computer` (device: Flask+SQLite backend, Svelte 5 kiosk, sync agent)
  - `goji_cloud/`      → `sophomorica/goji-cloud` (Supabase-as-code: migrations, RLS, edge functions)
  - `goji_learner_app/`→ `sophomorica/goji-learner-app` (Flutter parent app `goji_parent`)
- These are **private** repos. A Cloud Agent can only clone them if its git token has
  `Contents: Read` for all three. The most reliable setup is a **multi-repo Cloud
  environment** with all four repos selected so they are checked out automatically. If they
  are missing, clone them into `goji_computer/`, `goji_cloud/`, `goji_learner_app/`.

### One-time environment deps (not in the update script)
The update script only refreshes per-repo dependencies. These system-level installs are
one-time (do them once per fresh image, then they persist via the snapshot):
- `sudo apt-get install -y python3.12-venv` — required to create the backend virtualenv.
- **Flutter SDK** (for `goji_learner_app`): `git clone https://github.com/flutter/flutter.git -b stable --depth 1 ~/flutter`
  then add `~/flutter/bin` to `PATH` (e.g. in `~/.bashrc`). First `flutter --version` downloads the Dart SDK.
- **Supabase CLI** (for `goji_cloud`): use `npx supabase ...` (no global install needed).

### goji_computer — the flagship, fully runnable offline (primary dev target)
- Backend is a Python venv at `goji_computer/backend/.venv`; deps in `backend/requirements.txt`.
  Backend also has a **Node** dep (`backend/package.json`, svelte) that is load-bearing for the
  user-apps live-preview/compile feature — keep it installed.
- Run dev servers (from `goji_computer/`): backend `cd backend && source .venv/bin/activate && python app.py`
  (port 5000), frontend `cd frontend && npm run dev` (port 5173, proxies `/api` → 5000).
  `./dev.sh` starts both but uses `pkill` — prefer starting them separately (e.g. in tmux).
- Tests: backend `cd backend && python -m pytest tests/` (386 pass); frontend
  `cd frontend && npm run test:run`. **Known pre-existing frontend flake:**
  `TypingParatrooper.test.js` throws an unhandled-rejection during happy-dom teardown
  (`cancelAnimationFrame`) → 1 failing file / 436-of-438 tests pass. Not caused by setup.
- **No linter is configured** (no eslint/prettier/ruff/flake8, no `lint` script) — tests are
  the quality gate. Build: `cd frontend && npm run build`.
- DB is a local SQLite `goji.db` created + seeded on first backend start (curriculum, default
  user). Books are NOT seeded (they require `backend/scripts/download_gutenberg.py`), so
  `/api/books` is empty until you download some — this is expected, not a bug.

### goji_learner_app (Flutter parent app)
- `flutter pub get`, `flutter analyze` (passes; 2 info-level deprecation notices), `flutter test`
  (10 pass), `flutter build web` all work. Platform folders are already committed.
- **Running the app live needs the family Supabase cloud:** pass
  `--dart-define=SUPABASE_URL=... --dart-define=SUPABASE_ANON_KEY=...` (see `run_with_cloud.sh`).
  Without those it builds/tests but can't authenticate/pair.
- Prefer `./run_with_cloud.sh -d chrome` (or `flutter run -d web-server --web-port 8080 …`)
  after `goji_learner_app/.env` is written from environment secrets.

### goji_cloud (Supabase-as-code) — optional for the offline device
- Offline-first: the kiosk works fully without the cloud, so the cloud is optional for
  exercising the core device product. The live family project is already deployed
  (`README.md` / `HUMAN_CHECKLIST.md`).
- A local stack (`npx supabase start`) requires **Docker** (not set up here) and downloads
  Postgres/etc images. Only stand it up if you specifically need to test cloud sync.

### School Day integration testing (computer ↔ app ↔ cloud)
Goal: parent **Start school day** → Pi sync pulls plan + enters School Mode → child completes
tasks → status syncs back → parent sees completed.

**Hermetic (no secrets, no network):**
```bash
cd goji_computer/backend && source .venv/bin/activate
python -m sync.mock_family_cloud
python -m pytest tests/integration/test_school_day_e2e_mock.py -v
# or: ./scripts/school-day-smoke.sh
```

**Live loop (needs secrets):** `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `GOJI_CLOUD_URL`
(`https://<ref>.supabase.co/functions/v1`), `GOJI_CLOUD_ANON_KEY` (same anon key), plus
`GOJI_PARENT_TEST_EMAIL` / `GOJI_PARENT_TEST_PASSWORD` for the Flutter AuthGate.
Install writes gitignored `.env` files via `scripts/cloud-agent-install.sh`.

Live smoke steps:
1. Backend `GOJI_SYNC_MODE=live` + frontend on `:5173`; parent app with dart-defines.
2. `POST /api/device/register-cloud` → parent Pair screen / `device-claim` with the 6-char code
   → `POST /api/device/poll-claim`.
3. Parent wizard: draft plan with ≥1 task → **Start school day**.
4. On device: `python -m sync.agent --once` (or wait for the sync interval) → Hub Today shows
   the plan; School Mode locks to allowed apps.
5. Complete tasks on the kiosk (or log `app.session` activity) → another sync cycle → cloud
   `school_sessions.status=completed` / `ended_how=all_tasks_done`.

**Environment bootstrap scripts** (this repo): `scripts/cloud-agent-install.sh`,
`scripts/cloud-agent-start.sh`, `scripts/school-day-smoke.sh`. Prefer a **multi-repo** Cloud
environment that also checks out `kodi-computer`, `goji-learner-app`, and `goji-cloud`.
