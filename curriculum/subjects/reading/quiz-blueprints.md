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

## `quiz.reading.68.comp.01` — Theme vs topic (Call of the Wild, then Treasure Island)

```yaml
quiz.reading.68.comp.01:
  objectives: [obj.reading.68.comp.01]
  book_id: call-of-wild   # pass 2 re-instantiates with book_id: treasure-island
  skill: "distinguish topic from theme; pick the theme statement the book's events actually support"
  tools: parent-quiz (source_book_id: call-of-wild)
  item_type: multiple_choice
  n_items: 6
  pass_rule: ">= 5/6"
  difficulty: on-level
  constraints:
    must_include: [two topic-vs-theme sorts, one best-supported-theme pick, two evidence-to-claim matches, one "which event does NOT support this theme"]
    distractors: topic labels dressed as themes ("the theme is survival"), one-word answers, theme statements that fit OTHER shelf books but not this one
    evidence_rule: evidence-to-claim items store the quotable event/line for parent review
  writing_crossover: journal theme statement (full sentence + two proving events) reviewed alongside
```

## `quiz.reading.68.comp.02` — Motive, POV, irony (Tom Sawyer)

```yaml
quiz.reading.68.comp.02:
  objectives: [obj.reading.68.comp.02]
  book_id: tom-sawyer
  skill: "infer real motive vs stated reason; identify point of view; spot ironic distance (fence scene anchor)"
  tools: parent-quiz (source_book_id: tom-sawyer)
  item_type: multiple_choice
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: on-level
  constraints:
    must_include: [one stated-vs-real-motive, one why-did-X, one whose-eyes/POV, one irony-spot, one "which line tells you"]
    distractors: face-value readings (taking Tom's words as his motive), motives belonging to other characters/scenes in the same book
    evidence_rule: every inference item stores its quotable evidence line
  writing_crossover: journal motive analysis (stated reason / real want / proving line / where the author winks)
```

## `quiz.reading.912.comp.01` — Close reading (Poe)

```yaml
quiz.reading.912.comp.01:
  objectives: [obj.reading.912.comp.01]
  book_id: poe-tales   # CONFIRMED on device 2026-08-07 (8 complete tales as chapters)
  skill: "identify mood and tone of a passage; name the technique (word choice / sound / pacing) a quoted line uses"
  tools: parent-quiz (source_book_id: poe-tales)
  item_type: multiple_choice
  n_items: 5 per tale ("The Tell-Tale Heart" first)
  pass_rule: ">= 4/5"
  difficulty: on-level
  constraints:
    one_tale_per_quiz: true
    must_include: [one mood-of-passage, one tone-vs-mood distinction, two which-technique-is-this-line-using, one ghost-swap ("plainer word would mostly weaken: word choice / sound / pacing")]
    distractors: mood words fitting the PLOT but not the prose; technique labels swapped between quoted lines; tone offered where mood is asked
    evidence_rule: technique/tone items quote their exact line and store the annotation-style justification
  status: ready — book on device, id confirmed
  writing_crossover: notebooks annotation page (W/S/P key, >= 6 annotations) reviewed alongside
```

## Phonics deck gates (no item bank)

```yaml
gate.reading.k2.phonics.01:
  objectives: [obj.reading.k2.phonics.01]
  tools: flashcards (deck read-k2-cvc, anchor-sampled per INTEGRATION.md)
  pass_rule: ">= 9/10 read aloud to parent, two different days"

gate.reading.k2.phonics.02:
  objectives: [obj.reading.k2.phonics.02]
  tools: flashcards (deck read-k2-vce, >=10 minimal pairs)
  pass_rule: ">= 9/10 including 4+ minimal-pair items, two days"
  prerequisite: gate.reading.k2.phonics.01

gate.reading.k2.phonics.03:
  objectives: [obj.reading.k2.phonics.03]
  tools: flashcards (decks read-k2-vteams + read-k2-bossy-r, anchor-sampled per INTEGRATION.md)
  pass_rule: ">= 8/10 per pattern deck (vowel teams and bossy-r gate separately), two days"
  prerequisite: gate.reading.k2.phonics.02
  contrast_rule: each run mixes 2-3 reviewed CVC lookalikes (rain/ran, coat/cot, meat/met; cart/cat, her/hen) — proves the child reads the team, not guesses from length

gate.reading.k2.phonics.04:
  objectives: [obj.reading.k2.phonics.04]
  tools: flashcards (decks read-k2-digraphs + read-k2-blends, anchor-sampled)
  pass_rule: ">= 9/10 per deck, two days"
  prerequisite: gate.reading.k2.phonics.01   # teaching order: this gate sits BETWEEN .01 and .02 (OBJECTIVES.md strand note)
  contrast_rule: ">= 4 minimal-pair cards per run — digraph vs single letter (ship/sip, chat/cat, then/ten) and blend vs single (stop/top, black/back, trap/tap)"

gate.reading.k2.phonics.05:
  objectives: [obj.reading.k2.phonics.05]
  tools: flashcards (deck read-k2-diphthongs, anchor-sampled)
  pass_rule: ">= 8/10 per pattern group (oi/oy, ou/ow, au/aw, oo), two days; every run samples BOTH oo sounds (moon-oo and book-oo)"
  prerequisite: gate.reading.k2.phonics.03
  contrast_rule: mixes name-sayer teams from .03 (coin/cone, out/oat, how/hoe) — noise-maker vs name-sayer is the error this gate exists to catch

gate.reading.k2.phonics.06:
  objectives: [obj.reading.k2.phonics.06]
  tools: flashcards (deck read-k2-2syllable) + typing (base + -ing/-ed forms)
  pass_rule: ">= 8/10 incl. >= 3 open/closed contrast cards and >= 3 -ed cards sampling all three sounds (/t/ /d/ /id/), two days"
  prerequisite: gate.reading.k2.phonics.02 and gate.reading.k2.phonics.04
  contrast_rule: a doubling pair rides every run (hopping/hoping) — open vs closed first syllable is the diagnostic

gate.reading.35.vocab.01:
  objectives: [obj.reading.35.vocab.01]
  tools: flashcards (per-chapter deck vocab-<anchor>-ch<N> from the child's own lookups)
  pass_rule: ">= 90% two days running + 2 collected words used in a journal sentence"
```

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
