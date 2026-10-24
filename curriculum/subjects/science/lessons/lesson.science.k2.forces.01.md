# Lesson: `lesson.science.k2.forces.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.forces.01` |
| **Title** | Pushes and pulls — what makes things move |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5–10 min parent hand-off |
| **Objectives** | `obj.science.k2.forces.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.forces.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — force play is physical, not book-tied. Hand-off = parent push-pull scavenger hunt at home + one journal sentence (below). (Deliberate contrast with `lesson.science.k2.living.01`: the wolf moves *by itself*; the wagon never does.)

---

## 1. Goal (one sentence)

After this lesson, the child can say that a push or a pull makes an object move, that a pull works just as well as a push (toward you instead of away), that a stronger push moves things farther, and that nothing starts moving all by itself.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Here is a wagon, sitting very still. Can it start moving all by itself?" — child taps a guess; guess is revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Five animated beats: push = away (ball) · pull = toward (wagon) · gentle vs strong (same ball, two distances) · a push can change direction · nothing moves by itself (wagon waits… until a hand pushes). Each idea becomes a badge | lessons (stage `teach`) | `anim.science.k2.forces.01` (inline in package) |
| 3 | **Guided + independent practice** | 5 | Push-pull playground: 8 **predict-then-test** rounds on a ball, a wagon, and a swing. Child predicts (2 big buttons), taps "Test it!", watches the scene move (or refuse to move), gets misconception-named feedback; wrong predictions re-queue | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.forces.01`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 5–10 | Parent push-pull scavenger hunt: find 3 pushes and 3 pulls around the house (door, drawer, zipper, ball…) → journal one sentence "I pulled the ___ / I pushed the ___" | parent-led → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.forces.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "I pushed the ___. I pulled the ___.", `min_words: 6`, `lesson_id: lesson.science.k2.forces.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.forces.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + playground with the child
- [ ] Task 2: Journal — prompt as above (parent scribes if needed)

## 4. Checks

- **Formative:** the playground records which misconception each wrong prediction hit (`onlypush`, `strength`, `self`, `direction`) and posts it in the check's `practice` telemetry — does the child predict the swing will start by itself, or that gentle and strong pushes travel the same?
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch pushes and pulls again" button); then a physical re-teach with a real ball — parent says "gentle" / "strong" and the child pushes, then the child pulls a towel with a toy on it; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.forces.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.forces.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.forces.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions targeted: "only pushes cause motion" (pulls tested twice: wagon handle, rope on ball); "a stronger push doesn't matter" (gentle vs strong, stuck wagon); "things move by themselves" (untouched swing round + teach beat 5, explicit contrast with the living-things lesson).
- Must-not-show: no faces or eyes on the ball, wagon, or swing (non-living things stay clearly non-living); only a hand and forearm ever apply force — never an unexplained self-start.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice lines when `media/` lands).
