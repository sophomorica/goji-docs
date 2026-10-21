# Lesson: `lesson.science.k2.weather.03`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.weather.03` |
| **Title** | Junior forecaster — measure, record, predict, prepare |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 12 min on Goji + 10 min paper-pictograph hand-off |
| **Objectives** | `obj.science.k2.weather.03` (prereq: `obj.science.k2.weather.02` — the daily observe-and-record habit this lesson turns into data) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.weather.03/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — this unit's "text" is the child's **own weather journal** (the K–1 habit). Research hand-off: turn this week's weather journal into a **paper pictograph with a parent** → photo/entry in journal.

**Feeds the SEP row:** this lesson delivers the 2.1 graphing requirement's pictograph half with data the child already owns (see `skills/science-2.md` 2.1 — "journal record becomes a pictograph"). Note that in the 2.1 coverage when this flip is applied.

---

## 1. Goal (one sentence)

After this lesson, the child can match the thermometer, rain gauge, and windsock to what each measures, read a one-week weather pictograph (most / fewest / how many / how many more), and say that recorded patterns help us predict weather and prepare for storms.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Will tomorrow be sunny or stormy — can anyone know before it happens?" — child taps yes/no guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: thermometer = how warm (and it only *measures* — never makes the heat); rain gauge = a measuring cup for the sky; windsock = wind direction and strength; a recorded week becomes a PICTOGRAPH (each sunny day = one sun picture, stacked); the pattern lets you PREDICT and PREPARE (storm coming → flashlight charged, stay in) | lessons (stage `teach`) | `anim.science.k2.weather.03` (inline in package) |
| 3 | **Guided → independent practice** | 4 | "Forecaster training" tap rounds, misses re-queued: 3 tool→job matches, 4 pictograph-reading questions on an in-package chart (most / how many rainy / how many more / fewest), 1 prepare-for-storm pick. Wrong answers name the specific error (tool-makes-weather, chart-is-decoration, count again, can't-know-anything) | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.weather.03`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 10 | With a parent: take this week's weather journal entries and build a **paper pictograph** (one picture per day, rows for sunny/rainy/cloudy) → journal entry or photo "My week had most … days" | journal (+ parent) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.weather.03`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Make your paper pictograph with a parent, then write: My week had most … days", `min_words: 8`, `lesson_id: lesson.science.k2.weather.03`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.weather.03` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + training with the child
- [ ] Task 2: Journal — pictograph prompt as above (parent alongside, sign-off)

## 4. Checks

- **Formative:** the training rounds — does the child answer "the tool makes it hot" (tool-causes-weather), miscount pictograph rows, or pick "the chart is just decoration"? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again"); then with the parent, count ONE row of the paper pictograph aloud finger-on-picture (rebuilds picture=day), and re-match the three tools with the real objects/pictures around the house; retry the check next day.
- **Habit gate:** the weather journal keeps running — ≥ 5 recorded days before the paper-pictograph hand-off (parent confirms).

## 5. Tools

- **Uses existing:** journal (weather log + pictograph entry), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.weather.03` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.weather.03.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.weather.03` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- The in-package pictograph (4 sunny / 2 rainy / 1 cloudy) is drawn as one shared SVG used by both practice and check — identical pictures, one picture = one day, so counting is never ambiguous.
- Must-not-show: no faces on suns, clouds, or tools; the storm beat stays calm (distant lightning, cozy house, ready flashlight — preparedness, not fear).
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
