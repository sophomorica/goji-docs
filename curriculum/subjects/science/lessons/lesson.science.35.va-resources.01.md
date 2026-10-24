# Lesson: `lesson.science.35.va-resources.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.va-resources.01` |
| **Title** | Our Virginia — watersheds and riches |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 5–10 min research hand-off |
| **Objectives** | `obj.science.35.va-resources.01` (prereq `obj.science.35.conservation.01`, same wave) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.va-resources.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — home-state domain unit. **Pairs with Grade 4 Virginia Studies on the history side** (same rivers, same regions, same Bay — the history sequence's map work and this unit reinforce each other; note for the Virginia Studies authors). Research hand-off: Kiwix "Chesapeake Bay" → notebooks (one Bay animal + one thing that washes in and harms it).

---

## 1. Goal (one sentence)

After this lesson, the child can define a watershed (all the land that drains to one water body), race a raindrop down Virginia's three big drainage systems (most of the state → Chesapeake Bay; southwest → Tennessee River → Gulf of Mexico; south-central → North Carolina sounds), name Virginia's riches by kind (forests and soils, coal/granite/limestone, rivers and the Bay's oysters and blue crabs, deer/black bear/cardinal), and explain wise use — replant, and keep what washes off streets out of the Bay.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Rain falls on a Blue Ridge mountaintop — does it stay, or race downhill to the Bay?" — child taps a guess; revisited at the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Six beats: the ridge decides (watershed defined by the raindrop race) · Virginia's three drains kept simple (Bay / Gulf via Tennessee / NC sounds) · forests cover most of the state + rich soils · coal, granite, limestone · the Bay's oysters and blue crabs, deer/black bear/cardinal · use it wisely (replant; street drains lead to streams lead to the Bay — conservation tie) | lessons (stage `teach`) | `anim.science.35.va-resources.01` (inline in package) |
| 3 | **Guided practice** | 3 | Raindrop-race picks ×3 (Richmond / far southwest / south-central) — the destination board fills as each drop lands; wrong tap → three-drains hint read aloud, retry in place | lessons (stage `practice`, phase 1) | — |
| 4 | **Independent practice** | 3 | Sort-the-riches ×4 (coal → mineral, oaks → forest, James → water, blue crabs → wildlife), then protect-the-Bay scenarios ×2 (street-drain oil; endless-forests); wrong answers name the specific error and re-queue | lessons (phases 2–3) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.va-resources.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 6 | Hand-off | 5–10 | Research: Kiwix "Chesapeake Bay" → notebooks: one Bay animal + one thing that washes in and harms it | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.va-resources.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Chesapeake Bay", 5–10 min
- [ ] Task 3: Notebooks — "One Bay animal + one thing that washes in and harms it"

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.va-resources.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser first and walks the raindrop race with the child
- [ ] Task 2: Research — "Chesapeake Bay"
- [ ] Task 3: Journal — "A watershed is ___. Our rain flows to ___. One way I can protect the Bay is ___." (`min_words: 15`)

## 4. Checks

- **Formative:** practice telemetry — `stays` misses (stays-in-street), `wrongshed` misses (drainage mix-ups), `cat` misses (resource categories), `endless` misses. The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay only the watershed beat, then act it out off-device — pour a cup of water on a tented towel "ridge" with the parent and watch which side it runs; re-run the raindrop race after. For `cat` misses, a kitchen-table sort of four real objects (rock / leaf / cup of water / toy animal) rebuilds the categories; retry the check next day.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.va-resources.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.va-resources.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.va-resources.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: no faces on non-living things (raindrops, rocks, the drain); the three watershed systems kept simple — three arrows, no county detail; never show pollution "disappearing".
- Read-aloud: every instruction has a speaker button.
- Ties: `obj.science.35.conservation.01` (same-wave prereq) supplies the wise-use frame; Virginia Studies (history side) shares the rivers/regions/Bay geography — noted for cross-linking when those units land.
