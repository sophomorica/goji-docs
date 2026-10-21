# Lesson: `lesson.science.k2.matter.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.matter.01` |
| **Title** | Property detective — color, shape, feel, size |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5–10 min parent hand-off |
| **Objectives** | `obj.science.k2.matter.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.matter.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — everyday household objects, not book-tied. Hand-off = sort real spoons/socks with a parent + one journal sentence (below).

---

## 1. Goal (one sentence)

After this lesson, the child can name a describing word for an object's color, shape, texture, and relative size/weight, and can sort the SAME set of objects two different ways — understanding that the sorting rule, not the object, decides the group (and that big is not always heavy).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "A BIG balloon. A little rock. Which one is heavier?" — child taps a guess; guess is revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five animated beats: color words (red/blue/yellow) · shape words (round/square/pointy) · feel words (smooth/rough/soft) · size vs weight on a seesaw (big balloon UP, little rock DOWN — "big is not always heavy") · the rule decides the group (same three toys regrouped by color, then by size). Each property becomes a badge | lessons (stage `teach`) | `anim.science.k2.matter.01` (inline in package) |
| 3 | **Guided practice** | 2 | Property detective: 5 one-object rounds — "which word tells its COLOR / SHAPE / how it FEELS / its SIZE?" plus the balloon-vs-rock heavier question. Wrong word → feedback names the property it actually tells ("Round tells its SHAPE, not its color"); misses re-queue | lessons (stage `practice`, part A) | — |
| 4 | **Independent practice** | 3 | Sort, then RE-SORT: six objects (ball, button, kite, sock, plate, mitten) sorted by COLOR into red/blue bins — then the SAME six re-sorted by SIZE into big/small bins. Mixed rules → "Check the rule!" feedback; misses re-queue | lessons (stage `practice`, part B) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.matter.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5–10 | Parent sorting game with real spoons and socks: sort by color, then re-sort the same pile by size → journal one sentence "I sorted the ___ by ___." | parent-led → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.matter.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "I sorted the ___ by ___.", `min_words: 5`, `lesson_id: lesson.science.k2.matter.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.matter.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + detective + double sort with the child
- [ ] Task 2: Journal — prompt as above (parent scribes if needed)

## 4. Checks

- **Formative:** the package's telemetry splits misses into `wrongprop` (answered a shape word when asked for color, etc.), `bigheavy` (picked the balloon as heavier), and `rulemix` (kept sorting by color after the rule changed to size) — posted in the check's `practice` field.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the describing words again" button); then a physical re-teach — parent lays out 4 real objects and asks one property question per object with the answer word offered against ONE wrong word; re-sort a two-object pile; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.matter.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.matter.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.matter.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions targeted: "big = heavy" (balloon vs rock in hook, teach seesaw, practice, and check); mixing sort rules mid-sort (the whole re-sort mechanic exists for this); property-word confusion (each wrong option's feedback names which property that word really tells).
- Must-not-show: no faces or eyes on any object (they're all non-living — guards the living.01 boundary); the balloon is clearly a balloon on a string, not a creature.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice lines when `media/` lands).
