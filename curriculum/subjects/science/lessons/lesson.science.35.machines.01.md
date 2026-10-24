# Lesson: `lesson.science.35.machines.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.science.35.machines.01` |
| **Title** | Force-tricks — net force and simple machines |
| **Band** | 3–5 (grade hint 3) |
| **Duration (target)** | 15 min on Goji + 10 min research hand-off |
| **Objectives** | `obj.science.35.machines.01` |
| **Status** | ready — package authored (`assets/lessons/lesson.science.35.machines.01/`); **blocked for kid playback** on the lesson player (`TOOLS.md` §6A). Bridge today: parent quiz + parent walks the HTML on any browser. |

**Anchor:** n/a — this is a standalone science unit (no 3–5 anchor-book tie fits force & motion). Research hand-off named per PRACTICES §3.2: Kiwix **"Lever"** or **"Pulley"** → notebooks, plus a find-3-simple-machines-at-home hunt.

---

## 1. Goal (one sentence)

After this lesson, the child can predict which way an object moves when more than one force acts on it (the bigger **total** — the net force — wins), name the six simple machines as "force-tricks" that trade a longer path for a smaller push, and pick the right machine for a job — including spotting two machines inside a compound one (scissors = lever + wedge).

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 1 | Tug-of-war: 2 kids pull left, 3 pull right — "Which team wins the rope?" Child taps a guess; revisited on the result screen | lessons (package, stage `hook`) | in-package |
| 2 | **Teach** | 3 | Six beats: (1) unequal tug → the bigger TOTAL (net force) wins; (2) tied tug → still rope, but TWO forces still act; (3) lever lifts the rock a kid can't; (4) ramp — roll up, don't lift; (5) pulley pulls DOWN to lift UP + wheel-and-axle; (6) wedge splits, screw = ramp round a pole — and the price: less force, LONGER path, never free work | lessons (stage `teach`) | `anim.science.35.machines.01` (inline in package) |
| 3 | **Guided practice** | 2 | First two workshop jobs done thinking aloud with the parent (bridge) or with the hint feedback (solo): the wrong pick's feedback names the trade ("no machine adds free force — you need a longer path") | lessons (stage `practice`) | — |
| 4 | **Independent practice** | 5 | Machine workshop, 8 jobs: piano→ramp, flag→pulley, log→wedge, lid→lever, boards→screw, cart→wheel-and-axle, one net-force tug prediction (4 vs 6), one compound spot (scissors = lever + wedge). Misses name the misconception and re-queue | lessons | — |
| 5 | **Comprehension** | 3 | Built-in check, 5 items (`quiz.science.35.machines.01`), score posted to player | lessons (stage `check`) | — |
| 6 | Hand-off | 10 | Research: Kiwix "Lever" (or "Pulley") — copy 2 facts to notebooks; then hunt: find **3 simple machines at home** (door wedge, jar lid = screw, bottle opener = lever, blinds cord = pulley…) and log each with its type in notebooks | research → notebooks | — |

## 3. School Day mapping

**When the player ships:**
- [ ] Task 1: Lesson — `lesson.science.35.machines.01`, `min_score: 4`
- [ ] Task 2: Research — topic hint "Lever" (or "Pulley"), 5 min
- [ ] Task 3: Notebooks — "3 simple machines in my house" list, `lesson_id: lesson.science.35.machines.01`

**Bridge today (existing task types only):**
- [ ] Task 1: Parent quiz — `quiz.science.35.machines.01` (5 items from the blueprint), pass ≥ 4/5; parent opens the HTML package on a laptop/phone first and walks the teach + workshop with the child
- [ ] Task 2: Research — "Lever"
- [ ] Task 3: Notebooks — machine hunt list as above

## 4. Checks

- **Formative:** workshop telemetry — `job` misses mean machine-to-job matching is weak; `net` misses mean the child compares single pulls instead of totals; `compound` misses mean parts aren't seen inside tools. The package records which.
- **Summative:** built-in check ≥ 4/5 (or parent quiz ≥ 4/5 on the bridge).
- **If not yet:** replay the Teach stage only (package "watch again" button); then a physical re-teach with the parent — pry a paint can with a spoon (short handle) vs a screwdriver (long handle) and FEEL the difference; retry the check next day.

## 5. Tools

- **Uses existing:** research (Kiwix), notebooks, parent quiz (bridge).
- **Blocked on new tool:** lesson player — `TOOLS.md` §6A "Animation / explainer player" → proposed as `LessonPlayer` in [`../../../LESSON_PACKAGES.md`](../../../LESSON_PACKAGES.md).

## 6. Authoring notes

- Animation: `anim.science.35.machines.01` authored **inline** (SVG/CSS) in the package — brief in `assets/animations/anim.science.35.machines.01.md`, INDEX status `shipped-inline`.
- Quiz blueprint: `quiz.science.35.machines.01` in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Misconceptions driving distractors: **"machines add free force / do the work for you"** (they trade distance for effort — every machine beat and check item 1/5 encode the trade) and **"if it's moving, only one force acts on it"** (tie beat + steady-sled check item).
- Must-not-show: no faces/eyes on rope, rock, barrel, tools (non-living); no scene where a machine moves a load with nobody applying force (would show "free work").
- Read-aloud: every instruction has a speaker button (Web Speech API; silent fallback). Inline glosses used for band vocabulary: *net force*, *compound machine*, *inclined plane* ("ramp").
