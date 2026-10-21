# Lesson: `lesson.science.k2.change.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.change.02` |
| **Title** | The land changes too — fast changers, slow sculptors |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 12 min on Goji + 10 min outdoor hand-off |
| **Objectives** | `obj.science.k2.change.02` (prereqs: `obj.science.k2.change.01` — fast/slow change on *things*; `obj.science.k2.weather.02` — the observation habit) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.change.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — hand-off is a real-world hunt: find **one thing outside changed by weather** (rusty bolt, worn stone step, wind-bent tree) with a parent → journal sentence.

---

## 1. Goal (one sentence)

After this lesson, the child can say that living things respond to weather and seasons (geese fly, trees drop leaves, people bundle up), that wind and water change the land — slowly (canyon, sand, dunes) and fast (storm branch, flood) — and can sort a given change as fast or slow and name wind or water as its cause.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Who carved this giant canyon — a digger machine or a river?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: (1) seasons change and living things ANSWER (geese/leaves/coats); (2) water is a SLOW sculptor — the river carves the canyon little by little, too slow to watch but never stopping; (3) waves grind rock into sand, wind walks the dunes; (4) FAST changes — storm snaps a branch, flood moves soil in an afternoon; (5) recap — wind and water never rest, fast or slow | lessons (stage `teach`) | `anim.science.k2.change.02` (inline in package) |
| 3 | **Guided → independent practice** | 4 | (A) Fast-or-slow sort, 6 cards (canyon, storm branch, sandcastle wave, rusting swing, drifting dune, flood) — wrong drop → "could you stand and watch it happen?" read aloud; misses re-queue. (B) "Who did it?" detective taps: canyon→water, dunes→wind, smooth pebbles→water; plus one animals-respond item (geese in autumn). Wrong options name their misconception (someone-dug, never-changed, seasons-don't-reach-animals) | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.change.02`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 10 | Outside with a parent: find one thing weather changed (rust, worn step, bent tree, smoothed stone) → journal "The … was changed by …" | journal (+ parent) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.change.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Find one thing outside that weather changed. The … was changed by …", `min_words: 8`, `lesson_id: lesson.science.k2.change.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.change.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Journal — weather-changed-it hunt prompt as above (parent alongside)

## 4. Checks

- **Formative:** the sort — does the child call the canyon "fast" or refuse "slow = still happening" (invisible-change denial)? The detective taps — does the child pick "someone dug it"? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again"); then re-run `lesson.science.k2.change.01`'s fast/slow sort language on 3 *object* changes (ice melting, plant growing, leaf falling) to rebuild the fast/slow idea before returning to land changes; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.change.02` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.change.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.change.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no machines/diggers in any land-change scene (the hook's digger appears only as the wrong guess); storm beats stay calm (distant lightning, no destruction of homes); no faces on clouds, rocks, dunes, water, or the digger.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
