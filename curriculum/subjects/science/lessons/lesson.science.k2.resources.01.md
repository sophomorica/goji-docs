# Lesson: `lesson.science.k2.resources.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.resources.01` |
| **Title** | Earth helpers — the Earth gives, we choose |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 10 min home reuse-hunt hand-off |
| **Objectives** | `obj.science.k2.resources.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.resources.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — home-and-outdoors lesson. Hand-off: find 3 things at home to reuse with a parent, journal them; the Kiwix "Recycling" article is the parent read-aloud extension.

---

## 1. Goal (one sentence)

After this lesson, the child can say that the things we use come from the Earth (water, wood, food), sort a used item into **trash / reuse / recycle** (and say how reuse differs from recycle), and explain that our choices touch the water, land, air, and animals — trash doesn't disappear, and one person's choice matters.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "You drink a cup of water. Where did it come from — the Earth, or the store?" — child taps a guess; revisited at the end ("the store gets it from the Earth!") | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Three beats: the Earth gives (stream = water, tree = wood planks, garden = food) · when we're done we CHOOSE — three bins; the jar drops into REUSE; the truck hauls trash to a LANDFILL ("it does not disappear"); reuse = use again, recycle = made into something new · one gentle split scene: clean stream full of life vs littered stream where the animals left ("every choice matters — even one wrapper"). Each beat becomes a badge | lessons (stage `teach`) | `anim.science.k2.resources.01` (inline in package) |
| 3 | **Guided practice** | 1.5 | First two sorts (glass jar → reuse, drawing paper → recycle) with drag or tap; feedback says WHY (use again vs made into new) | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Four more sorts (banana peel → trash/compost, plastic bottle → recycle, old t-shirt → reuse, sticky wrapper → trash) then two "which choice helps the stream?" scenario taps (pocket the wrapper; take the bottle home). Wrong answers name the misconception aloud and re-queue — 8 interactions total | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.resources.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | With a parent: hunt the house for 3 things to reuse (jar → crayon cup, shirt → rag, box → treasure chest) → journal "I reused a … as a …"; parent optionally reads the Kiwix "Recycling" article aloud | off-device → journal (+ research for parent) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.resources.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "I reused a … as a …", `min_words: 6`, `lesson_id: lesson.science.k2.resources.01` (after the home reuse hunt)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.resources.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser and walks the teach + bin sort with the child first
- [ ] Task 2: Journal — prompt as above, after the parent-led home reuse hunt

## 4. Checks

- **Formative:** the sort logs `misses.reuse_recycle` (treats reuse and recycle as the same), `misses.trash_default` (trashes everything), `misses.compost` (recycles food), `misses.onep` (one-person-doesn't-matter), `misses.disappear` (trash vanishes) in `lesson.check.practice.misses`.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the Earth again"); then a physical 3-bin sort at home — parent sets out three real boxes labeled trash/reuse/recycle and 6 real household items; retry the check next day.

## 5. Tools

- **Uses existing:** journal, research (Kiwix "Recycling" — parent read), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.resources.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.resources.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.resources.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on bins, truck, trash, or the Earth; the littered stream is gentle (murky + empty, no dead or suffering animals — the absence tells the story); banana peel kept simple as "trash or compost" (no separate compost bin at K); no shaming language — choices, not guilt.
- Misconceptions encoded: trash-disappears (q1 distractor + scenario 2 feedback), reuse-equals-recycle (q2/q3 distractors + sort feedback), one-person-doesn't-matter (q4 distractor + scenario 1 feedback), things-come-from-the-store (q5 distractor + hook).
