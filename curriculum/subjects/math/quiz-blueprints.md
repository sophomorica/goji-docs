# Math — quiz blueprints (K–2 first strand + 3–5 strand set)

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

## 3–5 blueprints (strand set, 2026-08-07)

## `quiz.math.35.multiply.01` — Equal groups & arrays (meaning)

```yaml
quiz.math.35.multiply.01:
  objectives: [obj.math.35.multiply.01]
  skill: "translate story <-> picture (groups/array) <-> multiplication fact, both directions"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 with both translation directions correct at least once"
  difficulty: intro
  constraints:
    facts: within 12x12, factors 2-8 in gold items
    must_include: [two picture->fact, two fact->picture/story, one array rotation (commutativity), one groups-vs-items trap]
    distractors: adds-the-two-numbers, counts-groups-only, counts-one-group-only, skip-count-off-by-one-group
  animation_review: anim.math.35.multiply.01
```

**Gold items (v1):**

1. (Picture: 4 branches, 6 monkeys on each) Which fact matches? → 4×6=24 / 4+6=10 / 6−4=2 / 4×4=16
2. (Picture: 3 baskets, 5 apples each) How many apples in all? → 15 / 8 *(adds instead)* / 3 *(counts groups)* / 5 *(counts one group)*
3. Which picture shows 2×7? → 2 rows of 7 / 7 rows of 7 / a row of 2 and a row of 7 / 2 rows of 5
4. "5 wolves in each of 3 hunting parties" — the fact is → 3×5=15 / 3+5=8 / 5×5=25 / 3×5=12 *(skip-count slip)*
5. An array has 6 rows of 4. Turn it sideways. Now it shows → 4×6 — same total / 6×6 / 4×4 / a different total
6. Which story matches 4×8? → "4 shelves, 8 books on each" / "4 books and 8 more" / "8 shelves with 4 missing" / "4 books shared by 8"
7. (Picture: 5 rows of 5 dots) The fact is → 5×5=25 / 5+5=10 *(adds)* / 4×5=20 *(miscounted rows)* / 5×6=30 *(miscounted columns)*
8. 7×3 means → 7 groups of 3 / 7 and 3 more / 7 groups of 7 / 3 taken from 7
9. (Picture: 6 nests, 2 eggs each) How many eggs? → 12 / 8 *(adds)* / 6 *(counts groups)* / 2 *(one group)*
10. Which fact does this story need? "Each of the 9 carriages carries 4 travelers" → 9×4=36 / 9+4=13 / 9×4=32 *(skip-count slip)* / 4×4=16

---

## `quiz.math.35.divide.01` — Division meaning & fact families

```yaml
quiz.math.35.divide.01:
  objectives: [obj.math.35.divide.01]
  skill: "read division as sharing or grouping; complete the x/÷ fact family"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 including two complete fact families"
  difficulty: intro
  constraints:
    facts: within 12x12
    must_include: [two complete-the-family, one sharing read, one grouping read, one which-multiplication-answers-it]
    distractors: subtracts-instead, quotient-divisor-swapped, multiplies-instead, family-member-from-wrong-family
  animation_review: anim.math.35.multiply.01
```

**Gold items (v1):**

