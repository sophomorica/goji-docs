# Quizzes — strategy for Goji curriculum

Status: **planning** · 2026-08-05

Quizzes prove understanding and can satisfy School Day tasks. This doc separates **what exists**, **what we want**, and **how generation fits** without building generators yet.

---

## 1. What exists today

| Mechanism | Where | Notes |
|-----------|--------|-------|
| Parent-authored quizzes | Parent app → cloud → Pi (`ParentQuizzes`) | v1 prove path for School Day |
| Coding challenge **tests** | Coding curriculum JSON | Auto-check code; model for structured items |
| Math drills | Math modules | Practice with accuracy; not multi-item “quiz” objects |
| Flashcards | Flashcard app + synced decks | Fact check; can act as micro-quiz |
| Reading quizzes tied to books | Product TODO | Desired; not full spine yet |
| `content-generate` | Cloud stub | Future home for generation |

See also: `PARENT_APP_PRODUCT.md` (task types), workspace `TODO.md`.

---

## 2. Target model (curriculum-aligned)

Every quiz (or item bank) should declare:

```
quiz.<subject>.<band>.<strand>.<nn>
  objectives: [obj....]
  items: [...]
  tools: parent-quiz | flashcards | math-drill | reading-quiz | coding-tests
  pass_rule: score ≥ X% | N correct | module accuracy gate
```

**Layers:**

1. **Gold items** — human-authored, high trust (especially early grades).  
2. **Generated variants** — same skill, different numbers/words (from blueprint).  
3. **Placement / exit tickets** — short checks after an animation or PDF lesson.

Generation happens **parent/cloud-side** (product rule: Pi does not call third-party AI). On-device only runs cached items.

---

## 3. Item types we care about

| Type | Good for | Device surface |
|------|----------|----------------|
| Multiple choice | Reading, vocab, concepts | Parent quiz / future lesson player |
| Short numeric | Math | Math drill or quiz UI |
| Free response (short) | Explain thinking | Writing / journal (manual parent sign-off) |
| Flashcard reverse | Facts | Flashcards |
| Code assertion | CS | Coding tests |
| Book-referenced | Comprehension | Reading quiz (future) tied to book id |

---

## 4. Generation (later — design now)

**Input to a generator** should be a **blueprint**, not a vague prompt:

```yaml
# example only — not implemented
objective: obj.math.k2.place-value.03
skill: "identify tens and ones for numbers 10–99"
item_type: multiple_choice
n_items: 8
difficulty: intro
constraints:
  numbers: 10-99
  distractors: common place-value errors
animation_review: anim.math.k2.place-value.01  # optional "watch again" link
```

Outputs land in a bank versioned by objective. Parent can review before push (trust).

**Open product questions:** paywall / Grok path already flagged ~v1.2 in product TODO; curriculum generator rides that same capability.

---

## 5. How quizzes attach to lesson plans

Lesson plan fields (see template):

- `check.formative` — during lesson (2–3 items or a drill)  
- `check.summative` — end of lesson / unit  
- `check.remediation` — if fail → animation re-teach + easier bank  

School Day: parent (or future “suggested day”) assigns quiz task; Pi verifies score.

---

## 6. Near-term without new infrastructure

Until generators and lesson players exist:

1. Author **objectives + blueprints** in this folder.  
2. Use **parent quizzes** manually for pilot families.  
3. Use **math module accuracy** as proxy for math objectives.  
4. Use **flashcard decks** for vocab strands.  
5. Log desired auto-links in lesson plans (`blocked_on: reading-quiz-book-id`).

---

## 7. Reading-specific note

Workspace TODO: *“Reading quizzes tied to actual books.”*  
Curriculum planning should always store `book_id` / catalog key when a check is comprehension of a text — so engineering can wire once without re-authoring.
