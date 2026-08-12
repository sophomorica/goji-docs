# Module-scoped math tasks — design + build plan

Status: **slice A on main 2026-08-12**. Slice B landing (math.drill events + parent rollup). · Owner: Patrick
Contract: `goji_cloud/SYNC_API.md` → "Math modules" · Product: `PARENT_APP_PRODUCT.md` §5.1

Goal: the parent app assigns **"20 problems of Times Tables at 90%"**, not
"15 minutes of math" — and the child lands in that drill, not the math menu.

---

## 1. Why it's generic today (verified 2026-08-01)

| Layer | File | State |
|-------|------|-------|
| Wire | `goji_cloud/SYNC_API.md` | Only shape is `{"app": "math", "min_duration_s": 900}` |
| Parent app | `goji_learner_app/lib/services/verify_builders.dart` | `VerifyBuilders.math()` emits exactly that; no module arg |
| Parent app | `lib/screens/school_day_wizard_screen.dart` | `_TaskSlotKind.math` → `_pickTimedApp` (minutes sheet only); subtitle hardcoded `'Math · $mins min'` |
| Pi verify | `goji_computer/backend/database/plans.py` `task_is_satisfied` | `app_time` + `app == 'math'` → `max(apps['math'].active_s, summary.math.total_time_ms/1000)`. No module split exists to filter on |
| Pi summary | `backend/database/activity.py` `get_daily_summary` | `summary['math']` is one whole-day rollup; the SQL has no `GROUP BY drill_type` |
| Kiosk launch | `frontend/src/components/TodayPlan.svelte` `openForTask` | `app_time` → `navigateTo(verify.app)` with **no intent** → child lands on the math menu |
| Cloud | `activity_events`, `plan_tasks` | Both generic enough already (`verify_json jsonb`, `subject_type/subject_id/payload`) — **no migration needed** |

The data to do better already exists on the Pi and is thrown away at the
boundary: `math_drill_progress` has a `drill_type` column on every row.

### Modules that exist

Menu (`frontend/src/components/Math.svelte`): Times Tables, Mental Math,
Addition, Subtraction, Division, Word Problems.

**`Fractions.svelte` is built (1241 lines, saves `drill_type: "fractions"`)
but is not on the menu and is unreachable from anywhere in the kiosk.** It is
in the wire registry; wiring the tile is a one-line prerequisite (step 2.0).

`MultiplicationDrill.svelte` is a thin back-compat wrapper around
`ArithmeticDrill operation="multiplication"` — both write
`drill_type: 'multiplication'`. One wire id covers it.

### Two things found in passing

