# Virginia skills catalog — coverage checklist

Status: **started 2026-08-07** · K–2 math + Grades 1–2 English verified  
This is the coverage checklist from VISION.md §5: for each grade × pillar, the finite list of skills Virginia expects, and **what on Goji covers each one**.

**Provenance:** every SOL code and statement in these files was verified against fetched official VDOE documents (2023 Mathematics SOLs; 2024 English SOLs — "Understanding the Standards" grade docs), not written from memory. Source URLs are noted per file. When VDOE revises standards, re-verify before editing.

## Coverage statuses

| Status | Meaning |
|--------|---------|
| **covered** | A Goji objective + lesson + check exists (IDs linked) |
| **partial** | Goji objective covers a subset; gap described |
| **planned** | Objective IDs assigned, lessons not yet authored |
| **gap** | Nothing on Goji yet — candidate for next strand or TOOLS.md backlog |
| **off-device** | Deliberately parent-led / physical (e.g. handwriting, measuring real objects); Goji may hold the record, not the activity |

Rule from the vision: every skill ends up covered by **some combination** of animation, lesson, practice tool, quiz, book — or an explicit gap row. No silent omissions.

## Files

| File | Scope |
|------|-------|
| [`math-k.md`](./math-k.md) | Kindergarten math (2023 SOLs) |
| [`math-1.md`](./math-1.md) | Grade 1 math |
| [`math-2.md`](./math-2.md) | Grade 2 math |
| [`english-1.md`](./english-1.md) | Grade 1 English — reading + writing pillars |
| [`english-2.md`](./english-2.md) | Grade 2 English — reading + writing pillars |

Next grades: add `math-3.md` + `english-3.md` when the K–2 spine has lessons running on-device; do not sprint ahead of the vertical (VISION.md §11).

## How objectives relate

Goji objective IDs (`obj.math.k2.…`) are the native spine; the SOL code is the **crosswalk** column on each objective (see `subjects/*/OBJECTIVES.md`). One objective can serve several SOL sub-skills; one SOL can need several objectives. The catalog is the completeness check, not the teaching unit.
