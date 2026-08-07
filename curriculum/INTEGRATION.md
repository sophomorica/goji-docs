# Integration — anchor books, app chains, research pairings

Status: **locked intent 2026-08-07** (from owner direction) · Living doc  
The rule this file exists to enforce: **nothing on the Goji is random.** Every lesson pulls from a designated text, every research topic is germane to what's being read, and every app hands off to another app. The computer is one connected school, not a pile of tools.

---

## 1. The anchor-book model

Each band (eventually each grade) designates an **anchor book** from the on-device Gutenberg library. While a book is the anchor:

| Strand | Pulls from the anchor |
|--------|----------------------|
| Phonics / word study (K–2) | Decodable + high-frequency decks **sample the anchor's actual words** — the flashcards feed tonight's reading |
| Fluency | Read-aloud passages come from the anchor (or its rhyme companion for K) |
| Vocabulary | Per-chapter decks built from the child's own word-lookups in the anchor |
| Comprehension | Retells, quizzes (book-tied `source_book_id`), inference exit tickets — all on the anchor |
| Writing / grammar | Journal prompts and fix-the-sentence items sample anchor lines |
| Research (Kiwix) | Topics from the anchor's world (§4) — never decorative |
| Typing | Exercise text = anchor sentences and deck words |

One book, seven surfaces. That's the "vehicle + data" rule (TOOLS.md §5) made concrete.

### Current anchor assignments (from the on-device library)

| Band | Anchor | Rotation next | Notes |
|------|--------|---------------|-------|
| **K–2** | `aesop-fables` | Peter Rabbit, Mother Goose, Three Little Pigs **after ingest** | Fables are short, moral-bearing, animal-rich — ideal for retell + detective questions. Mother Goose (post-ingest) becomes the **phonics/rhyme companion**: rhymes are the traditional phonemic-awareness engine |
| **3–5** | `jungle-book` → `black-beauty` → `alice-wonderland` → `wizard-of-oz` | `secret-garden`, `wind-willows`, `peter-pan` | Each anchor carries the skill it's best at: Jungle Book = main idea (episodic), Black Beauty = inference (first-person clues), Alice = vocabulary (collectible words), Oz = sequence/cause-effect |
| **6–8** | `treasure-island` → `call-of-wild` → `tom-sawyer` → `anne-green-gables` | `little-women` | Theme, motive/irony, long-arc stamina |
| **9–12** | **pending ingest** (Poe, Pride & Prejudice, Frankenstein, Federalist) | — | Lessons authored and waiting; ingest priorities in `subjects/reading/reading-lists.md` |

Curriculum lead owns rotation timing (child's pace); agents never advance the anchor mid-book.

---

## 2. The standard app chain (one lesson, many apps)

The default integrated flow a School Day assigns — each step feeds the next:

```
  reader ──────► journal ──────► parent quiz
 (anchor        (retell /        (book-tied,
  chapter)       exit ticket)     source_book_id)
     │                                  │
     ▼                                  ▼
  word lookups ──► flashcards      research (Kiwix) ──► notebooks
  (count syncs)    (chapter          (anchor-germane        (fact log /
                    vocab deck)       topic, §4)             unit notes)
                        │
                        ▼
                     typing
                 (same words/lines)
```

**Working rules:**
1. **Same text everywhere.** The deck word came from the chapter; the typing line is the chapter's sentence; the quiz distractors are other chapters' details. A child never meets disconnected content in one day.
2. **Every chain ends in proof** — quiz score, journal entry, or deck gate — which syncs to the parent (PARENT_STANDING.md).
3. **Research is downstream of reading**, not a separate subject: the fable's wolf, the anchor's era, the story's geography.
4. **Household tasks and reward games stay outside** the chain (metrics honesty — VISION §7).

## 3. Chain templates by band

| Band | Typical daily chain (25–45 min) |
|------|--------------------------------|
| K–2 | flashcards (anchor phonics/HF deck) → reader (fable, aloud) → journal (3-sentence retell) → parent quiz (4–5 items) → *spice:* research animal fact |
| 3–5 | reader (chapter) → journal (umbrella / claim+proof) → parent quiz → research (anchor topic) → notebooks (2 facts) → flashcards (vocab deck) |
| 6–8 | reader (chapters) → notebooks (running summary / theme log) → parent quiz → research (era/geography unit §4) → journal (analysis paragraph) |
| 9–12 | reader (close-read passage) → notebooks (annotation/argument map) → writing (essay-form response) → research (primary-source context) → parent review |

## 4. Kiwix research pairings (germane topics per anchor)

Offline Wikipedia turns each anchor into a **unit**. Pairings are part of curriculum, chosen when the anchor is assigned:

| Anchor | Research topics (offline Wikipedia) |
|--------|--------------------------------------|
| `aesop-fables` | The fable's animal each week (wolf, fox, crow, ant, lion…); Ancient Greece (light, 2nd pass) |
| `jungle-book` | Wolf packs; Indian jungle; tigers; mongoose (Rikki-Tikki); India (geography) |
| `black-beauty` | Horses (behavior, gaits); Victorian era; carriages and cabs; animal welfare history |
| `alice-wonderland` | Playing cards; flamingos & hedgehogs; croquet; Victorian England |
| `wizard-of-oz` | Tornadoes; Kansas & the prairie; hot-air balloons; emeralds |
| `treasure-island` | Piracy (real history vs the book); sailing ships; navigation; maps |
| `call-of-wild` | Klondike gold rush; sled dogs; Yukon; wolves (revisited, deeper) |
| `tom-sawyer` | Mississippi River; steamboats; caves; 1840s America |
| `anne-green-gables` | Prince Edward Island / Canada; one-room schools |
| *(standalone unit example)* | **Egypt**: research → notebooks (pyramids, Nile, hieroglyphs) → parent quiz from notes → journal "day in the life" — the same chain works without a novel when a domain unit (history/science) leads |

**Germaneness rule:** a research topic must answer "why now?" with the anchor or the unit. "Because it's interesting" is allowed for the child's free curiosity time — not for the assigned chain.

## 5. What this asks of engineering (routed, not invented here)

Nothing in §2–4 requires a new app — the chain runs today on reader / journal / quiz / flashcards / research / notebooks / typing via School Day tasks. Friction worth logging in TOOLS.md §6:

- **Lookup → deck pipe** (vocab finds auto-propose a deck) — removes the parent copy step
- **Research task type with a topic hint** ("open research to 'Wolf'") — same `navigateTo(appId, intent)` mechanism PDF/book tasks already use
- **Anchor-book field on School Day plans** — lets the wizard preselect the reader/quiz/deck set for the current anchor
- Kiwix content itself: confirm the offline Wikipedia snapshot on device covers the §4 topics (research app audit — device work)

## 6. Session note for agents

When authoring any lesson: name the **anchor book**, pull practice text **from it**, pick the research topic **from §4 (or extend the table)**, and end the chain in synced proof. If a lesson can't connect to the anchor, either fix the lesson or propose an anchor change to the curriculum lead — don't ship a disconnected lesson.
