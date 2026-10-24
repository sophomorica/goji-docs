# Lesson: `lesson.science.k2.cycles.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.cycles.02` |
| **Title** | Two life stories: frog and bean |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 14 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.cycles.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.cycles.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `aesop-fables` — frog week in the animal-of-the-week slot (*The Frogs Who Desired a King* / *The Frog and the Ox*). The frog cycle deepens `cycles.01`'s frog ring; retake variants can ride whichever fable animal has a distinct cycle (butterfly week, hen week).

---

## 1. Goal (one sentence)

After this lesson, the child can build BOTH life cycles in order — frog (egg → tadpole → froglet → frog, water-breathing to air-breathing kept simple) and bean plant (seed → sprout → plant → flower → new seeds) — and say that animal and plant life cycles alike are circles that always run in the same order, each starting from a little beginning (egg or seed) that is alive and grows.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The frog was once a tiny egg. Did the bean plant start small and change too — or do plants just sit?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: life cycles go in ORDER, frog starts as an egg · tadpole swims and breathes under water · froglet grows legs, tail shrinks, breathes air → frog lays NEW eggs · plants too: seed → sprout → plant → flower · the flower makes NEW seeds — both circles side by side, both in order, both starting from a little beginning that grows | lessons (stage `teach`) | `anim.science.k2.cycles.02` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Build both rings, then compare: (a) frog ring — 4 stages placed in order (tap the stage for the glowing slot; wrong pick names the always-same-order rule and the slot stays until right); (b) bean ring — 5 stages the same way; (c) 3 cross-questions: which stage makes the NEW seeds? · what comes right after the tadpole? · how do BOTH life stories begin? (egg/seed — a beginning that grows) | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.k2.cycles.02`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 5 | Research: open Kiwix "Frog" — find what a tadpole eats; **or** check the real seed cup from the plant unit: which stage is it in today? → journal one sentence "My bean is in the ___ stage. Next comes ___." | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.cycles.02`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Frog", 5 min (or off-device seed-cup check)
- [ ] Task 3: Journal — prompt "My bean is in the ___ stage. Next comes ___", `min_words: 8`, `lesson_id: lesson.science.k2.cycles.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.cycles.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + ring-building with the child
- [ ] Task 2: Research — "Frog"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** ring-building logs every out-of-order pick per stage (`misses.order_*` in `lesson.check`) — a child who reaches for FROG right after EGG (skipping stages) or replays EGG after TADPOLE (cycle running backwards) is visible to the parent.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the two circles again"); then rebuild just the FROG ring (4 stages, the familiar one from `cycles.01`) before re-attempting the bean ring; if the seed items miss, replay `living.01`'s seed card ("still, but alive — give it water and it grows") with the parent; retry the check next day.
- **Ties back:** `obj.science.k2.cycles.01` (butterfly/frog rings, offspring resemble parents) is the base ring this lesson deepens; the seed-is-alive item deliberately re-tests `obj.science.k2.living.01`'s seed card.

## 5. Tools

- **Uses existing:** research (Kiwix "Frog"), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.cycles.02` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.cycles.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.cycles.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Gills/lungs kept simple: "breathes under water like a fish" → "starts to breathe air." No organ diagrams at this band.
- Must-not-show: cycles never run backwards on screen; no stage skipped in any teach visual; the seed and egg drawn the same size in the compare card (both are small beginnings); frog and froglet are the SAME character (on-model) so "different stage ≠ different animal."
- Read-aloud: every instruction has a speaker button (recorded line else Web Speech; silent fallback keeps text).
