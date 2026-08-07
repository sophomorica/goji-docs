# Parent app — standing UX spec (heat maps, glance-first)

Status: **spec v1** · 2026-08-07 · owner-directed  
Companion to `curriculum/PARENT_STANDING.md` (the data model) and `PARENT_APP_PRODUCT.md` §6 (app shell). Brand per `goji_learner_app/BRANDING.md`.

**Design stance (owner's words, kept):** a parent managing **any number of children** — one kid or a big family, K–12 — must never be overwhelmed with reading. **Glance → tap → evidence.** Color carries the first read; text appears only when the parent leans in. The family board is a dynamic list: families add, rename, and manage children freely (add/update child management is a first-class surface, not a fixed layout); a six-child K–8 household is simply the stress case every screen must survive.

---

## 1. Color system (one vocabulary everywhere)

Four semantic states, used identically on every surface (board, heat maps, day rings):

| State | Meaning | Color rule |
|-------|---------|------------|
| **Mastered** | objective gate met | deep green |
| **Developing** | evidence exists, gate not met | warm amber |
| **Struggling** | repeated misses / flagged by analysis | seal-red (brand red does double duty — attention, not shame) |
| **Not started** | no evidence yet | neutral cream/grey |

Rules: colorblind-safe pairings (states also differ by fill pattern/icon, never color alone); calm saturation per brand (no traffic-light neon); **red is rare by design** — it appears only on genuine struggle signals, so it stays meaningful.

## 2. Family board (the whole family, one glance)

Each child card = avatar + **day ring** + one optional attention dot:

```
 ┌──────────────┐  Day ring: today's School Day completion
 │   ◔ Ada (1)  │    empty=not started · filling=in progress · full=done
 │   ●          │  Attention dot (max ONE per card): red=struggle flagged,
 └──────────────┘    amber=needs parent action (sign-off, review waiting)
```

- **No numbers on the board.** Cards scale to the family — up to six fit one screen without scrolling; larger families scroll, smaller ones breathe. A parent reads the family's day in two seconds regardless of count.
- Tap card → child detail. Long-press → quick actions (Start day, Message, Pause games).
- Card order: attention-first (dots float up), then grade.

## 3. Child detail — bird's-eye first

Top of screen: **three pillar tiles** (Reading / Writing / Math), each showing only a mini coverage bar in the four state colors + trajectory word ("on track"). Below: today's checklist (when a day is active) pinned above the always-on activity feed (existing behavior).

### The heat map (tap a pillar tile)

The pillar opens to a **skill heat map** — the finite grade checklist as a grid of cells, one cell per skill from the catalog (`curriculum/skills/`):

```
 READING — Grade 1          17 skills · 6 mastered · 2 struggling
 Phonics    ■ ■ ■ ◪ □ □      ■ mastered  ◪ developing
 Fluency    ■ ■ ◪            ▨ struggling  □ not started
 Comprehension ■ ◪ ▨ □ □
 Vocabulary ◪ □
```

- **Finite is the feature:** grade 1 phonics has a countable number of skills; the map shows exactly which are tested, known, weak, untouched. That answers "where are they?" without a paragraph.
- Tap a cell → **evidence sheet**: the objective in plain language, the last 3 pieces of evidence (drill %, quiz score, writing-analysis line with its quote), and one button: **"Assign practice"** → pre-filled School Day task from the objective's lesson mapping.
- Struggling cells surface *why* (the diagnostic-distractor design pays off here: "misses are digit-swaps" not "60%").

### Writing pillar tile (with the writing loop live)

Adds a small **"to read" stack**: submissions awaiting parent review (analysis done, feedback held). Tap → child's actual text + skill results + one-tap "share feedback with child."

## 4. Set-the-day from standing

The wizard gains a **"from their road" mode**: preselects tasks from each child's weakest developing cells (never struggling-only — one win task, one stretch task, per pillar). The parent edits and starts as today. One tap per child on a good morning, however many children there are. (Suggested-day logic is deterministic from the catalog + states — Grok enrichment optional later, per VISION §6.)

## 5. Controls (existing product surface, restated for completeness)

Fun/reward games toggle (standing app locks) stays a **later** build per product TODO — but the board's long-press "Pause games" is the UX slot reserved for it.

## 6. Data requirements (all from existing plans — no new invention)

| Need | Source |
|------|--------|
| Skill cells per grade × pillar | curriculum catalog shipped to the app (bundled JSON asset v1; catalog sync later — TOOLS.md §6B) |
| Cell states | PARENT_STANDING.md mapping rules over already-synced signals (drill events, quiz scores, minutes, journal sign-offs) |
| Struggle flags | quiz diagnostic distractors + writing-loop `skill_results` (WRITING_LOOP_SPEC.md) |
| Assign-practice | objectives' lesson School-Day mappings (already authored per lesson) |

## 7. Build order

1. **Catalog asset**: export `curriculum/skills/` + objectives (IDs, statements, gates, lesson mappings) to a versioned JSON bundled in the Flutter app.
2. **State computer**: pure Dart — signals in, four-state cell map out (unit-testable, no UI).
3. Pillar tiles + heat map + evidence sheet (read-only v1).
4. Day ring + attention dots on the family board.
5. "From their road" wizard mode.
6. Writing-loop review stack (after SYNC_API lands the loop).
