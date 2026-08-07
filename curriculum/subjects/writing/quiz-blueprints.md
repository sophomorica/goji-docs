# Writing (grammar/mechanics) — quiz blueprints

Format per [`../../QUIZZES.md`](../../QUIZZES.md) §4. These are **blueprints**: gold items authored here, generation later (cloud-side). Until objective-linked quizzes exist on device, deliver via **parent quizzes** (§6 of QUIZZES.md).

Grammar items are **fix-the-sentence / label / combine** tasks rendered as multiple choice. The diagnostic-distractor rule is strict here: every wrong option encodes a **named error type** (shown in brackets after each distractor), so repeated misses tell the parent *which* misconception, not just "wrong." Generated variants change the sentences; the error type behind each distractor must not change.

Pass rules feed each objective's success criteria in [`OBJECTIVES.md`](./OBJECTIVES.md). Two banks live with their lessons instead of here, per OBJECTIVES: `quiz.writing.35.mechanics.01` (in `lessons/lesson.writing.35.mechanics.01.md`) and the `912.grammar.01` rubric (in `lessons/lesson.writing.912.grammar.01.md`).

Book-flavored sentences reference on-device catalog ids ([`../reading/reading-lists.md`](../reading/reading-lists.md)); they are grammar items, not comprehension items, so no `book_id` field is required — the flavor is free.

---

## `quiz.writing.k2.grammar.01` — Sentence or not

```yaml
quiz.writing.k2.grammar.01:
  objectives: [obj.writing.k2.grammar.01]
  skill: "recognize complete sentences (naming part + telling part); identify what a fragment is missing"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10"
  difficulty: intro
  constraints:
    must_include: [both fragment kinds (missing who, missing what-happened), one short-but-complete sentence, one long fragment, one book-flavored item]
    distractors: naming-part-only fragment, telling-part-only fragment, length-equals-sentence, period-equals-sentence
  animation_review: anim.writing.k2.grammar.01
```

**Gold items (v1):**

1. Which one is a complete sentence? → **The dog barks.** / The big brown dog. [naming-part-only fragment] / Ran down the hill. [telling-part-only fragment] / Under the warm bed. [phrase — no who, no what-happened]
2. "The little bird." What is it missing? → **the telling part — what happened** / the naming part — the who [part misidentified] / nothing, it is complete [period-equals-sentence] / a longer word [length-equals-sentence]
3. Fix it: "Hopped over the log." → **The frog hopped over the log.** / Hopped over the log very fast. [words added, still no who] / The log. [swapped to the other fragment kind] / Hopped and jumped over the log. [second verb added, still no who]
4. Which one is NOT a sentence? → **Went to the store.** / I went. [short-but-complete rejected — length-equals-sentence] / We ate lunch. / Birds fly.
5. From Aesop: "The tortoise kept walking." Is it a complete sentence? → **Yes — it has a who and a what-happened** / No — it needs to be longer [length-equals-sentence] / No — a tortoise is not a person [naming part must be a person] / Yes — because it ends with a period [period-equals-sentence]

---

## `quiz.writing.k2.grammar.02` — Nouns, verbs, and the match

```yaml
quiz.writing.k2.grammar.02:
  objectives: [obj.writing.k2.grammar.02]
  skill: "identify nouns and verbs in simple sentences; choose the verb form that agrees with the subject"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10, at least one identify item and one agreement item correct"
  difficulty: intro
  constraints:
    must_include: [identify-noun, identify-verb, singular-subject agreement, plural-subject agreement, one pick-the-correct-sentence]
    distractors: verb-picked-as-noun, noun-picked-as-verb, migrated-s (plural verb with -s), overregularized form, -ing without helper
```

**Gold items (v1):**

1. Which word is a noun in "The cat drinks quickly."? → **cat** / drinks [verb picked as noun] / quickly [describing word picked as noun] / the [helper word picked as noun]
2. Which word is the verb in "The girls jump rope."? → **jump** / girls [noun picked as verb] / rope [second noun picked as verb] / the [helper word picked as verb]
3. Pick the right word: "Two dogs ___ fast." → **run** / runs [migrated-s: plural subject with -s verb] / running [-ing without helper] / runned [overregularized form]
4. Pick the right word: "One duck ___ in the pond." → **swims** / swim [singular subject with plural verb] / swimming [-ing without helper] / swimmed [overregularized form]
5. Which sentence is right? → **The boys play outside.** / The boys plays outside. [migrated-s] / The boy play outside. [singular subject, plural verb] / The boys playing outside. [-ing without helper]

