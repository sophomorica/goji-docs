# Lesson: `lesson.science.35.ecosystems.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.ecosystems.01` |
| **Title** | The jungle is a team — ecosystems |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 8 min research hand-off |
| **Objectives** | `obj.science.35.ecosystems.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.ecosystems.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML in any browser. |

**Anchor:** `jungle-book` — Mowgli's Indian jungle IS the ecosystem under study; the river and a dry grassland are the contrast ecosystems.

---

## 1. Goal (one sentence)

After this lesson, the child can say that an ecosystem is all the living things in a place PLUS the nonliving things they use (sun, water, soil, air), tell that different places (jungle / river / dry grassland) are different ecosystems with different residents, and name the relationship in a pair of organisms as eat, help, or compete.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "The jungle has monkeys and fig trees — and sunshine, river water, soil. Which are part of the ecosystem?" — child taps a guess (only living / living AND nonliving); revisited at the end | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Five beats: (1) ecosystem = all living things in one place; (2) PLUS the nonliving they use — sun, water, soil, air; (3) jungle vs river vs dry grassland = different ecosystems, different residents; (4) relationships — python EATS deer, deer EATS grass, bee↔flower HELP, tiger vs python COMPETE for one deer; (5) recap stamp LIVING + NONLIVING | lessons (stage `teach`) | `anim.science.35.ecosystems.01` (inline in package) |
| 3 | **Guided → independent practice** | 5 | Phase A "Build the jungle": 9 cards tapped Belongs / Doesn't belong — living residents, nonliving parts (sun, water, soil, air — belong!), rejects polar bear and cactus (living, wrong ecosystem). Phase B "Eat, help, or compete?": 6 pairs. Wrong answers name the specific error and re-queue | lessons (stage `practice`) | — |
| 4 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.ecosystems.01`), pass ≥ 4/5, score posted to player | lessons (stage `check`) | — |
| 5 | Hand-off | 8 | Research: Kiwix "Jungle" or "Rainforest" (INTEGRATION §4, jungle-book row) → notebooks: two facts — one living part, one nonliving part of a real jungle | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.ecosystems.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Jungle" (or "Rainforest"), 8 min
- [ ] Task 3: Notebooks — "Two facts about a real jungle: one living part, one nonliving part"

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.ecosystems.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in a browser and walks teach + practice with the child first
- [ ] Task 2: Research — "Jungle" / "Rainforest"
- [ ] Task 3: Notebooks — two facts as above

## 4. Checks

- **Formative:** practice telemetry — does the child reject the sun/water/soil cards (nonliving-not-part), accept the polar bear (any-animal-belongs), or call every pair "eat" (all-relationships-are-eating)? The package records which misconception fired.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only ("Watch the jungle team again" button); then re-run practice Phase A with the parent naming aloud what each living thing USES (deer→river, tree→soil) before the child taps; retry the check next day. If the relationship items miss, re-teach with three concrete jungle-book moments (Kaa hunts = eat; bees and flowers = help; Shere Khan and the wolves both want Mowgli's camp's prey = compete).

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation `anim.science.35.ecosystems.01` is authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.ecosystems.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.ecosystems.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on sun, water, soil, air or clouds; predator pairs tense but never gory; the polar bear drawn on sea ice so "wrong place" is visible, not a trick.
- Vocabulary with inline glosses: ecosystem (say: EE-koh-sis-tem), nonliving, compete. Read-aloud 🔊 on every instruction.
- Prereq `obj.science.k2.habitats.01` (K–2 habitats): if the child can't say "animals live where their needs are met," run that lesson first.
