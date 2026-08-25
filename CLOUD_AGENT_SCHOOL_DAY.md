# Cloud Agent — school-day playthrough

How to run the **Goji computer kiosk** and **parent app** in a Cursor Cloud
environment and walk a school day through the live family cloud.

Product SoT: `PARENT_APP_PRODUCT.md`. Wire SoT: `goji_cloud/SYNC_API.md`.

## Safety

- Mint a **new anonymous parent session** for Cloud Agent tests. That creates a
  throwaway family. Do **not** type the household Pi’s pairing code into this
  VM — that would claim the real Goji into the test family.
- After pairing this VM’s kiosk, use **Settings → Pair another Goji → Join
  family** (8-character invite from `GET /api/device/parent-invite`) so the
  Flutter web session sees the same kids.
- Never commit `.env` files. Keys are `SUPABASE_URL` + `SUPABASE_ANON_KEY`
  (parent app) and `GOJI_CLOUD_URL` + `GOJI_CLOUD_ANON_KEY` (computer).

## One-time on a fresh VM

1. Sibling repos must exist as `goji_computer/`, `goji_cloud/`,
   `goji_learner_app/`. Preferred: add all four remotes to the Cloud
   environment so git checkout works. Fallback: `scripts/clone-product-repos.sh`.
2. Secrets on the environment (or local gitignored `.env` files):
   - `SUPABASE_URL` = `https://<ref>.supabase.co`
   - `SUPABASE_ANON_KEY` = project anon/legacy publishable key
3. Toolchains: `python3.12-venv`, Node, Flutter at `~/flutter` (see `AGENTS.md`).

## Start the three surfaces

```bash
# Kiosk API (port 5000) — live sync + dev plan API
cd goji_computer/backend
source .venv/bin/activate
# .env should set GOJI_SYNC_MODE=live GOJI_CLOUD_URL=.../functions/v1
# GOJI_CLOUD_ANON_KEY=... GOJI_DEV_API=1 FLASK_DEBUG=1
python app.py

# Kiosk UI (port 5173, proxies /api → 5000)
cd goji_computer/frontend && npm run dev -- --host 0.0.0.0 --port 5173

# Parent app (port 8080)
export PATH="$HOME/flutter/bin:$PATH"
cd goji_learner_app
set -a && source .env && set +a
flutter run -d web-server --web-hostname 0.0.0.0 --web-port 8080 \
  --dart-define=SUPABASE_URL="$SUPABASE_URL" \
  --dart-define=SUPABASE_ANON_KEY="$SUPABASE_ANON_KEY"
```

Open `http://127.0.0.1:5173/?dev=1` (kiosk) and `http://127.0.0.1:8080` (parent).

`flutter run` is debug: the pair gate is skipped (`kDebugMode`). Join the
throwaway family from Settings, then refresh the Family board (join does not
rebuild the board until reload — known gap).

## Happy-path loop

1. Kiosk `GET /api/device` → 6-char pairing code. `POST /api/device/register-cloud`.
2. Parent (or a throwaway anonymous JWT): `bootstrap_family` → add a child →
   `device-claim` → kiosk `POST /api/device/poll-claim`.
3. Parent: draft plan + `start_school_day`.
4. Computer: `cd goji_computer/backend && python -m sync.agent --once`
   (or `run_sync_cycle()`). Session acks `pending_start` → `active`. School
   Mode locks that profile to plan apps.
5. Child plays the School Day player (`I did it` / Start into the app).
6. Sync again. Cloud plan becomes `completed`, session `ended_how=all_tasks_done`.
7. Parent child-detail **Today** shows **Day finished**.

## Hermetic (no live cloud)

```bash
cd goji_computer/backend
source .venv/bin/activate
python -m sync.mock_family_cloud
python -m pytest tests/integration/test_school_day_e2e_mock.py -v
```

Covers Start → Pi pull/ack → work → completed / Release / messages. No Flutter UI.

## Gaps found in the 2026-08-25 Cloud Agent playthrough

- Family board card stays **Not started** after a completed day (`kidBoardStatus`
  only reads *open* sessions; child-detail hero correctly says **Day finished**).
- After **Join family**, the board stays empty until a full page reload.
- Carry-forward wizard can tag a freeform task as **Math**.
- A typing `min_duration_s=60` task can flip **done** when the exercise
  finishes, before the minute elapses.
