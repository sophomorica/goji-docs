# Lesson: `lesson.science.35.adapt.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.adapt.01` |
| **Title** | Why the mongoose wins — physical and behavioral adaptations |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 10 min research hand-off |
| **Objectives** | `obj.science.35.adapt.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.adapt.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** `jungle-book` — *Rikki-Tikki-Tavi* week. The strongest anchor synergy of the 3–5 year (`skills/science-3.md` summary): the story's own question — why does the mongoose beat the cobra? — IS the science objective. The tiger (Shere Khan) and the wolf pack (Mowgli's family) are the story's other specimens.

---

## 1. Goal (one sentence)

After this lesson, the child can classify an adaptation as physical (a body part it was born with) or behavioral (a thing the animal does), explain that populations change over many generations without any animal choosing to change, and read a fossil as evidence of long-ago animals and environments (a fish fossil on a mountain = this was once under water).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Rikki-tikki fights the cobra — and WINS. How?" Child taps a guess (luck / his body and moves); revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3.5 | Five beats: (1) the mongoose's physical kit — speed, thick coarse fur, tough body (resistance kept gentle); (2) tiger stripes = camouflage, physical; (3) wolf pack hunting TOGETHER + bear's winter sleep = behavioral; (4) finch-beak-style population change over many generations — no bird chose it; (5) fossils as clues — the mountain fish | lessons (stage `teach`) | `anim.science.35.adapt.01` (inline in package) |
| 3 | **Guided practice** | 2 | First two sorts with the parent (bridge) or with the hint feedback (solo): the sorting question is always "body part it was BORN with, or a thing it DOES?" | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 5 | Sort + detective round, 8 items: stripes / pack-hunting / thick fur / playing dead / sharp claws / flying south sorted physical vs behavioral, then a which-helps-it-survive-HERE habitat match (snow hare) and a fossil-inference item. Misses name the misconception and re-queue | lessons | — |
| 5 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.adapt.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | Research: Kiwix **"Mongoose"** (INTEGRATION §4 jungle-book chain) — find two real adaptations the story got right → notebooks (2 facts); optional journal claim-plus-proof: "Rikki-tikki wins because…" | research → notebooks (→ journal) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Reader — *Rikki-Tikki-Tavi* chapter (anchor)
- [ ] Task 2: Lesson — `lesson.science.35.adapt.01`, `min_score: 4`
- [ ] Task 3: Research — topic hint "Mongoose", 5 min
- [ ] Task 4: Notebooks — "2 real mongoose adaptations", `lesson_id: lesson.science.35.adapt.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Reader — *Rikki-Tikki-Tavi*
- [ ] Task 2: Parent quiz — `quiz.science.35.adapt.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + sort with the child
- [ ] Task 3: Research — "Mongoose"
- [ ] Task 4: Notebooks — 2 facts as above

## 4. Checks

- **Formative:** sort telemetry — `mix` misses mean the physical/behavioral test question ("born with it, or does it?") isn't being asked; `habitat` misses mean adaptations aren't tied to the home; `rock` misses mean fossils read as objects, not evidence. The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only (package "watch again" button); then re-sort just four cards with the parent asking aloud "body part, or action?" for each (fur, flying south, claws, playing dead); retry the check next day with the story fresh from the reader.

## 5. Tools

- **Uses existing:** reader (anchor), research (Kiwix), notebooks, journal, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.35.adapt.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.adapt.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.adapt.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions driving distractors: **"animals adapt on purpose / quickly because they want to"** (beat 4's "no bird chose it", check items 3 and 5); **"behavioral = physical"** (the whole sort, check items 1–2); **"fossils are just old rocks with no story"** (beat 5, detective item, check item 4).
- Must-not-show: no violence in the mongoose/cobra scenes (circling and dodging only — storybook tension, no strike landing); no animal shown "deciding" to change its body; venom resistance stated gently ("even the cobra can barely hurt him"), no venom mechanics.
- Read-aloud: every instruction has a speaker button. Inline glosses for band vocabulary: *adaptation*, *camouflage*, *behavioral* ("a thing it DOES"), *generations*, *fossil*.
