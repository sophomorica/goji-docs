# Lesson: `lesson.science.k2.senses.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.k2.senses.01` |
| **Title** | Sense detective — five senses, five body parts |
| **Band** | K–2 (grade hint K) |
| **Duration (target)** | 12 min on Goji + 5–10 min sense-walk hand-off |
| **Objectives** | `obj.science.k2.senses.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.k2.senses.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — K.5 is a body/senses skill, not an animal-of-the-week fit. The research hand-off is a **parent-led sense walk** (off-device, PRACTICES §6) ending in one journal sentence.

---

## 1. Goal (one sentence)

After this lesson, the child can match each of the five senses to its body part (eyes see, ears hear, nose smells, tongue tastes, hands feel) and say which sense — or senses — gave the clue in an everyday scene, including a scene where two senses work together.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Cookies are baking. Your eyes are closed. Which body part tells you?" — child taps nose or eyes; guess is revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2 | Five scenes, one per sense, each lighting a badge: eyes SEE a rainbow · ears HEAR a bird · nose SMELLS bread · tongue TASTES an apple · hands FEEL a fluffy cat. Close: "Five senses — your body's detective team" | lessons (stage `teach`) | `anim.science.k2.senses.01` (inline in package) |
| 3 | **Guided practice** | 2 | First three scenario cards sorted *with* the badge row visible: sweet cookie → tongue, singing bird → ears, rainbow → eyes. Wrong drop reads the mix-up aloud ("Your nose smells — it can't hear") | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 3 | Remaining cards: bread → nose, kitten → hands, lemon → tongue, stinky sock → nose, then the tricky one — **popcorn popping under a lid**: ears OR nose both accepted, feedback teaches that senses work together. Misses re-queue | lessons | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.k2.senses.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 5–10 | Parent sense walk (off-device): outside or around the house, find one thing per sense — then journal one sentence "My ears heard …" | parent-led → journal | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.k2.senses.01`, `min_score: 4`
- [ ] Task 2: Journal — prompt "On my sense walk, my ____ found …", `min_words: 6`, `lesson_id: lesson.science.k2.senses.01` (sense walk itself is off-device, parent-led)

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.k2.senses.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 2: Journal — sense-walk sentence as above

## 4. Checks

- **Formative:** practice sort — does the child drop sound scenes on the nose (organ mix-up) or insist the popcorn needs eyes (must-see-it)? The package records which mix-up by wrong body part.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("watch again" button); then a 5-card sort of the *baseline* pairs only (rainbow, bird, bread, apple, kitten — no multi-sense card) to rebuild the five pairs; retry the check next day with swapped scenes (drum, flowers, ice cube).

## 5. Tools

- **Uses existing:** journal, parent quiz (bridge); sense walk is off-device parent-led by design (PRACTICES §6 hands-on stance).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.k2.senses.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.k2.senses.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.k2.senses.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces/eyes on non-living things (bread, popcorn pot, rainbow stay plain); disembodied organ icons drawn as simple friendly emblems, not anatomical.
- "Taste = tongue" kept simple at K; the nose-helps-taste idea appears only softly in the popcorn "senses team up" line, never as a test item against the child.
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback).
