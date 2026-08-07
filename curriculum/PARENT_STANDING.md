# Parent "pillar standing" — metrics spec (planning)

Status: **spec v1** · 2026-08-07 · feeds future parent-app work  
Rule honored: **no new wire invented here** — everything below is either (a) computable from signals that already sync, or (b) explicitly marked *needs engineering* and routed through `goji_cloud/SYNC_API.md` before build.

This is the curriculum-side answer to VISION.md §6: parent opens app → sees, per child, **where they stand in reading, writing, math** — then runs a day from that picture.

---

## 1. The promise, made precise

For each child, each pillar gets a **standing card** with three layers:

| Layer | Question it answers | Freshness |
|-------|---------------------|-----------|
| **Standing** | Which objectives are mastered / in progress / not started, against the grade checklist? | Recomputed on sync |
| **Evidence** | What did they actually do? (drill scores, quiz scores, books, journal entries) | Per event |
| **Trajectory** | At this pace, is the grade-band checklist on track? | Weekly |

The standing layer is only as real as the **objective catalog** — that's why the skills catalog ([`skills/`](./skills/)) and objective success criteria (e.g. `subjects/math/OBJECTIVES.md`) define machine-checkable gates. No catalog entry → no standing claim; the card says "not yet mapped," never a vibes percentage.

---

## 2. What each pillar's standing is computed FROM (today's signals)

Signals that already sync per `SYNC_API.md` / `PARENT_APP_PRODUCT.md`:

### Math — strongest today
- `math.drill` activity events: module, duration, problems attempted/correct, avg time, best streak.
- Parent quiz scores.
- **Mapping rule:** each math objective's success criteria references a drill gate or quiz blueprint (see `subjects/math/quiz-blueprints.md`). Objective is **mastered** when its gate rule is met (e.g. addition ≥ 90% on 20 problems, two sessions on different days); **in progress** when any qualifying session exists; else **not started**.
- Per-module accuracy/minutes/last-practiced already specced for wizard picker (§5.1) — the standing card reuses that aggregation, grouped by objective instead of module.
- *Deferred (already known):* per-times-table mastery needs the device-side operation-column fix noted in SYNC_API.

### Reading — moderate today
- Reading minutes per book (idle-honest), book identity from catalog.
- Word-lookup count (v1 count signal).
- Parent quiz scores — **when the quiz carries `book_id`** (curriculum rule, QUIZZES.md §7).
- **Books read** list: derived from reading sessions per book; "finished" is *needs engineering* (no completion event exists — v1 proxy: cumulative minutes vs book length band, labeled as an estimate).
- **Mapping rule:** comprehension objectives master via book-tied quiz passes; fluency objectives stay evidence-only (minutes + parent observation) until a fluency check exists.

### Writing — weakest today (honest gap)
- Journal entries (word counts, parent read + optional sign-off).
- Typing active minutes (supporting fluency signal, not writing quality).
- **Mapping rule v1:** writing objectives master only by **parent judgment** — the app shows the evidence (entries, word-count trend) and the parent taps "meets the objective." No auto-scoring of writing in v1; do not fake it.

---

## 3. Standing card (per pillar) — v1 content

```
MATH                        ● on track
  Mastered      4 of 7 grade-checklist objectives
  In progress   Tens and ones (obj.math.k2.place-value.02)
                 — mental math 82% avg, last practiced Tue
  Next up       Comparing numbers (needs: tens and ones)
  Evidence      12 drill sessions this month · avg 91% addition
```

- **"Next up"** comes from objective prerequisites — this is what turns standing into a **day plan** (assign the lesson's School Day mapping with one tap; lesson docs already carry that mapping).
- Books read appears on the Reading card (`3 books this year · Treasure Island in progress, ~60%`).
- Writing card leads with the latest journal excerpt + word-count trend and a "review & sign off" action.

## 4. Trajectory — v1 definition (simple, honest)

`objectives mastered ÷ objectives in the grade checklist` vs `fraction of school year elapsed`, per pillar. On track / ahead / behind with plain-language phrasing ("At this pace, Grade 1 math finishes around April"). Child's-pace stance: **behind is information, not an alarm** — copy stays calm, and the grade checklist can be re-banded by the parent (a Grade 1 child working Grade 2 math is *ahead*, not "off plan").

---

## 5. Needs engineering (route via SYNC_API before any build)

| Gap | Why standing wants it | Size |
|-----|----------------------|------|
| Objective catalog on-device / in-cloud (IDs + gate rules) | Standing is computed against it; today catalog lives only in these docs | The real prerequisite — TOOLS.md §6B objective graph store |
| Quiz → objective ID link on the wire | Auto-credit mastery from quiz passes | Small field addition |
| Quiz → `book_id` link | Reading comprehension credit | Already a product TODO |
| Book "finished" signal | Books-read list without minute-estimates | Small |
| Per-table mastery operation column | "÷7 is shaky" granularity | Known, documented in SYNC_API deferred note |
| Parent "meets objective" sign-off event (writing) | Writing standing v1 | Small |

Everything in §3 that doesn't depend on this table can be built from **existing** synced events plus a catalog file shipped to the parent app.

## 6. Explicitly not in v1

- Composite 0–100 "scores" per pillar (false precision; standing is objectives + evidence).
- Auto-graded writing.
- Grok recommendations (rides later on the same standing data — co-pilot, not engine).
- Public/exportable transcripts (later; the data model above already supports it).
