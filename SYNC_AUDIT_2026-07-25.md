# Goji sync audit — 2026-07-25

Full audit of Pi ↔ cloud ↔ parent-app communication, focused on the issues you reported:
profile-switch showing the wrong plan, orphaned/stale commands, and stale catalog rows in
Supabase after deleting PDFs on the Pi. Three parallel deep-dives (cloud functions +
migrations, Pi backend + kiosk, Flutter app) surfaced ~60 findings; the ones below are
confirmed root causes. **Fixes are applied in your working tree** — see "What changed"
and "Deploy steps". Backend suite: 395 passed. Kiosk unit tests: 418 passed. All 11 cloud
migrations (incl. the new one) apply cleanly to a scratch Postgres 16; the changed RPCs
were smoke-tested. Flutter changes compile-reviewed only — run `flutter test` + a device
smoke locally (no Flutter SDK in the audit sandbox).

---

## 1. The bugs you reported — root causes

### Profile switch keeps the old profile's plan (3 stacked causes, all fixed)

1. **Kiosk never re-fetches on profile switch.** `UserSelector` only set the store;
   `TodayPlan`/`ParentQuizzes` load in `onMount` and are never remounted (Hub subtree is
   always mounted). The old plan stayed rendered indefinitely. → `Hub.svelte` now wraps
   both tiles in `{#key $currentUserId}` so they remount and reload per profile.
2. **Every synced plan was hard-coded to user 1.** `agent.py` called
   `upsert_plan(payload, user_id=1)`, and `upsert_plan` even rewrote `user_id` back to 1
   on update. → the agent now resolves the owning profile from the device's cloud child
   (`users.cloud_child_id`), falling back to 1.
3. **School Mode state is global and leaked the wrong plan.** `get_school_mode_state`
   fell back to the *requesting* profile's active plan for the app lockdown. → the
   fallback now resolves the **session owner's** plan, and the response includes
   `session_user_id`. School Mode still locks the whole device on purpose — otherwise a
   kid could dodge it by switching profiles (the profile-switch PIN remains a known open
   item, see §4).

### Stale catalog rows in Supabase (your 0-page PDFs)

`catalog-upload` was upsert-only — nothing ever deleted a row, so PDFs deleted on the Pi
lingered (and re-uploads got new local_ids, stranding the old rows). Fixed end-to-end:

- The Pi now sends its **full inventory ids** (`present_pdf_local_ids` /
  `present_book_local_ids`) each cycle; the cloud **prunes** rows not in the list. Your
  two stale 0-page rows will disappear on the first sync after deploy.
- Duplicate `local_id`s in one batch used to 500 the whole request forever (Postgres
  `ON CONFLICT ... cannot affect row a second time`); rows are now deduped last-wins.
- The wizard's PDF picker now hides `total_pages = 0` rows outright, and the assignment
  sheet refuses to assign a range when the page count is unknown (it used to silently
  allow pages 1–999).

### Orphaned / stale commands (the big cluster — fixed)

- **Obsolete open sessions never cleared on the Pi.** If the Pi missed a cancel while
  offline, the old session stayed locally open forever → kiosk stuck in School Mode with
  nothing able to release it. `apply_pulled_session` now releases every locally-open
  session the cloud no longer reports (including the `school_session: null` case, which
  now has defined semantics in the contract).
- **Ack queue could wedge permanently.** Several paths produced acks the cloud rejected
  forever (PIN during `pending_release` — a migration had narrowed the RPC to
  `active` only; `completed` overwriting an un-pushed `active` ack; acks for deleted
  sessions). Fixes on both sides: the RPC accepts PIN from any open state again
  (migration `20260725120000`), and `school-session-push` now treats every *definitive*
  answer (applied / no-op / state-machine rejection / unknown session) as accepted so
  the Pi's queue always drains. Moot local acks are dropped when the cloud already shows
  the session terminal.
- **Cancelled/archived plans never left the Pi.** Nothing archived local plans, and
  `get_active_plan` picks the lowest-position/lowest-id active plan — so a cancelled
  Monday plan could shadow Tuesday's forever. The pull is now authoritative: after a
  successful pull the Pi archives any local ACTIVE cloud plan absent from the response.
  `plans-pull` correspondingly bounds delivery (active always; completed ≤ 7 days;
  limit 50) instead of re-serialising all history every 60s.