1. 24 carrots shared equally among 4 horses — each horse gets → 6 / 20 *(subtracts)* / 96 *(multiplies)* / 4 *(swapped)*
2. 3×7=21. Which fact is in the same family? → 21÷3=7 / 24÷3=8 *(wrong family)* / 21−3=18 *(subtraction confusion)* / 7×7=49 *(wrong family)*
3. Which four facts make one family? → 4×6=24, 6×4=24, 24÷4=6, 24÷6=4 / 4×6=24, 6×4=24, 24÷2=12, 24÷12=2 / 4+6=10, 6+4=10, 10−4=6, 10−6=4 / 4×6=24, 24×6=4, 6÷4=24, 4÷6=24
4. 32÷4=? Which fact answers it fastest? → 4×8=32 / 4×4=16 / 32−4=28 / 8×8=64
5. "18 berries, 6 in each bag — how many bags?" This is → grouping: 18÷6=3 / sharing: 18÷3=6 / adding: 18+6 / taking away: 18−6
6. 45÷5 = → 9 / 40 *(subtracts)* / 5 *(swapped)* / 225 *(multiplies)*
7. Complete the family: 7×8=56, 8×7=56, 56÷8=7, __ → 56÷7=8 / 56÷8=8 / 8÷7=56 / 56−7=49
8. "12 travelers, 3 per carriage" asks → how many carriages: 12÷3=4 / how many travelers: 12×3 / 12−3 / how many wheels
9. 63÷9=? → 7 / 54 *(subtracts)* / 9 *(swapped)* / 6 *(wrong-family: 54÷9)*
10. Which division does 6×9=54 unlock? → 54÷6=9 / 54÷9=5 / 45÷9=5 / 54÷5=9

---

## `quiz.math.35.fractions.01` — Compare & order fractions

```yaml
quiz.math.35.fractions.01:
  objectives: [obj.math.35.fractions.01]
  skill: "compare/order fractions and mixed numbers (denominators <= 12) via benchmarks and like-numerator/denominator reasoning"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 with the bigger-denominator trap correct"
  difficulty: intro
  constraints:
    denominators: 2-12
    must_include: [two unit-fraction compares, one like-denominator, one like-numerator, one benchmark (vs 1/2), one ordering triple, one mixed number]
    distractors: bigger-denominator-means-bigger, compares-numerators-across-denominators, more-pieces-means-more, ignores-whole-number-part
  animation_review: anim.math.k2.fractions.01
```

**Gold items (v1):**

1. Which is more of the bottle: 1/3 or 1/4? → 1/3 / 1/4 *(bigger-denominator trap)* / same / can't tell
2. Which is more: 3/8 or 5/8? → 5/8 / 3/8 / same / can't tell
3. Which is more: 2/3 or 2/5? → 2/3 (bigger pieces) / 2/5 *(bigger-denominator trap)* / same / can't tell
4. Which is more than 1/2: 5/8 or 3/8? → 5/8 / 3/8 / both / neither
5. Order smallest → largest: 1/2, 1/6, 1/3 → 1/6, 1/3, 1/2 / 1/2, 1/3, 1/6 *(bigger-denominator order)* / 1/3, 1/2, 1/6 / 1/6, 1/2, 1/3
6. Which is more cake: 1 1/2 cakes or 5/4 of a cake? → 1 1/2 / 5/4 *(bigger numbers look bigger)* / same / can't tell
7. Which is more: 3/10 or 3/4? → 3/4 / 3/10 *(bigger-denominator trap)* / same — tops match *(numerator-only)* / can't tell
8. A pizza cut into 12 vs an identical one cut into 6. One slice of which is bigger? → the 6-cut / the 12-cut *(more-pieces trap)* / same / can't tell
9. Which is closest to 1 whole? → 11/12 / 1/12 / 6/12 / 2/3
10. Which is less: 7/8 or 7/12? → 7/12 / 7/8 / same — tops match *(numerator-only)* / can't tell

---

## `quiz.math.35.fractions.02` — Equivalent fractions

```yaml
quiz.math.35.fractions.02:
  objectives: [obj.math.35.fractions.02]
  skill: "recognize and generate equivalent fractions (same amount, different cuts)"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 including at least one generate-an-equivalent correct"
  difficulty: intro
  constraints:
    denominators: 2-12
    must_include: [two picture-overlap items, two generate-an-equivalent, one same-numerator non-example, one three-name family]
    distractors: adds-same-to-top-and-bottom, same-numerator-means-equal, scales-only-one-part, more-pieces-means-more
  animation_review: anim.math.35.fractions.01
```

