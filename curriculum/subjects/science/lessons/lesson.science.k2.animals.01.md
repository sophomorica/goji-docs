# Lesson: `lesson.science.k2.animals.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.animals.01` |
| **Title** | The fox's parts have jobs |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 12 min on Goji + 5 min research hand-off |
| **Objectives** | `obj.science.k2.animals.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.animals.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `aesop-fables` — *The Fox and the Crow* week. Both fable animals star: the **fox** is the specimen (this is the flagship Grade 1 science unit on the animal-of-the-week chain, INTEGRATION §4), the **crow** is the comparison animal, and the check's last item is the fable's cheese. Retake variants swap the specimen for the current fable animal.

---

## 1. Goal (one sentence)

After this lesson, the child can point to an animal part and name the job it does (fox ears hear, tail balances and warms, teeth eat meat, legs run; crow beak/wings/claws), say that animals are **born** with parts that fit their life and share the same basic needs, and sort animals by covering (fur / feathers / scales).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "A mouse squeaks far away. The fox hears it! Which part does that job?" — child taps ears or tail; guess revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Six beats: ears→hear the mouse · tail→balance + warm wrap · teeth→eat meat · legs→run · the crow's different parts (beak/wings/claws), same needs · people too (hands, teeth kinds — light) + "nobody picks their parts" | lessons (stage `teach`) | `anim.science.k2.animals.01` (inline in package) |
| 3 | **Guided practice** | 3 | Six "which part does this job?" taps on the labeled fox/crow scene — wrong tap names the tapped part's REAL job and re-queues | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 2 | Four covering sorts (rabbit→fur, duck→feathers, fish/snake→scales); wrong pick names what that covering actually is | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.animals.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5 | Research: open Kiwix "Fox" — find ONE job a fox part does → journal one sentence "The fox's ___ helps it ___." | research → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.animals.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Fox", 5 min
- [ ] Task 3: Journal — prompt "The fox's ___ helps it ___.", `min_words: 6`, `lesson_id: lesson.science.k2.animals.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.animals.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser first and walks the teach + taps with the child
- [ ] Task 2: Research — "Fox"
- [ ] Task 3: Journal — prompt as above

## 4. Checks

- **Formative:** part-tap round — does the child swap jobs (tail for hearing) or pick coverings by look-alike (fur for the duck)? The package records which misconception key was tapped.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch the jobs again" button); then re-run just the four fox part taps (ears/tail/teeth/legs — no crow, no coverings) with the parent naming each job aloud first; retry the check next day with the new fable animal as specimen.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` per [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.animals.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.animals.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.animals.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no animal "deciding" to grow a part (no wish-then-poof); no animals using human tools or eating people-food; the fox calm and non-scary (teeth beat shows eating, not menace); no faces on non-living things.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded lines when media lands).
- Fox is the one recurring character in `assets.json` (`characters.fox` + `ref` on fox images).
