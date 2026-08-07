# Goji — product TODO / feature list

Workspace-level features and product decisions, spanning all three repos.
Engineering-level TODOs for the device live in `goji_computer/TODO.md`.
Status of the cloud-sync build-out: `goji_computer/docs/CLOUD_SYNC_PLAN.md` §5.

**Parent app product SoT (grilled 2026-07-22):** [`PARENT_APP_PRODUCT.md`](./PARENT_APP_PRODUCT.md) — school-day remote, School Mode, wizard, dashboard, messages, brand. Agents coordinating across repos start there.

**Owned K–12 curriculum planning (docs only for now):** [`curriculum/README.md`](./curriculum/README.md) — objectives, lesson plans, Claude Design animations, quiz strategy, existing-tools vs tools-to-build. Not a pilot-blocker; advance in planning sessions without blocking School Day e2e.

## Now — get v1 live (human steps, ~1 evening)

- [x] Supabase project `goji-cloud` live; Phase 1–2 + School Day schema/functions pushed (2026-07-23 — `school_day_sync` migration + edge functions). Anonymous auth enabled for credential-free phone app (2026-07-24).
- [ ] `flutter create` + run `goji_learner_app` on a real phone
- [ ] End-to-end smoke test: pair → wizard/Start on phone → sync → School Mode + Today on Pi → progress/messages/journal on phone
- [ ] Install `goji-sync.service` on the real Pi; firewall `--dry-run` first, live later
- [x] GitHub repos created + pushed for all four repos (`goji-docs`, `kodi-computer`, `goji-cloud`, `goji-learner-app`); School Day feature branches all merged to `main` (verified 2026-08-01)
- [ ] **Finish the 2026-07-25 audit deploy** — `sync_hardening` migration is on the live project (verified 2026-08-01) but still owed: re-deploy the 9 audit-edited edge functions **plus new `device-unpair`**; restart Pi backend / `goji-sync.service`; rebuild kiosk (`npm install && npm run build` — picks up `uqr`); `flutter test`. See `SYNC_AUDIT_2026-07-25.md` "Deploy steps"

## Next — features

- [ ] **School Day v1** (see `PARENT_APP_PRODUCT.md`) — **cloud live**; Pi + Flutter **merged to main** and hardened by the 2026-07-25 sync audit; device + phone e2e smoke still open (multi-child "Child" assignment bugs seen on phone). Gaps: PDF today’s-work bookmark seeding, full hub message center (banner done), profile-switch PIN during School Mode
- [ ] **Parent → child messages + Goji message center**
  - Decisions locked: one-way text + canned reactions; non-blocking in-lesson banner; near-live via poll; full messenger shelved
  - Cloud live (`messages` + pull/ack/reactions); Pi banner + local cache on `feat/school-day-sync`; full message-center UI still open
