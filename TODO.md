# Goji — product TODO / feature list

Workspace-level features and product decisions, spanning all three repos.
Engineering-level TODOs for the device live in `goji_computer/TODO.md`.
Status of the cloud-sync build-out: `goji_computer/docs/CLOUD_SYNC_PLAN.md` §5.

**Parent app product SoT (grilled 2026-07-22):** [`PARENT_APP_PRODUCT.md`](./PARENT_APP_PRODUCT.md) — school-day remote, School Mode, wizard, dashboard, messages, brand. Agents coordinating across repos start there.

## Now — get v1 live (human steps, ~1 evening)

- [x] Supabase project `goji-cloud` live; Phase 1–2 + School Day schema/functions pushed (2026-07-23 — `school_day_sync` migration + edge functions). Remaining human: email auth if not done; see `goji_cloud/HUMAN_CHECKLIST.md`
- [ ] `flutter create` + run `goji_learner_app` on a real phone
- [ ] End-to-end smoke test: pair → wizard/Start on phone → sync → School Mode + Today on Pi → progress/messages/journal on phone
- [ ] Install `goji-sync.service` on the real Pi; firewall `--dry-run` first, live later
- [ ] Create GitHub repos + push `goji_cloud` and `goji_learner_app` (currently local-only — no backup!). Feature branches ready: cloud `feat/school-day-sync-contract`, Pi `feat/school-day-sync`, app `feat/school-day-parent`

## Next — features

- [ ] **School Day v1** (see `PARENT_APP_PRODUCT.md`) — **cloud live**; Pi + Flutter on feature branches (merge + device smoke). Gaps: PDF today’s-work bookmark seeding, full hub message center (banner done), profile-switch PIN during School Mode
- [ ] **Parent → child messages + Goji message center**
  - Decisions locked: one-way text + canned reactions; non-blocking in-lesson banner; near-live via poll; full messenger shelved
  - Cloud live (`messages` + pull/ack/reactions); Pi banner + local cache on `feat/school-day-sync`; full message-center UI still open
- [ ] Parent app **brand parity polish** — family board / wizard / sign-in use seal + wordmark/lockup + tokens end-to-end (`goji_learner_app/BRANDING.md`); keep `assets/brand/` synced with computer masters; Flutter small sizes should use flat-seal variants
- [ ] School Day follow-ups (**ticket, don’t block merge**): un-acked silently-dropped journal/catalog rows → infinite Pi retries; duplicate `local_id` batch 500s; journal family/child refresh on re-claim; wizard draft duplication; PDF page-range clamp
- [ ] Reading quizzes tied to actual books (quiz references a book; completing it can auto-verify a plan task)
- [ ] Lesson-suggestion payloads applying into plans with one parent tap (schema exists; apply path not built)
- [ ] Real LLM content generation (`content-generate` is a stub; Grok path + paywall per product doc; hard revisit ~v1.2)
- [ ] Standing app lock/unlock + child unlock-requests (after school-day loop)
- [ ] Parent app polish pass beyond brand (v1 screens are deliberately ugly functionally)

## Later — pre-sale blockers (each is a real project)

- [ ] OTA apply/install (check + download + signature verify exist; nothing installs yet) + `ota-releases` storage bucket + Ed25519 keypair ceremony (sign the sha256 digest — see `goji_cloud/SYNC_API.md`)
- [ ] Pricing model decision (assumptions in `goji_computer/docs/specs/cloud-sync-product/`)
- [ ] Multi-child / multi-device: cloud schema supports it; Pi still maps everything to local user 1
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
- [x] 2026-07-23 — School Day contract locked (`SYNC_API.md` + privacy schema); cloud migration `school_day_sync` + RPCs/edge functions deployed to live project; Pi + Flutter implementations on feature branches (not merged)

## Brand rollout follow-ups

- [ ] Generate rasterized favicon set from `goji_computer/frontend/src/assets/brand/goji-seal-letters-flat.svg` (16/32/48 favicon.ico, 180 apple-touch, 192/512 PWA) and wire into `index.html`/manifest.
- [ ] Launcher / OS icons for the kid device image: replace placeholder icons with the letters seal (flat variant <48px).
- [ ] Website: adopt `goji-lockup.svg` for the header/banner and the face-seal signature rules from `goji_computer/docs/BRAND.md`.
- [ ] Packaging: produce print-ready (CMYK/vector) files for the lockup and seal from the production SVGs.
- [ ] Decide on Figtree as the shipped UI font (brand prototypes use it) vs current system stack; if adopted, self-host the woff2 (device is offline-first).
- [ ] Flutter launcher icons via flutter_launcher_icons after `flutter create` (see `goji_learner_app/BRANDING.md`).
