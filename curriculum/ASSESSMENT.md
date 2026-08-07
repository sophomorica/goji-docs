# Placement assessment — establishing the starting point

Status: **spec v1** · 2026-08-07 · owner-directed ("we need a way to establish where the child is in each domain so the parent has a starting point")

The third assessment layer from PRACTICES.md §7. A new family adds a child, sets a grade, and runs **placement day** — a short battery per pillar that seeds the heat map so the parent's very first view of "where they stand" is real, not blank.

---

## 1. Design principles

1. **Short.** A placement battery is ≤ 20 minutes per pillar. Children shouldn't meet the Goji as an exam machine.
2. **Sample the gates, not everything.** Each band's placement quiz samples its **key skills** (the ones with hard gates) at 2 items each — enough to place, not to certify every cell.
3. **Diagnostic, as always.** Wrong answers use the same named-misconception distractors, so even a miss teaches the parent *what kind* of miss.
4. **Step, don't trap.** Start at the grade the parent set. Score ≥ 80% → offer the next band's quiz ("they may be ahead"). Score ≤ 40% → offer the band below, framed as "let's find their footing," never as failure. Child's-pace stance: bands describe skills, not children.
5. **Placement states are provisional.** Results seed cells as **placed-mastered / developing / struggling** with provenance `placement` visible on the evidence sheet ("from placement day — daily work will confirm"). Real gates (two-day rules, drill accuracy) later overwrite placement provenance. The heat map never lies about how it knows.

## 2. The battery (per pillar × band)

| Pillar | Placement instruments | Time |
|--------|----------------------|------|
| **Math** | Placement quiz (10–12 items across the band's strands) + two 5-problem micro-drills (device drills at low count — accuracy signal without a grind) | ~15 min |
| **Reading** | Placement quiz (phonics/word items + a short passage with comprehension items, K–5; passage-based at 6–12) + one read-aloud minute judged by parent (K–5) | ~15 min |
| **Writing** | One short prompt (band-appropriate) + parent judgment against a 3-point checklist (sentence completeness / organization / mechanics); grammar quiz items ride the reading placement | ~10 min |

Delivery today: **parent quizzes + drill assignments** — zero new device features. Sequencing: one pillar per day across three days beats one marathon.

## 3. Scoring → heat-map seeding

Per sampled skill (2 items): 2/2 → `placed-mastered` · 1/2 → `developing` · 0/2 → `struggling` (with the distractor's misconception noted). Unsampled skills in the band stay `not started` — placement claims nothing it didn't test. Band recommendation (step up/down) is advisory copy for the parent, never automatic.

## 4. Parent-app flow (build later; spec now)

Add child → set grade → card: **"Find their starting point"** → generates the 3-day placement plan (pre-filled School Days) → results populate the heat map with `placement` provenance → wizard's "from their road" mode suggests the first real week. Re-placement available anytime (start of year, after a break).

## 5. Blueprints

Placement quizzes live in [`assessment/`](./assessment/), one file per pillar × band: `placement.<pillar>.<band>.md` — same YAML + gold-item format as all quiz blueprints. Authored so far:

| File | Status |
|------|--------|
| [`placement.math.k2.md`](./assessment/placement.math.k2.md) | authored |
| [`placement.reading.k2.md`](./assessment/placement.reading.k2.md) | authored |
| Remaining pillars × bands | authored as each band's catalog + objectives land (PRACTICES §4 keeps this table honest) |

## 6. Engineering notes (routed, not invented)

- Quiz payloads already carry everything needed; a `placement: true` + `skill_map` metadata field on synced quiz content is the only wire addition worth proposing in SYNC_API (lets the app auto-seed cells instead of the parent reading scores).
- Micro-drill placement uses existing math drills at problem-count 5 — module-scoped tasks (in plan) make this assignable precisely.
- The placement plan generator is deterministic from the catalog — no AI required; Grok phrasing help is optional garnish later.
