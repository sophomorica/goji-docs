# Lesson: `lesson.science.k2.change.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.change.01` |
| **Title** | Before and after — fast changes, slow changes |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + month-long observation hand-off |
| **Objectives** | `obj.science.k2.change.01` (prereq: `obj.science.k2.weather.01` — the K.9 journal habit is the observation surface this lesson extends) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.change.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — the hand-off is the anchor: pick ONE thing to watch change this month (a planted seed or the moon) and journal it every few days. Pairs with the K.9 daily weather journal (`lesson.science.k2.weather.01`): same habit, longer clock.

---

## 1. Goal (one sentence)

After this lesson, the child can pair a thing with what it becomes (before → after), sort each change as **fast** (watchable) or **slow** (too slow to watch but still happening), and say that living things change by growing while nonliving things get changed by waves, wind, or people.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "An ice cream in the sun. A big oak tree. Which one is changing right now?" — child taps a guess (answer: BOTH); revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Three beats: FAST changes (leaf falls, ice cream melts — you can watch) · SLOW changes (acorn → sprout → sapling → tree; puppy cross-fades to dog — too slow to watch, never stops) · living things GROW, nonliving things GET CHANGED (waves wear the sandcastle; people build the road). Each beat becomes a badge | lessons (stage `teach`) | `anim.science.k2.change.01` (inline in package) |
| 3 | **Guided practice** | 1.5 | First two pairs (seed→tree, puppy→dog) — match the after picture, then tap FAST or SLOW; correct match reveals the pair side by side | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4.5 | Four more before/after pairs (ice cube→puddle, sandcastle→flat sand, new crayon→worn crayon, leaf on branch→leaf on ground), each matched then speed-sorted — 12 interactions total. Wrong answers name the misconception aloud and re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.change.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | month | With a parent: choose a slow change to watch — plant a seed OR track the moon; journal a drawing every few days; at month's end look at the first and last page: before and after! | journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.change.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "My [plant/moon] today looks …", recurring every 2–3 days, `lesson_id: lesson.science.k2.change.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.change.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser and walks the teach + matching with the child first
- [ ] Task 2: Journal — the recurring observation entry, set up together (plant a bean in a cup or start a moon page)

## 4. Checks

- **Formative:** the package logs `misses.pairing` (can't link before→after), `misses.slow_invisible` (calls slow changes "not changing" / fast), `misses.fast_slow` (speed confusion) in `lesson.check.practice.misses`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the changes again"); then a physical before/after: parent puts an ice cube on a plate — watch it melt (fast) — and looks at baby photos of the child ("you changed too — slowly!"); retry the check next day.

## 5. Tools

- **Uses existing:** journal (observation habit), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.change.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.change.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.change.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on nonliving things (castle, crayon, ice, road, truck); the puppy/dog is the SAME dog (recurring character in `assets.json`) so growth reads as one individual changing, not two dogs; slow changes shown as a stepped row, never as a magic instant transformation.
- Misconceptions encoded: only-living-things-change (q3 distractor + sandcastle why-line), slow-means-not-happening (q1 distractor + slow-miss feedback), all-at-once growth (q4 distractor), fast/slow speed-swap (q2/q5 distractors).
- Prereq note: `obj.science.k2.weather.01` listed as prereq — the recording habit (journal) taught there is reused here for the month-long observation.