1. **Division per-table stats are computed and thrown away.**
   `ArithmeticDrill.endGame()` aggregates `tableStats` for both
   `multiplication` and `division`, but the write is guarded
   (`ArithmeticDrill.svelte:543`, "only for multiplication — division shares
   tables") so division's are discarded. That guard is *correct* given the
   schema: `multiplication_table_mastery` is `UNIQUE(user_id, table_number)`
   with no operation column (`backend/database/base.py:504-517`), so it can
   physically hold only one operation. Existing rows are **not** polluted.
   Adding an operation dimension is a prerequisite for `decks` and for
   "÷7 is weak" in the parent view — a migration, but not a data cleanup.
2. **Abandoned drills earn nothing.** A row is written only in `endGame()`
   (no `onDestroy` save), so a child who quits mid-drill gets zero credit —
   true today for minutes too, but a problem-count goal makes it more
   visible. Not in scope; flag it if it bites during testing.

---

## 2. Build order

Cross-repo rule 1: the contract lands first. It already has — this plan
implements what `SYNC_API.md` now specifies.

### 2.0 Prerequisite (goji_computer, small)

Wire the Fractions tile into `frontend/src/components/Math.svelte` — four
edits: a Font Awesome icon import (lines 4-12), the `Fractions.svelte` import
(13-17), the `activities` entry `id: "fractions"` (26-68), and the
`{:else if currentView === "fractions"}` branch (90-107). `Fractions.svelte:26`
takes `{ onback }` only, so the branch itself is trivial. Without this a
`fractions` task deep-links to a view that does not exist.

Because the component has never been reachable, it has never been exercised
in use — smoke it by hand before assigning it to a child.

### 2.1 Pi: per-module day summary (goji_computer/backend)

`database/activity.py`:

- `_empty_summary()` → add `'by_module': {}` inside the `math` block.
- `get_daily_summary()` → add a second query beside the existing math rollup:

  ```sql
  SELECT drill_type,
         COUNT(*) AS drills,
         COALESCE(SUM(problems_attempted), 0) AS problems_attempted,
         COALESCE(SUM(problems_correct), 0)   AS problems_correct,
         COALESCE(SUM(total_time_ms), 0)      AS total_time_ms
  FROM math_drill_progress
  WHERE user_id = ? AND completed_at >= ? AND completed_at < ?
  GROUP BY drill_type
  ```

  **Careful:** `get_daily_summary` currently *reassigns*
  `summary['math'] = {...}` wholesale (`activity.py:246-252`), and `math_row`
  is always truthy (a bare `COUNT(*)` always returns a row), so a `by_module`
  key added only in `_empty_summary()` would be dropped on **every** day.
  Edit the reassignment too — add `by_module` to the dict it builds.

  Keep the four existing flat keys unchanged — unscoped tasks and any other
  consumer still read them.

Tests: extend `backend/tests/` day-summary coverage with two drill types in
one day + a day with none (empty dict, not missing key).

### 2.2 Pi: scoped verification (goji_computer/backend)

`database/plans.py` `task_is_satisfied()`, `app_time` branch:

```
modules = [m for m in (verify.get('modules') or []) if m in KNOWN_MODULES]
if app == 'math' and modules:
    by_mod   = (summary.get('math') or {}).get('by_module') or {}
    picked   = [by_mod.get(m) or {} for m in modules]
    drill_s  = sum(int(p.get('total_time_ms') or 0) for p in picked) // 1000
    attempted= sum(int(p.get('problems_attempted') or 0) for p in picked)
    correct  = sum(int(p.get('problems_correct')   or 0) for p in picked)
    # heartbeats are NOT module-attributable — drill data only (contract rule 1)
    ...
else:
    # unchanged: today's max(active_s, drill_s) path
```

**Restructure the early guard first.** `plans.py:124-126` currently reads
`min_s = int(verify.get('min_duration_s') or 0)` then
`if not app or min_s <= 0: return False` — which runs before anything
module-aware and would reject every `min_problems`-only task outright. It has
to become "no app, or neither `min_duration_s` nor `min_problems` > 0 → False".

Rules to encode:

1. `min_duration_s > 0` → `drill_s >= min_duration_s`.
2. `min_problems > 0` → `attempted >= min_problems`, **and** if
   `min_accuracy` is set, `attempted > 0 and correct / attempted >= min_accuracy`.
3. Both set → both must pass.
4. Neither set → `False`.
5. Unknown ids dropped; empty-after-drop → fall through to the unscoped path.
   **Never** return "unsupported task" — that strands the child.

`KNOWN_MODULES` belongs next to the existing `ALLOWED_PLAN_STATUSES`-style
constants, not inline.

Tests: extend the existing `task_is_satisfied` coverage
(`backend/tests/test_plans_device.py:329`, `tests/test_school_day.py`) with
each rule above, the degrade-to-unscoped case, and "40 min of addition does
not satisfy a Times Tables task" — that last one is the whole point of the
feature.

### 2.3 Pi: emit `math.drill` events (goji_computer/backend)

`routes/math.py` `save_progress()` — after `db.save_drill_progress(...)`,
insert an activity event by calling `database/activity.py insert_events`
directly (one event, `synced_at` null so the sync agent picks it up; the
agent uploads unsynced events with no type filter, `sync/agent.py:163-172`).

**This is a new server-side emit path, with no precedent.** Every other app
emits from the *frontend* by POSTing `/api/activity`, and that route enforces
an allowlist — `ALLOWED_EVENT_TYPES` in `backend/routes/activity.py:12-19`,
which does **not** include `math.drill` and is locked in by
`tests/test_activity.py:88 test_unknown_event_type_rejected`. Emitting
server-side sidesteps it (the kiosk already POSTs the drill to
`/api/math/progress`, so a second client round-trip would be redundant). If
you ever route this through `/api/activity` instead, extend
`ALLOWED_EVENT_TYPES` and that test.

**`occurred_at` needs work.** `save_drill_progress` returns only
`cursor.lastrowid` (`database/math.py:8-27`) and `completed_at` is a SQLite
`CURRENT_TIMESTAMP` default (`base.py:497`) formatted `2026-08-01 10:00:00` —
no `T`, no `Z` — whereas every existing `activity_events.occurred_at` is
ISO-8601 with `Z` (`tests/test_activity.py:221`). Either have
`save_drill_progress` accept/return the timestamp, or SELECT it back; either
way normalise the format before writing the event.

Event shape:

```
app='math', event_type='math.drill',
subject_type='math_module', subject_id=<drill_type>,
duration_s=round(total_time_ms / 1000),
payload={problems_attempted, problems_correct, average_time_ms,
         streak_max, difficulty_level},
occurred_at=<row completed_at>
```

Nothing else changes in the sync agent — `/activity-upload` batching, the
50-event cap and the accepted-ids dequeue rule all apply as-is.

### 2.4 Kiosk: deep-link into the drill (goji_computer/frontend)

`components/TodayPlan.svelte` `openForTask()`, `app_time` branch:

```js
if (verify.app === "math" && verify.modules?.length) {
  navigateTo("math", { modules: verify.modules });
  return;
}
```

`components/Math.svelte`:

- `import { consumeAppIntent } from "../lib/stores/navigation"`.
- On mount, consume the intent. **One** known module → set `currentView` to
  its kiosk view id. **Several** → stay on the menu but filter/highlight
  `activities` to those tiles with a line naming the task. Unknown-only →
  plain menu (mirrors the Pi's degrade rule).
- Module id → view id map lives here, one place:
  `multiplication → times-tables`, `mental_math → mental-math`,
  `word_problems → word-problems`, others identity.
- Back from a drill returns to the (filtered) menu, as today.

Tests (`frontend/src/components/__tests__/`): `TodayPlan.test.js` — scoped
task calls `navigateTo` with the intent, unscoped task does not;
`Math.test.js` — single module opens the drill, multi filters the menu,
unknown falls back, and a **manual** later visit is unfiltered (the intent is
one-shot; that was the whole reason `consumeAppIntent` exists).

### 2.5 Cloud (goji_cloud)

**No migration and no function changes** — verified by reading both functions
on 2026-08-01:

- `supabase/functions/plans-pull/index.ts:98` spreads `verify_json` verbatim
  into `verify` and only injects `subject_id` when `catalog_id` is present.
  Unknown keys (`modules`, `min_problems`, `min_accuracy`) pass through
  untouched.
- `supabase/functions/activity-upload/index.ts:64` has **no event-type
  allowlist** — it requires only non-empty `app` / `event_type` /
  `occurred_at`. `math.drill` is accepted as-is.
- `plan_tasks.kind` stays `app_time`, so the `CHECK (kind IN (...))`
  constraint is untouched. This is the main reason the design keeps scoped
  math inside `app_time` rather than introducing a `drill` kind.

Do add both behaviours as contract-test assertions so a future refactor
can't silently start stripping keys.

### 2.6 Parent app: authoring (goji_learner_app)

`lib/services/verify_builders.dart` — replace `math()`:

```dart
static Map<String, dynamic> math({
  List<String> modules = const [],
  int? minDurationS,
  int? minProblems,
  double? minAccuracy,
})
```

Emit `modules` only when non-empty, `min_accuracy` only alongside
`min_problems`. Today's signature is `math({required int minDurationS})`
(`verify_builders.dart:7`), called at `school_day_wizard_screen.dart:171` and
`test/verify_builders_test.dart:8` — `minDurationS:` must keep working once
it becomes optional, so carry-forward of existing plans is untouched. Add a
module-id constant list + display names beside it — one Dart SoT mirroring
the contract table.

`lib/screens/school_day_wizard_screen.dart`:

- `_addTask(_TaskSlotKind.math)` → new sheet replacing `_pickTimedApp`:
  module multi-select, then goal (minutes | problems), then optional accuracy.
- `titleFor` → `"Times Tables · 30 problems"`, `"Times Tables or Mental Math ·
  20 min"`, falling back to `"$mins min math"` when unscoped.
- `_humanSubtitle` `_TaskSlotKind.math` branch → same phrasing from `verify`.
- `_kindFromVerify` (line 122 — not `_kindFor`) needs no change:
  `app == 'math'` still discriminates at line 129. Note line 132 makes `math`
  the catch-all fallback for anything unrecognised, which is worth tightening
  separately but is out of scope here.

### 2.7 Parent app: progress (goji_learner_app)

`lib/services/dashboard_repository.dart` — new query alongside the existing
`activity_events` ones:

```
.from('activity_events')
.select('subject_id, duration_s, payload, occurred_at')
.eq('child_id', childId).eq('event_type', 'math.drill')
```

Aggregate client-side per `subject_id`: minutes, problems attempted/correct →
accuracy, best streak, last practiced. Same client-side-rollup shape the quiz
and lookup signals already use.

Surface it twice:

1. `lib/screens/child_day_detail_screen.dart` — per-module row in the
   always-on activity section (module · minutes · accuracy · last practiced).
2. The wizard module picker — the same numbers inline on each module chip, so
   the parent assigns while looking at where the child is weak. This is the
   answer to "surface the data": the decision point is the picker, not a
   separate progress screen.

Brand tokens per `PARENT_APP_PRODUCT.md` §8 — no new palette for accuracy
states; use seal red / leaf green.

---

## 3. Sequencing

Ship in two landable slices, not one big PR:

**Slice A — assignment works end to end.** 2.0 → 2.1 → 2.2 → 2.4 → 2.5 →
2.6. At the end a parent can assign "30 problems of Times Tables", the child
lands in the drill, and it auto-completes correctly. No new parent-visible
data yet.

**Slice B — progress is visible.** 2.3 → 2.7. Events start flowing, the
parent app aggregates and shows them, wizard chips get their numbers.

B depends on A only for the module registry. A is useful shipped alone; B is
not.

**Later, separately:** give `multiplication_table_mastery` an operation
dimension and a per-session/per-day breakdown (finding 1), then put `decks`
on the wire and add per-table mastery to the parent view.

---

## 4. Open questions for Patrick

1. **Accuracy gate default** — off unless the parent sets it, or a default
   like 80% pre-filled on problem-count tasks? Plan assumes **off**.
2. **Multi-module display on the kiosk** — filter the menu to the named tiles
   (assumed), or show all tiles with the assigned ones badged?
3. **Backfill** — `math.drill` events start at rollout, so per-module history
   begins empty even though `math_drill_progress` has rows going back. Worth
   a one-time backfill emit (bounded to e.g. 30 days), or start clean? Plan
   assumes **start clean**.
4. **Fractions on the menu** — confirm you want it kid-visible now; it is
   built but has never been reachable, so it is effectively untested in use.

---

## 5. Verification notes for whoever builds this

Every file path, symbol and line reference in this doc was checked against
the repos on 2026-08-01 by an independent adversarial pass. Two claims in the
first draft were wrong and are corrected above (the mastery "collision", and
the `insert_events` precedent); the plan's own §2.1/§2.2/§2.3 gotchas came
out of that pass.


- No Flutter SDK in the cloud sandbox — Dart is compile-reviewed only. Run
  `flutter test` locally before calling slice A done.
- `cd goji_computer/backend && python -m pytest tests/` ·
  `cd goji_computer/frontend && npm run test:run` (one known pre-existing
  `MyApps.test.js` flake).
- Deploy steps from the 2026-07-25 audit are still owed and unrelated to this
  work — don't bundle them.
