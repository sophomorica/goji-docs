# Lesson: `lesson.science.35.conservation.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.conservation.01` |
| **Title** | The caretakers — protecting ecosystems |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off + family water-saving pick |
| **Objectives** | `obj.science.35.conservation.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.conservation.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `jungle-book` (light) — the jungle studied all year closes the science sequence: its health depends on caretakers. Builds on this wave's `lesson.science.35.ecosystems.01` and `lesson.science.35.soil.01`.

---

## 1. Goal (one sentence)

After this lesson, the child can name how ecosystems get hurt by nature (fire, flood, disease — knowing some fires renew) and by people (litter, cutting every tree, wasting water), explain erosion as the soil thief on bare land, and pick the matching conservation counter-move (plant cover, use less water, keep streams clean, replant) — including moves a kid can make.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Ecosystems can get hurt. Who can help them heal — only grown-ups, or kids too?" — child taps a guess; revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 4 | Five beats: (1) nature's hurts — fire, flood, disease, honest-simple nuance: some fires clear brush and renew; (2) people's hurts — litter in the stream, every tree cut, wasted water; (3) EROSION revisited from the soil lesson — bare land + rain = soil thief, muddy stream; (4) conservation counter-moves — plant cover, use less water, keep streams clean, replant; (5) kids are caretakers — the year's jungle stays healthy when tended | lessons (stage `teach`) | `anim.science.35.conservation.01` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Phase A "Cause and effect": 4 cause→true-effect matches (bare hill + rain → muddy stream; all trees cut → homes lost; litter → downstream sickness; endless shower → less for everyone). Phase B "Pick the counter-move": 6 caretaker scenarios covering water-saving (tap, morning watering), soil cover (garden hill, winter cover crop), habitat/stream care (cleanup, replanting); each includes a "nothing a kid can do"-style distractor. Caretaker badges light up | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.conservation.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 5 | Hand-off | 8+ | (a) Family water-saving pick: choose ONE water-saving move together tonight (journal it); (b) Research: Kiwix "Erosion" → notebooks: two facts | off-device + research → journal/notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.conservation.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Erosion", 8 min
- [ ] Task 3: Journal — prompt "Our family's water-saving move is … It helps because …", `min_words: 12`, `lesson_id: lesson.science.35.conservation.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.conservation.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and walks teach + practice with the child first
- [ ] Task 2: Research — "Erosion"
- [ ] Task 3: Journal — family water-saving pick as above

## 4. Checks

- **Formative:** practice telemetry — does the child pick "nothing a kid can do" (helplessness), "erosion only happens in deserts", or "no harm — the stream carries it away"? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch hurts and helps again"); then re-run Phase B with the parent asking, for each scenario, "what does the soil / water / animal NEED here?" before the child taps; if erosion specifically misses, re-run the erosion beat plus `lesson.science.35.soil.01`'s washed-topsoil item; retry the check next day.

## 5. Tools

- **Uses existing:** research (Kiwix), journal, notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation `anim.science.35.conservation.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.conservation.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.conservation.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: fire/flood/disease drawn calm, never frightening; no injured or dead animals; fire nuance kept honest-simple (small ground fire clearing brush, green shoots beyond) without teaching "fire is fine"; no guilt-tripping imagery of children.
- Vocabulary with inline glosses: conservation (= protecting what the ecosystem needs), erosion (revisited from the soil lesson). Read-aloud 🔊 on every instruction.
- Prereqs are same-wave: `obj.science.35.ecosystems.01` (who uses what in the ecosystem) and `obj.science.35.soil.01` (topsoil, slow-made) — run those first; this lesson deliberately closes the grade-3 science year.