---

## `quiz.writing.k2.mechanics.01` — Capitals and end marks

```yaml
quiz.writing.k2.mechanics.01:
  objectives: [obj.writing.k2.mechanics.01]
  skill: "capitalize sentence starts, names, and I; choose end marks (. ? !) by sentence voice"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10"
  difficulty: intro
  constraints:
    must_include: [each end mark at least once, one name capital, one I capital, one over-capitalization trap]
    distractors: missing start capital, missing end mark, wrong end mark, lowercase name or I, over-capitalization
```

**Gold items (v1):**

1. Which is written correctly? → **My dog is fast.** / my dog is fast. [missing start capital] / My dog is fast [missing end mark] / My Dog Is Fast. [over-capitalization]
2. Pick the end mark: "Where is my hat__" → **?** / . [telling mark on an asking sentence] / ! [big-feeling mark on an asking sentence] / , [comma used as end mark]
3. "my friend tom lives here." Which words need capitals? → **My and Tom** / only My [name capital missed] / only Tom [start capital missed] / My, Tom, and Friend [over-capitalization of a plain word]
4. Pick the end mark: "The stove is hot__" (a warning shout) → **!** / . [flat telling mark for a shout] / ? [asking mark for a shout] / no mark [missing end mark]
5. Which is written correctly? → **I saw Ben at the park.** / i saw Ben at the park. [lowercase I] / I saw ben at the park. [lowercase name] / I saw Ben at the park [missing end mark]

---

## `quiz.writing.35.grammar.01` — Label the job (parts of speech)

```yaml
quiz.writing.35.grammar.01:
  objectives: [obj.writing.35.grammar.01]
  skill: "label a word's part of speech (noun, verb, adjective, adverb, pronoun, conjunction) inside a real sentence"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 across 2 sessions (assign twice in one week)"
  difficulty: intro
  constraints:
    must_include: [one adjective-vs-adverb pair, one linking verb, one pronoun, one conjunction, book-flavored sentences]
    distractors: adjective/adverb confusion, verb-must-show-action, pronoun-labeled-noun, noun/verb job confusion
```

**Gold items (v1):** *(sentences flavored from `wizard-of-oz` / `black-beauty`)*

1. "Toto ran quickly across the yard." What job is **quickly** doing? → **adverb — it tunes the verb *ran*** / adjective [adjective/adverb confusion — "it describes"] / verb [attached-to-action confusion] / noun [job misread entirely]
2. "The brave lion cried." What job is **brave** doing? → **adjective — it tunes the noun *lion*** / adverb [adjective/adverb confusion] / noun [describing word taken as a thing] / verb [feeling word taken as action]
3. "The forest was dark." Which word is the verb? → **was** / dark [adjective taken as verb — verb-must-show-action] / forest [subject taken as verb] / the [helper word taken as verb]
4. "Black Beauty was gentle, and he loved his master." Which word **joins** the two sentences? → **and — a conjunction** / was [linking verb taken as joiner] / he [pronoun taken as joiner] / gentle [adjective taken as joiner]
5. "She gave the scarecrow a brain." What job is **She** doing? → **pronoun — a substitute for Dorothy's name** / noun [pronoun-labeled-noun] / adjective [job misread] / verb [job misread]

---

## `quiz.writing.35.grammar.02` — Compounds and run-on repair

```yaml
quiz.writing.35.grammar.02:
  objectives: [obj.writing.35.grammar.02]
  skill: "join sentences with comma + conjunction; identify true compounds; repair run-ons and comma splices"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10, at least one run-on and one splice repaired"
  difficulty: intro
  constraints:
    must_include: [one run-on repair, one comma-splice repair, one true-compound identification, one conjunction-by-meaning, book-flavored sentences]
    distractors: comma splice, bare run-on, comma-after-conjunction, pause-comma, compound-object-mistaken-for-compound-sentence, wrong-meaning conjunction
```

