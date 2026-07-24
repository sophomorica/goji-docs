# Parent app — product definition (plan of record)

Status: **agreed 2026-07-22** (grilling session) · Owner: Patrick  
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

Pairing (not the PIN) maps **Goji → family**. The **phone app has no email/password login** — open it and use it. Under the hood the app keeps a silent on-device session so cloud RLS still works; parents never see credentials. Multiple equal parent phones can share that family (join path via pairing / invite — not a sign-in form). One **household PIN** on the device is for release / profile-switch at the box; it does not log anyone into the phone app. A future **web** client may require real login; that stays out of the phone UX.

---

## 3. Household & profiles

- **Children-first** data model (already in cloud schema). Support **many children** (real target: 6) and **shared Goji + optional extra devices**.
- Setup: **pair device → family once**; create/link children in the parent app; sync maps cloud children ↔ local Goji profiles.
- **School Mode is per child.** On a shared box, switching profile during that child’s School Mode requires **PIN or parent Release**.
- Adults: **multiple equal parents** from day one (Start/Release/dashboard/messages). No role matrix in v1.

---

## 4. School Mode (device behavior the app drives)

Hybrid lockdown:

1. Parent finishes wizard and taps **Start school day** for a specific child → device enters School Mode when the command arrives (pending OK in v1).
2. While active: only apps/tasks in that day’s plan are available.
3. Ends when **all tasks are done** (auto-unlock) **or** parent **Release** / **PIN** anytime.
4. Scheduled auto-Start = shelved (v2+ convenience).

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
| Math | Active minutes / challenges |
| Reading | Synced **book catalog** (same idea as PDFs) + minutes |
| Journal | Entry saved (min words); parent can **read**; optional “looks good” sign-off — **not** required to leave School Mode |
| Typing | Active minutes |

### PDF completion (specific)

1. School day **seeds a today’s-work bookmark** for the assigned file/pages.
2. Child opens via that bookmark.
3. **N minutes** in session.
4. Child **self-confirms**.

### Other completion rules

- Quiz: **submitted** (score always visible; pass threshold later if needed).
- Math / reading / typing: **idle-honest active minutes** matching the plan.
- Journal: saved + small minimum word count.

### Carry-forward

**Smart carry-forward:** clone yesterday’s structure; bump PDF ranges from last progress/assignment; keep other slots for light edits.

### Shelved on top of this schema

- AI quiz generation (~v1.2 hard revisit; edge function → Grok → JSON; **paywalled** in product). Hard part = right PDF/book slice, not the JSON pipe.
- Voice → Grok → full school-day JSON (**paywalled**, hands-off) — same structured schema, not a parallel system.
- Auto quiz-from-book; freeform custom tasks (add if needed); reward economy.

---

## 6. Parent app UX surfaces

**Home = family board** (all children as status cards) → tap child for detail.  
Primary action = **Plan today / Start** for that child (not a peer “lifestyle” tab equal to Pair/Plan/Progress/Content).

**Child day detail (dual mode):**

- **Always-on activity** year-round (summer included): e.g. “read 40 min of Alice,” typing minutes, quiz scores, word-lookup **count**.
- When a school day is active or completed that day: **pin the checklist** on top of the same activity.
- Near-live presence: current app / last sync (poll-honest).
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
