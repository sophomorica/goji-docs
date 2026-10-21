# Lesson: `lesson.science.k2.materials.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.materials.01` |
| **Title** | The material tester — what is it made of? |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 13 min on Goji + 5 min flashlight hand-off |
| **Objectives** | `obj.science.k2.materials.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.materials.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — this is a physical-science observation lesson; the hand-off is a real flashlight material test at home with the parent, ending in a journal sentence.

---

## 1. Goal (one sentence)

After this lesson, the child can name the material an everyday object is made of (a spoon can be wood OR metal — object and material are different words), say that cutting something into smaller pieces does not change its material (small pieces of paper are still paper), and predict whether light passes through a material — all, some, or none — including the trap that thin does not mean see-through.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Two spoons. Same shape. Are they made of the same thing?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | The material tester, five beats: object vs material (wood spoon / metal spoon) · one material makes many objects (wood → spoon, chair, block) · cut the paper — every small piece is STILL paper · flashlight test: window glass lets ALL light through, wax paper SOME · wood board lets NONE — and neither does a thin wooden ruler: thin does not mean see-through | lessons (stage `teach`) | `anim.science.k2.materials.01` (inline in package) |
| 3 | **Guided practice** | 2 | First three tester rounds with hints visible: metal spoon (what material?), cut paper (still paper?), window glass (how much light?) — wrong tap names the exact mix-up aloud | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Nine tester rounds total: what-is-it-made-of taps (spoon, chair, cup), cut-in-half questions (paper, wax candle), and the flashlight sort (glass / wax paper / wood board / thin cardboard) into all / some / none; misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.materials.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Flashlight material test at home with parent: shine a flashlight at a window, a sheet of paper, a wooden door, a glass of water — sort them all / some / none → journal one sentence "Light goes through ___ but not ___." | journal (parent alongside) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.materials.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Light goes through ___ but not ___.", `min_words: 6`, `lesson_id: lesson.science.k2.materials.01` (after the flashlight test with the parent)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.materials.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the tester rounds with the child
- [ ] Task 2: Journal — prompt as above, parent leads the home flashlight test first

## 4. Checks

- **Formative:** practice rounds — does the child say the cut pieces are "not paper any more"? Does the child predict light passes through the thin cardboard? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button), pausing on beat 3 (the cut paper) and beat 5 (the thin ruler); then do the real thing — parent cuts an actual sheet of paper with the child and asks "what are the pieces?", and shines a real flashlight at a thin ruler; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.materials.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.materials.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.materials.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Prereq: `obj.science.k2.matter.01` (K.3 property words — color, texture, size) — this lesson adds the material layer on top of properties.
- Must-not-show: no faces or eyes on spoons, cups, boards, or any object; the cut paper pieces always keep the paper's color/pattern so "still paper" is visible; the flashlight beam is always drawn stopping AT an opaque material, dimming INSIDE wax paper, and passing THROUGH glass — never ambiguous.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice when `media/` present).
