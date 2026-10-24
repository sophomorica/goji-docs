# Lesson: `lesson.science.35.structures.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.structures.01` |
| **Title** | Built to survive — the leaf factory and the horse |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off |
| **Objectives** | `obj.science.35.structures.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.structures.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `black-beauty` — the horse is the worked structure-function example (long legs + hard hooves, flat grinding teeth, mane/tail fly swatter); the meadow grass he grazes is the photosynthesis case. Every structure in the lesson earns its keep.

---

## 1. Goal (one sentence)

After this lesson, the child can state the word equation of photosynthesis (sunlight + carbon dioxide + water → sugar + oxygen, made in the leaf — **not** drawn from the soil) and explain how specific plant and animal structures help an organism get energy, survive, and make offspring, using the horse as the worked example.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Black Beauty eats grass all day. But what does the *grass* eat?" — child taps a guess (soil-drinker vs food-maker); revisited on the result screen | lessons (stage `hook`) | in-package |
| 2 | **Teach** | 3 | Five beats: ① the leaf food factory with the word equation in arrows; ② soil ≠ food (roots hold + drink water — the misconception beat); ③ oxygen is the leftover, not a gift made for us; ④ the horse's structures each earn their keep (legs/hooves outrun danger; flat teeth grind grass vs fox's pointed meat-slicers; mane/tail = fly swatter); ⑤ offspring structures: flower → seed, fruit carries the seed, egg shell protects | lessons (stage `teach`) | `anim.science.35.structures.01` (inline in package) |
| 3 | **Guided practice** | 3 | "Run the leaf factory": drag/tap 6 cards into *Into the factory* / *Out of the factory* / *Not in the recipe* — sunlight, CO₂, water in; sugar, oxygen out; **soil rejected** with the misconception named aloud | lessons (stage `practice`, phase A) | — |
| 4 | **Independent practice** | 4 | "Every structure has a job": 7 structure→job matches (horse legs+hooves, horse flat teeth, fox pointed teeth, mane/tail, flower, fruit, egg shell); wrong taps name decoration/diet/for-us errors | lessons (stage `practice`, phase B) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.structures.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 8 | Research: Kiwix "Photosynthesis" — copy the word equation into notebooks; Kiwix "Horse" — find one more structure and its job → notebooks 2-fact log (INTEGRATION §4, black-beauty row) | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.structures.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Photosynthesis", then "Horse", 8 min
- [ ] Task 3: Notebooks — 2 facts: the word equation + one horse structure and its job

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.structures.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and walks the teach + factory sort with the child
- [ ] Task 2: Research — "Photosynthesis" + "Horse"
- [ ] Task 3: Notebooks — 2-fact log as above

## 4. Checks

- **Formative:** phase A — does the child drop *soil* into the factory (plants-eat-soil, THE misconception)? Phase B — does the child call the mane/tail "decoration"? The package records which error types fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage ("Watch the factory again" button); then re-run phase A only with the parent naming each arrow aloud ("what goes IN?"); retry the check next day. If soil-as-food persists, do the off-device demo: two cups, one plant in plain water with light, one in rich soil in a dark closet — predict, then check in a week (parent-led, journal the prediction).

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.structures.01` authored **inline** (SVG/CSS slides) in the package — brief in `assets/animations/anim.science.35.structures.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.structures.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no chemistry symbols (word equation only at grade 4); no soil-to-leaf "food tube" imagery; no faces on the leaf, sun, soil, or egg; the fox teeth inset is calm, not gory.
- Read-aloud: every instruction has a speaker button (recorded line when generated, Web Speech fallback).
