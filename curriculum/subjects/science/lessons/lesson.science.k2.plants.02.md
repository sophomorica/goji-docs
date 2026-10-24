# Lesson: `lesson.science.k2.plants.02`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.plants.02` |
| **Title** | Thank a plant — products, air, homes, and roots that hold the land |
| **Band** | K–2 (grade hint 2) |
| **Duration (target)** | 12 min on Goji + 10 min home hunt hand-off |
| **Objectives** | `obj.science.k2.plants.02` (prereqs: `obj.science.k2.plants.01` — what plants are/need; `obj.science.k2.resources.02` — natural resources idea) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.plants.02/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — hand-off is a **plant-product hunt at home**: find 5 things that came from plants with a parent → journal list.

---

## 1. Goal (one sentence)

After this lesson, the child can trace everyday products back to plants (wood, cotton, bread-from-wheat, apple, paper, chocolate-from-cacao) and reject non-plant look-alikes (wool = sheep, glass = sand, metal = rock), name what plants give animals (fresh air, homes, food), and predict that a planted hill keeps its soil in the rain while a bare hill washes away.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The wooden chair or the glass cup — which one needed a PLANT to exist?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Five beats: (1) plant products everywhere — table/tree, shirt/cotton, bread/wheat, apple, paper/tree; (2) plants freshen the air we breathe (kept simple); (3) homes and food — nest in the oak, squirrel's acorns, caterpillar's leaves; (4) roots HOLD the soil — two hills in the rain, planted holds, bare washes away; (5) so we take care of plants — replant when we cut | lessons (stage `teach`) | `anim.science.k2.plants.02` (inline in package) |
| 3 | **Guided → independent practice** | 4 | (A) "From a plant, or not?" 8-card sort with tricky cases — bread ✓wheat, wool ✗sheep, paper ✓tree, glass ✗sand, chocolate ✓cacao, wooden chair ✓, cotton shirt ✓, metal fork ✗rock; wrong drop names the error (soft-isn't-plant, nature-but-not-plant, follow-it-back); misses re-queue. (B) Two-hills prediction tap (which keeps its soil?) — on the correct answer the scene updates to show the bare hill washing; plus one who-lives-here match (nest in the oak) | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.plants.02`), score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 10 | At home with a parent: hunt 5 plant products (furniture, clothes, pantry, paper) → journal list "Plant things I found: …" | journal (+ parent) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.plants.02`, `min_score: 4`
- [ ] Task 2: Journal — prompt "Hunt for 5 plant things at home. Plant things I found: …", `min_words: 10`, `lesson_id: lesson.science.k2.plants.02`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.plants.02` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Journal — plant-product hunt prompt as above (parent alongside)

## 4. Checks

- **Formative:** the sort — does the child claim wool (everything-soft-is-plant) or reject bread/paper (bread-isn't-plant)? The two-hills tap — does the child say plants change nothing? The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again"); then with the parent, hold 3 real objects (a wooden spoon, a wool sock, a piece of paper) and play "follow it back — what was it at the very start?" aloud; retry the check next day.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.plants.02` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.plants.02.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.plants.02` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Oxygen is kept as "plants freshen the air we breathe" — no gas-exchange mechanism at grade 2.
- The two-hills scene is one shared SVG used by teach, practice, and check (prediction → reveal), so the erosion claim is always the same picture.
- Must-not-show: no faces on objects, hills, clouds, or tools; the cut-trees item shows stumps and runoff calmly (no machines mid-destruction, no doom framing) and the teach close answers it with replanting.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
