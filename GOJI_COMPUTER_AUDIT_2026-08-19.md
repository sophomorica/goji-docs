# Goji computer — pre-lessons robustness audit

**Date:** 2026-08-19  
**Target repo:** [`sophomorica/kodi-computer`](https://github.com/sophomorica/kodi-computer) @ `5c8bbdd` (`fix(school): lock School Mode per profile so siblings stay unlocked`)  
**Scope:** full tree — Svelte 5 kiosk (`frontend/`), Flask + SQLite (`backend/`), sync agent, deployment. Not the parent app or cloud, except where the device contract is wrong.  
**Goal:** make the device robust before the next phase (authoring / shipping lessons on-device).

This is a **findings + backlog** audit. No device code was changed. Historical June 2026 work in `goji_computer/AUDIT.md` is treated as a baseline; items below were **re-verified in current `main`**. Already-fixed June items are not re-opened.

---

## How this was reviewed

Three review tracks, split across agents, then reconciled against source:

| Track | What ran | Note |
|-------|----------|------|
| **Svelte 5 best practices** | Official Svelte docs (`best-practices`, runes, `{#each}`, `$effect`, stores, legacy, `{@html}`, compiler warnings) + skill checklist + file-by-file scan of 74 `.svelte` files and stores/API clients | Vite + Svelte 5 kiosk (not SvelteKit). Stack rule: runes only. |
| **Bugbot** | Official Cursor Bugbot **could not start** — it only reviews a git PR/branch diff, and this was a full-`main` audit with no feature diff. Equivalent Bugbot-style pass over backend + frontend | Treat this document as the Bugbot report. |
| **Security Review** | Official Cursor Security Review **same limitation**. Equivalent SecurityBot pass over pairing, OTA, USB, WiFi, user-apps compile/preview, School Mode, local API, kiosk lock | Treat this document as the Security Review report. |

**Also scanned:** `backend/app.py`, `config.py`, all `routes/` and `sync/`, `database/device.py`, `school.py`, `settings.py`, `content.py`, `messages.py`, `wifi.py`, `utils/crypto.py`, `deployment/`, kiosk shell (`App.svelte`, Hub, School Day, stores), educational apps, `{@html}` / `innerHTML` / `subprocess` / dynamic SQL.

**Not verified in this pass:** live Pi hardware, real Evince install, nftables on a claimed device, Playwright/e2e (no frontend `node_modules` in the audit sandbox), parent-app or cloud RLS (those are other repos).

**Labels:** **VERIFIED** = seen in current source. **ASSUMED** = threat depends on LAN/kiosk/firewall deployment not re-tested here.

---

## Verdict (read this first)

The 2026-06/07 remediation **held**. The kiosk is on Svelte 5 runes (no `export let` / `on:click` / `$:` / `<slot>` left). Pairing still strips `access_token` / `register_secret` from the browser. WiFi connect uses list-args `nmcli`. USB import checks `realpath` + `commonpath`. School Mode is per-profile; Hub remounts Today/quizzes on `{#key $currentUserId}`.

It is **not** yet “robust enough to start lessons” if “robust” includes a kid or anyone on the LAN as an attacker, or a second child on the same box. The local Flask API is still a **trust-the-kiosk** API: no session, `user_id` is a query param, `CORS(app)` is wide open, and privileged routes (shutdown, Wi-Fi, PIN, pairing invite, users CRUD, Evince) have no gate.

**Do these before lesson authoring eats the calendar:**

1. Stop leaking the household PIN through `GET /api/settings`.
2. Gate or disable LAN-privileged routes (shutdown, wifi, pin, invite, users delete, Evince).
3. Kill or lock the Evince native-viewer routes (kiosk escape).
4. Fix parent-quiz + message profile scoping (sibling data bleed).
5. Harden the coding-preview iframe (sandbox + HTML escape).
6. Fix Journal autosave so a profile switch cannot write Child A’s entry as Child B.
7. Stop summing cumulative Journal `word_count` events (autosave inflates School Day writing goals).
8. Reset `todayPlan` + `schoolMode` on profile switch before the next fetch settles.
9. Remove the Tailwind CDN load from HTML coding previews.
10. Close Research article SSRF (`path` that starts with `http` is fetched as-is, then `{@html}`’d).

Everything else in this file is ranked so it can be ticketed without re-litigating.

---

## 1. What’s already good (do not re-open)

- **Runes migration is done.** Repo-wide search found no `export let`, `on:click`, `$:`, `<slot>`, `$$props`, or `<svelte:component>`. Event handlers are `onclick={...}`. Props use `$props()`.
- **Code splitting still in `App.svelte`.** Hub is eager; 13 apps + TipTap + pdf.js are `import()` lazy chunks.
- **Profile-switch plan bug (2026-07-25) still fixed.** `Hub.svelte` keys `TodayPlan` / `ParentQuizzes` on `$currentUserId`. `todayPlan.js` refetches immediately on `currentUserId` and resets School Mode latch per child.
- **Pairing public view is clean.** `database/device.py` `_public_device` / tests assert `access_token` and `register_secret` never go to the browser. Live `poll-claim` is the claim path; stub `/claim` is disabled when `GOJI_SYNC_MODE=live`.
- **WiFi injection (June P0) still fixed.** `/connect` and `/forget` use `subprocess` list args (`shell=False`).
- **USB traversal (June P0) still fixed.** `_is_within_usb_mounts` uses `realpath` + `commonpath`.
- **OTA is verify-only.** Streaming SHA-256 + Ed25519 over the 32-byte digest; install is explicitly not implemented. Correct for now.
- **Messages list is profile-aware when `user_id` is passed.** `list_messages` matches `users.cloud_child_id`. Frontend `messagesAPI.list` uses `appendUserId`.
- **Household Tasks** already has generation tokens so stale polls don’t clobber toggles.

---

## 2. Security Review

Threat model: kid at the kiosk is untrusted; Chromium is the only UI; Flask binds `0.0.0.0:5000`; the Pi may be on home Wi-Fi; pairing talks to one family Supabase; flashed image has no secrets.

### S-P0 — Household PIN is readable (and settable) with no auth

**VERIFIED.** `GET /api/settings` returns **every** settings row, including `household_pin` (`backend/database/settings.py`, `backend/routes/system.py`). Hub calls this on mount (`Hub.svelte` → `settingsAPI.get()`). Anyone who can hit the API — the kid via DevTools if `?dev=1`, or a sibling/phone on the LAN — can read the PIN and `POST /api/school/unlock`.

`POST /api/school/pin` sets the first PIN with **no** `current_pin` (by design) and no other auth. Combined with open CORS, a LAN client can set the household PIN before the parent does.

`household_pin` is stored in plaintext in SQLite (`settings.value`).

**Fix:** never return `household_pin` from `GET /api/settings` (return `household_pin_set: true/false` only). Store a hash (or at least don’t put the PIN on the wire). Require a pairing/device token or a one-time setup lock for first PIN. Do not log PIN in debug request bodies (`app.py` logs raw bodies when `DEBUG`).

### S-P0 — Unauthenticated privileged local API on `0.0.0.0`

**VERIFIED.** `create_app()` does `CORS(app)` with no origin allowlist. Dev entrypoint is `app.run(host='0.0.0.0')`. Production gunicorn is the same factory. There is no API key, cookie session, or CSRF token.

Unauthenticated today (non-exhaustive):

| Route | Impact |
|-------|--------|
| `POST /api/shutdown` | Power off the Pi |
| `POST /api/wifi/enable\|disable\|connect\|disconnect` | Steal Wi-Fi / cut sync |
| `POST /api/wifi/connect` | Kid or LAN sets home Wi-Fi password into nmcli |
| `GET /api/device` | Live pairing code while unclaimed |
| `GET /api/device/parent-invite` | Family invite code once claimed (uses server-side token; still no kiosk auth) |
| `POST /api/school/unlock` + PIN | End a child’s school day |
| `POST /api/school/pin` | Set/change household PIN |
| `DELETE /api/users/<id>` | Wipe a profile and their data |
| `POST /api/pdfs/<id>/open-native` | Launch Evince (kiosk escape) |
| `POST /api/settings` | Arbitrary settings write, including PIN if the client sends it |

**ASSUMED:** home LAN is the realistic attacker (another device, a curious kid with a laptop). This is acceptable for a **single-user offline appliance** only if the firewall + Chromium kiosk make the API unreachable except from localhost. `deployment/FIREWALL_SYNC.md` is **opt-in and not enabled on images**. Workspace `TODO.md` already says “Firewall still open.”

**Fix (pick one architecture, don’t invent a third):**

- A. Bind Flask to `127.0.0.1` only; Chromium kiosk talks localhost. LAN pairing stays on the phone↔cloud path. **Preferred** for a kiosk.
- B. Keep LAN bind but require a device-local capability (e.g. loopback-only for privileged routes, or a boot-time `X-Goji-Local` header Chromium injects that is never shown to the page).
- C. Ship the nftables allowlist **and** refuse privileged routes unless `request.remote_addr` is loopback.

Also replace `CORS(app)` with an explicit localhost origin list (or drop flask-cors if the kiosk is same-origin).

### S-P0 — Evince native viewer is still an API kiosk escape

**VERIFIED.** `AUDIT.md` / `TODO.md` said the UI no longer uses Evince (pdf.js instead) because the file-open dialog exposes the Pi filesystem. The routes are still live: `POST /api/pdfs/<id>/open-native` (`backend/routes/pdf_reader.py`) runs `evince --fullscreen` on `:0` with no auth. `GET /api/pdfs/native-viewer/status` still probes `which evince`.

**Fix:** delete both routes (and the evince package from the image). If something still calls them, fail closed.

### S-P0 — Coding preview iframe can escape into the kiosk origin

**VERIFIED.**

1. `SimplePreview.svelte` uses `sandbox="allow-scripts allow-same-origin"`. Same-origin + scripts means compiled tutorial/user Svelte **is the kiosk origin** — it can `fetch('/api/shutdown')`, read `localStorage` profile ids, call `/api/school/pin`, etc.
2. Preview error HTML interpolates `error_details`, `stdout`, `stderr`, and **raw `code`** into a `<pre>` with no HTML escape (`user_apps.py` `preview_app`). A `</pre><script>…` in the child’s (or a tutorial author’s) source is XSS on the parent origin.
3. Successful preview injects `compiled_js` and `css_content` into the document. That is the feature — but only safe if the iframe is **cross-origin isolated** (`sandbox="allow-scripts"` **without** `allow-same-origin`, plus a unique iframe `src` origin or `sandbox` null origin).
4. `?debug=source` dumps the full generated HTML. `/api/test-preview`, `/api/test-imports`, `/api/test-compile` are debug endpoints still registered in production.

Preview `fetch` is wrapped to attach `X-App-ID` and then hits the real `/api/*` (flashcards, etc.). Combined with same-origin, a compiled app is a full API client.

**Fix:** drop `allow-same-origin`; serve preview on a separate origin or `sandbox` opaque origin; `html.escape` all error-page interpolations; delete or `DEBUG`-guard test/preview debug routes; stop logging first 200 chars of user source and compiled JS at INFO (`compile_svelte`).

### S-P1 — CSP and kiosk locks are weaker than the comments claim

**VERIFIED.** `CSP_POLICY` allows `'unsafe-inline'` and `'unsafe-eval'` on scripts, and `http://localhost:*` / `127.0.0.1:*` for almost every directive (`app.py`). That is required for the preview compiler / Vite-ish eval, but it means CSP does **not** stop XSS once HTML is injected.

`?dev=1` on a production kiosk URL disables the hotkey / context-menu lock (`App.svelte` `isDev`). A kid who learns the query string gets DevTools-class chrome.

`window.open` / `location.assign` overrides are best-effort and documented as limited. They are not a security boundary.

**Fix:** ignore `?dev=1` unless `import.meta.env.DEV` or an env flag baked at image build. Tighten CSP on the main kiosk document (preview iframe can have a looser policy). Treat JS overrides as UX only.

### S-P0 — Research article fetch is open SSRF; HTML is rendered unsanitized

**VERIFIED.** `GET /api/research/article?path=` (`backend/routes/research.py` ~168–181): if `path` does not start with `http`, it is prefixed with `KIWIX_BASE_URL`; **if it does**, `article_url = article_path` and Flask fetches it. That is a third-party call from the Pi (product rule break) and an SSRF into the LAN/cloud.

`process_article_html` rewrites links/images; it does not strip scripts or event handlers. `Research.svelte` `sanitizeAndProcessContent` is a no-op (`return html`). `{@html articleContent}` and `{@html result.snippet}` inject the result on the kiosk origin.

**Fix:** allow only Kiwix paths under a fixed prefix. Reject `http://` / `https://` / `//`. Sanitize with a strict allowlist before `{@html}`, or render as text. Escape snippets (they already come from `get_text()`).

### S-P1 — `{@html}` Wikipedia / Kiwix (residual after SSRF close)

**VERIFIED.** Even after the open-URL fetch is rejected, Kiwix/ZIM HTML is still unsanitized. Snippets are text-extracted (safer). Full article HTML is ZIM content.

**ASSUMED:** ZIM is a trusted offline snapshot. Residual risk is a compromised/malicious ZIM or a Kiwix XSS.

**Fix:** same sanitizer as S-P0; ticket **SEC-RESEARCH-HTML** stays P2 once the open-URL path is gone.

### S-P1 — Compile / preview logging

**VERIFIED.** `compile_svelte` logs code preview, stdout, stderr, and compiled JS at INFO into `logs/goji.log` (rotated 10MB × 5). Kid code and compiler errors persist on disk.

**Fix:** log hash + length only at INFO; dump bodies at DEBUG.

### S-P2 — Other security

| ID | Severity | Finding | Evidence |
|----|----------|---------|----------|
| S-P2a | Medium | Fernet Wi-Fi key is fine (0600, cached); passwords are not returned by `GET /api/wifi/networks`. Residual: key file lives in `DATA_DIR` on the SD card. | `utils/crypto.py`, `database/wifi.py` |
| S-P2b | Medium | Dynamic SQL uses allowlisted columns / placeholders (`notebooks.py`, `pdf_reader.py` SET clauses, `users.py` delete table list). Not injection if those lists stay static. Add a review rule: never interpolate request strings into SQL. | `database/notebooks.py`, `users.py` |
| S-P2c | Medium | `user_id` query param is the only tenancy. Any client can read/write another profile’s journal, math, plans, unlock. Acceptable only if API is localhost-only. | almost every blueprint |
| S-P2d | Low | `DEBUG` error handler returns traceback JSON. Keep `FLASK_DEBUG` off on images (already the intent). | `app.py` |
| S-P2e | Low | Egress firewall installer exists but is not on by default. Third-party calls from the Pi are a product rule, not an enforced kernel rule. | `deployment/FIREWALL_SYNC.md` |
| S-P2f | Low | OTA download will follow `http://` `image_url` from cloud metadata. Trust is the Ed25519 key; still prefer HTTPS-only URL allowlist when apply is built. | `sync/ota.py` |
| S-P2g | Info | Pairing one-shot token loss (cloud delivers `access_token` once) remains the 2026-07-25 §4 brick-pairing issue. Device handles 409 correctly; recovery is still human. | `routes/device.py` `poll_claim` |
| S-P1h | High | School Mode is **UI-only**. No `before_request` 403s journal/coding/math while a day is open. Kid with `fetch` or `?dev=1` walks around the Hub lock. | all blueprints |
| S-P1i | High | `POST /api/activity` with `event_type=quiz.submitted` and a `content_cloud_id` calls `mark_quiz_tasks_done` — no quiz runtime. Forges School Day completion. | `routes/activity.py` |
| S-P1j | Medium | `POST /api/settings` accepts **any** key, including `household_pin` and sync watermarks (`household_tasks_since`). Kid-writable allowlist needed. | `routes/system.py` |
| S-P2h | Medium | PDF `file_path` from DB is joined onto `PDF_READER_DIR` with no `resolve()`/`is_relative_to` guard. Safe unless the row is poisoned. | `routes/pdf_reader.py` `_get_pdf_file_path` |
| S-P2i | Medium | `/api/school/unlock` has no rate limit / lockout. 4-digit PIN is brute-forceable on LAN. | `routes/school.py` |
| S-P2j | Low | `/api/research/debug` and user-apps test routes are registered in production. | `research.py`, `user_apps.py` |
| S-P1k | High | `rebuild-pi.sh` grants `goji ALL=(ALL) NOPASSWD: ALL`; `setup-pi.sh` does not remove `010-goji-nopasswd`. | `deployment/rebuild-pi.sh` |
| S-P2k | Medium | USB browse roots are all of `/mnt` and `/media`, not live USB mountpoints only. | `routes/usb.py` |
| S-P2l | Medium | `goji-wifi-sudoers` allows any `nmcli` subcommand, not the argv the API uses. | `deployment/goji-wifi-sudoers` |

Household-task toggle: the HTTP route **does** require `child_id` (400 if omitted). The DB helper is fail-open if called with `child_id=None` — keep the route gate; don’t treat the HTTP API as broken.

---

## 3. Bugbot (correctness)

### B-P0 — Parent quizzes are not per-child

**VERIFIED.** `syncedContentAPI.list("quiz")` does **not** send `user_id`. `GET /api/synced-content` → `list_synced_content()` selects the whole `synced_content_cache` with no child filter. Hub remounts `ParentQuizzes` on profile switch, but **every profile sees every quiz**. Completing a quiz (`POST .../complete`) removes it for **all** siblings.

Sync agent applies pulled decks with `apply_pending_synced_content(user_id=1)` hardcoded (`sync/agent.py`). Sibling flashcard imports land on user 1.

**Impact:** wrong child takes the other child’s placement/check quiz; parent standing gets attributed to the wrong kid; lesson phase will make this worse.

**Fix:** add `child_id` / `user_id` on `synced_content_cache` (contract in `goji_cloud/SYNC_API.md` first). Filter list + complete. Stop hardcoding `user_id=1` on apply. Frontend: `appendUserId` on the client.

This is the same family as the known **multi-child attribution** gap (`devices.child_id` on uploads). Ticket them together.

### B-P1 — Message banner does not refetch on profile switch

**VERIFIED.** `MessageBanner` is mounted once in `App.svelte` (not inside `{#key $currentUserId}`). It polls every 10s. `messagesAPI.list` uses `appendUserId`, so the **next** poll is correct, but for up to 10s after a switch the previous child’s banner stays on screen. `dismissed` is a module-lifetime `Set` of `cloud_id`s (OK if ids are globally unique; confusing if two children ever shared a cache row).

**Fix:** subscribe to `currentUserId` and `load()` immediately; or wrap the banner in `{#key $currentUserId}` and reset `dismissed`.

### B-P1 — `?dev=1` on a flashed image

**VERIFIED.** `isDev = import.meta.env.DEV || query.has("dev")`. Production build still honors `?dev=1`: no hotkey lock, context menu on, splash skipped. e2e needs this in Vite; production should not.

**Fix:** `import.meta.env.DEV` only, or a compile-time `GOJI_DEV_KIOSK` define. Keep `?dev=1` for Vite.

### B-P1 — Journal / writing / notebooks stay mounted across profile switch

**VERIFIED.** Lazy apps are keyed on `$currentApp`, not `$currentUserId`. Switching profiles while inside Journal/Writing/Math does **not** remount the app. `appendUserId` updates, but in-memory `content` / `todayEntry` / drill state is the previous child until the user navigates away.

Today-plan and School Mode **do** refetch (controller subscribes to `currentUserId`). The open app does not.

**Fix:** `{#key $currentUserId + $currentApp}` around the lazy app, or an explicit “profile changed → hub” rule during School Mode (product already wants the parent to know who is at the box).

### B-P0 — Journal debounce can write Child A’s entry as Child B

**VERIFIED.** `Journal.svelte` `handleEditorUpdate` schedules `saveEntry()` after 2s. `onDestroy` only clears `journalLiveWords`, **not** `saveTimeout`. `backToHub()` calls `saveEntry()` without `await` then navigates. `saveEntry()` uses live `getUserId()`. On a shared kiosk: leave Journal → switch profile on Hub before the debounce or in-flight POST finishes → text lands on the new `user_id`. Corrupts journal and plan-window word counts.

**Fix:** Clear `saveTimeout` in `onDestroy`; capture `userId` at edit start and pass it through the save; await save before `navigateToHub()`; cancel in-flight work on `currentUserId` change.

### B-P1 — School Day Player stays open after unlock

**VERIFIED.** `refreshToday()` calls `openPlayer()` when School Mode turns on; it never calls `closePlayer()` when `school.active` becomes false (parent remote release, empty pull, sibling with no session). Child can stay on the full-screen overlay while tiles are already unlocked.

**Fix:** If `!school.active && !todayPlan.completed`, `closePlayer()`. Optionally key the player on `currentUserId`.

### B-P1 — Legacy `school_session` pull can unlock a sibling

**VERIFIED.** `apply_pulled_session()` (singular) calls `_release_obsolete_open_sessions`, which releases **every** locally-open session except the payload’s `cloud_id`. The family-scoped `apply_pulled_sessions()` does not. The agent uses the legacy path when `school_sessions` is absent (`agent.py`). An older cloud that only sends the claimed child’s session can clear a sibling’s offline-open day.

**Fix:** Scope obsolete cleanup to the payload’s `child_id`, or require family-scoped pulls on multi-profile devices.

### B-P1 — Coding autosave can fire after leave

**VERIFIED.** `Coding.svelte` `$effect` sets a 3s `saveTimeout` when `userCode` changes. `onDestroy` clears it, so navigate-away is OK. If `currentChallenge` becomes null while a timer is queued, the effect re-runs and does **not** clear the old timeout (clear is inside the `if`). A stale save can POST the previous challenge’s code after the user hit Back.

**Fix:** `return () => clearTimeout(saveTimeout)` from the effect; clear unconditionally at the top.

### B-P2 — Other bugs

| ID | Finding | Evidence |
|----|---------|----------|
| B-P2a | `Tasks.svelte` `$effect(() => { void loadUsers(true); })` has no reactive dependency. In Svelte 5 it runs once (OK) but is the wrong primitive — `onMount` is the intent. If `loadUsers` later reads state, this becomes a refetch loop (the 2026-06 Hub bug class). | `Tasks.svelte` |
| B-P2b | `SchoolDayPlayer` `$effect` writes `justDone` / `prevStatus` from `tasks`. Effects-that-write-state are the official “avoid” case; can double-fire on the same transition. Prefer comparing previous in the poller or a `$derived` + keyed animation. | `SchoolDayPlayer.svelte` |
| B-P2c | `SchoolTaskChip` three `$effect`s mutate `workingTask` / `doneMoment`. Same class; works, but fragile when adding lessons that swap tasks quickly. | `SchoolTaskChip.svelte` |
| B-P2d | `list_messages(user_id=None)` is the unfiltered family cache. Any client that omits `user_id` sees every child’s mail. Frontend is fine; LAN client is not (see S-P0). | `database/messages.py` |
| B-P2e | `GET /api/stats` loads **all books** and sums in Python. Fine at 29 books; will hurt when Gutenberg ingest grows for lessons. | `routes/system.py` |
| B-P2f | No ESLint / `svelte-check` / ruff in CI (`AGENTS.md`: “No linter is configured”). Lessons will add a lot of Svelte; catch runes mistakes in CI. | `frontend/package.json`, `.github/workflows/ci.yml` |
| B-P2g | Known flake: `MyApps.test.js` (workspace `CLAUDE.md`). Don’t start lessons on a red main. | frontend tests |
| B-P2h | Known product: `content-generate` stub; OTA apply not implemented; PDF bookmark seeding; full message-center UI. Not new. | workspace `TODO.md` |
| B-P2i | `delete_user()` cascade omits plans, plan_tasks, activity_events, school_sessions, flashcard_decks; silent `except: pass`. | `database/users.py` |
| B-P2j | `GET /api/plans/today` mutates (auto-verify / maybe-complete). Surprising races vs the sync agent. | `database/plans.py` |
| B-P2k | Activity tracker subscribes to `currentApp` only, not `currentUserId`. Latent until profile switch exists outside Hub. | `lib/activity/tracker.js` |

---

## 4. Svelte 5 best practices

Official guidance used: `$state` only when reactive; `$derived` over `$effect` for computation; don’t write state in effects; treat props as changing; keyed `{#each}` (never index); `createContext` over module stores for SSR (N/A for kiosk — stores are OK but the skill prefers rune classes); avoid legacy (`class:`, `use:`, stores-as-default); `{@html}` is a sanitizer problem.

### Already aligned

- Runes-only components; `$props()` / `$state` / `$derived` / `$derived.by` in Hub, Tasks, School Day, math, research.
- Keyed lists in Hub apps, Tasks, ParentQuizzes, MessageBanner reactions, Research results (`result.url`).
- `onMount` for Hub / UserSelector / WiFi settings loads (June `$effect` refetch bug stayed fixed).
- `<svelte:window>` for kiosk key / context handlers (not `onMount` listeners).
- Lazy apps + `{#await}` / `{:catch}` instead of a giant eager graph.
- `clsx` via `cn()` on Hub tiles.

### SBP-P1 — `$effect` used as a state machine

`SchoolDayPlayer`, `SchoolTaskChip`, `SimplePreview`, `Tasks` (loadUsers), `Coding` autosave, `Journal` (`journalLiveWords.set`), `FractionInput` (focus), `UsbUploadWizard`. Several write `$state` inside the effect. This is the #1 Svelte 5 footgun and the one that already bit Hub in June.

**Rule to lock before lessons:** data load = `onMount` or an event; derived view = `$derived`; external sync (stores, iframe src) = `$effect` with a **cleanup return** and no `$state` writes if a derived/event will do.

### SBP-P1 — Shared stores instead of rune classes / context

`user.js`, `navigation.js`, `schoolMode.js`, `todayPlan.js`, `player.js`, `settings.js` are classic `writable` stores. Fine for a single kiosk (no SSR leak). The skill’s direction is classes with `$state` fields or `createContext`. Not a rewrite-now; **do not add a sixth store** for lessons — put lesson progress on `todayPlan` / activity events.

`getUserId()` module subscription is the right pattern for API tenancy; keep it.

### SBP-P2 — Leftover `class:` directive

`App.svelte` (`class:opacity-0`), `PdfViewer`, `PdfCoverThumb`, `KeyboardGuide`, `FractionVisual`, `TipTapEditor`. Skill: prefer `class={['…', { 'opacity-0': splashFading }]}`. Cosmetic; migrate when those files are touched.

### SBP-P2 — `{@html}` without a sanitizer helper

Only `Research.svelte`. Add one `sanitizeHtml()` used by research (and any future lesson HTML / quiz stems). Do not sprinkle `{@html}` in lesson players.

### SBP-P2 — No `<svelte:boundary>` around lazy apps

`{#await}` has `{:catch}` (good). A render-time throw inside a mounted lesson won’t recover. When the lesson player lands, wrap it in `<svelte:boundary>` with a “back to Hub” fallback.

### SBP-P2 — A11y debt (compiler-warning class)

`Research.svelte` already `svelte-ignore`s click-on-non-button for article HTML. Lesson UI should use real `<button>` / links. Hub tiles are `<button>` (good). Confirm/shutdown flows: verify focus trap when you next touch them.

### SBP-P2 — Tooling

No `svelte-check`, no ESLint svelte plugin, no autofixer in CI. Before a lesson factory, add `npm run check` (`svelte-check`) to CI. `AGENTS.md` already admits this gap.

---

## 5. Prioritized backlog (ticket these)

Copy into `goji_computer/TODO.md` when that repo is opened. Do **not** start lesson-player work in front of P0.

### P0 — before lessons

- [ ] **SEC-PIN-LEAK** — Strip `household_pin` from `GET /api/settings`; hash at rest; never log PIN. (`routes/system.py`, `database/settings.py`, Hub settings load)
- [ ] **SEC-API-BIND** — Bind API to loopback **or** lock privileged routes to loopback; replace open `CORS(app)`. (`app.py`, gunicorn unit)
- [ ] **SEC-PRIV-ROUTES** — Authz or delete: shutdown, wifi mutate, users DELETE, school pin/unlock, parent-invite, settings POST, Evince. (`routes/system.py`, `wifi.py`, `users.py`, `school.py`, `device.py`, `pdf_reader.py`)
- [ ] **SEC-EVINCE** — Remove `open-native` + `native-viewer/status`; drop evince from the image.
- [ ] **SEC-PREVIEW** — Preview iframe: drop `allow-same-origin`; HTML-escape error page; DEBUG-guard `/api/test-*`; stop INFO-logging source. (`SimplePreview.svelte`, `routes/user_apps.py`)
- [ ] **BUG-JOURNAL-SAVE** — Clear Journal `saveTimeout` on destroy; pass captured `userId`; await save before Hub. (`Journal.svelte`)
- [ ] **BUG-JOURNAL-WORDS** — Do not SUM cumulative `journal.entry` word_count; snapshot once or use `MAX` / `journal_entries.word_count`. (`database/activity.py`, `Journal.svelte`)
- [ ] **BUG-PLAN-STALE** — On `currentUserId` change: `plan: null`, `setSchoolModeState({ active: false })`, generation-guard `refreshToday`. Key `SchoolModeBar`. (`todayPlan.js`, `Hub.svelte`)
- [ ] **SEC-CDN-TAILWIND** — Replace `cdn.tailwindcss.com` in `HTMLChallenge.svelte` with the on-device Tailwind subset.
- [ ] **SEC-RESEARCH-SSRF** — Reject `http`/`https`/`//` on `GET /api/research/article?path=`; allow only Kiwix prefix. (`routes/research.py`, `Research.svelte`)

### P1 — first engineering week of lessons (or sooner)

- [ ] **BUG-QUIZ-SCOPE** — Per-child synced quizzes + complete; stop `apply_pending_synced_content(user_id=1)`. Contract change → `SYNC_API.md` first. (`content.py`, `syncedContent.js`, `sync/agent.py`)
- [ ] **BUG-MSG-SWITCH** — Refetch/remount `MessageBanner` on `currentUserId`. (`MessageBanner.svelte`, `App.svelte`)
- [ ] **BUG-APP-SWITCH** — Remount open app (or bounce to Hub) on profile change. (`App.svelte`)
- [ ] **BUG-DEV-QUERY** — Ignore `?dev=1` in production builds. (`App.svelte`)
- [ ] **BUG-CODING-SAVE** — Effect cleanup for coding autosave. (`Coding.svelte`)
- [ ] **SEC-DEV-ENDPOINTS** — Gate or delete test-compile / test-preview / debug=source.
- [ ] **SEC-CSP-DEVTOOLS** — Don’t let query-string Dev mode disable kiosk chrome; optional CSP split (kiosk vs preview).
- [ ] **KNOWN-MULTI-CHILD** — `child_cloud_id` on the wire (2026-07-25 §4.2). Still blocks honest lesson attribution.
- [ ] **SEC-SCHOOL-UI** — Enforce School Mode on the API, not only the Hub. 
- [ ] **SEC-QUIZ-FORGE** — Only mark quiz tasks done from a trusted quiz-complete path, not raw `quiz.submitted` activity.
- [ ] **BUG-PLAYER-STICK** — `closePlayer()` when `school.active` becomes false. (`todayPlan.js`)
- [ ] **BUG-LEGACY-SESSION** — Don’t let singular `school_session` pull release every other child’s open session. (`database/school.py`)
- [ ] **SEC-SETTINGS-KEYS** — Allowlist kid-writable settings; never accept `household_pin` or sync watermarks via `POST /api/settings`.
- [ ] **BUG-DELETE-USER** — Cascade `plans` / `activity_events` / decks before `DELETE users`; add a test with a plan + event. (`database/users.py`)
- [ ] **BUG-WRITE-SWITCH** — Flush Writing autosave before `openDocument`. (`Writing.svelte`)
- [ ] **BUG-ACK-EMPTY** — Treat missing `accepted_message_cloud_ids` as “assume all”; treat `[]` as none. (`sync/cloud.py`)
- [ ] **BUG-SCHOOL-OR** — Lock only on the session’s mapped child, not `OR p.user_id`. (`database/school.py`)
- [ ] **BUG-PLAN-PRUNE** — Scope `archive_missing_cloud_plans` per child. (`sync/agent.py`, `database/plans.py`)
- [ ] **BUG-MATH-ACCURACY** — Honor `verify.min_accuracy` on unscoped math tasks. (`database/plans.py`)
- [ ] **SEC-SUDO-ALL** — `rebuild-pi.sh` writes `goji ALL=(ALL) NOPASSWD: ALL`; `setup-pi.sh` does not remove `010-goji-nopasswd`. Delete it at end of rebuild; keep only narrow sudoers.

### P2 — hygiene before a lesson factory

- [ ] **SBP-EFFECTS** — Replace state-writing `$effect`s in School Day player/chip, Tasks `loadUsers`, FractionInput focus. Impure `$derived` in `SchoolTaskChip` (`shownFloor`). `$bindable` without `bind:` on `ErrorDisplay`. Unkeyed `{#each}` on `UserSelector`.
- [ ] **SBP-SPLIT** — Lazy-import Math drills, PdfViewer, Typing games, Coding challenges (App split is intact; those menus re-bundle).
- [ ] **SBP-TIPTAP** — Toolbar `isActive()` needs a transaction subscription; Writing `saveTimeout` on destroy.
- [ ] **SBP-HTML** — Shared HTML sanitizer for Research (and future lesson HTML).
- [ ] **SBP-BOUNDARY** — `<svelte:boundary>` around the lesson player when it lands.
- [ ] **SBP-CLASS** — Migrate leftover `class:` when touching those files.
- [ ] **CI-STATIC** — `svelte-check` + ruff (or ruff-only) + ESLint svelte plugin; keep MyApps flake from being the only red.
- [ ] **SEC-FIREWALL** — Enable `setup-firewall.sh` on real images (human + `HUMAN_CHECKLIST`).
- [ ] **SEC-RESEARCH-HTML** — Sanitize Kiwix HTML even if ZIM is trusted.
- [ ] **SEC-USB-ROOTS** — Browse only live USB mountpoints (`lsblk`/`findmnt`), not all of `/mnt` + `/media`.
- [ ] **SEC-NMCLI-SUDO** — Constrain `goji-wifi-sudoers` to the exact `nmcli`/`rfkill` argv the API uses.
- [ ] **PERF-STATS** — Don’t load every book for `/api/stats` once the library grows.
- [ ] **HYGIENE** — Mixed `os.path`/`pathlib`; `LOG_DIR.mkdir` at import (`config.py`); emoji fonts on Pi (existing P2).

### Already on the product TODO (do not duplicate effort)

E2e smoke (pair → school day → phone), OTA apply, full message center, PDF bookmark seeding, Grok writing loop, placement per-item results, content-generate stub. This audit does not replace those.

---

## 6. Suggested implementation order on `kodi-computer`

1. **PIN + Evince + preview HTML escape + Research SSRF** — small, no product debate, high severity.  
2. **Loopback bind / privileged-route guard** — one architectural choice (escalate; don’t invent).  
3. **Quiz + message profile scope** — needs a SYNC_API sentence if the cache grows a `child_id`.  
4. **Svelte effect cleanups + `?dev=1`** — cheap, unblocks lesson UI work.  
5. **CI `svelte-check`** — so new lessons don’t reintroduce `$effect` loads.  
6. Then lesson player / animation format (`curriculum/ANIMATIONS.md`).

---

## 7. Files touched by the hottest tickets

```
backend/app.py
backend/config.py
backend/routes/system.py
backend/routes/school.py
backend/routes/device.py
backend/routes/wifi.py
backend/routes/users.py
backend/routes/pdf_reader.py
backend/routes/user_apps.py
backend/routes/content.py
backend/database/settings.py
backend/database/content.py
backend/sync/agent.py
frontend/src/App.svelte
frontend/src/lib/SimplePreview.svelte
frontend/src/lib/api/syncedContent.js
frontend/src/components/MessageBanner.svelte
frontend/src/components/Hub.svelte
frontend/src/components/Coding.svelte
frontend/src/components/Research.svelte
```

---

*End of 2026-08-19 Goji computer audit. Next lesson-phase work should treat P0 as blocking.*
