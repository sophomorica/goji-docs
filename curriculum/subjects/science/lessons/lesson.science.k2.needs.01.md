# Lesson: `lesson.science.k2.needs.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.needs.01` |
| **Title** | What does the lion need? — five basic needs |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.needs.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.needs.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `aesop-fables` — the lion (*The Lion and the Mouse* week). Sister lesson to `lesson.science.k2.living.01` (same badge visual language, new badges); the fable's own mouse is the built-in second animal for "same needs, different forms." Retake variants swap the specimen for the current fable animal.

---

## 1. Goal (one sentence)

After this lesson, the child can name the five basic needs of animals (food, water, shelter, air, space), pick what the lion needs vs does not need, and say that the mouse has the very same needs — just in different forms and amounts.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The lion is the king of beasts. What does even a king need — water, or a toy?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | The lion earns five badges one at a time: FOOD (eats meat) · WATER (drinks at the waterhole) · SHELTER (shade of rocks and tall grass — *not* a house with walls) · AIR (breathes, in and out) · SPACE (room to roam). Then the toy ball is tested against the badges and is none of them | lessons (stage `teach`) | `anim.science.k2.needs.01` (inline in package) |
| 3 | **Guided practice** | 2 | First three cards sorted *with* badges visible: meat, waterhole, toy ball. Wrong drop reads the specific error aloud ("A toy is people-fun. It is not one of the five needs") | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 3 | Remaining cards: shady rocks, air to breathe, room to roam, TV, candy — needs it / doesn't need it; misses re-queue. Then the **mouse round**: 3 quick items showing the SAME five needs in mouse-sized forms (seeds not zebras; a burrow not a rock den; a little space, not a savanna) | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.needs.01`) incl. one "which is NOT a basic need?", score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Research: open Kiwix "Lion" — find one thing lions eat → journal one sentence "A lion needs … " | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.needs.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Lion", 5 min
- [ ] Task 3: Journal — prompt "A lion needs …", `min_words: 8`, `lesson_id: lesson.science.k2.needs.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.needs.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Research — "Lion"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** practice sort — does the child give the lion the toy/TV/candy (people-fun-as-need, candy-as-food) or reject the rocks as shelter (shelter-equals-house)? The package records which miss by item.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button); then a reduced 5-card sort of the five need cards alone (no distractor wants) to rebuild the badges; retry the check next day with the next fable animal as specimen.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Sister lesson to `lesson.science.k2.living.01`: deliberately reuses its badge visual language (earn-a-badge teach, badge test against a non-example) with five new badge icons.
- Animation: `anim.science.k2.needs.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.needs.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.needs.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: shelter never drawn as a human house; the toy ball and TV clearly human objects with no faces; candy shown as a wrapped people-treat, never in the lion's mouth.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
