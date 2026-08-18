# Parent app — design spec for the redesign passes

Status: **spec v1** · 2026-08-18 · derived from `PARENT_APP_LAYOUT_STUDIO.html` (visual SoT — open it in a browser and use the zoom view; every screen below maps to a numbered frame in it)
Companions: `PARENT_STANDING_UX.md` (standing/glance rules), `PARENT_APP_PRODUCT.md` §8 (brand, non-negotiable), `goji_learner_app/BRANDING.md` (asset wiring).

**Audience:** an implementing agent working in `goji_learner_app/`. This spec is written to be executed in **two passes** (§9). Do not redesign beyond it; where it is silent, keep current behavior.

---

## 1. What this is (and is not)

The studio HTML is a click-through mockup of 12 redesigned screens plus a tokens page. It settles **layout and visual language**. This spec translates it into Flutter terms against the real codebase (`lib/` file map in §8).

Not in scope: new sync contract work, the games/reward toggle, math-module task internals, and anything touching `goji_cloud/` or `goji_computer/`. If a screen needs data the app doesn't consume yet, build the surface against a clearly-marked stub (§7) — do not invent contract changes.

---

## 2. Design language — "crafted & warm"

The app should feel like the Goji device family: warm paper, carved seal, calm color. Current build reads as default Material on cream; the target reads as a crafted object.

### 2.1 Color tokens (locked — `lib/theme/goji_colors.dart`)

Use `GojiColors` exclusively. **Never invent a hue.** The studio introduced no new colors; everything below is composition of existing tokens.

| Token | Value | Role |
|---|---|---|
| `sealRed` | `#C6392F` | one primary action per screen; attention; active nav stamp |
| `brandCream` | `#EFE8DC` | scaffold background ("paper") |
| `carveCream` | `#FBF6EE` | recessed/flat surfaces, nav bar |
| `card` | `#FFFDF9` | raised cards |
| `ink` | `#2A211E` | text; alpha steps .70/.55/.40 for hierarchy, .10/.16 for hairlines |
| `leaf` | `#5A7C4C` | positive/sync/progress |
| `stateMastered/Developing/Struggling/NotStarted` | see file | standing states only |

### 2.2 Type system (new — create `lib/theme/goji_type.dart`)

Two families:

- **Display serif** — screen titles, child names, sheet titles, big numerals in rings. The studio uses Iowan Old Style/Palatino; in Flutter, bundle an OFL serif (recommend **Source Serif 4**, weights 400/600) under `assets/fonts/` and register as `GojiSerif`. Do NOT use the serif for the wordmark (brand rule: never recreate the wordmark in a font — always `goji-lockup.svg`). *(Decided 2026-08-18: serif is adopted now.)*
- **Sans** — everything else. Keep platform default (SF/Roboto) for these passes. The shipped-sans decision (**Figtree vs system stack**, `TODO.md` §Brand rollout) is **still open** — do not bundle a sans; if Figtree is later adopted, only the sans family token changes.

Scale (logical px, from the studio):

| Style | Spec |
|---|---|
| `display` | serif 600, 28/1.12, letter-spacing −0.3 |
| `heroName` | serif 600, 26 |
| `screenTitle` (app bar) | serif 600, 19 |
| `cardTitle` | serif 600, 15–16 (kid names, strand headers, pillar names, swatch labels) |
| `rowTitle` | sans 600, 14.5 |
| `body` | sans 400, 13.5–14, ink70 |
| `meta` | sans 400, 12.5, ink55 |
| `sectionLabel` | sans 700, 11.5, tracking +1.3, UPPERCASE, ink55 |
| `chipLabel` | sans 600, 10.5, tracking +0.6, UPPERCASE |

### 2.3 Surfaces, depth, corners

- Cards: `card` fill, 1 px hairline `ink@.10`, radius **15** (kid cards and pair choices: **19**), and a soft two-layer shadow: `(0,1,2, ink@.06)` + `(0,4,14, ink@.05)`. Implement once as `GojiCard` (§5) — stop using bare `Card`/theme elevation.
- Flat/recessed panels (`.flat` in studio): `carveCream@.80`, hairline `ink@.06`, no shadow.
- Hover/press states: cards that navigate get a pressed scale ~0.98 or 2 px translate — pick one and use it everywhere.
- The studio's organic uneven radii, SVG wobble filters, and paper-grain overlay are **HTML-only texture. Do not port them** (cost/benefit is wrong in Flutter). The craft translation is: serif display + section markers + stamped active states + the shadow recipe above. Optional Pass-2 polish: a very-low-opacity noise texture asset behind the scaffold — only if it costs nothing at 60 fps on the low-end target.

