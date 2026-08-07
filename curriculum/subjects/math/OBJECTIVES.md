# Math — objectives

ID format: `obj.math.<band>.<strand>.<nn>`  
Bands: `k2` | `35` | `68` | `912`  
Status: **K–2 first strand authored 2026-08-07** (place-value + fluency, lessons in [`lessons/`](./lessons/)); **3–5 strand set authored 2026-08-07** (13 objectives across 6 strands, 7 lessons).

---

## How to add an objective

Copy from [`../../assets/templates/objective.md`](../../assets/templates/objective.md).

Required fields: id, band, strand, statement, success criteria, practice tools, animations (optional).

---

## K–2 (`k2`) — first strand (authored)

Virginia crosswalk codes are drafts from the 2023 Math SOLs — see [`../../skills/`](../../skills/) for the coverage catalog.

### Place value (`place-value`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA (draft) | Status |
|----|-----------|------------------|---------|----------------|------------|------|------------|--------|
| `obj.math.k2.place-value.01` | Count forward to 20; read and write numerals 0–20; count a set of up to 20 objects | 9/10 numeral↔quantity matches on flashcard deck; parent quiz 8/10 | — | flashcards (numeral↔dots deck), journal | — | `quiz.math.k2.place-value.01` | K.NS.1 | ready |
| `obj.math.k2.place-value.02` | Explain a 2-digit number (10–99) as tens and ones, and build it both ways | Names tens/ones for 8/10 numbers incl. teens and round tens; explains one in own words (journal) | `.01` | math (mental math), flashcards, journal | `anim.math.k2.place-value.01` | `quiz.math.k2.place-value.02` | 1.NS.2 | ready |
| `obj.math.k2.place-value.03` | Compare two 2-digit numbers using greater than / less than / equal, by comparing tens first | 8/10 comparisons correct incl. tricky pairs (e.g. 39 vs 41, 52 vs 25); states the tens-first rule | `.02` | math (mental math), parent quiz | `anim.math.k2.place-value.02` | `quiz.math.k2.place-value.03` | 1.NS.3 | ready |

### Fact fluency (`fluency`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA (draft) | Status |
|----|-----------|------------------|---------|----------------|------------|------|------------|--------|
| `obj.math.k2.fluency.01` | Add within 10 accurately, moving from counting-on to known facts (doubles, make-ten pairs) | Addition drill ≥ 90% on 20 problems (0–10), two sessions on different days | `place-value.01` | math (addition drill), flashcards | `anim.math.k2.fluency.01` | drill gate (see blueprint) | 1.CA.1 | ready |
| `obj.math.k2.fluency.02` | Subtract within 10, using the addition relationship ("what plus 4 makes 9?") | Subtraction drill ≥ 90% on 20 problems, two sessions; explains fact-family link once (journal) | `fluency.01` | math (subtraction drill), journal | `anim.math.k2.fluency.01` (re-teach) | drill gate (see blueprint) | 1.CA.1 | ready |

**Misconceptions to watch (strand-level):** teens read backwards ("41" for fourteen); "more digits = bigger" without comparing tens; treating subtraction as unrelated to addition; counting-all forever instead of counting-on.

### Fractions intro (`fractions`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA (draft) | Status |
|----|-----------|------------------|---------|----------------|------------|------|------------|--------|
| `obj.math.k2.fractions.01` | Partition shapes and sets into halves and fourths; name equal shares and explain why unequal cuts aren't fair shares | Fractions module ≥ 85% on a halves/fourths session; explains "equal parts" once (journal) | `place-value.01` | math → fractions (tile live 2026-08-07), journal | `anim.math.k2.fractions.01` | `quiz.math.k2.fractions.01` | 1.NS.3 | ready |

---

## 3–5 (`35`) — authored strand set (2026-08-07)

VA crosswalk codes are **verified** against the 2023 Math SOLs (fetched VDOE document — see [`../../skills/math-3.md`](../../skills/math-3.md), [`math-4.md`](../../skills/math-4.md), [`math-5.md`](../../skills/math-5.md)). Anchor books for the band (INTEGRATION.md): `jungle-book`, `black-beauty`, `alice-wonderland`, `wizard-of-oz`.

### Multiplicative thinking (`multiply`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.multiply.01` | Explain multiplication as equal groups and as arrays; translate between story, picture, and fact both ways (4 groups of 6 ↔ 4×6=24) | Quiz ≥ 8/10 incl. picture↔fact in both directions; writes one equal-groups story of their own (journal) | `k2.fluency.01`–`.02` | math (times tables, word problems), journal | `anim.math.35.multiply.01` | `quiz.math.35.multiply.01` | 3.CE.2 | ready |
| `obj.math.35.multiply.02` | Fluency: recall multiplication facts through **12×12** with automaticity, climbing table by table | Times-tables drill ≥ 90% per table (2–12), each table on two different days; then two mixed-table sessions ≥ 90% | `multiply.01` | math (times tables), flashcards (stubborn facts) | `anim.math.35.multiply.01` (map beat) | `gate.math.35.multiply.02` | 3.CE.2 / 4.CE.2 | ready |

### Division (`divide`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.divide.01` | Explain division as sharing and as grouping; write the complete fact family linking × and ÷ (3×4=12, 4×3=12, 12÷3=4, 12÷4=3) | Quiz ≥ 8/10 incl. two complete fact families; writes one sharing story (journal) | `multiply.01` | math (division drill, word problems), journal | `anim.math.35.multiply.01` (re-teach — the array read backwards) | `quiz.math.35.divide.01` | 3.CE.2 | ready |
| `obj.math.35.divide.02` | Fluency: recall division facts through 144÷12, table by table (inverse recall of the times tables) | Division drill ≥ 90% per table (2–12), two sessions on different days — the device records **per-table division mastery** | `divide.01`, `multiply.02` | math (division drill) | — | `gate.math.35.divide.02` | 3.CE.2 / 4.CE.2 | planned (lesson pending — runs on the `multiply.02` routine pattern) |

