# Lesson: `lesson.science.k2.motion.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.motion.01` |
| **Title** | The motion museum — four ways things move (and how sound happens) |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 13 min on Goji + 5 min sound-hunt hand-off |
| **Objectives** | `obj.science.k2.motion.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.motion.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — this is a physical-science observation lesson; the hand-off is a real-object sound hunt (rubber band and spoon) with the parent, ending in a journal sentence.

---

## 1. Goal (one sentence)

After this lesson, the child can watch a moving object and name its motion type — straight, circular (around a path), spinning (turns in one spot), or back-and-forth — and can say that sound is made by something vibrating (moving back and forth very fast), including the tricky contrast between spinning and moving in a circle.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The swing moves. The top moves. Do they move the SAME way?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | The motion museum: five animated exhibits, one per beat — arrow slides STRAIGHT · merry-go-round horse travels a CIRCLE path · top SPINS in one spot (explicit contrast with the horse) · swing goes BACK-AND-FORTH · rubber band is plucked, VIBRATES (fast back-and-forth), and that is why we HEAR it | lessons (stage `teach`) | `anim.science.k2.motion.01` (inline in package) |
| 3 | **Guided practice** | 2 | First three museum rounds with the four motion badges visible: ball (straight), top (spinning), merry-go-round (circular) — wrong tap names the exact mix-up aloud | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Nine watch-and-tap rounds: ball, top, merry-go-round horse, swing, drum skin, sled, guitar string, coin, ferris wheel car — includes two sound-makers whose answer is back-and-forth (vibrating); misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.motion.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Sound hunt with parent: stretch a rubber band over a cup and pluck it, tap a spoon on the table — watch and feel the vibration → journal one sentence "I heard the ___ because it vibrated." | journal (parent alongside) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.motion.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "I heard the ___ because it vibrated.", `min_words: 6`, `lesson_id: lesson.science.k2.motion.01` (after the rubber-band-and-spoon hunt with the parent)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.motion.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the museum + rounds with the child
- [ ] Task 2: Journal — prompt as above, parent leads the rubber-band-and-spoon sound hunt first

## 4. Checks

- **Formative:** practice rounds — does the child tap SPINNING for the merry-go-round horse (or CIRCULAR for the top)? Does the child miss that the drum skin moves at all? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button), pausing on beat 3 — the top-vs-horse contrast; then re-run practice with just the four silent exhibits (no sound-makers) to rebuild the four badges; retry the check next day, and do the spoon tap with the parent so the child *feels* a vibration before re-answering item 5.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.motion.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.motion.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.motion.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: never let "spinning" and "circular path" share one visual — the top always stays on its spot, the horse always travels a visible round path; no faces on the top, sled, drum, or any object; sound is never drawn appearing from nothing — waves always start at the vibrating part.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice when `media/` present).
