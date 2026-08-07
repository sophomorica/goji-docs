# Curriculum practices — how lessons get made (agents: read this first)

Status: **locked 2026-08-07** (owner-directed) · The methodology every curriculum session and subagent follows. VISION.md says *what*; this says *how*.

**The mission bar:** a child using **only the Goji computer** should reach high-school graduation with a high degree of proficiency. That means: every VA SOL skill catalogued, every catalogued skill covered or explicitly gapped, every covered skill measurable. No skill left silently untaught.

---

## 1. The learning cycle (looser than a formula, firmer than vibes)

The full arc a skill travels — lessons pick the stages they need, but the arc is the map:

```
(Socratic starter?) → TEACH → GUIDED PRACTICE → INDEPENDENT PRACTICE → QUIZ → TEST
                                                                        (check)  (mastery)
```

| Stage | What it is | Goji surfaces |
|-------|-----------|---------------|
| **Starter** (optional) | A hook: a question, a paradox, a Socratic exchange, a trap ("39 vs 41 — but 9 is bigger!") that makes the brain *want* the principle | Parent script in lesson; discussion prompts at older bands |
| **Teach** | The principle, stated clearly once | Animation, parent demo, worked example |
| **Guided practice** | Doing it *with* support — parent alongside, worked examples, echo reading, first 5 flashcards together | Parent-in-the-loop steps in the lesson sequence |
| **Independent practice** | Doing it alone, volume + accuracy | Drills, decks, typing, module sessions |
| **Quiz (check)** | Prove the skill stuck — short, per-lesson | Parent quiz / drill gate / deck gate |
| **Test (mastery)** | Prove it *stays* — cumulative, spaced, across sessions | Two-day gate rules; unit tests per strand (blueprint layer 3); placement/assessment quizzes |

Rules of flexibility: Socratic starters are encouraged, not required. Some lessons are pure practice (fluency days). Guided → independent can happen in one sitting for easy skills or across weeks for phonics. **But every objective must terminate in a measurable check** — that's non-negotiable, because the parent heat map is only as honest as the gates.

## 2. Authoring pipeline (plan → build → audit → fix)

Every curriculum work cycle, whether human or agent:

1. **PLAN** — pick the target from the skills catalog (never invent scope): which SOL rows, which band, which anchor book.
2. **BUILD** — objectives → lessons → briefs → quiz blueprints, in that order (VISION §8 authoring loop).
3. **AUDIT** — run the checklist (§4) against what was built. Agents self-audit; a second agent audits large batches.
4. **FIX** — close every audit finding or log it as an explicit gap row. Then update the coverage catalog (`skills/`) in the same commit — coverage files may never lag reality.

## 3. Authoring rules (the house style)

1. **One objective per lesson** (K–5 strictly; 6–12 may pair tightly-coupled objectives).
2. **Anchor integration** (INTEGRATION.md): practice text from the anchor book; research topics germane; decks feed the reading. A disconnected lesson is a defect.
3. **Measurable gates**: success criteria in countable terms (≥ 8/10, two days, parent sign-off). "Understands X" alone is a defect.
4. **Diagnostic distractors**: every quiz wrong-answer encodes a named error type. Numbers change in generated variants; the misconception each distractor encodes must not.
5. **Misconceptions named** per strand — the animation's "must not show" and the remediation path both come from them.
6. **Remediation is specific**: "If not yet" names the exact re-teach step (easier deck, physical manipulative, prerequisite lesson) — never "review and retry."
7. **Existing tools first** (TOOLS.md §5 order); a needed-but-missing tool gets a TOOLS.md §6 row and the lesson is marked blocked — casually inventing device apps is a defect.
8. **Animations are stubs until generated**: brief + INDEX row (status `brief`), lessons reference the ID, parent-side preview note until the player ships.
9. **IDs are law**: `obj.` / `lesson.` / `anim.` / `quiz.` naming exact; every cross-reference resolvable. The parent app's catalog asset is generated from these files — broken IDs break heat maps.
10. **Honest statuses**: ready / planned / blocked (with the blocker named). Aspirational "ready" is a defect.

## 4. Audit checklist (run every cycle)

- [ ] Every new objective has: statement, measurable gate, prereqs, tools, VA crosswalk (or "draft" flag), status
- [ ] Every `ready` objective has a lesson; every lesson's objective exists
- [ ] Every lesson: anchor book named (or explicitly n/a), stages from §1 identifiable, School Day mapping uses existing task types, specific remediation
- [ ] Every quiz/gate referenced exists in a blueprints file (or is explicitly "with lesson")
- [ ] Every animation ID referenced has a brief + INDEX row
- [ ] Coverage files (`skills/`) updated — statuses match what now exists
- [ ] Parent-app catalog asset (`goji_learner_app/assets/curriculum/catalog_v1.json`) regenerated/extended when objectives changed, its count test updated
- [ ] No invented SOLs: catalog rows trace to a fetched VDOE document (or carry an explicit "draft — unverified" flag)

## 5. SOL catalog methodology (research agents)

- Fetch the **official VDOE documents** (2023 math, 2024 English, current science/history) — web-archive mirrors of doe.virginia.gov acceptable; **never write standards from model memory**. Record source URL per grade.
- One coverage file per grade × subject in `skills/`, using the established table format and status vocabulary (covered / partial / planned / gap / off-device).
- High school: catalog by **course** (Algebra I, Geometry, Algebra II; English 9–12; Biology, Chemistry…) — that's how VA structures graduation.
- Every row gets a coverage verdict on arrival, even if it's `gap` — the gap map *is* the roadmap.

## 6. Subject scope for "graduate proficient"

| Tier | Subjects | Delivery stance |
|------|----------|-----------------|
| Pillars | Reading, Writing, Math | Full native curriculum (lessons, drills, quizzes) |
| Core graduation | Science, History/Social science | Kiwix-anchored units + PDF lessons + quizzes (INTEGRATION §4 chain); labs/hands-on flagged off-device parent-led |
| Supporting | Typing, Coding, Health/PE-adjacent | Typing/coding native (exists); PE/health = off-device, parent-tracked |

## 7. Assessment layers (placement → daily → mastery)

1. **Placement** (new, owner-directed): short per-pillar × band assessment quizzes that establish a child's **starting point** — seed the heat map before any lessons run. Spec: `ASSESSMENT.md`.
2. **Daily checks**: lesson quizzes / gates (existing).
3. **Mastery tests**: cumulative per-strand unit tests, spaced (blueprint layer 3) — prove retention, not just recency.

All three write to the same objective states; the parent app reads one truth.
