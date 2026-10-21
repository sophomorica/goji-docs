# Lesson: `lesson.science.k2.plants.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.plants.01` |
| **Title** | Grow a plant — parts with jobs, and what every plant needs |
| **Band** | K–2 (grade hint 1) |
| **Duration (target)** | 13 min on Goji + 10 min seed-cup hand-off |
| **Objectives** | `obj.science.k2.plants.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.plants.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** n/a — this is a living-systems lesson; the hand-off is starting a real seed cup with the parent and a journal sentence, which ties into the `obj.science.k2.change.01` observation-journal habit (the growing seed becomes the ongoing slow-change log).

---

## 1. Goal (one sentence)

After this lesson, the child can point to each plant part and name its JOB — roots drink water and hold the plant, the stem carries water up and holds the plant up, leaves make food from light and air (plants do not eat soil), the flower makes seeds — and can pick what a plant needs (water, light, air, soil with nutrients, a place to grow) versus what it does not (candy, toys).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "This plant is droopy. What will make it better — water, or candy?" — child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Grow-a-plant, five beats: ROOTS drink water and hold the plant tight (water drops travel up — the roots drink, they don't "eat dirt") · STEM carries the water up and holds the plant up · LEAVES make the plant's food from light and air (the plant's kitchen — soil is not food) · FLOWER makes seeds for new plants (a job, not a decoration) · the wilting plant rescued: give water, light, air, soil, and a place to grow, and it stands tall again | lessons (stage `teach`) | `anim.science.k2.plants.01` (inline in package) |
| 3 | **Guided practice** | 2 | First rounds of tap-the-part with the part names visible: "Which part drinks?" "Which part makes food?" — wrong tap names the exact mix-up aloud ("leaves don't drink from soil — they make food from light and air") | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 4 | Eleven rounds total: five which-part-does-this-JOB taps on the plant (drinks / carries+holds up / makes food / makes seeds / holds tight in soil), then six give-the-plant-what-it-needs rounds (sun lamp ✓, water ✓, soil ✓, air ✓, candy ✗, toy ✗ — echoes `obj.science.k2.needs.01`); misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.plants.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | Start a real seed cup with the parent: cup, soil, bean seed, water, windowsill → journal one sentence "My seed has soil, water, light and air. Now it needs time to grow." — then keep observing it in the journal (the `change.01` slow-change habit) | journal (parent alongside) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.plants.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "My seed cup has ___. Now it needs ___.", `min_words: 6`, `lesson_id: lesson.science.k2.plants.01` (after planting the seed cup with the parent)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.plants.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the plant rounds with the child
- [ ] Task 2: Journal — prompt as above, parent leads the seed-cup planting first

## 4. Checks

- **Formative:** practice rounds — does the child tap the LEAVES when asked which part drinks (leaves-eat-dirt)? Does the child say the plant doesn't need air? Does the child give the plant candy? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button), pausing on beat 3 (leaves make food — soil is not food); then re-run just the five tap-the-part rounds with the part names spoken first; retry the check next day, ideally after looking at the real seed cup together and naming each part it will grow.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.plants.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.plants.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.plants.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Prereq: `obj.science.k2.needs.01` (K.7a animal needs) — the needs rounds deliberately reuse its candy/toy distractors so "living things need real things, not treats" carries over from animals to plants.
- Must-not-show: never draw roots "munching" soil or a mouth anywhere (no faces on the plant, sun, or any object); water is always drawn traveling roots → stem → leaves so the drinking path is visible; the flower's seeds must visibly fall and sprout so "makes seeds" reads as a job, not decoration.
- Read-aloud: every instruction has a speaker button (Web Speech API; recorded voice when `media/` present).