- [ ] Parent app **brand parity polish** — family board / wizard / splash use seal + wordmark/lockup + tokens end-to-end (`goji_learner_app/BRANDING.md`); keep `assets/brand/` synced with computer masters; Flutter small sizes should use flat-seal variants
- [ ] **Sync-audit open issues** (2026-07-25, ranked in `SYNC_AUDIT_2026-07-25.md` §4 — the previously-ticketed follow-ups here were all fixed in that audit): device-poll one-shot token loss can brick pairing; **multi-child attribution** (all uploads land on `devices.child_id` — needs `child_cloud_id` on the wire before multi-child is real); no session expiry (orphaned `pending_start` blocks Start until manual cancel); `device-register` squatting / no rate limit; **anonymous-session loss forks the family** (blocks the two-phones goal — needs invite/recovery code); profile-switch PIN during School Mode; parent `plan_tasks` RLS toggle bypasses completion side-effects; minor board/wizard items (§4.8–9)
- [ ] **Household Tasks board** (grilled 2026-08-01 — product: `PARENT_APP_PRODUCT.md` §10; contract: `goji_cloud/SYNC_API.md` "Household tasks") — standing **per-child** title-only chore board, fully separate from School Mode. Cloud migration + edge functions deployed (`household_tasks`, `household-tasks-pull`, `household-tasks-status-push`); Pi cache/sync + Tasks hub + School Mode allow; parent pair-first shell **Family | Tasks | Content** + avatar Settings. Still owed: e2e smoke on device/phone; follow-ups in §7 (OS push, kid inbox, notes/due/recurrence)
- [ ] **Module-scoped math tasks** — parent assigns "30 problems of Times Tables at 90%", not "15 min math"; child deep-links into that drill; per-module progress surfaces in the wizard picker. Contract landed in `SYNC_API.md` ("Math modules") + `PARENT_APP_PRODUCT.md` §5.1 on 2026-08-01. Build plan: [`MATH_MODULE_TASKS_PLAN.md`](./MATH_MODULE_TASKS_PLAN.md) — slice A (assignment) then slice B (progress)
  - Prereqs found while designing — **both fixed 2026-08-07**: ~~`Fractions.svelte` unreachable from the math menu~~ (tile restored, `12314c3`); ~~`multiplication_table_mastery` missing operation column~~ (`ebaff08` — operation in the UNIQUE key via table-rebuild migration, division per-table stats now persist; unblocks "÷7 is weak" parent views. Device-side done; parent-side wire still rides SYNC_API's deferred note)
- [ ] Reading quizzes tied to actual books (quiz references a book; completing it can auto-verify a plan task)
- [ ] Lesson-suggestion payloads applying into plans with one parent tap (schema exists; apply path not built)
- [ ] Real LLM content generation (`content-generate` is a stub; Grok path + paywall per product doc; hard revisit ~v1.2)
- [ ] Standing app lock/unlock + child unlock-requests (after school-day loop)
- [ ] Parent app polish pass beyond brand (v1 screens are deliberately ugly functionally)

## Curriculum planning (docs in `curriculum/` — not pilot blockers)

Vision SoT: [`curriculum/VISION.md`](./curriculum/VISION.md) (pillars R/W/M, VA skills catalog, parent standing metrics, Gutenberg + Kiwix, Claude Design, Grok co-pilot). Curriculum lead works here with agents.

- [x] 2026-08-05 — Stand up `curriculum/` planning home (VISION, TOOLS inventory, animations/quizzes conventions, subject + band scaffolds, templates)
- [x] 2026-08-05 — Lock north-star vision (three pillars, teach→practice→comprehension, VA skills coverage, parent metrics, offline knowledge stores)
- [x] 2026-08-07 — First pillar strand authored: **math K–2** — 5 objectives (place-value + fluency) + 5 lesson plans (`curriculum/subjects/math/lessons/`); curriculum lead reviews/adjusts, then picks strand #2
- [x] 2026-08-07 — Virginia skills catalog started (`curriculum/skills/`): K/1/2 math + G1/2 English, **verified against fetched VDOE 2023-math / 2024-English documents**, with per-SOL Goji coverage status
- [x] 2026-08-07 — Gutenberg on-device audit (13 books in reader DB) + classic reading lists K–12 (`curriculum/subjects/reading/reading-lists.md`); ingest priorities noted (K–2 shelf thinnest)
- [x] 2026-08-07 — First 3 teaching-animation briefs registered in `curriculum/assets/animations/INDEX.md` (place-value ×2, fluency ×1) — Claude Design generation next
- [ ] Decide on-device animation playback format (see `curriculum/ANIMATIONS.md` §4) — briefs exist; parent-side preview is the interim
- [x] 2026-08-07 — Quiz blueprints for first strand (`subjects/math/quiz-blueprints.md`, `subjects/reading/quiz-blueprints.md` — book-tied via `source_book_id`, already carried by the quiz payload spec)
- [x] 2026-08-07 — Parent “pillar standing” metrics spec (`curriculum/PARENT_STANDING.md`) — computed-from-existing-signals + explicit needs-engineering table; no wire invented
- [ ] Engineering only when docs say so: animation player, lesson sequence, objective-linked items, standing metrics (see `curriculum/TOOLS.md` §6). ~~Fractions tile~~ (restored 2026-08-07, goji_computer `12314c3`)

## Later — pre-sale blockers (each is a real project)

- [ ] OTA apply/install (check + download + signature verify exist; nothing installs yet) + `ota-releases` storage bucket + Ed25519 keypair ceremony (sign the sha256 digest — see `goji_cloud/SYNC_API.md`)
- [ ] Pricing model decision (assumptions in `goji_computer/docs/specs/cloud-sync-product/`)
- [ ] Multi-child / multi-device: cloud schema supports it; since the 2026-07-25 audit the Pi attributes uploads to the device's claimed child (no longer hardcoded user 1), but child B's work on a shared Goji still records as child A's — needs `child_cloud_id` on the wire (see audit §4.2)
- [ ] Kid-facing branding polish beyond hub wordmark (box, website, character naming)
- [x] CodeBox→Goji env rename: `GOJI_*` only, no `CODEBOX_*` fallback (`NAMING.md`; landed on `feat/school-day-sync`)
- [ ] Printed privacy one-pager for the box (draft: `goji_computer/docs/PRIVACY_SYNC_SCHEMA.md`)
- [ ] Image build guard: fail the SD build if `cloud/` or `parent-app/` reappear in goji_computer
- [ ] Goji website (separate track)

## Done (highlights)

- [x] 2026-07-21 — Phase 0: unified activity_events stream (app sessions w/ idle-honest time, reading, research, journal) + daily summary API
- [x] 2026-07-21 — Phase 1 Pi: lesson-plan queue + auto-verify, Today tile, pairing (no secrets in image), sync agent
- [x] 2026-07-22 — goji_learner/ reorg (3 repos), GOJI_* envs, pairing security hardening (register_secret; poll never leaks codes), plan-status-push (self-confirms reach parents)
- [x] 2026-07-22 — Phase 2b: synced decks auto-import to Flashcards, Hub ParentQuizzes, OTA download/verify (streaming sha256 + Ed25519-over-digest), opt-in firewall installer + goji-sync.service
- [x] 2026-07-23 — School Day contract locked (`SYNC_API.md` + privacy schema); cloud migration `school_day_sync` + RPCs/edge functions deployed to live project
- [x] 2026-07-25 — Full Pi↔cloud↔app sync audit: profile-switch stale plans, catalog prune, session/ack hardening, wizard draft duplication, PDF clamp — 33 files fixed (`SYNC_AUDIT_2026-07-25.md`); School Day branches merged to main; kiosk task deep-links (`navigateTo(appId, intent)` → PDF page / book)
- [x] 2026-08-01 — Module-scoped math tasks contract + product spec landed (`SYNC_API.md` "Math modules", `PARENT_APP_PRODUCT.md` §5.1, `MATH_MODULE_TASKS_PLAN.md`); Household Tasks board grilled + docs landed (`PARENT_APP_PRODUCT.md` §10, `SYNC_API.md` "Household tasks")

## Brand rollout follow-ups

- [ ] Generate rasterized favicon set from `goji_computer/frontend/src/assets/brand/goji-seal-letters-flat.svg` (16/32/48 favicon.ico, 180 apple-touch, 192/512 PWA) and wire into `index.html`/manifest.
- [ ] Launcher / OS icons for the kid device image: replace placeholder icons with the letters seal (flat variant <48px).
- [ ] Website: adopt `goji-lockup.svg` for the header/banner and the face-seal signature rules from `goji_computer/docs/BRAND.md`.
- [ ] Packaging: produce print-ready (CMYK/vector) files for the lockup and seal from the production SVGs.
- [ ] Decide on Figtree as the shipped UI font (brand prototypes use it) vs current system stack; if adopted, self-host the woff2 (device is offline-first).
- [ ] Flutter launcher icons via flutter_launcher_icons after `flutter create` (see `goji_learner_app/BRANDING.md`).
