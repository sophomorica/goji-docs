# Parent app — product definition (plan of record)

Status: **agreed 2026-07-22** (grilling session) · math tasks §5.1 added 2026-08-01 · Household Tasks §10 + nav chrome §6 added 2026-08-01 · §6 board/child-detail layout amended 2026-08-18 (layout studio pass — see `PARENT_APP_DESIGN_SPEC.md`) · Owner: Patrick  
Workspace home for agents coordinating `goji_learner_app/` ↔ `goji_computer/` ↔ `goji_cloud/`.

This doc is the **product** source of truth for what the Flutter parent app (`goji_parent` in `goji_learner_app/`) is for, what it can do relative to the Goji computer, and what is explicitly deferred. Sync wire shapes still live in `goji_cloud/SYNC_API.md`. Device behavior details live in `goji_computer/docs/CLOUD_SYNC_PLAN.md`.

**Design is non-negotiable.** Parent app UI must use the same Goji brand system as the computer — see §8.

---

## 1. One-line job

The parent app is the family’s **school-day remote + trust dashboard**: run a child’s day without nagging, see real proof of work, message the child, manage the household. It talks to the **family cloud**; the Goji syncs with that cloud. It is not a full CMS and not a second kid UI.

---

## 2. Connection model

| Concern | v1 | Later |
|--------|----|--------|
| Plans, progress, messages, Start/Release | Via family Supabase; Pi polls (minutes OK) | Away-from-home Start/Release in **seconds** (Realtime) |
| UX honesty | Show **pending → active** while waiting on sync | Instant feel |
| At-the-box escape | **Household PIN** on the Goji | unchanged |
| Direct phone ↔ Pi LAN control | Not required | Optional, not the default path |

Pairing (not the PIN) maps **Goji → family**. The **phone app has no email/password login** — open it and use it. Under the hood the app keeps a silent on-device session so cloud RLS still works; parents never see credentials. Multiple equal parent phones can share that family (join path via pairing / invite — not a sign-in form). One **household PIN** on the device is for releasing that child’s School Mode at the box; it does not log anyone into the phone app. A future **web** client may require real login; that stays out of the phone UX.

---

## 3. Household & profiles

- **Children-first** data model (already in cloud schema). Support **many children** (real target: 6) and **shared Goji + optional extra devices**.
- Setup: **pair device → family once**; create/link children in the parent app; sync maps cloud children ↔ local Goji profiles.
- **School Mode is per child.** Each profile is locked only to that child’s plan apps while their school day is open. A sibling who finished (or never started) keeps free play on their own profile — kids may be on different learning paths. Profile switch is allowed so a finished child can play; the parent app should know who is at the box and alert if a child mid-school-day switches onto a finished sibling’s profile (see TODO).
- Adults: **multiple equal parents** from day one (Start/Release/dashboard/messages). No role matrix in v1.

---

## 4. School Mode (device behavior the app drives)

Hybrid lockdown:

1. Parent finishes wizard and taps **Start school day** for a specific child → **that child’s profile** enters School Mode when the command arrives (pending OK in v1). Other profiles stay unlocked.
2. While that child’s day is active: only apps/tasks in **their** plan are available on their profile. (Exception: the **Tasks** hub app — the Household Tasks board, §10 — is always present, like the hub itself. It is informational and never satisfies or blocks a school-day task.) A sibling who already finished deserves play time on their own profile.
3. Ends for that child when **all their tasks are done** (auto-unlock) **or** parent **Release** / **PIN** on that profile.
4. Scheduled auto-Start = shelved (v2+ convenience).
5. **Parent-app follow-up (not v1 device):** during the school day the parent app should know which child is at the box. If a child whose day is still open tries to switch to a profile that already finished, alert the parent — other profiles need to stay open for the kids who earned play time.

**Standing app locks** (after school-day loop is solid — not v1):

