# Lesson: `lesson.science.35.weather.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.weather.01` |
| **Title** | Reading the sky — records, storms, and climate |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off |
| **Objectives** | `obj.science.35.weather.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.weather.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `wizard-of-oz` — the tornado over the Kansas prairie is the extreme-weather case study; Uncle Henry's barn-wall instruments frame the hook; Kansas prairie summers anchor weather-vs-climate. The child's own weather journal (habit begun in K–2) is the prediction dataset.

---

## 1. Goal (one sentence)

After this lesson, the child can name what each grown-up weather tool measures (thermometer °F, barometer/air pressure, anemometer/wind speed, rain gauge), use a multi-day measurement record as evidence for a forecast (falling pressure hints storms — a forecast is evidence, not a guess and not a promise), describe how extreme events affect ecosystems and what to do when one comes, and tell weather (one day) from climate (the many-year pattern).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The sky turns green-grey. Uncle Henry checks the barn-wall tools: 'Storm's coming.' Lucky guess — or evidence?" — child taps a guess; revisited on the result screen | lessons (stage `hook`) | in-package |
| 2 | **Teach** | 3.5 | Five beats: ① the four tools grown up; ② daily records reveal patterns — the falling-pressure line; ③ a forecast = the pattern pointed at tomorrow (not magic, not a promise); ④ extreme events (thunderstorm, Dorothy's tornado — plain funnel, hurricane, drought), their ecosystem effects, and the storm-cellar rule; ⑤ weather (today) vs climate (many years — Kansas prairie summers) | lessons (stage `teach`) | `anim.science.35.weather.01` (inline in package) |
| 3 | **Guided practice** | 2.5 | Match tool → measurement (4 taps, misconception-aware feedback), then read two 5-day pressure/temperature records and pick tomorrow's likely forecast (falling → storm likely; high & steady → fair likely) | lessons (stage `practice`, phases A–B) | — |
| 4 | **Independent practice** | 4 | Weather-or-climate statement sort (5 drag/tap sorts incl. the cold-week trap) and two storm-safety picks (tornado siren → cellar; thunderstorm → inside, away from tall trees) | lessons (stage `practice`, phases C–D) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.weather.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 8 | Research: Kiwix "Tornado" (research chain) — how a funnel forms → notebooks 2 facts; then reread the child's own weather journal: find one pattern across entries and journal one forecast sentence with the evidence ("Tomorrow will likely be … because …") | research → notebooks → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.weather.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Tornado", 8 min
- [ ] Task 3: Journal — prompt "Tomorrow will likely be … because my records show …", `min_words: 12`, `lesson_id: lesson.science.35.weather.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.weather.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and reads the records with the child
- [ ] Task 2: Research — "Tornado"
- [ ] Task 3: Journal — forecast sentence as above, from the child's own weather-journal entries

## 4. Checks

- **Formative:** phase B — does the child pick "no one can know" (forecasts-are-guesses) or "for certain" (forecast-as-promise)? Phase C — does the cold-week statement land in CLIMATE (cold-week-means-climate-changed)? The package records which error types fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage (beat 2 is the records-to-patterns beat); then re-run phase B with the parent tracing the pressure column with a finger day by day ("up or down?"); retry the check next day using that week's real journal entries as the record.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, journal (weather-journal habit from K–2), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.weather.01` authored **inline** (SVG/CSS slides) in the package — brief in `assets/animations/anim.science.35.weather.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.weather.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no face on the tornado** (plain funnel, seen from a safe distance); no forecaster-as-wizard imagery (forecast ≠ magic); no people in danger during the extreme-weather beat; no faces on sun, clouds, or tools.
- Read-aloud: every instruction has a speaker button (recorded line when generated, Web Speech fallback).
