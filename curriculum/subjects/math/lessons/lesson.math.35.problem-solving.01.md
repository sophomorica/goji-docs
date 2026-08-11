# Lesson: `lesson.math.35.problem-solving.01`

| Field | Value |
|-------|--------|
| **ID** | `lesson.math.35.problem-solving.01` |
| **Title** | Multistep word problems — plan first, then compute |
| **Band** | 3–5 |
| **Duration (target)** | 25–35 min on Goji (repeatable with fresh problem sets) |
| **Objectives** | `obj.math.35.problem-solving.01` |
| **Anchor book** | `wizard-of-oz` |
| **Status** | ready |

---

## 1. Goal (one sentence)

After this lesson, the child attacks a multistep problem by stating a plan — what's asked, which operations, in what order — before touching the arithmetic, and sanity-checks the answer after.

## 2. Sequence (teach → practice → comprehension)

| Step | Pattern | Minutes | Activity | Goji tool | Media |
|------|---------|---------|----------|-----------|-------|
| 1 | Hook | 3 | Road-to-Oz problem, no numbers hidden: "Dorothy walks 3 days at 8 miles a day, then a balloon carries her 40 more miles. How far in all?" Ask for the *plan* only — forbid computing. ("First multiply the walking, then add the balloon") | (off-device) | — |
| 2 | **Teach** | 4 | The 4-question protocol, written on paper where it stays visible: **1) What is asked? 2) What do I know? 3) Which operations, in what order? 4) Is my answer sensible?** Model it once on a trap problem: "There are 5 munchkins and Dorothy is 9 years old — how many hats do the munchkins need?" (the 9 is bait; keyword-grabbers add it) | parent demo, journal | — |
| 3 | **Guided practice** | 6 | Two problems from the word-problems bank done *aloud together* — child states the plan, parent computes (role reversal keeps the child in planning); include one division problem where the remainder must be interpreted ("58 travelers, 6 per carriage — how many carriages?" → 10, not 9 r4) | math → word problems | — |
| 4 | **Practice** | 12 | Word-problems bank, multistep set, solo — plan muttered or jotted first, target ≥ 80% | math → word problems | — |
| 5 | **Comprehension** | 5 | Quiz (plans required, one remainder item); journal: write the plan for one problem in words, no numbers computed | parent quiz, journal | `quiz.math.35.problem-solving.01` |

## 3. School Day mapping (how a parent would assign today)

- [ ] Task 1: Math — word problems, multistep set, ~8 problems at ≥ 80%
- [ ] Task 2: Parent quiz — `quiz.math.35.problem-solving.01`, pass ≥ 4/5 with plan stated
- [ ] Task 3: Journal — "Pick one problem from today. Write your plan in words — the steps you would take — without doing any computation."
  - Checklist: What the problem asks for · Step 1 in words · Step 2 in words · No answers or arithmetic — plan only

(When module-scoped math tasks ship, Task 1 becomes "8 problems of Word Problems at 80%" — see `MATH_MODULE_TASKS_PLAN.md`.)

## 4. Checks

- **Formative:** listen during guided practice for keyword-grabbing ("altogether — so I add everything") — the trap problem in Teach exists to surface exactly this.
- **Summative:** bank ≥ 80% on the multistep set on two different days + quiz ≥ 4/5 with plans stated and the remainder item interpreted correctly.
- **If not yet:** shrink to *plan-only* practice — five problems where the child writes the plan and never computes (removes arithmetic anxiety from the reasoning work); if a specific operation keeps failing inside otherwise-good plans, that's a fact-fluency gap — route to `multiply.02` / `divide.02` drills, not more word problems.

## 5. Tools

- **Uses existing:** math word-problems bank, parent quiz, journal.
- **Blocked on new tool:** none required. (A curated *multistep* subset inside the word-problems bank is assumed — if the bank can't filter single- vs multistep, note it in TOOLS.md §6D as seed/content work, and parent-select items meanwhile.)

## 6. Authoring notes

- Quiz blueprint: `quiz.math.35.problem-solving.01` (+ bank gate `gate.math.35.problem-solving.01`) in [`../quiz-blueprints.md`](../quiz-blueprints.md).
- Anchor integration: journey math (miles, days, carriages, emeralds) recasts naturally onto Oz — parent-authored quiz variants should keep the story flavor; the bank's own items stay generic.
- Order of operations (`obj.math.35.problem-solving.02`, planned) is this lesson's symbolic twin — same "order matters" idea on bare expressions.