**Gold items (v1):**

1. (Two identical bars: one shows 1/2 shaded, one shows 2/4 shaded) The amounts are → equal / 2/4 is more *(more-pieces)* / 1/2 is more / can't tell
2. Another name for 1/2 is → 4/8 / 2/3 *(added 1 to top and bottom)* / 1/4 *(scaled bottom only)* / 2/2
3. Another name for 2/3 is → 4/6 / 3/4 *(added 1 each)* / 2/6 *(scaled bottom only)* / 4/3 *(scaled top only)*
4. Are 2/3 and 2/4 the same amount? → No — thirds are bigger pieces / Yes — both are 2 pieces *(same-numerator)* / Yes — 3 and 4 are close / can't tell
5. Which family is all the same amount? → 1/2, 2/4, 4/8 / 1/2, 2/3, 3/4 *(add-one-each chain)* / 1/2, 1/4, 1/8 / 2/4, 2/6, 2/8 *(same-numerator chain)*
6. (Picture: 1/3 shaded, then every piece cut in two) Now the shading shows → 2/6 — same amount / 2/6 — more than before / 1/6 / 2/3
7. To turn 3/4 into eighths → cut every piece in 2: 6/8 / add 4 to the top: 7/8 / just change the bottom: 3/8 *(scaled bottom only)* / it can't be done
8. Which is NOT another name for 1/2? → 3/5 / 2/4 / 5/10 / 6/12
9. 4/6 in its simplest cut is → 2/3 / 1/2 / 4/6 can't be renamed / 2/6 *(scaled top only)*
10. Sam says "1/4 = 2/5 because I added 1 to the top and the bottom." He's → wrong — cuts must multiply every piece the same way / right / right only for small fractions / wrong — you can never rename fractions

---

## `quiz.math.35.decimals.01` — Decimals & place value (money-anchored)

```yaml
quiz.math.35.decimals.01:
  objectives: [obj.math.35.decimals.01]
  skill: "read/write/compare decimals through thousandths; money-anchored fraction<->decimal partners"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 with the 0.5-vs-0.05 trap correct"
  difficulty: intro
  constraints:
    range: through thousandths (money items through hundredths)
    must_include: [one dime item, one build-from-coins, two compares incl. 0.5-vs-0.05, one longer-is-bigger trap, one fraction<->decimal partner, one place-name item]
    distractors: longer-decimal-is-bigger, reads-digits-as-whole-number, wrong-column (tenths/hundredths swapped), coin-value-error
  animation_review: anim.math.35.decimals.01
```

**Gold items (v1):**

