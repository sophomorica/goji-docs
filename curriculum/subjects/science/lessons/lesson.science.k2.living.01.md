# Lesson: `lesson.science.k2.living.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.living.01` |
| **Title** | Living or not living? — the four signs of life |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.living.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.living.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `aesop-fables` — the wolf (*The Boy Who Cried Wolf* / *The Wolf and the Lamb* week). The package's specimen is the wolf; retake variants swap in the current fable animal.

---

## 1. Goal (one sentence)

After this lesson, the child can sort a thing as living or not living and say which sign of life (grows, needs food and water, moves on its own, makes more of its kind) was the clue — including the tricky cases of a moving river and a still tree.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The wolf moves. The river moves. Which one is alive?" — child taps a guess; no judgement yet, guess is revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Animated wolf shows the four signs one at a time: pup grows into wolf · eats and drinks · runs on its own · has pups. Each sign becomes a badge. Then the river is tested against the four badges and fails three | lessons (stage `teach`) | `anim.science.k2.living.01` (inline in package) |
| 3 | **Guided practice** | 2 | Three sorts *with* the badges shown: tree, rock, child. Wrong drop → the badge that fails lights up and a one-line why is read aloud | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Ten-card sort into LIVING / NOT LIVING: wolf, river, oak, log, cloud, ant, toy robot, seed, fire, bird. Instant feedback per card; misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.living.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Research: open Kiwix "Wolf" — find one thing the wolf eats (a sign of life) → journal one sentence "A wolf is living because …" | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.living.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Wolf", 5 min
- [ ] Task 3: Journal — prompt "A wolf is living because …", `min_words: 8`, `lesson_id: lesson.science.k2.living.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.living.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Research — "Wolf"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** practice sort — does the child drop *river* into LIVING (movement-as-life) or *oak* into NOT LIVING (stillness-as-nonlife)? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only (package "watch again" button); then a 6-card sort with *no* moving nonliving things (rock, cup, spoon vs ant, tree, child) to rebuild the badges; retry the check next day with the new fable animal.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.living.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.living.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.living.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no cartoon objects with faces (reinforces "looks alive = alive"); the toy robot is drawn clearly as a toy.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
