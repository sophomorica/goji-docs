# Lesson: `lesson.science.k2.matter.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.matter.02` |
| **Title** | Shape-shifter: solid, liquid, gas |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 14 min on Goji + 5 min hand-off |
| **Objectives** | `obj.science.k2.matter.02` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.matter.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — physical-science unit. Research hand-off named: kitchen chocolate-melt watch with a parent → journal sentence (below).

---

## 1. Goal (one sentence)

After this lesson, the child can say that matter has mass and takes up space, sort things as solid (keeps its shape), liquid (takes the container's shape — even slow honey), or gas (fills all the space — even "invisible" air and steam), and predict that heating melts/boils and cooling freezes while the stuff stays the SAME stuff.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The same juice goes into a tall cup, a round bowl, a wide dish. Does it keep one shape?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: matter has mass + takes space (even air) · solids keep their shape (block in a cup) · liquids take the container's shape (same juice, three containers) · gases fill ALL the space (balloon; air is not nothing) · heat melts chocolate / boils water, cold freezes — and it's the SAME stuff every time | lessons (stage `teach`) | `anim.science.k2.matter.02` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Two-part lab: (a) 8-card sort into SOLID / LIQUID / GAS bins (drag or tap): block, milk, balloon air, honey (slow liquid), steam (gas), sand (many tiny solids), ice cube, juice — wrong drop names the specific misconception and re-queues; (b) heat lab, 3 predictions: heat chocolate (melts, still chocolate), boil water (steam, a gas), freeze juice (solid) | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.k2.matter.02`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 5 | Kitchen watch with a parent: melt one square of chocolate in a warm spoon/bowl, let it cool again → journal one sentence "The chocolate melted into a liquid, but it was still chocolate because ___." | off-device (parent) → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.matter.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "The chocolate melted into a liquid, but it was still chocolate because ___", `min_words: 8`, `lesson_id: lesson.science.k2.matter.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.matter.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Journal — prompt as above (parent runs the real chocolate-melt first)

## 4. Checks

- **Formative:** the sort logs which misconception each miss encodes — does the child drop *sand* into LIQUID (pours-means-liquid), call the balloon "nothing" (gas-is-nothing), or expect melted chocolate to be new stuff? The package records `misses` per misconception in `lesson.check`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch solid, liquid, gas again"); then a real-objects re-sort at the table (spoon, water cup, empty jar "full of air" — parent-led, three bins on paper) before retrying the check next day. Prereq refresh if the ice/steam items miss: `lesson.science.k2.water.01` (ice and steam are the same water).
- **Ties back:** `obj.science.k2.matter.01` (describing/sorting by properties) supplies the sorting habit; `obj.science.k2.water.01` supplies "ice = steam = same water" that this lesson generalizes to chocolate and juice.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge); kitchen ice/steam/chocolate demo is off-device parent-led per `skills/science-2.md` row 2.3.
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.matter.02` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.matter.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.matter.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on blocks, balloons, pots or chocolate; melted chocolate always stays brown chocolate (never becomes a "new" food); steam always drawn as visible wisps of water gas, never as smoke; the balloon interior shows air dots (gas is real stuff).
- Phase-change examples deliberately go beyond water (chocolate, juice) so "melting = same stuff" isn't memorized as a water-only fact.
- Read-aloud: every instruction has a speaker button (recorded line else Web Speech; silent fallback keeps text).
