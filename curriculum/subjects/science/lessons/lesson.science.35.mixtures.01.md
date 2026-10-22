# Lesson: `lesson.science.35.mixtures.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.mixtures.01` |
| **Title** | The dissolve-or-not lab — what mixes with water |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 15 min kitchen hand-off |
| **Objectives** | `obj.science.35.mixtures.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.mixtures.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — standalone science unit. Hand-off named per PRACTICES §3.2: the **real kitchen investigation** (salt vs sand in two cups, parent-led, off-device) → journal/notebooks record. This is the year's designated at-home investigation (also serves SOL 3.1's predict-and-test practice — see `skills/science-3.md` summary).

---

## 1. Goal (one sentence)

After this lesson, the child can predict whether a material will dissolve in water (salt, sugar, drink-mix yes; sand, pebbles, flour no — cloudy is not dissolved), explain that dissolved material is still there in pieces too small to see (and how to prove it), state that some liquids like oil refuse to mix, and predict that hot water dissolves things faster than cold.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Stir salt into water — it disappears! Where did it go?" Child taps a guess (gone forever / still there hiding); revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Five beats: (1) salt dissolves but is STILL THERE — taste it, or evaporate the water and it comes back; (2) sand never dissolves — it settles; (3) oil floats — liquids can refuse to mix; (4) hot vs cold sugar race — hot wins; (5) the three lab rules | lessons (stage `teach`) | `anim.science.35.mixtures.01` (inline in package) |
| 3 | **Guided practice** | 2 | First two predict-then-test rounds with the parent (bridge) or with the hint feedback (solo): every answer shows the TEST result, not just right/wrong | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 5 | Predict-then-test lab, 8 rounds: salt, sugar, sand, pebbles, drink-mix, flour (the cloudy trick), the hot-vs-cold race prediction, and "where did the salt go?" Misses name the misconception and re-queue | lessons | — |
| 5 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.mixtures.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 15 | **Kitchen test with a parent:** two cups of water — a spoon of salt in one, a spoon of sand in the other; predict first, stir, wait, observe. Optional third round: sugar in warm vs cold water. Record predictions + results in journal ("I predicted… the test showed…") | off-device (parent-led) → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.mixtures.01`, `min_score: 4`
- [ ] Task 2: Household — kitchen dissolve test with parent (salt vs sand, two cups)
- [ ] Task 3: Journal — prompt "I predicted… the test showed…", `min_words: 15`, `lesson_id: lesson.science.35.mixtures.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.mixtures.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + lab with the child
- [ ] Task 2: Household — kitchen test as above
- [ ] Task 3: Journal — record as above

## 4. Checks

- **Formative:** lab telemetry — `gone` misses mean dissolved-equals-destroyed persists; `stir` misses mean the everything-dissolves belief; `temp` misses mean the hot/cold rule didn't land; `cloudy` flags the flour trick. The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** the kitchen test IS the remediation — run the real salt-vs-sand cups with the parent, then taste-test salty water and (parent-supervised) leave a saucer of it to dry overnight to see the salt return; retry the check next day.
- **Safety note for the plan:** taste tests use clean cups and kitchen salt/sugar only, parent poured; nothing from the lab bench metaphor is real chemistry.

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge), household task (kitchen test).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.35.mixtures.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.mixtures.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.mixtures.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions driving distractors: **"dissolved = gone forever/destroyed"** (beat 1, lab round 8, check items 1 and 4); **"everything dissolves if you stir hard enough"** (beat 2, sand/pebbles/flour rounds, check item 2); **"hot and cold water act the same"** (beat 4, race round, check item 3).
- Must-not-show: never show dissolved material simply ceasing to exist without the still-there proof; no faces/eyes on beakers, spoons, materials.
- Read-aloud: every instruction has a speaker button. Inline glosses for band vocabulary: *dissolve*, *mixture*, *evaporate* ("let the water dry up").