### 2.4 Signature details (these carry the redesign — all cheap, all required)

1. **Red-square section marker.** Every section label is preceded by a 7×7 `sealRed` square rotated −4°. One widget: `SectionLabel(text)`. Replaces every ad-hoc `Text('...')` header.
2. **Stamped active nav.** Active bottom-nav icon sits in a `sealRed` rounded-rect (radius 9) rotated −2°, `carveCream` glyph. Inactive: ink55, no container. (Custom `indicator` work in `NavigationBar` theme or a custom bar — agent's choice, visual result is the contract.)
3. **Letterpressed primary button.** `FilledButton` restyled: vertical gradient `#CE4136→#BE352B`, radius 12, subtle inner top highlight, text with 1 px dark shadow. One primary per screen — audit every screen against this (§6).
4. **Day ring** everywhere a child appears (§5.1), replacing avatar-only circles.
5. **Seal semantics** (locked): **face** seal = alive/waiting/pending (sync banners, message pending, board banner); **letters** seal = identity/brand (app icon, settings device card). Never red seal on ink backgrounds.

---

## 3. Global structure changes

- Shell (`home_shell.dart`) keeps pair-gate → `Family | Tasks | Content` tabs and avatar→Settings. Only its visual chrome changes (nav stamp, serif app-bar titles via theme).
- App bar: brand lockup (`goji-lockup.svg`) on the three root tabs; back-arrow + serif title on pushed screens. Sync status is a **chip** (leaf dot + "Goji synced 2 min ago"), never a banner, except the face-seal "waiting on the Goji" card which is a `GojiBanner`.
- Screen titles use the display serif; date lines like "Tuesday / August 18" use `display` + `body`.

---

## 4. Screen-by-screen (studio frame → target file → changes → acceptance)

### 4.1 Pair gate — studio #1 → `pair_device_screen.dart` + gate in `home_shell.dart`

**Change:** branch on intent before any input. Two large choice cards: "I have a Goji to set up" (primary-tinted, grid glyph) and "Someone already set ours up" (letters seal glyph, invite-code copy incl. "Don't reset the Goji"). Below, a single "or enter the code by hand" section: one 6-char field + `Pair` button + helper line. The 8-char invite path lives **behind** the second choice, on its own screen/sheet — never two code fields on one scroll. Footer: face-seal banner "Nothing to sign in to…".
**Accept:** exactly one visible code field at a time; both paths reachable in ≤2 taps; QR scan entry (`scan_pairing_screen.dart`) hangs off choice 1.

### 4.2 Family board — studio #2 → `family_board_screen.dart` (retire `child_status_card.dart` in favor of `KidCard`)

**Change:** glance-first. Header: serif weekday + date + sync chip. Then a **2-column grid** of `KidCard`s: day ring (with initial), name (serif), grade (meta), **one status word/phrase** (e.g. "Day finished" leaf, "Halfway", "Struggling in math" red, "Draft ready", "Not started"). Max ONE attention dot per card, riding the ring's top-right. Dashed "Add child" tile ends the grid. Optional face-seal `GojiBanner` when a day is waiting on the device. Then `SectionLabel('Needs you')` — the **only actionable list**: small-ring rows, one line of what + one line of the action, chevron. Card order: attention first, then grade. Long-press card → quick actions (Start day, Message, Pause games — last one may be a disabled slot).
**Hard rules (PARENT_STANDING_UX §2):** **no numbers on the board**, no per-card button stacks, six children fit without scrolling on a 390×800 viewport.
**Accept:** a six-child board shows zero digits and zero buttons above "Needs you"; every action reachable from the board lives in Needs-you or long-press.

### 4.3 Child detail — studio #3 → `child_day_detail_screen.dart`

**Change:** the nine stacked sections become **hero + action bar + three tabs**.
Hero: large day ring, serif name, meta line ("Kindergarten · at the Goji now"), one state chip ("● School day active", leaf). Action bar: `Message` (ghost) + ONE primary (contextual: `Release day` / `Start day` / `Review draft`) + `⋯` overflow holding everything else that's currently a button.
Tabs (segmented control, `card` active pill): **Today** — "Today's plan · 3 of 5 done" section, task rows (tick, title, meta, kind chip, thin leaf progress bar when partial), quiet "Edit today's plan". **Standing** — three `PillarTile`s (reuse/restyle `pillar_standing_tiles.dart`: serif pillar name, 4-state mini coverage bar, count, trajectory word), state legend (glyph + color, all four), then "Waiting for you" rows (journal to read, browse lessons). **Activity** — grouped Today/Yesterday rows with right-aligned serif timestamps.
**Accept:** exactly one `sealRed` button visible; no vertical scroll longer than ~2 screens per tab with seed data; all previously-reachable functions still reachable (count them before refactor, verify after).

### 4.4 Skill heat map — studio #4 → `pillar_heatmap_screen.dart`

**Change (additive):** keep grid + glyph-plus-color cells. Add: grade-band segmented control at top (K–2 / 3–5 / 6–8 per `standing/grade_band.dart`); a summary card ("17 skills mapped / 5 mastered · 3 developing · 2 struggling") with a small completion ring; per-strand header = serif strand name + *italic status word* right-aligned ("2 struggling" / "on track" / "not started"). Cells 44 px, radius 10; not-started cells are dashed-outline, near-transparent.
**Accept:** grid skimmable without tapping — every strand states its status in words; glyphs (■ ◪ ! □) present on every cell.

### 4.5 Evidence sheet — studio #5 → sheet within `pillar_heatmap_screen.dart`

**Change:** bottom sheet (radius 26 top, grab handle), does NOT navigate away. Order: state chip (glyph+color) → objective in plain language (serif, 19) → evidence method line → **diagnostic finding first** in a flat panel ("The misses are digit swaps — … Not a comparison problem, a place-value one."), then the last 2–3 evidence rows → primary `Assign practice` (wired to `lesson_assign_service.dart` mapping) → quiet `Not now`.
**Accept:** diagnosis is the first prose a parent reads; one primary; dismissing restores the untouched grid.

### 4.6 Plan wizard — studio #6 → `school_day_wizard_screen.dart`

**Change:** two steps with a step indicator (`1 Build the day — 2 Review & start`; active step number is a red stamp). Step 1: optional carried-forward notice (flat panel, letters seal), reorderable task rows (drag handle, remove ✕), a single **`+ Add a task`** ghost button (replaces the six type chips), then `SectionLabel('Suggested from Eli's road')` rows with one-tap add — sourced per PARENT_STANDING_UX §4 (one win + one stretch from weakest developing cells; never struggling-only). Actions (`Save draft` ghost / `Review & start` primary) live in a **pinned bottom bar**; errors surface next to the field that caused them, not at scroll-bottom.
**Accept:** no add-type chips on the main scroll; actions always visible without scrolling; suggestions appear when standing data exists (stub per §7 otherwise).

### 4.7 Add-task type sheet — studio #7 → new `widgets/add_task_type_sheet.dart`

**Change:** bottom sheet listing task types as rows (kind chip + name + availability line): Math drill, Reading ("From the book catalog · 8 books synced"), Journal, Typing, PDF ("3 PDFs synced from the Goji"), Quiz. Types with an empty catalog render at 45% opacity with the reason ("No quizzes yet — write one under Content") — **visible and explained, not tappable-then-snackbar**. Selecting a row opens the existing leaf flows (`math_task_sheet.dart`, `book_picker_sheet.dart`, `minutes_sheet.dart`, `pdf_assignment_sheet.dart`, `count_picker_sheet.dart`). Order rows by real usage frequency, math first.
**Preserve:** the per-module rollup stats (accuracy, minutes, last-practiced) on the module-picker chips **inside** `math_task_sheet.dart` — landed 2026-08-12 (`b5f4373`, PARENT_APP_PRODUCT §5.1, MATH_MODULE_TASKS_PLAN §4). The type sheet replaces the outer add-type chips row only; the informed module picker is a product requirement, not decoration.
**Accept:** availability counts are live from the repositories; a dead-end tap is impossible; module chips still show their numbers.

### 4.8 Household tasks board — studio #8 → `tasks_board_screen.dart`

**Change:** subtitle line ("Chores, not school work. Kids check them off on the Goji."). Per-child rows: small ring (fraction of tasks done), name, one status line ("All done" leaf+face seal / "2 of 3 done" / "No tasks yet" + inline `Add` ghost button). Counts are fine here — the no-numbers rule is family-board-only.
**Cut from the studio frame (decided 2026-08-18):** the "Quick add to everyone" composer is **not built** — it is the assign-one-to-many explicitly deferred by PARENT_APP_PRODUCT §7/§10. The studio keeps it as a later idea only; do not implement it in either pass.
**Accept:** a child with zero tasks gets an inline add without navigation; adds remain strictly per-child via `household_tasks_repository.dart`.

### 4.9 Child task list — studio #9 → `child_tasks_screen.dart`

**Change:** one tap target per row — checkbox + title + drag handle only. Tap row body → rename (inline or sheet); swipe → delete; no per-row edit/delete icons. Real `Open · n` / `Done · n` section headers; `Clear completed` sits with the Done header (never appears/disappears from the app bar). Add-field pinned to bottom composer. Done rows show origin meta ("Checked off on the Goji · 8:15am").
**Accept:** row has ≤2 interactive zones (check, drag) besides the row-tap; list never blocks on a row action.

### 4.10 Messages — studio #10 → `messages_screen.dart`

**Change:** day separators (hairline-flanked uppercase labels); per-message delivery meta ("delivered 4:02pm"); child reactions rendered as a small pill under the message they belong to; pending state = **face seal + "waiting for the Goji to check in"** in the meta line, never a layout-shifting banner. Composer pinned bottom; bubbles right-aligned `card` with 18/18/5/18 radii.
**Accept:** composer never moves when delivery state changes; every bubble has a time or a pending mark.

### 4.11 Content library — studio #11 → `author_content_screen.dart`

**Change:** the tab becomes a **library**: filter segmented control (All / Quizzes / Cards / Ideas), item rows (kind chip, title, meta: "6 questions · for Eli · used Friday" / "never used", chevron → view/edit/delete). Letters-seal banner: "Everything here syncs to the Goji the next time it checks in." Authoring moves behind one pinned primary: `Write something new`.
**Accept:** every authored item is listed, openable, editable, deletable; creating still works end-to-end.

### 4.12 Settings — studio #12 → `settings_screen.dart` (+ `computer_settings_screen.dart` content folds in)

**Change:** "Your Goji" device **card** (letters seal, name, "Checked in 2 minutes ago · 5 children", chevron → device detail) + `Pair another Goji` ghost. "Parents" group: invite-another-parent row, this-phone row. "Children" group: per-child rows (ring, name, grade · current book, chevron → manage) + add-child row — child management moves here from the board dialog. "About" group: Help, Version.
**Accept:** no duplicate rows describing the same device; add/rename/manage child reachable from Settings.

### 4.13 Theme/tokens — studio #13 → `theme/` (`goji_theme.dart`, new `goji_type.dart`, new `widgets/goji_surfaces.dart`)

Codify §2 so screens compose, not restyle: `GojiCard`, `SectionLabel`, `DayRing`, `AttentionDot`, `SyncChip`, `GojiBanner`, `KindChip`, `StateChip`, button styles, tab/segmented styles, nav stamp. The studio's tokens frame is the reference rendering.

---

## 5. Component contracts (build once, in Pass 1)

### 5.1 `DayRing({double progress, Color color, double size, Widget center, AttentionDot? dot})`
Conic progress ring, 5 px track inset, `card` center disc with a faint inner shadow, serif center content (initial or %). Sizes: 44 / 64 / 86. Track: `stateNotStarted`. Progress color: `leaf` normally; may be `stateDeveloping` when the day is stalled. Dot: 14 px, 2.5 px `card` border, top-right, red (struggle) or amber (needs parent action), **max one**.

### 5.2 `SectionLabel(String)` — §2.4-1. Also used inside sheets and tabs.

### 5.3 `GojiCard` / `GojiFlat` — §2.3 recipes; `GojiCard.pressable` adds the press effect + `onTap`.

### 5.4 `StateChip(state)` — glyph + word + tinted pill. Glyph mapping is already in `pillar_standing_tiles.dart` (`stateIcon`); reuse it. Color **never** carries state alone, anywhere.

### 5.5 `GojiBanner({seal, child, alert})` — flat leaf-tinted (or red-tinted `alert`) panel, 26 px seal, body text. Face seal for waiting/alive, letters for identity/info.

### 5.6 `SyncChip({synced, when})` — leaf/red dot + short text, pill, meta type.

---

## 6. Non-negotiables (audit list — run after each pass)

1. Brand: tokens from `goji_colors.dart` only; lockup/seal from `assets/brand/` SVGs; no wordmark-in-font; no red seal on ink; no default-Material look surviving on touched screens.
2. **One `sealRed` primary per screen.** Everything else ghost/quiet/overflow.
3. **No numbers on the family board.** Words and rings only.
4. Standing states always glyph+color (■ ◪ ! □). Red appears only on genuine struggle signals.
5. Seal semantics: face = waiting/working, letters = identity.
6. Six-child K–8 family is the stress case: board glanceable in 2 s, no layout breakage.
7. Copy tone: plain, warm, no exclamation-mark cheer ("It checks in every few minutes — nothing for you to do.").

## 7. Data dependencies & permitted stubs

| Surface | Needs | If absent |
|---|---|---|
| Needs-you list | derivations from synced signals (missed drills, unread journal) | derive what's derivable from `dashboard_repository.dart`/`standing_computer.dart`; stub the rest behind a single `NeedsYouRepository` with `// STUB:` markers |
| Status words on board | day session state + standing | map from existing `ChildBoardItem`; "Struggling in <pillar>" only from real struggle flags |
| Wizard suggestions | weakest developing cells | `standing_computer.dart` output; if catalog absent for grade, hide section |
| Type-sheet availability | catalog counts | live counts from repositories (books, PDFs, quizzes) — this one may NOT be stubbed |
| Message delivery/reactions | sync contract fields | if not yet synced, show "waiting for the Goji to check in" state only; no fake timestamps |

Never render invented data as real. Stubs must be visibly seeded or clearly derived.

## 8. File map

| Studio frame | Files touched |
|---|---|
| tokens/type/components | `theme/goji_theme.dart`, new `theme/goji_type.dart`, new `widgets/goji_surfaces.dart`, new `widgets/day_ring.dart` |
| 1 Pair gate | `screens/pair_device_screen.dart`, `screens/home_shell.dart`, `screens/scan_pairing_screen.dart` |
| 2 Family board | `screens/family_board_screen.dart`, retire `widgets/child_status_card.dart` → new `widgets/kid_card.dart`, new `widgets/needs_you_row.dart` |
| 3 Child detail | `screens/child_day_detail_screen.dart`, `widgets/pillar_standing_tiles.dart`, `widgets/task_progress.dart` |
| 4–5 Heat map + evidence | `screens/pillar_heatmap_screen.dart` |
| 6–7 Wizard + type sheet | `screens/school_day_wizard_screen.dart`, new `widgets/add_task_type_sheet.dart`, existing leaf sheets |
| 8–9 Tasks | `screens/tasks_board_screen.dart`, `screens/child_tasks_screen.dart` |
| 10 Messages | `screens/messages_screen.dart` |
| 11 Content | `screens/author_content_screen.dart` |
| 12 Settings | `screens/settings_screen.dart`, `screens/computer_settings_screen.dart` |

## 9. Pass plan

**Pass 1 — foundation + the two screens that matter (§9 build order in PARENT_APP_PRODUCT: family board first, wizard second):**
1. Theme/type/components (§2, §5) — including font bundling.
2. Family board (4.2) + shell chrome (§3, nav stamp).
3. Child detail (4.3).
4. Plan wizard + type sheet (4.6, 4.7).

**Pass 2 — the rest + polish:**
5. Pair gate (4.1), heat map + evidence sheet (4.4, 4.5).
6. Tasks board + child tasks (4.8, 4.9), Messages (4.10), Content library (4.11), Settings (4.12).
7. Polish sweep: press states, transitions (fade-through between tabs, sheet springs), §6 audit, optional grain.

**Per-pass verification (required):**
- `flutter analyze` clean; existing tests in `test/` pass; add/adjust widget tests for: pair-gate branching, board shows-no-numbers, one-primary audit helpers where practical.
- Run on a 390×844 viewport with a seeded six-child family; screenshot each touched screen and compare against the corresponding studio frame (layout parity, not pixel parity).
- Grep audit: no raw `Color(0xFF...)` outside `theme/`, no `Icons.` glyph carrying a standing state without its shape pairing.

---

*Where studio and this spec disagree, the studio wins on layout; this spec wins on Flutter translation (§2.3 explicitly drops wobble/grain/organic radii) **and on scope cuts (§4.8 quick-add)**. Where both are silent, current app behavior wins.*

## 10. Doc consolidation (2026-08-18)

This spec was reconciled against the workspace SoT docs on 2026-08-18:

- `PARENT_APP_PRODUCT.md` §6 was **amended** the same day to match this spec: board primary action moved off the card (long-press + Needs-you), child detail restated as hero + Today | Standing | Activity tabs, "Needs you" recorded as a product surface. If §6 and this spec ever disagree again, §6 wins — update it first (CLAUDE.md rule 8).
- `PARENT_STANDING_UX.md` §3's "checklist pinned above the activity feed" single-surface layout is superseded by the tabbed child detail (noted in that file). Its glance→tap→evidence rules, §1 color system, §2 board rules, and §4 wizard mode are untouched and still bind this spec.
- Household quick-add-to-everyone: cut (see §4.8). Fonts: serif adopted; sans decision stays open in `TODO.md` §Brand rollout.