- **Poison rows retried forever.** One malformed journal entry blocked *all* later
  journal uploads (the agent's loop exits on empty accept); malformed activity events
  and deleted plan-task ids retried every cycle. All upload endpoints now follow the
  dequeue-safe rule: permanently-unfixable rows are accepted-and-dropped with a server
  log. The Pi journal loop also bails if the local sync-mark fails (previously a real
  infinite loop within one cycle on old DBs missing `synced_at`).
- **Sync-cycle ordering ate offline completions.** The pull ran before the status push,
  and `upsert_plan` deleted tasks removed cloud-side even when their local `done` was
  unreported — the kid's offline work vanished. Status/ack pushes now run **before** the
  pull, session acks push again right after it (so pending→active reaches you in the
  same cycle), and `upsert_plan` never deletes a done-but-unsynced task.
- **Wizard draft duplication (orphaned drafts).** Editing a draft created plan P2 and
  archived P1 only *after* Start; a failed Start (very common: "child already has an open
  school session") left both as drafts, with P1 unreachable from any UI, multiplying on
  retries. The wizard now checks for an open session up-front, archives the superseded
  draft before Start, and `createDraftPlan` deletes its plan row if the task insert
  fails (no more zero-task drafts — which, when started, created sessions that could
  never complete). Zero-task plans are also rejected by `start_school_day` (cloud) and
  can no longer instantly self-complete on the Pi (`maybe_complete_plan` requires ≥1 task).

---

## 2. Other confirmed bugs fixed in the same pass

**Cloud**
- `device-unpair` was fully specified in SYNC_API.md but **didn't exist** — with no
  recovery path, a claimed device could never re-pair (your dev re-flash workflow hits
  this). Implemented + registered in `config.toml`.
- `device-claim` hard-failed for a brand-new family (the `stop_bootstrap_child`
  migration removed the auto-created child but claim still required one). It now creates
  a placeholder "Child" and links it.
- `plans.status` defaulted to `'active'` — any INSERT omitting status leaked a
  half-authored plan straight to the kid's device. Default is now `'draft'`.
- `plan-status-push` re-runs the plan/session completion check on already-done acks (a
  retry can now fire a side-effect a partial failure missed).
- Messages: a reaction now backfills `delivered_at` (a reacted message could previously
  be re-delivered forever if its ack was lost); undelivered feed bounded (30 days / 200).
- `plans-pull` returns only an open session, or a terminal one updated ≤ 48h — a
  months-old released session is no longer re-sent on every pull.

**Pi**
- `children-push` now respects the contract's 20-profile batch cap (was: unbatched, so
  >20 profiles = permanent 400).
- Profile linking order fixed: children are pulled (name-matched, case-insensitive)
  **before** `link_device_child`, which used to grab an arbitrary unlinked user —
  the cause of mislinked profiles, wrong renames ("Ada (2)") and duplicate cloud
  children. The rename guard is also case-insensitive now.
- Repeated `pending_start` pulls no longer bounce the session state / re-queue acks
  every cycle while the first ack is in flight.

**Parent app**
- `currentFamilyParent()` picked an *arbitrary* parent row (RLS exposes all parents in
  the family) — with two parent phones, message sending failed non-deterministically for
  one of them. Now filtered by `auth_user_id`.
- Session query failures were swallowed into "no school day" — the board showed a live
  **Start** button while the child was actually locked in School Mode. Only
  "table missing" is tolerated now; real errors surface.
- The board and child detail now **poll every 30s while a session is open**, so
  "Starting…" resolves to active (and device-side completions appear) without manual
  pull-to-refresh. Stale in-flight loads can no longer overwrite fresh state (request
  sequence guard) — this was the "card reverts, parent taps Start twice" race.
- `release`/`cancel` now read the RPC's actual response: "This day already ended on the
  Goji" / "Nothing to cancel" instead of always claiming success.
- PDF carry-forward clamps to the document's real page count (was: happily produced
  pages 25–34 of a 24-page PDF, which the sheet's validation never saw again) and drops
  finished PDFs with a note.
- "Today's plan" uses the parent's local day, not UTC (the finished checklist used to
  vanish mid-evening in US timezones).
- Pair/Content tabs reload their child list when selected (IndexedStack built them once
  at boot — a fresh family could never pair without pull-to-refresh, and renamed
  children could get a device claimed under a stale name).
- Quiz picker includes family-wide (`child_id IS NULL`) content.

---

## 3. What changed (33 files)

