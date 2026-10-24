# Lesson: `lesson.science.k2.forces.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.forces.02` |
| **Title** | Invisible forces: gravity and magnets |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 14 min on Goji + 5 min hand-off |
| **Objectives** | `obj.science.k2.forces.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.forces.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — physical-science unit. Research hand-off named: fridge-magnet "what sticks?" hunt with a parent → journal sentence (below).

---

## 1. Goal (one sentence)

After this lesson, the child can say that some forces need a touch (kick, push) and some work at a distance — gravity pulls everything down, magnets pull or push some metals without touching — and can predict what a magnet will and won't grab, including through paper and when two same ends meet.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The magnet is NEAR the paperclip — not touching. Can it make the clip move?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Five beats: kick = a touch force · gravity pulls the apple down with no touch · gravity pulls the feather too (air slows it) · a magnet pulls a paperclip through air and even paper, but only iron/steel · two ends: different ends snap, same ends push apart | lessons (stage `teach`) | `anim.science.k2.forces.02` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Invisible-forces lab, 8 predict-then-test questions: paperclip (grab), crayon (no), through-paper (yes), aluminum can (no — not ALL metal), ball off table (down), feather (falls slowly), N–N (push apart), N–S (snap). Wrong prediction → the specific misconception is named aloud and the item re-queues | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.k2.forces.02`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 5 | Fridge-magnet hunt with a parent: try the magnet on 5 kitchen things — journal one sentence "The magnet stuck to ___ but not ___ because ___." | off-device (parent) → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.forces.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "The magnet stuck to ___ but not ___ because ___", `min_words: 8`, `lesson_id: lesson.science.k2.forces.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.forces.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + lab with the child
- [ ] Task 2: Journal — prompt as above (parent runs the real fridge hunt first)

## 4. Checks

- **Formative:** the lab logs which misconception each miss encodes — does the child grab-everything the crayon (magnets-grab-everything), grab the aluminum can (all-metal), or snap N–N (same-ends-snap)? The package records `misses` per misconception in `lesson.check`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the forces again" button); then re-run just the four magnet lab items with a real fridge magnet and a real paperclip/crayon in hand (parent-led — feeling the pull beats seeing it); retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge); parent-led magnet kit is off-device per `skills/science-2.md` row 2.2.
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.forces.02` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.forces.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.forces.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on magnets, balls, feathers or cans; the magnet never grabs the aluminum can or the crayon anywhere on screen; nothing ever falls up or floats without a named reason (air).
- Prereq: `obj.science.k2.forces.01` (pushes and pulls) — this lesson deliberately extends "nothing moves by itself" to "…unless an invisible force pulls it."
- Read-aloud: every instruction has a speaker button (recorded line else Web Speech; silent fallback keeps text).
