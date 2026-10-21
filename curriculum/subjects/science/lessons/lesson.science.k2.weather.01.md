# Lesson: `lesson.science.k2.weather.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.weather.01` |
| **Title** | Patterns in the sky — day and night, seasons, weather |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5 min journal hand-off (then daily) |
| **Objectives** | `obj.science.k2.weather.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.weather.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `aesop-fables` — *The North Wind and the Sun* week. The fable's wind-vs-sun duel opens the weather talk ("which one won? what was the weather that day?"); the lesson's hand-off starts the daily weather journal habit.

---

## 1. Goal (one sentence)

After this lesson, the child can say that day and night repeat, name the four seasons **in order** (spring → summer → fall → winter → spring…), explain that daily weather changes but can be **recorded** to find patterns, and tell a hot day apart from a season change.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The sun is going down. Will it come back tomorrow?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Three beats: sun arcs up, sets, stars come out, sun rises again ("day, night, day — again and again") · season wheel turns in order and loops back to spring · a week strip stamps sun/cloud/rain icons into a weather journal ("we can WRITE it down — one rainy day doesn't change the season"). Each beat becomes a badge | lessons (stage `teach`) | `anim.science.k2.weather.01` (inline in package) |
| 3 | **Guided practice** | 1.5 | Pattern-wheel build: the wheel starts lit at spring; the first four taps place summer, fall, winter, and spring-again — each correct tap lights the next quarter | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | 6 more items: "what comes next?" strips (day→night→day→?, night→day→night→?, spring→summer→fall→?) and season-match cards (mittens+snow, falling leaves, blossoms+chicks). Wrong tap names the misconception aloud and re-queues | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.weather.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 (then daily) | With a parent: open the journal app and draw/write today's sky (sun/cloud/rain) — day 1 of the daily weather journal habit; after a week, look back together for the pattern | journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.weather.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Today the sky was …", `min_words: 4`, `lesson_id: lesson.science.k2.weather.01` (repeats daily as the weather-journal habit)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.weather.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser and walks the teach + pattern wheel with the child first
- [ ] Task 2: Journal — daily "Today the sky was …" entry, started together

## 4. Checks

- **Formative:** pattern wheel — does the child place seasons out of order (`misses.order`), think the sun might not return (`misses.cycle`), or misread season clues (`misses.season`)? Posted in `lesson.check.practice.misses`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the patterns again"); then make a paper season wheel with the parent (four paper quarters, physically arrange and re-arrange them in order three times); retry the check next day.

## 5. Tools

- **Uses existing:** journal (the weather-journal habit — K.9's own recording surface), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.weather.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.weather.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.weather.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no faces** on sun, moon, clouds, or weather symbols; night is calm (no scary dark); seasons always shown in the same clockwise order — never shuffled in the teach stage.
- Misconceptions encoded: seasons-in-random-order (q2/q3 distractors + wheel feedback), sun-gone-forever (q1 distractor + cycle feedback), weather-equals-season (q4 distractor + teach beat 3 line), weather-is-unrecordable/random (q5 distractor).
- K.10 pairing: this lesson's journal habit is the prerequisite observation surface for `lesson.science.k2.change.01` (change over time).