**goji_cloud** — `SYNC_API.md` (contract updated for everything above),
`supabase/config.toml`, new `functions/device-unpair/`, new migration
`20260725120000_sync_hardening.sql`, and edits to functions: `activity-upload`,
`catalog-upload`, `device-claim`, `journal-upload`, `message-reactions-push`,
`messages-pull`, `plan-status-push`, `plans-pull`, `school-session-push`.

**goji_computer** — `backend/sync/agent.py` (cycle reorder, per-child plan ownership,
catalog present-ids, batching, loop guards), `backend/sync/cloud.py` (catalog prune
payload), `backend/database/{school,plans,profiles,__init__}.py`,
`backend/tests/test_profile_sync.py` (fixture isolation), `frontend/src/components/
Hub.svelte` (profile-keyed tiles), `frontend/package.json` + lockfile (adds `uqr`,
which `PairingBanner` imports but was missing from package.json).

**goji_learner_app** — `lib/services/{school_day,family,catalog}_repository.dart`,
`lib/screens/{school_day_wizard,family_board,child_day_detail,home_shell,pair_device,
author_content}_screen.dart`, `lib/widgets/pdf_assignment_sheet.dart`.

## Deploy steps

1. **Cloud:** `supabase db push` (applies `20260725120000_sync_hardening.sql`), then
   `supabase functions deploy` for the nine edited functions **plus the new
   `device-unpair`**.
2. **Pi:** deploy the backend as usual; restart `goji-sync.service`. Rebuild the kiosk
   frontend (`npm install && npm run build` — picks up `uqr`).
3. **App:** `flutter test && flutter run` on your phone.
4. Your stale catalog rows clean themselves up on the first Pi sync after (1)+(2). If
   you want them gone immediately:
   `delete from catalog_pdfs where total_pages = 0;` in the Supabase SQL editor.

Note: fixes were made against your folder as of today ~12:10 — if you edited any of the
33 files since, diff before overwriting.

---

## 4. Known issues NOT fixed (ranked — worth tickets)

1. **One-shot token delivery can brick a device.** `device-poll` clears
   `pending_access_token` *before* the response is written; a lost response = token gone
   forever. Recovery now exists via `device-unpair` + re-pair, but a token-ack handshake
   (or re-issue while `last_seen_at IS NULL`) is the real fix.
2. **Multi-child attribution.** Every upload (activity, journal, quiz scores) is
   attributed to `devices.child_id`, and messages/plans are pulled only for that child —
   local profiles for other kids sync nothing / mislabel data. Matches the TODO ("Pi
   still maps everything to local user 1" — now "to the device child"), but on a shared
   Goji, child B's work is recorded as child A's. Needs `child_cloud_id` on the wire
   (contract change) before multi-child is real.
3. **Profile-switch PIN during School Mode** (product doc gap): the device stays locked
   for all profiles (deliberate), but there's no PIN gate on switching, and the Today
   tile for the non-session profile just shows nothing.
4. **No session expiry.** An orphaned `pending_start` (device dead/unpaired) blocks
   `start_school_day` until a manual cancel. A pg_cron job terminalizing sessions older
   than ~24h would close it.
5. **`device-register` squatting / no rate limit** — unauthenticated endpoint accepts
   any device_id and stores the first secret presented; also an unbounded-INSERT vector.
6. **Anonymous-session loss forks the family.** App-data clear / reinstall mints a new
   auth user → new empty family; the Goji stays claimed by the orphan family. Needs a
   family invite/recovery code (also blocks the two-phones product goal).
7. Parent marking tasks done via direct `plan_tasks` RLS update bypasses the
   plan/session completion side-effect (only `plan-status-push` runs it). A trigger on
   `plan_tasks` would unify the paths.
8. Board has no "completed today" state (finished day renders as "No school day yet"),
   quiz scores show a raw UUID when the title lookup is missing, `wordLookupCount`
   silently caps at PostgREST max-rows, plans are all written `position: 0`, wizard
   catalog pickers aren't device-scoped (multi-device families can pick a PDF that
   lives on the other kid's Goji → unsatisfiable task), and `plans-pull` does up to 2
   sequential catalog lookups per task (N+1) — all minor, all still open.
9. Housekeeping: `cancel_school_day` reports `released` even when it lost the race to
   `completed`; `release_school_day` treats an old released session as a success;
   `latest_ota_release()` RPC and `plans-pull`'s selected-but-unused `plan_tasks.status`
   are dead code; `20260725001622` is a byte-identical no-op migration.