- Apply when the child is **not** in School Mode.
- During School Mode, the session wins.
- After School Mode completes, **standing policy remains underneath**.
- Child can tap a locked app → **request access** → parent notification → approve with **timer** or **rest of day**, or open settings and toggle the standing lock. Keep notification grants simple.

**Rewards / fun unlock pool:** shelved for v1; keep a clean post–School Mode free-play state so rewards can plug in later.

---

## 5. School Day wizard (v1)

Always **child-scoped** (from that child’s board card, or pick-child first if a global action).

### Task types in v1

| Task | Notes |
|------|--------|
| PDF lesson | Synced **catalog picker** (names + page metadata). Assigned page range. **No** parent PDF upload. |
| Parent-authored quiz | Prove wizard + device loop; scores on dashboard |
| Math | **Module-scoped.** Parent names which drills count (Times Tables, Mental Math, Addition, Subtraction, Division, Word Problems, Fractions) — one task may list several, any-of. Goal is **minutes or problems solved**, parent's choice, with an optional accuracy gate. Naming no modules keeps the old "any math" behavior. See §5.1. |
| Reading | Synced **book catalog** (same idea as PDFs) + minutes |
| Journal | Entry saved (min words); parent can **read**; optional “looks good” sign-off — **not** required to leave School Mode |
| Typing | Active minutes |

### 5.1 Math tasks — module-scoped (agreed 2026-08-01)

"15 minutes of math" is not an assignment. A math task says **what kind of
math**, and the child lands in that drill instead of the math menu.

- **Which:** any-of list of module ids. One task = one checklist row, even
  when it names two or three modules ("20 min: Times Tables or Mental Math").
  A parent who wants them separately tracked adds separate tasks.
- **How much:** minutes *or* problems solved, chosen per task. Problems is
  the honest unit for drills; minutes stays for open-ended practice.
- **How well (optional):** accuracy gate, valid only with a problem count.
  It never traps the child — Release / PIN work as on any task.
- **On the device:** tapping the task deep-links straight into that drill
  (single module) or into the math menu scoped to the named tiles (several),
  reusing the `navigateTo(appId, intent)` mechanism the PDF/book tasks use.
- **Back-compat:** a task with no modules behaves exactly as today.

**Progress the parent sees:** each completed drill session syncs as a
`math.drill` activity event carrying module, duration, problems attempted /
correct, average time and best streak. The parent app aggregates these into
per-module accuracy, minutes and last-practiced — shown both on child detail
and inline in the wizard's module picker, so assigning work is informed by
where the child is weak. Per-times-table mastery ("7× is shaky") is a
follow-up, blocked on a device-side data fix — see the deferred note in
`goji_cloud/SYNC_API.md`.

Wire shapes and verification rules: `goji_cloud/SYNC_API.md`, "Math modules".

### PDF completion (specific)

1. School day **seeds a today’s-work bookmark** for the assigned file/pages.
2. Child opens via that bookmark.
3. **N minutes** in session.
4. Child **self-confirms**.

### Other completion rules

- Quiz: **submitted** (score always visible; pass threshold later if needed).
- Math: per §5.1 — minutes or problems in the named modules, from drill
  sessions. Reading / typing: **idle-honest active minutes** matching the plan.
- Journal: saved + small minimum word count.

### Carry-forward

**Smart carry-forward:** clone yesterday’s structure; bump PDF ranges from last progress/assignment; keep other slots for light edits.

### Shelved on top of this schema

- AI quiz generation (~v1.2 hard revisit; edge function → Grok → JSON; **paywalled** in product). Hard part = right PDF/book slice, not the JSON pipe.
- Voice → Grok → full school-day JSON (**paywalled**, hands-off) — same structured schema, not a parallel system.
- Auto quiz-from-book; freeform custom tasks (add if needed); reward economy.

---

## 6. Parent app UX surfaces

**App chrome (agreed 2026-08-01 — pair-first shell):**

