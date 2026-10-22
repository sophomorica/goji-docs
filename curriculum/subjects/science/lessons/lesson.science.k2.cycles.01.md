# Lesson: `lesson.science.k2.cycles.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.cycles.01` |
| **Title** | Round and round — life cycles |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.cycles.01` (prereq: `obj.science.k2.needs.01`) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.cycles.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — specimens are the butterfly and frog named by the K.7 skills row for life cycles (not fable-tied this week). Research hand-off: Kiwix "Butterfly" → journal. Retake variants may swap in the chicken (egg → chick → hen).

---

## 1. Goal (one sentence)

After this lesson, the child can put the stages of the butterfly and frog life cycles in order as a circle that keeps going, match a baby to its parent even when they look nothing alike (caterpillar → butterfly, tadpole → frog), and say that babies look like their parents but are not identical copies.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "This caterpillar and this butterfly — are they the same animal?" — child taps yes or no; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | The circle fills one node at a time: egg → caterpillar → chrysalis → butterfly → *she lays eggs, arrow loops back* — "the circle keeps going." Then the frog quickly (egg → tadpole → frog) to show the SAME pattern in another animal. Last beat: a litter of puppies — same kind as their mother, different spots: "like her, not copies" | lessons (stage `teach`) | `anim.science.k2.cycles.01` (inline in package) |
| 3 | **Guided practice** | 2 | Build the butterfly circle: drag (or tap) the four stage cards into the circle in order; the loop arrow closes the circle. Wrong pick reads the specific error aloud ("The egg hatches a caterpillar — not a tiny butterfly"); one extra item: "After the butterfly — what next?" | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 2.5 | Build the frog circle (3 stages, same pattern); then "Who is the baby's parent?" — 3 matches including the non-obvious pairs (tadpole → frog, caterpillar → butterfly) and chick → hen | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.cycles.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Research: open Kiwix "Butterfly" — find what the caterpillar eats → journal one sentence "First the egg, then …" | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.cycles.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Butterfly", 5 min
- [ ] Task 3: Journal — prompt "First the egg, then …", `min_words: 8`, `lesson_id: lesson.science.k2.cycles.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.cycles.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + circle-builder with the child
- [ ] Task 2: Research — "Butterfly"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** circle-builder — does the child put the butterfly right after the egg (tiny-adult / skips the caterpillar) or stop the circle at the adult (cycle-ends)? Parent match — does the child pick the "bigger caterpillar" as the parent (different-animal)? The package records misses by misconception.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button); then rebuild ONLY the butterfly circle with the stage cards pre-labeled 1–4 (numbers as scaffolding); retry the check next day with the frog circle first.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.cycles.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.cycles.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.cycles.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: never show the cycle running backwards; never show the adult as "the end" (the loop arrow always closes the circle); the puppies visibly share the mother's kind and coloring but differ in spots; no faces on eggs or the chrysalis.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
