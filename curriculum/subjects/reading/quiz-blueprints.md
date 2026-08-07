# Reading — quiz blueprints (book-tied)

Format per [`../../QUIZZES.md`](../../QUIZZES.md). Rule §7: every comprehension quiz carries the **device catalog `book_id`** (real ids below, confirmed on device 2026-08-07).

Device wire fact (from the sync audit): a parent quiz payload is
`{ "source_book_id": "<book_id>", "questions": [{ "prompt", "choices", "answer" }] }` —
`source_book_id` is already in the spec, so these blueprints ship **today** as parent quizzes with the book link attached; the device just doesn't act on the link yet (product TODO: auto-verify reading tasks from it). Choices within one question must be distinct strings (UI keys on choice text).

---

## `quiz.reading.k2.comp.01` — Aesop retell checks (per-fable)

```yaml
quiz.reading.k2.comp.01:
  objectives: [obj.reading.k2.comp.01, obj.reading.k2.comp.02]
  book_id: aesop-fables
  skill: "retell + who/what/where on a single short fable"
  tools: parent-quiz (payload carries source_book_id)
  item_type: multiple_choice
  n_items: 5 per fable (one quiz per fable read)
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    one_fable_per_quiz: true
    must_include: [one who, one what-happened, one where-or-when, one order question, one moral/main-idea]
    distractors: events from OTHER fables in the same collection (tests real reading, not plausibility)
```

**Gold items — "The Boy Who Cried Wolf" (chapter in `aesop-fables`):**

1. Who watched the sheep? → A shepherd boy / A farmer / A wolf / A king
2. What did the boy shout for fun? → "Wolf!" / "Fire!" / "Help, a lion!" / "Dinner!"
3. What happened when the wolf really came? → No one believed him / The villagers ran fast / The dog saved the sheep / The wolf ran away
4. Which happened FIRST? → The boy tricked the villagers / The wolf came / The sheep were lost / The villagers stopped coming
5. What does this story teach? → Liars aren't believed even when truthful / Wolves are dangerous / Sheep need fences / Shouting is rude

*(Pattern repeats per fable; distractor rule keeps generation honest.)*

---

## `quiz.reading.35.comp.01` — The Jungle Book, story-by-story

```yaml
quiz.reading.35.comp.01:
  objectives: [obj.reading.35.comp.01]   # main idea + key details
  book_id: jungle-book
  skill: "main idea and key details per story; episodic structure"
  tools: parent-quiz (source_book_id: jungle-book)
  item_type: multiple_choice
  n_items: 6 per story
  pass_rule: ">= 5/6"
  difficulty: on-level
  constraints:
    per_story: true   # Mowgli stories are self-contained; quiz after each
    must_include: [one main-idea, three key-detail, one sequence, one vocabulary-in-context]
    distractors: details from adjacent stories; too-broad and too-narrow main-idea statements
```

---

## `quiz.reading.35.comp.02` — Black Beauty, inference

```yaml
quiz.reading.35.comp.02:
  objectives: [obj.reading.35.comp.02]   # inference from text evidence
  book_id: black-beauty
  skill: "infer character feelings/motives from first-person narration"
  tools: parent-quiz (source_book_id: black-beauty)
  item_type: multiple_choice
  n_items: 5 per chapter-chunk (3–4 chapters)
  pass_rule: ">= 4/5"
  difficulty: on-level
  constraints:
    must_include: [two feelings-inference, one why-did-X, one "which sentence tells you", one prediction]
    evidence_rule: every correct answer must be supportable by a quotable line — store the line with the item for parent review
  writing_crossover: journal exit ticket — "How did Beauty feel when …? How do you know?"
```

---

## Fluency (no item bank)

```yaml
gate.reading.k2.fluency.01:
  objectives: [obj.reading.k2.fluency.01]
  tools: reader minutes + parent observation
  pass_rule: "parent judgment after listening to ~1 page aloud; Goji records minutes"
  note: honest limit — no auto fluency scoring in v1 (see PARENT_STANDING.md writing/fluency rules)

gate.reading.k2.fluency.02:
  objectives: [obj.reading.k2.fluency.02]
  tools: flashcards (high-frequency word deck)
  pass_rule: ">= 90% on deck run, two different days"
```

---

## Authoring rules

- One quiz = one text chunk the child actually just read (fable, story, chapter-chunk) — never whole-book quizzes for K–5.
- Distractors come **from the same book** (other chapters/fables) so guessing from general knowledge fails.
- Inference items store their **evidence line** — parents see *why* the answer is right, which also seeds future generated-variant review (QUIZZES.md §4 trust rule).
