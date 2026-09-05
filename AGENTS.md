# AGENTS.md

Standing brain for Grok Bot, Grok Build, Cursor, and GitHub. Start here. Then read `CLAUDE.md`. This clone is the instruction set. Hub is not here.

**Repo:** Goji docs (`sophomorica/goji-docs`).

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

### goji_cloud (Supabase-as-code) — optional for the offline device
- Offline-first: the kiosk works fully without the cloud, so the cloud is optional for
  exercising the core device product. The live family project is already deployed
  (`README.md` / `HUMAN_CHECKLIST.md`).
- A local stack (`npx supabase start`) requires **Docker** (not set up here) and downloads
  Postgres/etc images. Only stand it up if you specifically need to test cloud sync.
