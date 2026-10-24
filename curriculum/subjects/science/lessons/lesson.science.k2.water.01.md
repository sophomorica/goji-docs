# Lesson: `lesson.science.k2.water.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.water.01` |
| **Title** | The water journey — uses, places, three forms, downhill |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 10 min parent hand-off |
| **Objectives** | `obj.science.k2.water.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.water.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — kitchen-and-weather science, not book-tied. Hand-off = kitchen ice-melt watch with a parent + one journal sentence (below). Optional light Kiwix "Water" read for a curious child (the K.4 slot the skills file flagged).

---

## 1. Goal (one sentence)

After this lesson, the child can name ways we use water, places we find it, its three forms (ice, liquid, steam) — knowing ice and steam are still water — and can predict which way water flows (always downhill, never up).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "An ice cube. A puddle. Are they both water?" — child taps a guess; guess is revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five animated beats: we USE it (drink / wash / grow) · we FIND it (rain → river → lake → ocean panorama) · THREE FORMS (cold→ice, warm→liquid, very hot→steam) · ice and steam are STILL water (stamp: ALL THREE ARE WATER) · water flows DOWNHILL (drop rolls to the low ground; stamp: NEVER UPHILL). Each idea becomes a badge | lessons (stage `teach`) | `anim.science.k2.water.01` (inline in package) |
| 3 | **Guided practice** | 2.5 | "Which form is this?" — 5 tap rounds: ice cube, puddle, steam over a pot, icicles, rain. Distractor options include "not water — its own cold thing" and "just air"; wrong taps get form-specific feedback and re-queue | lessons (stage `practice`, form rounds) | — |
| 4 | **Independent practice** | 2.5 | "Which way will it flow?" — 3 **predict-then-test** slope rounds: hill leaning right, hill leaning left, and a dip with a little hill ("can it climb over by itself?"). Child predicts, taps "Test it!", watches the drop find the low path | lessons (stage `practice`, flow rounds) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.water.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | Kitchen ice-melt watch with a parent: one ice cube on a plate — watch it melt, touch the puddle → journal one sentence "The ice melted into ___." (Optional: parent boils water so the child can SEE steam — parent handles everything hot.) | parent-led → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.water.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "The ice melted into ___.", `min_words: 5`, `lesson_id: lesson.science.k2.water.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.water.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + rounds with the child
- [ ] Task 2: Journal — prompt as above (parent scribes if needed)

## 4. Checks

- **Formative:** practice telemetry splits misses into `icenot` (ice is not water), `steamair` (steam is just air), `uphill` (water can flow up), and `formmix` (ice/liquid/steam confusion) — posted in the check's `practice` field.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the water journey again" button); then the physical re-teach IS the hand-off — melt a real ice cube with the parent and say together "ice is water, frozen"; pour water down a tilted tray and watch it find the low edge; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge), research (Kiwix "Water", optional light touch).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.water.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.water.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.water.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions targeted: "ice is not water" (hook + practice options + check item 1); "steam is air" (practice pot round + check item 2); "water can flow uphill" (all three slope rounds + two check items).
- Must-not-show: no faces on clouds, drops, or the sun (non-living things stay clearly non-living); steam never drawn as smoke (no fire under the pot); the boil demo is parent-only in the hand-off — the package never asks the child to touch anything hot.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice lines when `media/` lands).