### Place value (`place-value`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.place-value.01` | Read, write (standard, expanded, word form), compare and order whole numbers — six-digit range first (grade 3), stretching to nine digits (grade 4) | Quiz ≥ 8/10 incl. compare traps (digit count vs leading digits) and one expanded-form build in each direction | `k2.place-value.03` | math (mental math), flashcards, journal | — | quiz (with lesson) | 3.NS.1 / 3.NS.2 / 4.NS.1 / 4.NS.2 | planned |
| `obj.math.35.place-value.02` | Identify prime vs composite numbers to 100; build prime factorizations | Quiz ≥ 8/10 prime/composite sorts; three factor trees (journal) | `multiply.02` | math (times tables — factor fluency), flashcards, journal | — | quiz (with lesson) | 5.NS.2 | planned |

### Fractions (`fractions`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.fractions.01` | Represent unit fractions as parts of a whole; compare and order fractions and mixed numbers (denominators ≤ 12) using benchmarks 0, ½, 1 and like-numerator / like-denominator reasoning | Fractions module compare session ≥ 85%; quiz ≥ 8/10 incl. the bigger-denominator trap | `k2.fractions.01` | math → fractions, parent quiz, journal | `anim.math.k2.fractions.01` (optional refresher) | `quiz.math.35.fractions.01` | 3.NS.3 / 4.NS.3 | ready |
| `obj.math.35.fractions.02` | Generate and recognize equivalent fractions — same amount, different cuts (1/2 = 2/4 = 4/8) | Quiz ≥ 8/10 incl. naming two equivalents for a given fraction; fractions module session ≥ 85% | `fractions.01` | math → fractions, journal | `anim.math.35.fractions.01` | `quiz.math.35.fractions.02` | 3.NS.3 / 4.NS.3 | ready |
| `obj.math.35.fractions.03` | Add and subtract fractions: like denominators first, then unlike denominators by rewriting with equivalence (LCD) | Quiz ≥ 8/10 on a mixed like/unlike set; explains one LCD rewrite (journal) | `fractions.02` | math → fractions, word problems, journal | `anim.math.35.fractions.01` (re-teach) | quiz (with lesson) | 4.CE.3 / 5.CE.2 | planned |

### Decimals (`decimals`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.decimals.01` | Read, write, and compare decimals through thousandths as place value continuing right of the ones; know money-anchored fraction↔decimal partners (1/10 = 0.1 = a dime; 1/4 = 0.25) | Quiz ≥ 8/10 incl. the 0.5-vs-0.05 trap; money-match flashcard deck 9/10 | `place-value.01` (concept), `fractions.02` | flashcards (money-match deck), math (mental math — money sums, **partial**), journal — **practice gap: no decimals drill (TOOLS.md §6D)** | `anim.math.35.decimals.01` | `quiz.math.35.decimals.01` | 4.NS.4 / 4.NS.5 / 5.NS.1 | ready (teach + quiz path; drill practice gapped) |
| `obj.math.35.decimals.02` | Add and subtract (grade 4), then multiply and divide (grade 5) decimals, including money contexts | Decimals drill ≥ 90%, two sessions on different days + quiz ≥ 8/10 — **not yet assessable on device** | `decimals.01` | **gap — decimals drill (TOOLS.md §6D)**; word problems (money items) interim | — | quiz (with lesson, once drill ships) | 4.CE.4 / 5.CE.3 | blocked (no decimals drill) |

### Problem solving (`problem-solving`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|----|--------|
| `obj.math.35.problem-solving.01` | Solve single- and multistep contextual problems with all four operations: state the plan (which operations, what order) before computing, check reasonableness, and interpret remainders sensibly | Word-problems bank ≥ 80% on a multistep set, two sessions on different days; quiz ≥ 4/5 with the plan stated (aloud or journal) | `multiply.01`, `divide.01` | math → word problems, journal | — | `quiz.math.35.problem-solving.01` + `gate.math.35.problem-solving.01` | 3.CE.1 / 4.CE.1 / 5.CE.1 | ready |
| `obj.math.35.problem-solving.02` | Apply order of operations to evaluate expressions (no exponents; one set of parentheses) | Quiz ≥ 8/10 incl. left-to-right ×/÷ and parentheses-first traps | `multiply.02` | math (mental math — needs an expression set; engineering note), journal | — | quiz (with lesson) | 5.CE.4 | planned |

**Misconceptions to watch (band-level):** "multiplication always makes bigger"; multiplication as only repeated addition (breaks at arrays/area); division as only sharing (grouping reading lost); quotient/divisor swapped; **bigger denominator = bigger fraction**; treating numerators/denominators as separate whole numbers ("add tops, add bottoms"); **longer decimal = bigger number** (0.125 > 0.5); 0.5 confused with 0.05; keyword-grabbing in word problems ("altogether always means add"); solving left-to-right regardless of operation order.

---

## 6–8 / 9–12

Intentionally empty until elementary spine is real. Add strand headers when ready.

---

## Coverage notes

- Prefer linking **existing** math modules in “Practice tools.”  
- If only animation + PDF teach a concept, mark `practice: gap` and add to `TOOLS.md`.  