1. One dime is what part of a dollar? → 0.1 / 0.01 *(penny's value)* / 0.5 / 10
2. 1 dollar + 3 dimes + 4 pennies = → 1.34 / 1.43 *(columns swapped)* / 134 *(digits as whole number)* / 1.7
3. Which is more: 0.5 or 0.05? → 0.5 (five dimes) / 0.05 *(looks similar)* / same / can't tell
4. Which is more: 0.5 or 0.125? → 0.5 / 0.125 *(longer-is-bigger trap)* / same / can't tell
5. 1/4 of a dollar (a quarter) as a decimal is → 0.25 / 0.4 *(reads the 4)* / 0.14 / 4.0
6. In 2.36, the 3 is worth → 3 tenths / 3 ones / 3 hundredths *(column swap)* / 36
7. Which is more: 0.35 or 0.4? → 0.4 / 0.35 *(35 beats 4 as whole numbers)* / same / can't tell
8. "Seven tenths" is written → 0.7 / 0.07 *(column swap)* / 7.10 / 710
9. Which shows the same amount as 0.50? → 0.5 / 0.05 / 5.0 / 0.055
10. 0.204 means → 2 tenths and 4 thousandths / 2 tenths and 4 hundredths *(column swap)* / 204 / 2 hundreds and 4 ones *(whole-number read)*

---

## `quiz.math.35.problem-solving.01` — Multistep word problems (plan first)

```yaml
quiz.math.35.problem-solving.01:
  objectives: [obj.math.35.problem-solving.01]
  skill: "plan and solve multistep contextual problems, all four operations; interpret remainders"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 5
  pass_rule: ">= 4/5 with the plan stated (aloud or journal) before answering; remainder item correct"
  difficulty: intro
  constraints:
    operations: all four, at least two steps in 4 of 5 items
    must_include: [one plan-only item (no computing), one extra-number bait, one remainder-interpretation, one all-four-operations mix across the set]
    distractors: first-step-only-answer, adds-all-the-numbers, keyword-grab-wrong-operation, remainder-dropped
  variants_note: "parent-authored variants may recast items with anchor-book characters (Oz journey math); plan structure and misconceptions stay fixed"
```

**Gold items (v1):**

1. Dorothy walks 3 days at 8 miles a day, then rides 40 miles. How far in all? → 64 / 24 *(first step only)* / 51 *(adds all numbers)* / 320
2. PLAN ONLY — "A shop has 6 shelves of 9 emeralds and sells 15. How many are left?" The plan is → multiply, then subtract / add, then subtract / subtract, then multiply / just add everything *(adds-all)*
3. 58 travelers, 6 per carriage. How many carriages are needed? → 10 / 9 *(remainder dropped)* / 9 r4 as the final answer / 64 *(keyword-grab: adds)*
4. Em bakes 4 trays of 12 biscuits and shares them equally among 8 workers. Each gets → 6 / 48 *(first step only)* / 24 / 3
5. A kite costs 5 dollars. Toto is 3 years old. Jo buys 4 kites — total cost? → 20 dollars / 23 *(bait number added)* / 12 *(wrong pair multiplied)* / 9 *(adds 5+4)*

---

## Drill gates (3–5 — module accuracy, incl. per-table mastery)

```yaml
gate.math.35.multiply.02:
  objectives: [obj.math.35.multiply.02]
  tools: math-drill (times tables)
  pass_rule: "per table 2-12: accuracy >= 90% on ~20 problems, two sessions on different days; then two mixed-table sessions >= 90%"
  note: "climb order suggestion in lesson.math.35.multiply.02; stubborn facts -> flashcards mini-deck"

gate.math.35.divide.02:
  objectives: [obj.math.35.divide.02]
  tools: math-drill (division)
  pass_rule: "per table 2-12: accuracy >= 90%, two sessions on different days"
  prerequisite: matching times table passed in gate.math.35.multiply.02
  note: "device persists per-table division mastery (operation-keyed stats, shipped 2026-08-07) - the parent reads mastery per table, not just per session"

gate.math.35.problem-solving.01:
  objectives: [obj.math.35.problem-solving.01]
  tools: math-drill (word problems, multistep set)
  pass_rule: "accuracy >= 80% on a multistep set (~8 problems), two sessions on different days"
```

When **module-scoped math tasks** ship (`MATH_MODULE_TASKS_PLAN.md`), these gates become directly assignable ("20 problems of Times Tables (7s) at 90%"). Until then: parent assigns the drill and reads the score.

**With-lesson blueprints (not yet authored):** `place-value.01`/`.02`, `fractions.03`, `problem-solving.02` quizzes arrive with their lessons; `decimals.02` gate additionally waits on the decimals drill (TOOLS.md §6D).

---

## Authoring rules recap

- Distractors are **diagnostic** — each wrong answer encodes a known misconception (digit swap, ones-digit-wins, off-by-one), so a parent seeing repeated misses learns *which* error, not just "wrong."
- Numbers in generated variants change; the misconception each distractor encodes must not.
- Reading comprehension quizzes always carry `book_id` (QUIZZES.md §7) — see `../reading/quiz-blueprints.md`.