**Gold items (v1):** *(sentences flavored from `black-beauty` / `wizard-of-oz`)*

1. Fix the run-on: "The night was dark my master rode fast." → **The night was dark, and my master rode fast.** / The night was dark, my master rode fast. [comma splice] / The night was dark and, my master rode fast. [comma-after-conjunction] / The night was dark my master, rode fast. [pause-comma]
2. Which is a compound sentence? → **I called Toto, but he did not come.** / I called Toto and my dog. [compound object mistaken for compound sentence] / When I called, Toto came. [complex mistaken for compound] / I called and called. [compound verb mistaken for compound sentence]
3. Pick the joiner: "Dorothy was tired, ___ she kept walking." → **but** / and [contrast ignored — additive default] / so [cause reversed] / or [false choice]
4. Fix the comma splice: "The lion roared, everyone jumped." → **The lion roared, and everyone jumped.** / The lion roared everyone jumped. [comma removed — bare run-on] / The lion roared, Everyone jumped. [capital patch, splice remains] / The lion, roared everyone jumped. [pause-comma]
5. Which is correct? → **It rained all day, so we stayed inside.** / It rained all day so, we stayed inside. [comma-after-conjunction] / It rained all day, we stayed inside. [comma splice] / It rained, all day so we stayed inside. [pause-comma]

---

## `quiz.writing.68.grammar.01` — Clauses, phrases, and combining

```yaml
quiz.writing.68.grammar.01:
  objectives: [obj.writing.68.grammar.01]
  skill: "distinguish clauses from phrases; independent from dependent; combine into complex sentences with correct commas"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 including the dependent-clause-fragment item"
  difficulty: intro
  constraints:
    must_include: [clause-vs-phrase, dependent-clause fragment, one combine item, leading-clause comma placement, one relative-clause complex sentence, book-flavored sentences]
    distractors: phrase-taken-as-clause, because-fragment-accepted, comma splice, compound-instead-of-complex, missing/misplaced leading comma, long-simple-mistaken-for-complex
```

**Gold items (v1):** *(sentences flavored from `treasure-island` / `anne-green-gables`)*

1. Which word group is a **clause**? → **when the tide turned** / in the old sea chest [prepositional phrase taken as clause] / running down the beach [participial phrase taken as clause] / the black spot [noun phrase taken as clause]
2. "Because the map was torn." What is it? → **a fragment — a dependent clause standing alone** / a complete sentence [because-fragment-accepted] / a phrase [clause/phrase confusion — it has a subject and verb] / a run-on [any-error-is-a-run-on]
3. Combine into ONE complex sentence: "Jim hid in the barrel. He heard the pirates' plan." → **While Jim hid in the barrel, he heard the pirates' plan.** / Jim hid in the barrel, he heard the pirates' plan. [comma splice] / Jim hid in the barrel and heard the pirates' plan. [compound-instead-of-complex] / While Jim hid in the barrel he heard the pirates' plan. [missing leading comma]
4. Where does the comma go? "When the storm ended we sailed on." → **after *ended*** / after *When* [comma glued to the leaning word] / after *we* [pause-comma] / no comma needed [leading-clause comma missed]
5. Which sentence is **complex**? → **Anne, who talked the whole way, charmed Matthew.** / Anne talked and Matthew listened. [compound-mistaken-for-complex] / Anne talked all the way to Green Gables. [long-simple-mistaken-for-complex] / Talking all the way, without a single pause. [fragment]

---

## `quiz.writing.68.grammar.02` — Agreement and reference at distance

```yaml
quiz.writing.68.grammar.02:
  objectives: [obj.writing.68.grammar.02]
  skill: "hold subject-verb agreement, pronoun reference, and tense consistency across long sentences and paragraphs"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 including at least one agreement-at-distance item"
  difficulty: intro
  constraints:
    must_include: [agreement with intervening phrase, each-of construction, ambiguous pronoun, tense-drift, one repair-choice item, paragraph-flavored stems]
    distractors: proximity agreement, each-as-plural, ambiguity-unnoticed, case-confusion, tense shift, nonfinite verb
```

