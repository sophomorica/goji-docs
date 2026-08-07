# Goji computer — tools inventory

**Purpose:** Maximize what already runs on the device; keep a clear backlog of teaching tools we still need.

Last inventory: **2026-08-05** (from kiosk `lazyApps` + math modules + parent task types + seed data).  
Update this file when a tool ships or a gap closes.

---

## 1. Kid-facing apps on the computer (shipped)

Source: `goji_computer/frontend/src/App.svelte` `lazyApps` + Hub.

| App id | What it is | Curriculum use |
|--------|------------|----------------|
| `reader` | Book reader | Reading minutes, book-tied quizzes later |
| `pdf` | PDF reader (catalog + page ranges) | Lessons as PDFs; School Day task type |
| `math` | Math hub + drills | Primary math practice surface |
| `typing` | Typing lessons / games | Keyboard fluency; literacy support |
| `coding` | Courses + challenges (HTML/CSS/JS, Flexbox Froggy, …) | CS pathway (strongest seed today) |
| `flashcard-app` | Flashcard study (+ parent-synced decks) | Vocabulary, facts, quick checks |
| `journal` | Journal entries | Reflection; School Day optional sign-off |
| `writing` | Writing surface | Compositions / prompts (underused in curriculum plan) |
| `notebooks` | Long-form notes (TipTap) | Project notes, research write-ups |
| `research` | Offline research (Wikipedia-style path) | Inquiry projects |
| `quotes` | Quotes | Light literacy / discussion starters |
| `tutorial` | In-app tutorials / user-apps path | Meta-learning; coding “build a flashcard app” |
| `my-apps` | User-built apps | Creative coding portfolio |
| `tasks` | Household chores board | **Not** academic curriculum (always allowed in School Mode) |
| Hub / Today / School Mode | Plan queue, lockdown | Delivery shell for any academic day |

**Also related (not always separate hub tiles):** Parent Quizzes UI (`ParentQuizzes`), Speed Reading component path, Wi‑Fi / USB / pairing chrome — supporting, not core teach tools.

---

## 2. Math modules (inside `math`)

Source: `Math.svelte` + `MATH_MODULE_TASKS_PLAN.md`.

| Module / drill | Status | Notes |
|----------------|--------|-------|
| Times tables / multiplication | Live | Module-scoped tasks planned |
| Mental math | Live | |
| Addition | Live | |
| Subtraction | Live | |
| Division | Live | Per-table mastery schema gap (see math plan) |
| Word problems | Live | Bank in frontend |
| Fractions | **Live** (tile restored 2026-08-07) | Was wired once, lost in a merge; re-wired + tested |

**Missing for rich curriculum (math):** principle explainer player, fraction/place-value visual *lessons* (not only drills), multi-step unit sequences, adaptive “you’re weak on ÷7” parent view (schema work).

---

## 3. Content already seeded (implementation)

| Content | Location | Curriculum note |
|---------|----------|-----------------|
| Typing lessons | `goji_computer/backend/seed_data/typing_lessons.json` | Map later to literacy bands |
| Coding courses | `goji_computer/backend/seed_data/coding/*.json` | JS basics + HTML/CSS/etc. — model for owned courses |
| Notebooks / PDFs / books in DATA_DIR | Runtime data | Catalog sync for School Day; not “Goji curriculum spine” |

Coding seed structure (lessons → challenges → tests/hints) is a **template** for how math/reading courses may eventually serialize.

---

## 4. Parent / cloud tools (not on-device teaching, but part of ecosystem)

| Capability | Status | Curriculum relevance |
|------------|--------|----------------------|
| School Day wizard + Start/Release | Built / e2e open | Delivers any day’s mix of tools |
| PDF + book catalog assign | Built | Vehicle for lessons until first-party packages exist |
| Parent-authored quizzes | v1 path | Bridge until curriculum quizzes |
| Module-scoped math tasks | Spec + plan; not fully built | Critical for objective-aligned math days |
| `content-generate` edge function | Stub | Future: generate from objective IDs (cloud-side) |
| Synced flashcard decks | Phase 2b | Vocab packs per unit |
| Lesson-suggestion → apply to plan | Schema exists; apply path open | Curriculum “suggested day” UX |

---

## 5. Tools we **maximize first** (no new app)

When designing a lesson, pick from this list before proposing a new surface:

