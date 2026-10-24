# Lesson: `lesson.science.35.solar.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.solar.01` |
| **Title** | Our solar system — rotate, revolve, eight worlds |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 5–10 min research hand-off per day |
| **Objectives** | `obj.science.35.solar.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.solar.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — standalone Egypt-style unit (INTEGRATION §4): the solar system is its own domain unit. Research hand-off: Kiwix "Solar System" then **one planet per research day** (Mercury on day 1 … Neptune on day 8) → notebooks fact log ("planet · one hook fact · rocky or gas"), cumulative parent quiz from the notes at the end of the planet-a-day run.

---

## 1. Goal (one sentence)

After this lesson, the child can tell **rotate** (spin — makes day and night) from **revolve** (travel around the sun — makes a year), name the eight planets in order with one hook fact each, split them into rocky-inner vs gas-giant-outer, and say why the sun dwarfs everything (beach ball vs peppercorn).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Your birthday comes around every year. What does Earth DO to make a year?" — child taps SPINS or TRAVELS; guess revisited at the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Six beats: ROTATE (spin, day/night) · REVOLVE (travel, year) — the two words are the heart · eight planets in order with one hook fact each · rocky four vs gas-giant four · sun = beach ball, Earth = peppercorn · posters lie: real space is mostly empty | lessons (stage `teach`) | `anim.science.35.solar.01` (inline in package) |
| 3 | **Guided practice** | 4 | Place-the-planets order build (8 taps, track fills planet by planet); wrong tap → "My Very Educated Mother Just Served Us Noodles" mnemonic hint read aloud, retry in place | lessons (stage `practice`, phase 1) | — |
| 4 | **Independent practice** | 4 | Rotate-or-revolve scenario taps ("this makes your birthday come around" · "24 hours" · "the sun seems to rise") ×5, then size/spacing picks ×3; wrong answers name the specific error and re-queue | lessons (phases 2–3) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.solar.01`), pass ≥ 4/5, score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5–10/day | Research: Kiwix "Solar System", then one planet per day → notebooks: planet name + one fact + rocky-or-gas | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.solar.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Solar System" (then "Mercury" … "Neptune", one per day), 5–10 min
- [ ] Task 3: Notebooks — "Planet of the day: name, one amazing fact, rocky or gas giant"

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.solar.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser first and walks the teach + order build with the child
- [ ] Task 2: Research — "Solar System" / planet of the day
- [ ] Task 3: Journal — "Rotate means ___. Revolve means ___. My favorite planet is ___ because ___." (`min_words: 15`)

## 4. Checks

- **Formative:** practice telemetry — does the child confuse rotate/revolve (`rr` misses), scramble the order (`order` misses), or shrink the sun (`sunsmall`)? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage's first two beats only (rotate vs revolve is the load-bearing distinction); then re-run just the rotate-or-revolve scenarios with the parent saying "spin" or "trip" aloud before each tap; retry the check next day. Order trouble → chant the mnemonic while re-doing the 8-slot build with the track visible.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.solar.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.solar.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.solar.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no faces on the sun, moon, or planets** (they are not alive); never draw the planets evenly/closely spaced as truth — the "poster lies" beat exists to kill that; sun never drawn merely 2–3× Earth.
- Read-aloud: every instruction has a speaker button (Web Speech API when no generated narration; text stays).
- Sister unit: `lesson.science.35.moon.01` (4.6) lists this objective as its prerequisite.