**Gold items (v1):** *(flavored from `anne-green-gables` / `call-of-wild` / `tom-sawyer`)*

1. "The box of old letters ___ under the stairs." → **was** / were [proximity agreement — verb matched to *letters*] / are [proximity agreement + tense shift] / being [nonfinite verb]
2. "When Anne met Diana at the brook, she was nervous." What's wrong? → ***she* could point to either girl — unclear reference** / *she* should be *her* [case-confusion] / nothing is wrong [ambiguity-unnoticed] / *she* should be *they* [number patch that changes meaning]
3. "Buck pulled the sled all day and then ___ by the fire." → **slept** / sleeps [tense drift to present] / sleeping [nonfinite verb] / will sleep [tense drift to future]
4. "Each of the sailors ___ a knife." → **carries** / carry [each-as-plural — verb matched to *sailors*] / are carrying [each-as-plural + aspect shift] / have carried [each-as-plural + aspect shift]
5. Fix the unclear pronoun: "Tom told Huck that he had found the treasure." → **Tom told Huck, "I found the treasure."** / leave it — it's fine [ambiguity-unnoticed] / Tom told Huck that him had found the treasure. [case-confusion] / Tom told Huck that they had found the treasure. [number patch that changes meaning]

---

## `quiz.writing.912.grammar.02` — Editing real prose

```yaml
quiz.writing.912.grammar.02:
  objectives: [obj.writing.912.grammar.02]
  skill: "edit for parallelism, dangling/misplaced modifiers, and commonly confused words"
  tools: parent-quiz
  item_type: multiple_choice
  n_items: 10
  pass_rule: ">= 8/10 with at least one correct in each family (parallelism, modifiers, confusables)"
  difficulty: intro
  constraints:
    must_include: [one series-parallelism repair, one dangling-modifier repair, one placement-changes-meaning item, two confusable families]
    distractors: partial-parallel fix, error-unnoticed, still-dangling rewrite, placement-indifference, confusable swap, hypercorrection
```

**Gold items (v1):**

1. Fix the series: "She liked reading, writing, and to hike." → **She liked reading, writing, and hiking.** / She liked to read, writing, and hiking. [partial-parallel fix — shape not carried through] / Leave it — it's correct. [error-unnoticed] / She liked reading, writing, and she liked hiking. [clause patch breaks the series]
2. Fix the modifier: "Walking to the barn, the rain soaked my coat." → **Walking to the barn, I was soaked by the rain.** / Walking to the barn, my coat was soaked by the rain. [still-dangling — the coat isn't walking] / The rain, walking to the barn, soaked my coat. [modifier moved, agent still wrong] / Leave it — it's correct. [error-unnoticed]
3. Which sentence says the pie is *almost gone*? → **He ate nearly the whole pie.** / He nearly ate the whole pie. [placement misread — that one says he almost didn't eat] / Both mean the same thing. [placement-indifference] / Neither — *nearly* can't modify *the whole pie*. [overcorrection]
4. "The ship lost ___ mast in the storm." → **its** / it's [apostrophe-means-possessive confusable swap] / its' [hypercorrection] / it is [expansion-test failure]
5. "There were ___ mistakes in her second draft." → **fewer** / less [count/mass confusable swap] / lesser [comparative form error] / few [comparison dropped — meaning changed]

---

## Authoring rules recap

- Distractors are **diagnostic** — each wrong answer encodes a named error type (comma splice, proximity agreement, dangling modifier, confusable swap), so a parent seeing repeated misses learns *which* habit to work on, not just "wrong." The bracketed tag on every distractor above is that name; it travels with the item into any generated variant.
- Sentences in generated variants change; the error type each distractor encodes must not. Book-flavored stems may be re-flavored from any on-device title ([`../reading/reading-lists.md`](../reading/reading-lists.md)).
- Correct answers are listed first here for authoring clarity — **shuffle option order at delivery.**
- These are grammar/usage items, not comprehension items — no `book_id` required (QUIZZES.md §7 applies to comprehension checks only).
- `quiz.writing.35.mechanics.01` and the `912.grammar.01` rubric live with their lessons (per [`OBJECTIVES.md`](./OBJECTIVES.md)), not in this file.
