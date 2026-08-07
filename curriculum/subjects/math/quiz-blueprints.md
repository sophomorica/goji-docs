# Math K–2 — quiz blueprints (first strand)

Format per [`../../QUIZZES.md`](../../QUIZZES.md) §4. These are **blueprints**: gold items authored here, generation later (cloud-side). Until objective-linked quizzes exist on device, deliver via **parent quizzes** (§6 of QUIZZES.md).

Pass rules feed each objective's success criteria in [`OBJECTIVES.md`](./OBJECTIVES.md).

---

## `quiz.math.k2.place-value.01` — Numbers to 20

```yaml
quiz.math.k2.place-value.01:
  objectives: [obj.math.k2.place-value.01]
  skill: "match quantity (0–20) to numeral; order within 20"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10"
  difficulty: intro
  constraints:
    numbers: 0-20
    must_include: [at least 3 teens, one zero-or-one item, two "what comes next" items]
    distractors: reversed teens (41 for 14), off-by-one counts
```

**Gold items (v1):**

1. Which number shows this many? (12 dots) → 12 / 21 / 20 / 11
2. Which number shows this many? (7 dots) → 7 / 6 / 8 / 17
3. Which number shows this many? (15 dots) → 15 / 51 / 14 / 13
4. Which number shows this many? (20 dots) → 20 / 12 / 19 / 2
5. What comes right after 13? → 14 / 12 / 15 / 31
6. What comes right after 19? → 20 / 18 / 21 / 91
7. Which number shows this many? (0 dots) → 0 / 1 / 10 / 5
8. Which number shows this many? (18 dots) → 18 / 81 / 17 / 19
9. Which is the number fourteen? → 14 / 41 / 4 / 40
10. What comes right before 16? → 15 / 17 / 14 / 61

---

## `quiz.math.k2.place-value.02` — Tens and ones

```yaml
quiz.math.k2.place-value.02:
  objectives: [obj.math.k2.place-value.02]
  skill: "decompose 10–99 into tens and ones; compose from tens and ones"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10, at least one teen correct"
  difficulty: intro
  constraints:
    numbers: 10-99
    must_include: [two teens, one round ten, both directions (number→tens/ones and tens/ones→number)]
    distractors: digit-swap (tens/ones reversed), digit-as-count errors
  animation_review: anim.math.k2.place-value.01
```

**Gold items (v1):**

1. 34 is __ tens and __ ones → 3 and 4 / 4 and 3 / 34 and 0 / 3 and 40
2. 71 is __ tens and __ ones → 7 and 1 / 1 and 7 / 70 and 10 / 7 and 10
3. 5 tens and 2 ones makes → 52 / 25 / 57 / 502
4. 14 is __ tens and __ ones → 1 and 4 / 4 and 1 / 14 and 0 / 0 and 14
5. 90 is __ tens and __ ones → 9 and 0 / 0 and 9 / 9 and 9 / 90 and 9
6. 2 tens and 8 ones makes → 28 / 82 / 210 / 208
7. 17 is __ tens and __ ones → 1 and 7 / 7 and 1 / 17 and 0 / 10 and 7
8. 6 tens and 0 ones makes → 60 / 6 / 66 / 600
9. Which number has 4 tens and 9 ones? → 49 / 94 / 44 / 99
10. 8 tens and 3 ones makes → 83 / 38 / 811 / 80

---

## `quiz.math.k2.place-value.03` — Compare 2-digit numbers

```yaml
quiz.math.k2.place-value.03:
  objectives: [obj.math.k2.place-value.03]
  skill: "compare two 2-digit numbers; tens-first rule"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 including both reversed-digit traps"
  difficulty: intro
  constraints:
    numbers: 10-99
    must_include: [two reversed-digit pairs, two tied-tens pairs, one equal pair, one "big ones digit loses" trap]
    distractors: bigger-ones-digit wins, more-different-digits wins
  animation_review: anim.math.k2.place-value.02
```

**Gold items (v1):**

1. Which is greater: 39 or 41? → 41 (trap: big ones digit)
2. Which is greater: 52 or 25? → 52 (reversed digits)
3. Which is greater: 67 or 76? → 76 (reversed digits)
4. Which is greater: 84 or 88? → 88 (tied tens)
5. Which is less: 45 or 42? → 42 (tied tens)
6. 36 __ 36 → equal
7. Which is greater: 19 or 91? → 91
8. Which is less: 78 or 87? → 78
9. Which is greater: 50 or 49? → 50 (trap)
10. Which is less: 63 or 36? → 36

---

## `quiz.math.k2.fractions.01` — Fair shares (halves & fourths)

```yaml
quiz.math.k2.fractions.01:
  objectives: [obj.math.k2.fractions.01]
  skill: "identify halves and fourths as equal shares; reject unequal partitions"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one pick-the-fair-cut, one name-the-share, one set model (not just shapes), one more-pieces trap]
    distractors: unequal partitions labeled as halves/fourths; "4 pieces beats 2" trap
  animation_review: anim.math.k2.fractions.01
```

**Gold items (v1):**

1. Which circle is cut into halves? → (2 equal pieces) / (2 unequal pieces) / (3 pieces) / (uncut)
2. A square cut into 4 equal pieces shows → fourths / halves / thirds / wholes
3. Share 4 berries fairly between 2 friends — each gets → 2 / 1 / 3 / 4
4. Which is MORE cookie: one half, or one fourth of the same cookie? → one half / one fourth / same / can't tell
5. Is a sandwich cut into one big and one small piece cut in halves? → No — pieces aren't equal / Yes — it's 2 pieces / Only if it's big / Yes — any cut works

---

## Drill gates (fluency strand — no item bank)

Fluency objectives are checked by **module accuracy**, not authored items:

```yaml
gate.math.k2.fluency.01:
  objectives: [obj.math.k2.fluency.01]
  tools: math-drill (addition)
  pass_rule: "accuracy >= 90% on 20 problems (range 0-10), two sessions on different days"

gate.math.k2.fluency.02:
  objectives: [obj.math.k2.fluency.02]
  tools: math-drill (subtraction)
  pass_rule: "accuracy >= 90% on 20 problems (range 0-10), two sessions on different days"
  prerequisite: gate.math.k2.fluency.01 passed
```

When **module-scoped math tasks** ship (`MATH_MODULE_TASKS_PLAN.md`), these gates become directly assignable ("20 problems of Addition at 90%"). Until then: parent assigns the drill and reads the score.

---

## Authoring rules recap

- Distractors are **diagnostic** — each wrong answer encodes a known misconception (digit swap, ones-digit-wins, off-by-one), so a parent seeing repeated misses learns *which* error, not just "wrong."
- Numbers in generated variants change; the misconception each distractor encodes must not.
- Reading comprehension quizzes always carry `book_id` (QUIZZES.md §7) — see `../reading/quiz-blueprints.md`.
