# Lesson: `lesson.science.k2.resources.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.resources.02` |
| **Title** | Only so much |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 12 min on Goji + a week-long family reduce habit |
| **Objectives** | `obj.science.k2.resources.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.resources.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — the hand-off is a **family choice**: pick ONE reduce habit for this week (faucet off while brushing, lights off when leaving, shorter bath) → journal it, parent signs off at week's end. Builds on the K.11 reuse hunt (`lesson.science.k2.resources.01`).

---

## 1. Goal (one sentence)

After this lesson, the child can say that water, trees and soil come from nature and are limited (a forest of stumps doesn't refill by morning — and the birds lose their home), and can pick the right help for a scenario, telling reduce (use less), reuse (use again) and recycle (old made new) apart as three different helps.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "We cut down EVERY tree today. Will new tall trees be there tomorrow?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Forest scene: nature gives (stream, trees, soil) → take every tree: stumps, the bird has nowhere to land (LIMITED) → replant beat: a sapling takes many years → the three helps, one at a time: REDUCE (faucet off) · REUSE (jar → crayon cup) · RECYCLE (old paper → mill → new paper) | lessons (stage `teach`) | `anim.science.k2.resources.02` (inline in package) |
| 3 | **Guided practice** | 2.5 | Six which-help-fits scenario taps (running faucet→reduce, jam jar→reuse, newspapers→recycle, back of paper→reuse, lights on→reduce, metal can→recycle) — a wrong R names what that R actually means | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 1 | The habitat choice: berry bush in the woods — take some and leave some for the birds (vs instant-refill / doesn't-matter) | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.resources.02`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | the week | Family picks ONE reduce habit for the week → journal "Our reduce habit: ___"; end-of-week entry "Did we keep it?"; parent signs off | journal (family) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.resources.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Our family reduce habit this week: ___", `min_words: 6`, `lesson_id: lesson.science.k2.resources.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.resources.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser first and walks the forest + three helps with the child
- [ ] Task 2: Journal — reduce-habit prompt as above (family activity)

## 4. Checks

- **Formative:** the reuse-vs-recycle discriminators (jam jar, back of paper) — does the child call every help "recycle" (three-Rs-one-word)? The package records which R was wrongly tapped.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge) + the week's reduce-habit journal with parent sign-off.
- **If not yet:** replay the Teach stage only ("watch the forest again"); then re-run just the three cleanest scenarios (faucet=reduce, jar=reuse, can=recycle) with the parent saying each help's one-line definition before the tap; retry the check next day with fresh scenario variants.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` per [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.resources.02` is authored **inline** (SVG/CSS forest + helps chips) in the package — brief in `assets/animations/anim.science.k2.resources.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.resources.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no guilt-tripping or doom (the bare-hill beat is sad-but-fixable, replanting follows immediately); no faces on stumps, bins, faucets or any non-living thing; the three R's never collapsed into one word — each gets its own beat, icon and definition.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded lines when media lands).
