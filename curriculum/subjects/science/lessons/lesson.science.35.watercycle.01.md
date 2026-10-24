# Lesson: `lesson.science.35.watercycle.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.watercycle.01` |
| **Title** | One drop's endless journey — the water cycle |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off |
| **Objectives** | `obj.science.35.watercycle.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.watercycle.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — research hand-off is **Kiwix "Water cycle"** → notebooks (draw the circle, two facts). Builds directly on K–2 water (`obj.science.k2.water.01`: three forms, downhill) and matter (`obj.science.k2.matter.02`: solid/liquid/gas).

---

## 1. Goal (one sentence)

After this lesson, the child can follow one water drop around the cycle — evaporation (sun heats, liquid→gas, rises), condensation (cools high up, gas→droplets = cloud), precipitation (rain/snow falls), downhill flow back to the sea — name the sun as the engine, name the ocean as the biggest reservoir (lakes, rivers, underground, ice hold the rest), and say that rain is the same water recycled forever.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The morning puddle is gone by lunch — where did the water GO?" — child taps a guess (vanished forever / went up into the air); revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3.5 | Five beats following ONE drop: (1) EVAPORATION — sun heats the sea, drop rises as invisible gas (liquid→gas); (2) CONDENSATION — cold high up, gas→tiny droplets, a cloud is water (not smoke, not cotton); (3) PRECIPITATION — heavy droplets fall as rain/snow; (4) the CIRCLE — downhill through river back to sea, sun is the engine; (5) reservoirs — most water is ocean; lakes/rivers/underground/ice; same water forever (the dinosaur drank it!) | lessons (stage `teach`) | `anim.science.35.watercycle.01` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Phase A "Label the cycle": place the three process labels on the glowing spots of the diagram (retry in place). Phase B "What happens next?": 4 drop-journey steps around the circle. Phase C "Name the process": 6 real-life scenarios (dew, vanished puddle, snowfall, foggy mirror, drying towel, rain). 13 interactions total; wrong answers name the error | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.watercycle.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 5 | Hand-off | 8 | Research: Kiwix "Water cycle" → notebooks: draw the circle with the three labels + two facts (e.g. which reservoir is biggest) | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.watercycle.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Water cycle", 8 min
- [ ] Task 3: Notebooks — "Draw the water circle with its three labels; write two facts"

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.watercycle.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and walks teach + practice with the child first
- [ ] Task 2: Research — "Water cycle"
- [ ] Task 3: Notebooks — as above

## 4. Checks

- **Formative:** practice telemetry — does the child mix the three process names (procmix), pick "destroyed/vanished" (water-destroyed), or call the cloud smoke? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Follow the drop again"); then run a kitchen demo with the parent — breathe on a cold window (condensation) and watch a wet spot dry (evaporation) — naming each aloud; retry the check next day. If forms of water are shaky, re-run `lesson.science.k2.water.01` first.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation `anim.science.35.watercycle.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.watercycle.01.md`, INDEX status `shipped-inline`. The brief notes this as the **classic standalone animation candidate** (skills/science-3.md §Summary item 2) if/when a richer generated animation lane opens.
- Quiz blueprint: `quiz.science.35.watercycle.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: NO faces on clouds, drops, or the sun (the followed drop is marked by a glow, not a face); clouds never drawn as smoke or cotton; water never flows uphill anywhere, even decoratively.
- Vocabulary with inline glosses: evaporation, condensation, precipitation (each glossed by direction: up-as-gas / gas-to-droplets / falling); reservoir avoided in kid copy ("where water waits").
- Prereqs `obj.science.k2.water.01` + `obj.science.k2.matter.02`: if solid/liquid/gas is shaky, run those first.
