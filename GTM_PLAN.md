# Goji GTM Plan — v1 (device-only + OTA)

Status: ACTIVE · Owner: Patrick · Created 2026-10-21 · Committed 2026-10-30 (includes sell-now plan v6 and the 10/24 answers)
Audience: any agent (Claude Code, Cursor) working on Goji toward first sale.
**This file is the single source of truth for v1 scope and decisions.** Roadmap cards link here; they don't restate it.
Contracts: `goji-cloud/OTA_CONTRACT.md` (wire/manifest/signing SoT). Device design: `kodi-computer/docs/OTA_DESIGN.md`. Tasks: `kodi-computer/docs/OTA_TASKS.md`.

---

## 1. Decisions (locked — do not relitigate in a PR)

| # | Decision |
|---|---|
| D1 | **v1 ships device-only.** Kiosk runs in offline `stub` sync mode. Parent app, pairing, School Day/Mode, plans, chores, messages are NOT in v1. |
| D2 | **Cloud is used for OTA only** (update manifests, bundles, and an anonymous device heartbeat). **No child data leaves the device in v1.** |
| D3 | **OTA is foundational, not a later feature.** Every unit sold must be updatable and must recover automatically from a bad update. |
| D4 | **No touchscreen in v1.** Buyer supplies HDMI monitor/TV + USB keyboard/mouse. Box: Pi 5 8 GB, 27 W PSU, active cooler, flashed 64 GB SD, micro-HDMI→HDMI cable, Goji Bento case, quickstart card. Pi 5 only (no Pi 4). |
| D5 | **Pre-bake future dependencies into the golden image** (e.g. CUPS for local print) so post-launch features ship as app-level OTA bundles, not OS changes. |
| D6 | **Early buyers are the hardening cohort.** Beta channel is for family/dev units; early buyers get direct support. v2 (parent app + sync) ships after their feedback. |
| D7 | Flexbox Froggy is **cut** from v1 (licence). Done in kodi-computer #76. |
| D8 | **Keys.** Primary ed25519 key on Patrick's Mac, plus an encrypted copy in his end-to-end-encrypted password manager. A **backup key stored separately** (encrypted USB stick), in the device keyring from image 1.0.0 and **pinned**: only a bundle the backup key signs can remove it. A **revocation list** signed by the backup key is fetched and checked on every update check, before any release is trusted. Contract §12.2–12.3. |
| D9 | **CI never signs.** CI builds unsigned bundles; Patrick signs on his Mac (`release/sign_release.py`). |
| D10 | **Channel is read-only on the unit**, set at flash. Changed only by reflash or a signed channel-switch file from us. Contract §12.5. |
| D11 | **Auto-apply, never mid-use.** Download in the background; install at next boot or after 20 min with no input; auto-rollback on a failed health check. In-progress work (journal, notebooks, code) must be autosaved before an install. No parent action required. |
| D12 | **Heartbeat** = random install ID (not serial/MAC), versions, channel, last update result, free disk (full closed list: contract §8.2). Listed in the privacy policy. **Opt-out is on the device in v1** (PIN-gated Settings); it stops heartbeats, never update checks. Contract §12.4. |
| D13 | **Storage:** app bundles on Supabase Storage (verify file-size cap + egress against the measured bundle, task C1); large content (Wikipedia ZIMs) on Cloudflare R2. |
| D14 | **Image 1.0.0 package promise** = everything the app uses today **plus what planned updates need** (CUPS for U2), frozen as the 1.0.0 list. |
| D15 | **Halt = yank + fix forward.** A bad release is pulled by re-pointing the channel; units that installed it stay until a higher `x.y.z+1` ships. No server-driven downgrades. The only backwards move is the device's own automatic rollback after a failed install (contract §1, goji-cloud #9). |
| D16 | **Updater code lives only in `updater/goji_updater/`.** The apply/rollback logic in `backend/sync/ota.py` (kodi-computer #77) is ported by task B5, then B17 deletes `ota.py`. No agent adds a second apply path. |

**Commercial terms (sell-now plan v6, locked):** $400, shipping included · 30-day returns, buyer pays return shipping · "Any HDMI monitor or TV, 1080p recommended" · no paid OTA plan until U3 ships · ex-dogfood units sold as "Refurbished".

**Open (needs Patrick):** the contract heartbeat (§8.2) also sends `hw.model`, `hw.mem_mb`, `uptime_s`, `updater_version`, `schema_version`. Either add them to the privacy policy (recommended) or drop them from the contract.

---

## 2. v1 product (what ships)

Offline kid computer: Reading (+speed reading), Typing, Writing/Notebooks/Journal, Research (offline Wikipedia via Kiwix, `wikipedia_en_all_mini_2026-09` baked in), PDF Reader, Math, Coding (+tutorials), Flashcards (local + USB CSV import), Quotes/dictionary, local profiles.
Plus: setup wizard, optional Wi-Fi, OTA updates, factory reset, log export, heartbeat opt-out.

## 3. Post-launch OTA roadmap (delivered to v1 owners as updates)

- **U1** Better connect-to-internet wizard
- **U2** Local print (CUPS pre-baked per D5/D14)
- **U3** Parent app + device sync — requires the cloud hardening list: device-poll token loss, session expiry, device-register rate limit, multi-child attribution, unpair path, School Mode PIN setup + offline expiry
- **U4** On-device lesson player + curriculum packs (K–12 path). goji-docs #9/#10 are design input for U3/U4, not v1 scope.
- Ongoing: patches, content packs (books, decks, larger ZIMs)

---

## 4. Milestones (exit test = done)

| M | Target | Status (2026-10-30) |
|---|---|---|
| M0 Scope lock | — | Done for v1 purposes (#76). Stale-branch cleanup is housekeeping, not a gate. |
| M1 Updatable device | **Fri 11/20** (was 11/6) | B0 + contract + design merged; ~20 of 27 tasks open. **Tripwire:** if no M1 task merges by Wed 11/4, re-plan. |
| M2 Golden image + first boot | ~12/4 (was 11/20) | Not started |
| M3 Supportability | with M2 | Not started (WS-G) |
| M4 Dogfood | 2+ weeks after M3 | Decide: before or after Christmas |
| M5 GTM | after M4 | — |

### M0 — Scope lock
- SHIP_PLAN.md matches §1–2; Froggy removed; `offline-deps/` matches `backend/requirements.txt`.
- **Exit:** clean main in every repo; SHIP_PLAN == reality.

### M1 — Updatable device (CRITICAL PATH)
- Standalone updater (`updater/goji_updater/`): check → download → verify (keyring, revocation list) → stage → **apply** → health check → **auto-rollback**; boot guard; self-update; USB source; heartbeat client with opt-out.
- Release pipeline (build → sign offline → upload), beta/stable channels, versioned SQLite migrations with backup/restore.
- Cloud: `goji-ota` bucket, `ota-heartbeat` function + tables.
- **Exit:** 3 consecutive updates to a dev Pi, including one deliberately broken release that rolls back unattended and reports the failure; power-cut tests per `OTA_TASKS.md` B18; every §5a item has a contract field/rule and a test vector in `goji-cloud/ota/test-vectors/`.

### M2 — Golden image + first boot
- Reproducible image build (pi-gen or sdm), updater + public keys (primary + backup) baked in.
- First boot: expand FS, per-device SSH host keys / passwords / `.wifi_key` / install ID; **sshd disabled**; egress firewall on.
- Baked content: Kiwix + mini ZIM + `kiwix.service`, books (Gutenberg import), WordNet, Node, USB automount, CUPS.
- Setup wizard: profile → optional Wi-Fi → first update check.
- Fit checks: 64 GB card (OS + content + current & previous release); **active cooler under the 41 mm Bento lid**.
- **Exit:** someone who isn't Patrick flashes, boots, and has a child using it in <10 min with no SSH; Wi-Fi + update check verified on a network that isn't Patrick's.

### M3 — Supportability
- Factory reset (keeps OS + current release; wipes profiles/data after confirm; keeps install ID).
- Log export to USB.
- Heartbeat live + on-device opt-out toggle.
- Consumer reflash doc + recovery SD procedure.
- **Exit:** Patrick can diagnose a unit he has never touched.

### M4 — Dogfood
- 3 units in Patrick's home + 2 friend families, ≥2 weeks, ≥2 OTA releases shipped to them.
- **Exit:** zero bricks, zero SSH sessions, issues triaged into U1+ or patches.

### M5 — GTM
- Landing page, Stripe Payment Link (Patrick creates it; capped), quickstart card, privacy policy (heartbeat fields + opt-out; no child data leaves the device), Virginia sales-tax check, batch-build checklist.
- **Exit:** 5 sold → 20 sold.

---

## 5. M1 architecture constraints

1. **Contract first.** `goji-cloud/OTA_CONTRACT.md` is the SoT for manifest schema, bundle layout, signatures, channels, revocation, heartbeat. Device and pipeline code follow it.
2. **Signing:** ed25519; public keys baked into the image; private keys offline (D8). A compromised bucket must not be able to push code.
3. **Atomic swap:** versioned release dirs + `current` symlink; keep the previous release. Apply runs in the separate `goji-updater` service (D16).
4. **Health check + rollback:** after swap, restart and require a passing health check within a timeout; otherwise swap back, restore DB backup, record failure, report on next heartbeat. Boot-loop protection.
5. **Data safety:** SQLite backup before migrations; forward-only idempotent migrations; restore on rollback; autosave before install (D11).
6. **Self-update** with no window where neither updater can run.
7. **Bundles are app-level.** OS packages are out of scope for bundles (D5/D14). Content packs are a separate bundle type.
8. **Offline-tolerant:** no network → nothing breaks; USB update path as fallback.
9. **Channels:** beta/stable, read-only on device (D10); promotion re-points the stable pointer, no rebuild.
10. **Storage:** D13.

### 5a. Built for scale — frozen at image 1.0.0 (every unit carries this forever)

Cloud-side choices are cheap to change later. Device-side choices baked into 1.0.0 are not.

11. **Staged rollout:** `rollout.percent` + salt, deterministic per device (contract §2.1). Beta → stable 5% → 25% → 100%.
12. **Halt = yank + fix forward** (D15, contract §5).
13. **Upgrade from any version:** stepping-stone releases named in the manifest so a unit months behind still reaches the newest (contract §12.1).
14. **Forward-compatible manifest:** `format`, `schema_version`, unknown fields ignored, `min_updater_version` forces an updater self-update first.
15. **Jittered, server-tunable checks:** 10–20 min after boot, then `check_interval_s` ±10% from the pointer (contract §7).
16. **Versioned heartbeat payload** (`format`) so fields can be added later.
17. **Opt-out on the device in v1** (D12); parent-app toggle comes with U3.
18. **Release health dashboard (cloud, post-M1):** version distribution and rollback rate per release; block promotion if rollback rate exceeds a threshold.
19. **Pinned backup key + revocation list** (D8, contract §12.2–12.3).

---

## 6. Workstreams

| WS | Scope | Repo(s) | Milestone |
|---|---|---|---|
| WS-0 | M0 cleanup, doc fixes, deps alignment | all | M0 |
| WS-A | `OTA_CONTRACT.md` (done: goji-cloud #6, #9, #10) | goji-cloud | M1 |
| WS-B | Standalone updater + backend update routes + migrations + Settings UI + units | kodi-computer | M1 |
| WS-C | Release pipeline: build, sign (offline), verify, publish/promote/yank | kodi-computer `release/` | M1 |
| WS-D | Cloud: `goji-ota` bucket, heartbeat function + tables | goji-cloud | M1/M3 |
| WS-E | Golden image + first boot + content baking | kodi-computer `deployment/` | M2 |
| WS-F | Setup wizard (profile → Wi-Fi → update check) | kodi-computer frontend | M2 |
| WS-G | Factory reset, log export, recovery doc | kodi-computer | M3 |
| WS-H | Security: SSH off, firewall default-on, narrow nmcli sudoers, sanitize Kiwix HTML, School Mode code inert in v1 | kodi-computer | M2 |

Task-level breakdown and dependencies for WS-B/C/D: `kodi-computer/docs/OTA_TASKS.md`.

---

## 7. Rules for agents

- Read this file, your repo's `CLAUDE.md`, and your task spec. Stay inside your task; one task per PR.
- Contracts (`OTA_CONTRACT.md`, `SYNC_API.md`) change first, in their own PR, then code.
- Do not add any path that sends child or profile data to the cloud (D2).
- Do not touch parent-app or sync code except to make it inert in v1; that belongs to U3.
- Every PR: tests for new behavior, updated docs, and a "how I verified" section. Anything needing real hardware is marked **NEEDS-PI**; anything needing Patrick (key ceremony, `supabase db push`, function deploy) is marked **NEEDS-PATRICK**.
- No secrets, signing keys, or real device IPs in git.
- If a decision in §1 blocks you, stop and write the question in the PR — don't decide it.
