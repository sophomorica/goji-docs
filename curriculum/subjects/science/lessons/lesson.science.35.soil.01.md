# Lesson: `lesson.science.35.soil.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.soil.01` |
| **Title** | Dig deeper — what soil is made of |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 10 min parent-led dig-and-look |
| **Objectives** | `obj.science.35.soil.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.soil.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — the research hand-off is a **parent-led dig-and-look**: dig a cup of real soil, hunt for the four ingredients, record in notebooks/journal. (Kiwix "Soil" optional light read.)

---

## 1. Goal (one sentence)

After this lesson, the child can name soil's four ingredients (rock bits, humus, water, air), say that nature makes soil very slowly (rock crumbles, leaves rot), order the layers (topsoil richest, then subsoil, then rock), explain that soil both holds and feeds plants, and defend the soil's animal helpers (worm tunnels = air + mixing).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Scoop up a handful of soil — what's really inside? Just 'dirt', or a mix?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Five beats: (1) magnified soil = MIX of rock bits + humus + water + air (gloss: humus = rotted dead leaves); (2) made SLOWLY — rock crumbles, leaves rot, hundreds of years (ties to slow change); (3) layers — topsoil dark and richest, subsoil, solid rock; (4) soil HOLDS and FEEDS plants (roots grip + drink nutrients); (5) soil helpers — worms, moles, roly-polys; worm tunnels = air + mixing. Stamp: A MIX, MADE SLOWLY | lessons (stage `teach`) | `anim.science.35.soil.01` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Phase A "Mix the soil": 5 cards Into the mix / Not soil (rejects the plastic bottle); bowl fills as ingredients land. Phase B "Stack the layers": build the column top-down (wrong order retries in place). Phase C "Helper or trouble?": 6 good-for-soil / bad-for-soil scenarios (worm, rotting leaves, mole, roly-poly, buried plastic, washed-away topsoil). Wrong answers name the error and re-queue | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.soil.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 5 | Hand-off | 10 | Parent-led dig-and-look: dig a cup of garden soil, spread it on paper, hunt for all four ingredients (grit, dark crumbs/leaf bits, dampness, crumbly air pockets) → journal: "In my cup of soil I found …" | off-device → journal/notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.soil.01`, `min_score: 4`
- [ ] Task 2: Off-device (parent-tracked): dig-and-look cup of soil, 10 min
- [ ] Task 3: Journal — prompt "In my cup of soil I found …", `min_words: 12`, `lesson_id: lesson.science.35.soil.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.soil.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and walks teach + practice with the child first
- [ ] Task 2: Off-device dig-and-look as above
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** practice telemetry — does the child reject water/air from the mix (soil-is-one-thing), mis-stack the layers, or call the worm "bad for the soil" (worms-wreck-soil)? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the soil recipe again"); then do the real dig-and-look FIRST with the parent naming each ingredient as it is found, and retry the check the next day — the physical cup of soil is the manipulative for this lesson.

## 5. Tools

- **Uses existing:** journal, notebooks, parent quiz (bridge); research (Kiwix "Soil") optional.
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation `anim.science.35.soil.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.soil.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.soil.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on soil, rocks, water drops or air bubbles; worms/moles drawn as helpers at work, never as pests; the plastic bottle clearly artificial.
- Vocabulary with inline glosses: humus (say: HYOO-mus), nutrients (= plant food), topsoil. Read-aloud 🔊 on every instruction.
- Prereq `obj.science.k2.plants.01` (K–2 plants): if the child can't say what a plant needs, run that lesson first.
