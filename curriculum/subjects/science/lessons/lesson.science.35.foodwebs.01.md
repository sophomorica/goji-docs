# Lesson: `lesson.science.35.foodwebs.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.foodwebs.01` |
| **Title** | The jungle food web — energy on the move |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off |
| **Objectives** | `obj.science.35.foodwebs.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.foodwebs.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `jungle-book` — the anchor animals become one energy web: bamboo grass and banyan (producers), deer and the Bandar-log monkeys (herbivore consumers), Shere Khan, the wolf pack, and Kaa (carnivores), mushrooms and dung beetles (decomposers). Extends the Grade 3 jungle unit.

---

## 1. Goal (one sentence)

After this lesson, the child can build a food web with arrows that follow the energy (sun → producers → consumers → decomposers, arrow pointing TO the eater), predict the ripple when one population is removed, and place any jungle organism as producer, consumer, or decomposer — using population/community/ecosystem and niche correctly.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Shere Khan is strong. Where did the energy in his muscles BEGIN?" — child taps a guess (the tiger himself vs the sun); revisited on the result screen | lessons (stage `hook`) | in-package |
| 2 | **Teach** | 3.5 | Five beats: ① energy starts at the sun → producers; ② consumers: herbivore deer, carnivore tiger/wolves; ③ **arrow direction taught explicitly** — the arrow follows the energy, TO the eater; ④ chains cross = a WEB, the deer feeds more than one hunter, niche = the animal's job; ⑤ decomposers close the loop, then population < community < ecosystem as nested rings | lessons (stage `teach`) | `anim.science.35.foodwebs.01` (inline in package) |
| 3 | **Guided practice** | 3 | "Build the jungle web": 7 arrow placements (sun→grass, grass→deer, deer→tiger, deer→wolf, fruit→monkey, monkey→python, dead leaves→beetle) — each correct arrow is drawn onto a growing web diagram; wrong direction names the arrow-at-food error aloud | lessons (stage `practice`, phase A) | — |
| 4 | **Independent practice** | 4 | "Remove the deer — who goes hungry?" ripple taps (tiger + wolf, with Kaa and the monkeys as trap options), then sort 7 organisms into producer / consumer / decomposer bins (drag or tap) | lessons (stage `practice`, phases B–C) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.foodwebs.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 8 | Research: Kiwix "Food web" — find one food chain that is NOT in the jungle lesson → notebooks: draw it with arrows pointing to the eater, label producer/consumer/decomposer (INTEGRATION §4, jungle-book row) | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.foodwebs.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Food web", 8 min
- [ ] Task 3: Notebooks — one new 3-link chain drawn with correct arrows + labels

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.foodwebs.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and builds the web with the child
- [ ] Task 2: Research — "Food web"
- [ ] Task 3: Notebooks — chain drawing as above

## 4. Checks

- **Formative:** phase A — does the child point arrows AT the food (arrow-at-food)? Phase B — does the child think the top hunters are untouched? Phase C — does the child dodge the decomposer bin? The package records which error types fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage (beat 3 is the arrow-direction beat); then re-run phase A only while the parent says the sentence aloud for each pair ("the grass GIVES energy TO the deer — so the arrow goes…"); retry the check next day. If producer/consumer confusion persists, redo the Grade 3 jungle unit's plant-vs-animal sort first (`obj.science.35.ecosystems.01` prereq path).

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.foodwebs.01` authored **inline** (SVG/CSS slides) in the package — brief in `assets/animations/anim.science.35.foodwebs.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.foodwebs.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: arrows pointing from eater to food (the exact misconception); predation gore (the tiger watches, never kills on screen); decomposers drawn as villains or "yuck" — they are the cleanup crew; no faces on sun, leaves, or mushrooms.
- Read-aloud: every instruction has a speaker button (recorded line when generated, Web Speech fallback).