- **Unpaired** (no family / no claimed device): the app is a **full-screen Pair experience** — no tabs, nothing else to do yet.
- **Paired:** bottom nav = **Family | Tasks | Content**. Family = the board below; Tasks = the Household Tasks bird's-eye + per-child editor (§10); Content = author/manage synced content.
- **Settings via the avatar** in the AppBar — Pair (add another device) and Computer live there, not as top-level tabs.

**Home = family board** (amended 2026-08-18; layout SoT: `PARENT_APP_LAYOUT_STUDIO.html` + `PARENT_APP_DESIGN_SPEC.md` §4.2): glance-first per `PARENT_STANDING_UX.md` §2 — 2-up grid of child cards (day ring + name + ONE status word, **no numbers, no per-card buttons**) → tap child for detail. Per-child primary actions (Plan today / Start / Release) live on **child detail** and in the card **long-press** quick actions, not on the board face. Below the grid, a **“Needs you”** list is the board's single actionable surface: rows derived from synced signals (missed drills, journal awaiting read, drafts ready) — derivation only, no new wire in v1.

**Child day detail (amended 2026-08-18 — hero + tabs, replacing the single pinned-scroll):**

- **Hero:** day ring + name + state chip + ONE primary action (contextual) + ⋯ overflow; then three tabs: **Today | Standing | Activity**.
- **Today** = the checklist when a school day is active or completed that day (the old “pinned checklist”, now a tab that leads).
- **Activity** = the **always-on activity** year-round (summer included): e.g. “read 40 min of Alice,” typing minutes, quiz scores, word-lookup **count**.
- **Standing** = pillar tiles → heat maps per `PARENT_STANDING_UX.md` §3 (glance→tap→evidence unchanged).
- Near-live presence: current app / last sync (poll-honest) — carried in the hero meta line.
- Drill-down matures later (fuller forensic feed optional, not default).

**Quotes (books only):** soft “save a quote?” after book reading — optional, not a wizard hard task; parent-visible on drill-down. Not for PDFs.  
**Word lookups:** v1 = **count signal**; full word list = enhancement.

**Messages (v1):** parent → specific child text; child **canned reactions**; **non-blocking banner** even during a lesson. Near-live delivery. Full messenger app on the Goji = shelved idea.

---

## 7. Explicitly not v1

- Instant away-from-home control  
- Standing app-policy UI (design for it; build after school day)  
- AI / voice planning  
- Reward unlock catalog  
- Full child↔parent chat  
- Parent PDF upload to cloud  
- Required journal sign-off to unlock  
- Weekly schedule templates / timed School Mode windows  
- OS push notifications (incl. “child finished their Tasks board” — in-app signal only in v1)  
- Kid Inbox / message center on the Goji (shared Goji-face alert language; banner only for now)  
- Household-task extras: notes, due dates, recurrence, templates, assign-one-to-many, parent verify gate (optional soft “looks good” is a follow-up, never blocking)  

---

## 8. Design & brand (non-negotiable)

The parent app and the Goji computer must **feel like one product**. Agents working in `goji_learner_app/` must follow the same brand system as the device — do not invent a parallel palette, logo treatment, or “generic Flutter Material” look.

| Source | Role |
|--------|------|
| `goji_computer/PRODUCT_DESIGN.md` | Product design identity (vibe, tokens, seal rules, type) |
| `goji_computer/docs/BRAND.md` | Engineering brand one-pager + asset inventory |
| `goji_computer/frontend/src/assets/brand/` | **Canonical SVG masters** |
| `goji_learner_app/assets/brand/` | App copies of those masters (keep in sync) |
| `goji_learner_app/BRANDING.md` | Flutter-specific wiring (pubspec, launcher icons) |

### Must use

