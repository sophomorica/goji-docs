# Lesson: `lesson.science.k2.weather.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.weather.02` |
| **Title** | One meadow, four seasons |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 12 min on Goji + ongoing season-tagged weather journal |
| **Objectives** | `obj.science.k2.weather.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.weather.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — the hand-off upgrades the **weather journal habit carried from K** (`lesson.science.k2.weather.01`): from today every daily weather entry is tagged with the season, and one summary entry per season closes the pattern loop.

---

## 1. Goal (one sentence)

After this lesson, the child can say how one meadow (its tree, its fox, a kid) changes through spring–summer–fall–winter, insist that one cold rainy summer day is STILL summer, and read a week's weather strip to count and compare days — which is why we record weather at all.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "It rained all day and it's cold — 'it must be winter!' Can ONE day tell the season?" — child taps yes/no; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | The SAME meadow cycles: spring (buds, rain, fox kits, rain jacket) → summer (green, thin coat, sun hat) → fall (leaves drop, coat thickens, jacket) → winter (bare, snow, thickest coat, bundled up); beat 5: a cold rainy day appears INSIDE summer — still summer; beat 6: the weather strip reveals the pattern | lessons (stage `teach`) | `anim.science.k2.weather.02` (inline in package) |
| 3 | **Guided practice** | 2.5 | Five season-detective taps: match clue → season (bare tree, thickening fox coat, opening buds, "is the tree bare in summer?" trap, cold-rainy-summer-day trap) — wrong tap names the misconception | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 2 | Read the week weather strip: "how many sunny days?", "more sunny or rainy?", "why keep a strip at all?" — misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.weather.02`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | daily | Weather journal (K habit) now tagged with the season: "Rainy. Cool. Season: FALL." Parent signs off after a week of tagged entries | journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.weather.02`, `min_score: 4`
- [ ] Task 2: Journal — daily weather entry with season tag, prompt "Today's weather ___. Season: ___", `min_words: 5`, `lesson_id: lesson.science.k2.weather.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.weather.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser first and walks the four-season meadow with the child
- [ ] Task 2: Journal — season-tagged weather entry as above (continues the K weather-journal routine)

## 4. Checks

- **Formative:** the two trap items — does the child call a cold rainy summer day "winter" (one-day-season) or say the strip can't tell anything (records-pointless)? The package records which misconception key was tapped.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge) + a week of season-tagged journal entries with parent sign-off.
- **If not yet:** replay the Teach stage only ("watch the seasons again"); then re-run just the four plain season-match items (no traps, no strip) with the parent naming each season's clues aloud; retry the check next day — and keep the journal going, it IS the remediation for the pattern idea.

## 5. Tools

- **Uses existing:** journal (weather habit from K, now season-tagged), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` per [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.weather.02` is authored **inline** (SVG/CSS four-season meadow) in the package — brief in `assets/animations/anim.science.k2.weather.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.weather.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no season shown as a random jumble (always the fixed cycle); never mock the "one day = season" guess — the trap items teach it; snow/rain plain (no faces on clouds, sun, or snowflakes); the fox's coat GROWS (never dressed in human clothes).
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded lines when media lands).
- The fox recurs from the 1.5 unit (same storybook fox as `assets.json` character), tying the science year together.