1. **PDF lesson** (structured pages) + page-range task  
2. **Math module** deep-link (once intents ship)  
3. **Flashcards** for facts / vocab  
4. **Reader** + minutes (and later book-tied quiz) — prefer **Gutenberg classics** when curating  
5. **Typing** exercise set for the same spelling list  
6. **Journal / Writing** for explain-in-words exit tickets (writing pillar)  
7. **Research (Kiwix / offline Wikipedia) + Notebooks** for curiosity domains once pillars support them  
8. **Coding challenge** only if CS pathway (supporting, not pillar)

### Offline knowledge (not “apps,” but core fuel)

| Source | Curriculum use |
|--------|----------------|
| Project Gutenberg library on device | Classic reading path; **audit lineup by grade** |
| Kiwix (full Wikipedia offline) | History/science/domain text; lesson augment; quiz source material |
| Seed coding/typing JSON | Existing structured courses |

### Games

| Kind | Role | Metrics |
|------|------|---------|
| **Learning games** | Facilitate teach/practice (math, typing, spelling, …) | Count toward standing / School Day |
| **Reward / pure-fun games** | Motivation after work | **Do not** count as academic proof |  

---

## 6. Tools we may **need to create**

Ranked by how often curriculum talks will hit the wall. Status = planning only.

### A. Teaching media

| Tool | Why | Priority |
|------|-----|----------|
| **Animation / explainer player** | Play Claude Design (or converted) clips mapped to objectives; skip, replay, Pi-safe | **High** |
| Animation package format + seed pipeline | IDs, offline assets on image or USB/catalog sync | High |
| Interactive visual (Svelte) for core models | Place value, fraction bars, number line — when video isn’t enough | Medium |

### B. Curriculum runtime

| Tool | Why | Priority |
|------|-----|----------|
| **Objective graph store** (local) | Track mastery per child per objective | Medium (after first strand designed) |
| **Lesson player / unit sequence** | Ordered teach → practice → quiz without parent hand-building every day | Medium–High |
| Curriculum catalog sync | Push units like PDFs/books | Medium |
| Suggested School Day from unit progress | “Next 3 lessons” → plan | Later |

### C. Quizzes & generation

| Tool | Why | Priority |
|------|-----|----------|
| Quiz items tied to **objective + book/module** | Stronger than free-floating parent quizzes | High (spec in QUIZZES.md) |
| Generator (parent/cloud) from blueprint | Scale item banks | Medium |
| Auto-verify plan task from quiz score | Already directionally in product TODO | Medium |

### D. Math / reading / writing depth

| Tool | Why | Priority |
|------|-----|----------|
| ~~Wire Fractions~~ (done 2026-08-07) + division mastery schema (`operation` column on `multiplication_table_mastery`, incl. unique-key change — division per-table stats are computed then discarded at `ArithmeticDrill.svelte` endGame) | Unlock real fraction/division strands | High (fractions done; division schema next) |
| Reading comprehension quiz ↔ book ID | Product TODO already | High for reading spine |
| Parent **pillar standing** views (R/W/M + books read + trajectory) | Vision §6 — core parent promise | High (product; after data model) |
| Gutenberg inventory + grade reading lists (docs then data) | Classic lineup as main reading path | High (curriculum lead) |
| Kiwix-augmented lesson/quiz blueprints | Domain learning without live web | Medium |
| Grok-assisted day plan / quiz suggestions (cloud) | Parent co-pilot | Medium (with content-generate) |
| Guided reading modes (chunking, vocab side panel) | Beyond minutes | Later |
| Worked-example / error-analysis UI | Teach from mistakes | Later |

### E. Authoring (human / agent, not kid UI)

| Tool | Why | Priority |
|------|-----|----------|
| This `curriculum/` docs system | Planning SoT | **Now** |
| Claude Design brief → INDEX pipeline | Consistent media production | Now |
| Optional: export lesson → seed JSON | When ready to ship a unit | Later |

---

## 7. Decision rule

> If a lesson needs a tool in §6, **either** (1) rewrite the lesson to use §5, or (2) add a row to the tools backlog and keep the lesson **blocked** until that tool has a phase.  
> Do not invent a third app casually — Pi bundle and kid UX cost are real.

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-08-05 | Initial inventory from goji_computer + parent product docs |
| 2026-08-07 | Fractions tile restored to math menu (goji_computer `12314c3`); book library audited (13 books in DB, ingest pipeline documented in `subjects/reading/reading-lists.md`); mastery-schema gap pinpointed |