- **Letters seal** (`goji-seal-letters` / `-flat`) for app icon / primary brand mark.
- **Wordmark** / **lockup** for splash / branded headers — product name stays lowercase **goji** in the mark.
- **Face seal** for alive/waiting/pending states (sync pending, waiting on device), matching device semantics: face = working; letters = identity.
- Tokens: seal red `#C6392F`, brand cream `#EFE8DC`, carve cream `#FBF6EE`, ink `#2A211E`, leaf green `#5A7C4C`. Card surface `#FFFDF9` where surfaces are needed.
- Tagline where appropriate: elevating knowledge, one child at a time (see brand docs for casing/tracking on splash-like surfaces).

### Must not

- Red seal on ink backgrounds.
- Recreate the wordmark in a font.
- Drop the leaf or recompose lockups by hand — use `goji-lockup.svg`.
- Ship unbranded default Flutter chrome as the long-term UI; scaffold ugliness is temporary, brand tokens/assets are not optional.

When adding brand files to the app, **copy from the computer’s `assets/brand/`** so the seal stays identical across phone and kiosk.

---

## 9. Cross-repo build order (for agents)

1. Agree contract changes in `goji_cloud/SYNC_API.md` (school-day session, messages, catalogs, journal sync, unlock requests, etc.).
2. Implement cloud + Pi behavior for School Mode / catalogs / verification.
3. Implement parent app surfaces against the contract — **family board first**, wizard second — with brand tokens/assets from §8.
4. Do not put parent-app or cloud code into `goji_computer/` image roots.

Workspace TODO list: `TODO.md`. Device engineering TODOs: `goji_computer/TODO.md`.

---

## 10. Household Tasks board (agreed 2026-08-01)

A standing **per-child chore/task board**, fully separate from School Mode:
it is **audit/info only** and never locks or unlocks the device. Wire shapes:
`goji_cloud/SYNC_API.md`, "Household tasks" — a **new** `household_tasks`
table mirroring the messages sync pattern; do **not** reuse `plan_tasks` or
freeform school tasks for this.

### Locked decisions

- **Standing per-child board.** Tasks are **title-only** (1–120 chars); no
  notes, due dates, recurrence, or multi-assign in v1 (§7).
- **States:** open ↔ done. Either the kid (on the Goji) or the parent (in
  the app) can toggle; last write wins on `updated_at`.
- **Parent can:** create, edit title, delete, reorder, **Clear completed**.
  Completed tasks stay visible on the Goji until the parent clears them.
- **“All done”** (no open tasks left for a child) = an **in-app** bird's-eye
  signal on the Tasks tab / child card — no OS push in v1.
- **On the Goji:** a dedicated **Tasks hub app** — always present, cute
  checklist with the Goji face, open tasks above done, friendly empty state.
  **School Mode exception:** treated like the hub itself — always allowed
  (§4). Profile-scoped: shows the current profile's board only.
- **Offline-first:** local Pi cache (like messages) so a kid can mark done
  offline; the sync agent pushes status opportunistically.

### Parent app surfaces

- **Tasks tab** (§6 chrome): bird's-eye across children (per-child cards
  with open/done counts + all-done state) → tap child for the list editor
  (add / edit / delete / reorder / toggle / Clear completed).

### Follow-ups (documented, not built — see §7)

OS push on board completion · kid Inbox/message center · notes, due dates,
recurrence, templates, assign-one-to-many · optional soft parent “looks good”.

### Build order (cross-repo, after the contract)

1. Cloud: migration + RLS (parent CRUD via PostgREST) + `household-tasks-pull`
   / `household-tasks-status-push` edge functions (copy structure from
   `messages-pull` / `plan-status-push`).
2. Pi: local cache table + sync agent hooks + Tasks hub app; School Mode
   allow-list + Hub tile filter exception.
3. App: pair-first shell + nav (§6), Settings screen (Pair + Computer),
   Tasks tab + editor; repository against the Supabase table.
4. Tests: cloud RLS/idempotency; Pi cache merge, school-mode allow, toggle
   push; Flutter nav gate + repository units.
