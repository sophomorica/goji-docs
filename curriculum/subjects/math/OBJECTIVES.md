# Math — objectives

ID format: `obj.math.<band>.<strand>.<nn>`  
Bands: `k2` | `35` | `68` | `912`  
Status: **K–2 first strand authored 2026-08-07** (place-value + fluency, lessons in [`lessons/`](./lessons/)); 3–5 still skeleton.

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

## 3–5 (`35`) — seed strands (placeholders)

### Multiplicative thinking (`multiply`)

| ID | Statement (draft) | Practice tools | Animations |
|----|-------------------|----------------|------------|
| `obj.math.35.multiply.01` | Meaning of multiplication as equal groups | times tables + animation | TBD |
| `obj.math.35.multiply.02` | Fluency: multiply through 10×10 | times tables | — |

### Fractions (`fractions`)

| ID | Statement (draft) | Practice tools | Animations |
|----|-------------------|----------------|------------|
| `obj.math.35.fractions.01` | Unit fractions as parts of a whole | fractions module | TBD |
| `obj.math.35.fractions.02` | Equivalent fractions (conceptual) | fractions + animation | TBD |

---

## 6–8 / 9–12

Intentionally empty until elementary spine is real. Add strand headers when ready.

---

## Coverage notes

- Prefer linking **existing** math modules in “Practice tools.”  
- If only animation + PDF teach a concept, mark `practice: gap` and add to `TOOLS.md`.  
