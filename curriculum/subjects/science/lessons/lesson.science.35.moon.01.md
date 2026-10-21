# Lesson: `lesson.science.35.moon.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.moon.01` |
| **Title** | Our closest neighbor — moon, seasons, tides |
| **Band** | 3–5 (grade hint 4) |
| **Duration (target)** | 15 min on Goji + 2-week off-device moon-phase log |
| **Objectives** | `obj.science.35.moon.01` (prereq `obj.science.35.solar.01`) |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.moon.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — Earth & space unit continuing `lesson.science.35.solar.01`. Research hand-off: a **real moon-phase log** with a parent — at least 4 dated sketches spread over 2 weeks (look up, draw the shape, name the phase) → journal. Kiwix "Moon" article as the reading companion.

---

## 1. Goal (one sentence)

After this lesson, the child can describe the Earth–moon–sun dance (moon around Earth, Earth around sun), explain moonlight as reflected sunlight, name and order the four major phases and explain them as viewing angle (not shadow), explain **seasons as tilt, not distance** — the unit's misconception assassination — and connect the moon's pull to the twice-daily tides.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | "Summer is hot — why? Does your half of Earth LEAN toward the sun, or does Earth move CLOSER?" — child taps a guess; revisited at the result screen with the farther-in-summer surprise | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 2.5 | Six beats: the two-orbit dance · the moon is a mirror (no light of its own) · four phases via the classic lamp-and-ball view · seasons = TILT not distance (with the Earth-is-farther-in-summer proof) · tides = the moon's pull, twice a day · moon profile (closer, smaller, airless, cratered) | lessons (stage `teach`) | `anim.science.35.moon.01` (inline in package) |
| 3 | **Guided practice** | 3 | Phase-order build (new → first quarter → full → last quarter), track fills with phase icons; wrong tap → order chant read aloud, retry in place | lessons (stage `practice`, phase 1) | — |
| 4 | **Independent practice** | 5 | Tilt-vs-distance duel ×3 (incl. the Virginia-summer/Australia-winter clincher and the farther-in-summer fact check), then moonlight/phase-from-diagram/tides picks ×7; wrong answers name the specific error and re-queue | lessons (phases 2–3) | — |
| 5 | **Comprehension** | 2 | Built-in check, 5 items (`quiz.science.35.moon.01`), pass ≥ 4/5, score posted | lessons (stage `check`) | — |
| 6 | Hand-off | 2 wks | Moon-phase log with parent: ≥ 4 dated sketches over 2 weeks → journal ("tonight the moon was ___ because ___") | journal (+ parent) | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.moon.01`, `min_score: 4`
- [ ] Task 2: Journal — "Moon log night 1: draw the shape, name the phase" (repeats ×4 over two weeks), `lesson_id: lesson.science.35.moon.01`
- [ ] Task 3: Research — topic hint "Moon", 5 min

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.moon.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package in any browser first and walks the teach + phase build with the child
- [ ] Task 2: Journal — moon-log entry as above (parent supervises the evening look-up)
- [ ] Task 3: Research — "Moon"

## 4. Checks

- **Formative:** practice telemetry — `dist` misses (closer-in-summer), `shadow` misses (phases-as-shadow), `glow` misses (self-glowing moon), `phord` misses (phase order). The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge) **and** the moon-phase log with ≥ 4 dated entries (parent sign-off).
- **If not yet:** on `dist` misses, replay only the seasons beat and have the parent act it out — child = Earth, lamp = sun, lean a globe (or the child's own tilted head) toward/away; the "is Australia closer too?" question usually breaks the misconception. On `phord`/`phread` misses, re-run the phase build after two more log nights — the real sky is the remediation. Retry the check next day.

## 5. Tools

- **Uses existing:** journal (moon log), research (Kiwix), parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A → `LessonPlayer` in `LESSON_PACKAGES.md`.

## 6. Authoring notes

- Animation: `anim.science.35.moon.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.moon.01.md`, INDEX status `shipped-inline`. The brief also flags this unit as the band's strongest candidate for a richer generated animation (lamp-and-ball phases + tilt orbit) when clip budget lands.
- Quiz blueprint: `quiz.science.35.moon.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Must-not-show: **no face on the moon or sun**; never draw phases as Earth's shadow creeping across; never show summer-Earth nearer the sun (the seasons scene keeps both Earths at equal distance); eclipse imagery avoided entirely at this grade.
- Read-aloud: every instruction has a speaker button.
- Prereq: `obj.science.35.solar.01` (rotate/revolve vocabulary is assumed and reused).
