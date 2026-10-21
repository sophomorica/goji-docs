# Lesson: `lesson.science.k2.sun.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.sun.01` |
| **Title** | Sun and shadows — warm light, blocked light |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 10 min outdoor hand-off |
| **Objectives** | `obj.science.k2.sun.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.sun.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — this is a look-outside lesson. The hand-off IS the anchor: trace a real shadow with a parent in the morning and again in the afternoon, then journal what moved.

---

## 1. Goal (one sentence)

After this lesson, the child can say that the sun warms land, air, and water, that a shadow happens when something **blocks** the light, predict which side of an object its shadow falls on (away from the sun), and pick the shady spot as the cooler one.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Two rocks sat outside all morning — one in the sun, one in the shade. Which feels warmer?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Four beats: sun warms land/air/water (pond + heat shimmer) · touch the sunny rock (warm) vs shady rock (cool) · toy dinosaur slides between sun and ground — shadow appears on the OPPOSITE side · sun glides across the sky and the shadow flips sides. Each idea becomes a badge | lessons (stage `teach`) | `anim.science.k2.sun.01` (inline in package) |
| 3 | **Guided practice** | 1 | First two shadow-lab items with the sun far left / far right — the shadow fades in on the correct spot when tapped, reinforcing "away from the sun" | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Shadow lab, 9 items: 6 "where will the shadow fall?" taps with the sun in different positions + 3 "which spot is cooler / warmer?" taps (tree shade vs open sun). Wrong tap names the misconception aloud and the item re-queues | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.sun.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | Outside with a parent: stand a toy on the sidewalk, chalk-trace its shadow in the morning, come back in the afternoon and trace again → journal one sentence "The shadow moved because …" | off-device → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.sun.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "The shadow moved because …", `min_words: 6`, `lesson_id: lesson.science.k2.sun.01` (after the chalk tracing)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.sun.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser and walks the teach + shadow lab with the child first
- [ ] Task 2: Journal — prompt as above, after the parent-led chalk shadow tracing (morning + afternoon)

## 4. Checks

- **Formative:** shadow lab — does the child tap the SUN side (shadow-on-sun's-side misconception) or miss the cooler-spot items (shade-and-sun-same-temperature)? The package records which in `lesson.check.practice.misses`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the sun again" button); then do the real-world version — parent holds a flashlight on one side of a cup, child points where the shadow will be, flip the flashlight side, repeat 4 times; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.sun.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.sun.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.sun.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no face on the sun** (plain disc + rays only — a smiley sun teaches "sun is a character"); the dinosaur is drawn unmistakably as a wheeled wooden toy (no eyes); the shadow is a flat dark shape ON the ground, never a creature or a thing that "comes out of" the toy.
- Misconceptions encoded: shadow-as-leaking-substance (q1 distractor), shadow-on-the-sun's-side (q2/q5 distractors + lab feedback), shade-same-temperature-as-sun (q3 distractor + lab feedback).
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice when `media/` lands).
