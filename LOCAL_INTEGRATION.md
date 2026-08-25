# Running the whole Goji product locally

How to bring up **cloud + Goji computer + parent app** on one machine and drive a
real School Day across all three. Everything talks over real HTTP — no mocks —
so this exercises the actual `SYNC_API.md` contract.

This complements, not replaces, the hermetic mock in
`goji_computer/backend/tests/integration/test_school_day_e2e_mock.py`. That one
is fast and runs in CI with no Docker; this one is the only thing that can catch
contract drift, RLS/grant problems and edge-function bugs, because the mock
substitutes a Python object for the cloud.

## What runs where

| Piece | URL | Repo |
|-------|-----|------|
| Supabase (Postgres + auth + PostgREST + edge functions) | `http://127.0.0.1:54321` | `goji_cloud` |
| Goji device backend (Flask + SQLite) | `http://127.0.0.1:5000` | `goji_computer` |
| Goji kiosk (Svelte dev server) | `http://127.0.0.1:5173` | `goji_computer` |
| Parent app (Flutter, built for web) | `http://127.0.0.1:8088` | `goji_learner_app` |

The device runs with `GOJI_SYNC_MODE=live` and `GOJI_CLOUD_URL` pointed at the
local edge runtime, so it is exercising the same code path as a real Pi talking
to the family project.

## Quick start

```bash
# One-time per VM: make Docker usable (see "Docker in the sandbox" below)
scripts/setup-docker.sh

# Bring everything up (add --reset for a clean cloud DB + unpaired Goji)
scripts/local-stack-up.sh --reset

# Assert the whole loop, headless
scripts/local-school-day-smoke.sh

# Leave a school day open so you can click through the UIs
scripts/local-school-day-smoke.sh --keep

scripts/local-stack-down.sh          # stop device + app
scripts/local-stack-down.sh --all    # also stop Supabase
```

Each service runs in its own tmux session — `goji-backend`, `goji-frontend`,
`goji-parent-app`, `goji-sync-agent`:

```bash
tmux -f /exec-daemon/tmux.portal.conf ls
tmux -f /exec-daemon/tmux.portal.conf attach -t goji-backend
# logs also land in /tmp/goji-{backend,frontend,sync,parent-app}.log
```

## What the smoke check covers

`scripts/local_school_day_smoke.py` walks the product loop and asserts at each
hop. In order: parent signs in and bootstraps a family; the Goji pairs
(`device-register` → parent `device-claim` → `device-poll`); a **draft** plan
stays invisible to the device; `start_school_day` puts the session in
`pending_start`; the device pulls the plan and acks it to `active`, which turns
on School Mode and narrows `allowed_apps`; a parent message reaches the kiosk
and reports back as delivered; the kid's math minutes auto-verify a task and a
freeform task is self-confirmed; the plan completes and the session ends as
`all_tasks_done`; the parent then sees completed tasks, the preserved
`completed_how`, uploaded activity and a working `child_progress_summary`; and a
second day is ended early via `release_school_day` → `parent_release`.

## Clicking through it by hand

1. `scripts/local-stack-up.sh --reset` — it prints the pairing code, and
   registers it with the cloud for you (see the note below).
2. Open the kiosk (`:5173`); the hub shows the same code while the Goji is
   unpaired. (`curl -s localhost:5000/api/device` also has it.)
3. Open the parent app (`:8088`), create an account (any email — local auth has
   confirmations off, and mail is captured by Inbucket on `:54324`).
4. **Pair** tab → enter the code → Claim.
5. **Family** tab → *Plan today* → add tasks → *Save & Start*.
6. Within ~10s the sync agent pulls the plan: the kiosk drops into School Mode
   and the School Day player opens. `python -m sync.agent --once` forces it.
7. Do the work on the kiosk; watch the tasks tick over in the parent app.

The sync agent polls about every 10s while a day is open (`.env.local-cloud`
sets `GOJI_SYNC_INTERVAL_ACTIVE_S=10`), so the UI is not instant — that is the
real product behaviour, not a local artifact.

> **Claim before the kiosk has ever been opened and you get "Invalid pairing
> code".** The device pushes its code to the cloud only when the hub mounts
> `PairingBanner.svelte`, which on a real Pi happens at boot but locally does not
> happen until you load `:5173`. `local-stack-up.sh` now calls
> `POST /api/device/register-cloud` itself so the printed code is claimable right
> away; if you ever recreate the device by hand, call that first.

## Two things you cannot test locally

**`goji_cloud` is missing edge functions that the device already calls.** A sync
cycle logs a 404 for each and carries on:

| Device calls (`goji_computer/backend/sync/cloud.py`) | In `goji_cloud`? | In `SYNC_API.md`? |
|---|---|---|
| `children-pull`, `children-push` | no | no |
| `household-tasks-pull`, `household-tasks-status-push` | no | no |
| `device-invite` | no | no |

`TODO.md` records these as deployed to the live project, so the repo has drifted
from live and is no longer a full description of the wire. Multi-child
assignment, the Household Tasks board and parent invite/recovery therefore
cannot be exercised locally. Per `CLAUDE.md` rule 1 the fix starts by writing
them into `SYNC_API.md`, then adding the migrations and functions — that is
product work, not a harness gap.

**`goji_cloud`'s default branch is `feat/school-day-sync-contract`, not `main`.**
It has no `main` branch, despite `TODO.md` saying the School Day branches were
merged to main.

## Docker in the sandbox

`supabase start` needs Docker, and two sandbox quirks break it. Both are handled
by `scripts/setup-docker.sh`; they are written up here because the symptoms are
misleading.

1. **overlay2 cannot mount on the VM's overlayfs root**, so every container
   fails with `mount source: overlay ... invalid argument`. The `vfs` fallback
   works but is slow enough that Postgres misses the Realtime migration
   container's 15s connection timeout, so `supabase start` dies at
   `Initialising schema...`. Fix: back `/var/lib/docker` with a real ext4
   filesystem on a loop device, then use overlay2 normally.

2. **The sandbox keeps an iptables _legacy_ ruleset whose FORWARD policy is
   DROP**, while Docker writes its rules to the _nft_ tables. Both are
   evaluated, so container-to-container traffic is dropped — DNS resolves fine
   and every TCP connect times out, which reads exactly like a slow or
   unreachable database. Fix: allow forwarding on Docker's bridges in the legacy
   table. Confirm with:

   ```bash
   docker network create t && docker run -d --name p --network t -e POSTGRES_PASSWORD=pw postgres:16-alpine
   docker run --rm --network t -e PGPASSWORD=pw postgres:16-alpine psql -h p -U postgres -c 'select 1'
   ```

Studio, imgproxy, vector, logflare and supavisor are excluded to cut startup
cost; none is part of the sync contract. Realtime is kept because the CLI runs
its migrations during schema init.

## Local keys

The anon/service keys in `scripts/local-env.sh` are the fixed Supabase **local
development** demo keys — identical on every `supabase start` machine, and not
secrets. The live family project's keys are not in any repo (`CLAUDE.md` rule 4).

The device's `backend/.env.local-cloud` is **generated** by the harness, never
committed: `goji_computer` is the flashable SD image source (rule 3), so
dev-cloud config must not live there and nothing key-shaped should be checked in.
Regenerate it any time with `source scripts/local-env.sh && goji_write_device_env`.
