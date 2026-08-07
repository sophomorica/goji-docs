# Reading — objectives (K–12 spine)

ID format: `obj.reading.<band>.<strand>.<nn>` · Bands: `k2` | `35` | `68` | `912`  
Status: **K–12 spine authored 2026-08-07** — K–2/3–5 crosswalks draw on the verified VDOE catalog ([`../../skills/`](../../skills/)); 6–8/9–12 crosswalks are drafts (verify when those grades' catalogs are built).

Strands: `phonics` (word study) · `fluency` · `vocab` · `comp` (literary) · `info` (informational). Grammar/language lives in the **writing** pillar ([`../writing/OBJECTIVES.md`](../writing/OBJECTIVES.md)) — reading lessons cross-link it.

Book-tied objectives use the device catalog ids from [`reading-lists.md`](./reading-lists.md).

---

## K–2 (`k2`)

### Phonics / word study (`phonics`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA (verified) | Status |
|----|-----------|------------------|---------|----------------|------------|------|---------------|--------|
| `obj.reading.k2.phonics.01` | Decode CVC (closed-syllable, short-vowel) words | 9/10 on decodable flashcard deck, two days | — | flashcards, typing (same word list) | `anim.reading.k2.phonics.01` | deck gate | 1.FFR.3 | ready |
| `obj.reading.k2.phonics.02` | Decode VCe ("magic-e") and open-syllable long-vowel words | 9/10 on VCe deck incl. minimal pairs (cap/cape) | `.01` | flashcards, typing | `anim.reading.k2.phonics.02` | deck gate | 1.FFR.3 | ready |
| `obj.reading.k2.phonics.03` | Decode common vowel teams (ai, ee, oa, ea) and r-controlled vowels (ar, or, er) | 8/10 per pattern deck | `.02` | flashcards, typing | TBD (reuse .02 pattern) | deck gate | 1.FFR.3 / 2.FFR.3 | planned |

### Fluency (`fluency`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.k2.fluency.01` | Read grade-level text aloud with accuracy and phrasing | Parent judgment on ~1 page aloud + reader minutes logged (gate.reading.k2.fluency.01) | `phonics.01` | reader (`aesop-fables`), parent observation | — | fluency gate | 1.DSR | ready |
| `obj.reading.k2.fluency.02` | Recognize grade-level high-frequency words with automaticity | ≥ 90% on HF deck, two days (gate.reading.k2.fluency.02) | — | flashcards | — | deck gate | 1.FFR.3 | ready |

### Comprehension (`comp`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.k2.comp.01` | Retell a story in order (beginning/middle/end) with its central message | Oral or journal retell hits the 3 parts + message, 2 different texts | `fluency.01` | reader, journal, parent quiz | `anim.reading.k2.comp.01` | `quiz.reading.k2.comp.01` | 1.RL.1 | ready |
| `obj.reading.k2.comp.02` | Answer who/what/where/when questions from a short text | ≥ 4/5 on book-tied quiz per fable | `fluency.01` | reader (`aesop-fables`), parent quiz | — | `quiz.reading.k2.comp.01` | 1.RL.1 | ready |

---

## 3–5 (`35`)

### Vocabulary (`vocab`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.35.vocab.01` | Use context (and the lookup tool) to work out unfamiliar words, then own them | Per-book vocab deck ≥ 90%; word-lookup count shows active use | k2 spine | reader (`alice-wonderland`), flashcards, word lookups | — | deck gate | 3–5 RV (draft) | ready |

### Comprehension — literary (`comp`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.35.comp.01` | Identify main idea and distinguish it from details (not too broad, not too narrow) | ≥ 5/6 per story on book-tied quiz, 2 stories | k2 comp | reader (`jungle-book`), parent quiz | `anim.reading.35.comp.01` | `quiz.reading.35.comp.01` | 3–5 RL (draft) | ready |
| `obj.reading.35.comp.02` | Make inferences about characters' feelings/motives and cite the line that proves it | ≥ 4/5 with evidence lines on book-tied quiz | `.01` | reader (`black-beauty`), parent quiz, journal | `anim.reading.35.comp.02` | `quiz.reading.35.comp.02` | 3–5 RL (draft) | ready |
| `obj.reading.35.comp.03` | Track sequence and cause→effect across chapters | Chapter-chunk quizzes ≥ 4/5 (`wizard-of-oz` or `secret-garden`) | `.01` | reader, parent quiz | — | blueprint TBD | 3–5 RL (draft) | planned |

### Informational (`info`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.35.info.01` | Use text features (headings, captions, diagrams) to preview and find information | Applied in a PDF lesson + research-app task, parent sign-off | — | pdf, research | — | manual check | 3–5 RI (draft) | planned |

---

## 6–8 (`68`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.68.comp.01` | Distinguish theme from topic; state a text's theme as a claim about life | Theme statements for 2 novels pass parent review; quiz ≥ 5/6 | 35 comp | reader (`call-of-wild`, `treasure-island`), journal | `anim.reading.68.comp.01` | `quiz.reading.68.comp.01` | 6–8 RL (draft) | ready |
| `obj.reading.68.comp.02` | Analyze character motive and point of view, including unreliable or ironic narration | Book-tied quiz ≥ 4/5 + one journal analysis | `.01` | reader (`tom-sawyer`, `treasure-island`), journal | — | `quiz.reading.68.comp.02` | 6–8 RL (draft) | ready |
| `obj.reading.68.comp.03` | Follow and summarize a long plot arc (chapter-chunk summaries that connect) | Running summary journal across a novel, parent sign-off | `.01` | reader (`anne-green-gables`), journal, notebooks | — | manual + quiz TBD | 6–8 RL (draft) | ready |
| `obj.reading.68.info.01` | Read nonfiction/domain text for information and take structured notes | Notebook notes on a research topic pass review (Kiwix later) | 35 info | research, notebooks, pdf | — | manual check | 6–8 RI (draft) | ready |

---

## 9–12 (`912`)

| ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status |
|----|-----------|------------------|---------|----------------|------------|------|-----|--------|
| `obj.reading.912.comp.01` | Close-read a short text: mood, tone, word choice, and how they're built | Annotated close reading (notebooks) + quiz ≥ 4/5 | 68 comp | reader (Poe — **needs ingest**), notebooks | `anim.reading.912.comp.01` | `quiz.reading.912.comp.01` | 9–12 RL (draft) | blocked: ingest 9–12 shelf |
| `obj.reading.912.comp.02` | Analyze theme, symbolism, and character development across a full novel | Essay-form journal/notebook responses, parent review | `.01` | reader (`pride-prejudice`, `frankenstein` — **needs ingest**), writing | — | essay rubric TBD | 9–12 RL (draft) | blocked: ingest |
| `obj.reading.912.info.01` | Read and evaluate an argument: claim, evidence, reasoning, rhetoric | Argument map (notebooks) for 2 founding-era texts, parent review | 68 info | reader (Federalist — **needs ingest**), notebooks | — | argument-map rubric | 9–12 RI (draft) | blocked: ingest |

**9–12 blocker is content, not tools:** the device's 9–12 shelf is empty — see ingest priorities in [`reading-lists.md`](./reading-lists.md). Lessons are authored against the plan so ingest unblocks them without re-authoring.

---

## Coverage notes

- Phonics is the **largest authored addition** — it was the top gap the skills catalog exposed. Decks are the vehicle (vehicle + data rule); each pattern gets a decodable deck seed list in its lesson.
- Comprehension objectives are **book-tied** wherever possible (QUIZZES.md §7) — on-device ids in statements.
- Fluency/expression and essay-quality checks stay **parent-judged** (PARENT_STANDING.md honesty rule) — the device holds evidence, not fake scores.
