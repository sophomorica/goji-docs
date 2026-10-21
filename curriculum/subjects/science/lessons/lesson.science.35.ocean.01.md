# Lesson: `lesson.science.35.ocean.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.ocean.01` |
| **Title** | Down to the deep — the ocean |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 5–10 min research hand-off |
| **Objectives** | `obj.science.35.ocean.01` (prereq `obj.science.35.ecosystems.01`) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.ocean.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a this band — but note the **cross-band tie**: this unit is deliberately shaped as a submarine dive so it revisits richly when `treasure-island` becomes the 6–8 anchor (sailing, navigation, the sea itself — INTEGRATION §1/§4). Research hand-off now: Kiwix "Ocean" or "Coral reef" → notebooks (one floor feature + one deep-sea creature).

---

## 1. Goal (one sentence)

After this lesson, the child can describe the ocean floor's real shape (shelf → slope → abyssal plain → trench, plus ridges), say how the water changes with depth (darker, colder, always salty — the three light zones), name what moves the water (wind → waves, moon → tides, currents = rivers-in-the-sea like the Gulf Stream), and explain that life fills every zone with plankton at the base of the web.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "A submarine dives to the very bottom. What does it find — flat sand, or mountains and canyons?" — child taps a guess; revisited at the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Six beats riding one dive: the floor has SHAPE (dive profile) · light zones + salty/cold (sunlight/twilight/midnight kept vivid) · waves = wind, tides = moon (4.6 tie-in) · currents = rivers-in-the-sea, the Gulf Stream warms places · sunlit reef crowds vs deep-dark specialists (anglerfish) · plankton = the ocean's grass, webs continue underwater | lessons (stage `teach`) | `anim.science.35.ocean.01` (inline in package) |
| 3 | **Guided practice** | 3 | Label-the-dive build: 4 stops in order, shore → deepest; wrong tap → profile chant read aloud, retry in place; track fills with the profile | lessons (stage `practice`, phase 1) | — |
| 4 | **Independent practice** | 4 | Zone→resident matches ×3 (reef fish / anglerfish / "is the deep empty?"), what-moves-the-water cause taps ×4 (waves/tides/Gulf Stream/still-water), plankton-web item ×1; wrong answers name the specific error and re-queue | lessons (phases 2–3) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.ocean.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 6 | Hand-off | 5–10 | Research: Kiwix "Ocean" or "Coral reef" → notebooks: one floor feature + one deep-sea creature and what it eats | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.ocean.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Ocean" (or "Coral reef"), 5–10 min
- [ ] Task 3: Notebooks — "One ocean-floor feature + one deep-sea creature and what it eats"

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.ocean.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser first and walks the dive with the child
- [ ] Task 2: Research — "Ocean" / "Coral reef"
- [ ] Task 3: Journal — "The ocean floor is not flat. On my dive I would pass ___ then ___ then ___." (`min_words: 15`)

## 4. Checks

- **Formative:** practice telemetry — `profile` misses (dive order), `still` misses (still-water), `empty` misses (empty-deep), `cause` misses (waves/tides swapped). The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay only the floor beat and re-run the 4-stop build with the parent tracing the profile with a finger ("beach… drop… flat… CANYON"); for `cause` misses, the two-column chant "wind→waves, moon→tides" plus a re-run of phase 3; retry the check next day. The moon-lesson tides beat (`lesson.science.35.moon.01`) is the prerequisite re-teach for tides confusion.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.ocean.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.ocean.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.ocean.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on non-living things (moon, waves, submarine — the sub is clearly a machine); the floor never drawn flat except in the hook's wrong-guess card; the deep never drawn lifeless.
- Read-aloud: every instruction has a speaker button.
- Ties: tides reuse `obj.science.35.moon.01` (the moon's pull); food-web language reuses `obj.science.35.ecosystems.01` (prereq).
