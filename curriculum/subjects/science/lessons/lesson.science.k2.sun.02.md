# Lesson: `lesson.science.k2.sun.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.sun.02` |
| **Title** | The sun's day trip |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 12 min on Goji + a spread-across-the-day shadow check with a parent |
| **Objectives** | `obj.science.k2.sun.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.sun.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — the research/real-world hand-off is the **same-tree shadow check**: with a parent, look at one tree (or the child's own shadow) in the morning, at noon, and in the evening, then journal what changed. This extends the K.8 chalk shadow-tracing routine (`lesson.science.k2.sun.01`).

---

## 1. Goal (one sentence)

After this lesson, the child can point to where the sun is at morning, noon and evening, predict when a shadow is shortest, say the sun warms land, air AND water, and explain (gently) that at night the sun is still shining — on the other side of the turning Earth.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "You just woke up — where is the sun? Low near the hills, or high overhead?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | One scene, one tree: the sun arcs morning-low (long shadow) → noon-high (shortest shadow) → evening-low (long again); then the great-warmer beat (land, air, water); then the gentle night beat (Earth turns, sun shines on the other side, sun not alive) | lessons (stage `teach`) | `anim.science.k2.sun.02` (inline in package) |
| 3 | **Guided practice** | 2 | Four sun-tracker taps: three sky positions marked on the scene ("It's morning — tap where the sun is", noon, evening, "tap the spot that makes the shortest shadow") — wrong spot names the time that spot really is | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 2 | Four question taps: shortest-shadow time, warm/cool sand pick, sunny/shady puddle pick, where-is-the-sun-at-night — misconception-named feedback, misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.sun.02`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | across the day | With a parent: same tree, three looks (morning / noon / evening) → journal "In the morning the shadow was ___. At noon it was ___." Parent signs off | off-device → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.sun.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Our tree's shadow: morning ___, noon ___, evening ___", `min_words: 8`, `lesson_id: lesson.science.k2.sun.02` (parent helps take the three looks)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.sun.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser first and walks the sun arc with the child
- [ ] Task 2: Journal — shadow-check prompt as above (off-device, parent-led, extends the K.8 tracing)

## 4. Checks

- **Formative:** sun-tracker taps — does the child put the morning sun overhead (noon-swap) or say shadows never change (same-shadow)? The package records which spot/option was tapped.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge) + parent sign-off on the three-look shadow check.
- **If not yet:** replay the Teach stage only ("watch the sun again"); then re-run just the three time→position taps (morning/noon/evening, no shadow questions) while the parent says the time-of-day story aloud; do the real outdoor morning/noon look together the same day, retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` per [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.sun.02` is authored **inline** (SVG/CSS sun-arc scene) in the package — brief in `assets/animations/anim.science.k2.sun.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.sun.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no face on the sun** (plain disc + rays — a smiley sun feeds "the sun is alive"); night beat stays gentle (no scary darkness, stars + a horizon glow); no compass jargon — "the side where it rises / sets" carries east/west.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded lines when media lands).
