# Lesson: `lesson.science.k2.habitats.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.habitats.01` |
| **Title** | Home sweet habitat — where the hare's needs are met |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 12 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.habitats.01` (prereq: `obj.science.k2.needs.01` — the five needs are the checklist this lesson applies to a place) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.habitats.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `aesop-fables` — the hare (*The Tortoise and the Hare* week). The specimen is the hare; retake variants swap in the current fable animal (and its habitat).

---

## 1. Goal (one sentence)

After this lesson, the child can say that a habitat is the place where an animal's needs are met, name what the hare's meadow provides (food, water, shelter, space), explain that living and nonliving parts work together (sun → grass → hare → fox), and give one example of a habitat changing.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The hare needs a home — green meadow or ice and snow?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: (1) a habitat is where needs are MET; (2) the meadow provides grass-food, stream-water, burrow-shelter, space — four badges light; (3) living + nonliving work together: sun grows the grass, hare eats grass, fox watches hare (kept gentle); (4) the desert meets the *cactus's* needs, not the hare's — different animals, different homes; (5) habitats change: pond shrinks in a hot summer, forest grows back after a fire | lessons (stage `teach`) | `anim.science.k2.habitats.01` (inline in package) |
| 3 | **Guided → independent practice** | 4 | (A) Build-the-habitat: 8-card sort — does this belong in the hare's meadow (grass, stream, burrow, running room) or the cactus's desert (hot sand, blazing sun, little rain, rocky ground)? Wrong drop → "different animals need different homes" read aloud; misses re-queue. (B) Scenario taps: "the stream dries up — what happens to the hare?" then "the rain returns" — each wrong option names its misconception | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.habitats.01`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 5 | Research: open Kiwix "Hare" (or "Meadow") — find one thing the hare's habitat gives it → journal one sentence "The hare's habitat gives it …" | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.habitats.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Hare" (or "Meadow"), 5 min
- [ ] Task 3: Journal — prompt "The hare's habitat gives it …", `min_words: 8`, `lesson_id: lesson.science.k2.habitats.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.habitats.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + build with the child
- [ ] Task 2: Research — "Hare"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** the build sort — does the child put desert cards in the meadow (any-animal-anywhere)? The scenario taps — does the child pick "animals don't need the nonliving parts" or "habitats stay the same forever"? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button), then re-run just practice part A with the parent naming each need aloud against the `obj.science.k2.needs.01` five-needs badges (food, water, shelter, space is the overlap set); retry the check next day with the current fable animal's habitat.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.habitats.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.habitats.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.habitats.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on sun, stream, burrow, cactus, rocks, or clouds; the fox is distant and calm (interdependence stays gentle — no chase, no catch); the desert is shown as *right for the cactus*, never as a "bad" place.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
