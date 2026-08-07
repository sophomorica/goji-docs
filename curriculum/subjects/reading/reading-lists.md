# Classic reading lists by band — Project Gutenberg spine

Status: **curated draft v1** · 2026-08-07  
Purpose: the **core classic reading path** on the Goji (VISION.md §7). Public-domain classics from Project Gutenberg, banded by grade, each earmarked for the role it plays and the quiz hook it will carry.

Rules:
- Every comprehension quiz for these books carries `book_id` (QUIZZES.md §7) — the catalog key on device is the source of truth; Gutenberg numbers below are for **ingest**, marked *verify at download* (numbers occasionally shift between editions).
- **Read-aloud** entries are for parents reading to pre-readers — listening comprehension counts as reading-pillar work in K–1.
- "On device?" column: fill from the device library audit; blank = not yet confirmed.

---

## K–2 (mostly read-aloud → early independent)

| Title | Author | Gutenberg # (verify) | Role | On device? |
|-------|--------|----------------------|------|------------|
| The Tale of Peter Rabbit | Beatrix Potter | 14838 | Read-aloud → first independent read; retell practice (`obj.reading.k2.comp.01`) | |
| The Tale of Benjamin Bunny (+ other Potter tales) | Beatrix Potter | 14407 etc. | Series comfort — same characters lower decoding load | |
| Mother Goose (illustrated collections) | trad. | 10607 | Rhyme/phonemic awareness read-aloud | |
| Aesop's Fables (children's editions) | Aesop | 11339 | Short texts — who/what/where checks (`obj.reading.k2.comp.02`); moral = first "main idea" | ✓ `aesop-fables` |
| The Story of the Three Little Pigs | trad./Jacobs | 18155 | Beginning/middle/end retell | |
| English Fairy Tales | Joseph Jacobs | 7439 | Read-aloud anthology; prediction practice | |
| Winnie-the-Pooh is **NOT** public domain everywhere — *excluded*; use Potter/Jacobs instead | — | — | — | — |

## Grades 3–5 (independent chapter books)

| Title | Author | Gutenberg # (verify) | Role | On device? |
|-------|--------|----------------------|------|------------|
| The Wonderful Wizard of Oz | L. Frank Baum | 55 | First long chapter book; sequence-of-events quizzes | ✓ `wizard-of-oz` |
| Alice's Adventures in Wonderland | Lewis Carroll | 11 | Vocabulary richness; word-lookup signal shines here | ✓ `alice-wonderland` |
| Black Beauty | Anna Sewell | 271 | First-person perspective; character-feelings inference (`obj.reading.35.comp.02`) | ✓ `black-beauty` |
| The Jungle Book | Rudyard Kipling | 236 | Episodic — one quiz per story; main idea + details (`obj.reading.35.comp.01`) | ✓ `jungle-book` |
| Peter Pan | J. M. Barrie | 16 | Fantasy; character motives; rich read-aloud crossover | ✓ `peter-pan` |
| The Secret Garden | F. H. Burnett | 113 | Character change over time; setting as mood | ✓ `secret-garden` |
| The Wind in the Willows | Kenneth Grahame | 289 | Friendship episodes; descriptive language | ✓ `wind-willows` |
| Heidi | Johanna Spyri | 1448 | Setting/contrast comprehension | |
| The Adventures of Pinocchio | Carlo Collodi | 500 | Cause-and-effect chains | |
| Five Children and It | E. Nesbit | 778 | Prediction + "what would you wish" journal crossover (writing pillar tie-in) | |

## Grades 6–8 (fluent independent)

| Title | Author | Gutenberg # (verify) | Role | On device? |
|-------|--------|----------------------|------|------------|
| Treasure Island | R. L. Stevenson | 120 | Plot tracking, unreliable adults, motive inference | ✓ `treasure-island` |
| Anne of Green Gables | L. M. Montgomery | 45 | Character growth across a novel; theme | ✓ `anne-green-gables` |
| Robinson Crusoe (abridged path OK) | Daniel Defoe | 521 | Problem→solution structure; older prose on-ramp | |
| Little Women | Louisa May Alcott | 514 | Long-novel stamina; four-character contrast | ✓ `little-women` |
| The Adventures of Tom Sawyer | Mark Twain | 74 | Irony and point of view | ✓ `tom-sawyer` |
| Around the World in Eighty Days | Jules Verne | 103 | Geography crossover (Kiwix: countries en route) | |
| A Christmas Carol | Charles Dickens | 46 | Short Dickens — flashback structure; theme | |
| The Call of the Wild | Jack London | 215 | Theme + tone; short enough to finish | ✓ `call-of-wild` |

## Grades 9–12 (literature proper)

| Title | Author | Gutenberg # (verify) | Role | On device? |
|-------|--------|----------------------|------|------------|
| Pride and Prejudice | Jane Austen | 1342 | Social subtext, irony; essay prompts (writing pillar) | |
| Jane Eyre | Charlotte Brontë | 1260 | First-person voice; moral dilemma essays | |
| Great Expectations | Charles Dickens | 1400 | Full Dickens; plot architecture | |
| The Scarlet Letter | Nathaniel Hawthorne | 25344 | Symbolism | |
| Frankenstein | Mary Shelley | 84 | Frame narrative; ethics essays; science crossover | |
| The Picture of Dorian Gray | Oscar Wilde | 174 | Theme/aesthetics argument writing | |
| Poe — complete tales (selections) | Edgar Allan Poe | 2147 | Short-form close reading; mood/tone analysis | |
| The Federalist Papers / founding docs (selections) | various | 1404 | Non-fiction argument reading (civics crossover) | |

---

## How a band list becomes School Days

1. Parent assigns **Reading: `<book>` + minutes** (existing task type).
2. Curriculum adds a **book-tied quiz** per chapter-chunk (blueprints in [`quiz-blueprints.md`](./quiz-blueprints.md)) — delivered as parent quiz until book-tied quizzes ship (product TODO).
3. **Journal exit ticket** for retell/inference objectives — the writing-pillar crossover is deliberate.
4. Finish a book → it shows in **books read** on the parent Reading standing card ([`../../PARENT_STANDING.md`](../../PARENT_STANDING.md)).

## Device audit (2026-08-07)

**13 books live in the reader's library** (`goji_computer` SQLite `books` table) — all marked ✓ above. Facts from the engineering audit:

- Books live in the DB (id/title/author/emoji/category/difficulty/age_range + chapters as paragraph arrays), **not** as files; no EPUBs, no cover images (emoji only, and the Reader grid doesn't render it yet).
- Ingest path exists: `backend/scripts/download_gutenberg.py` (15-book manifest, strips PG headers) + `backend/scripts/import_books.py` (json/folder/text modes; the `gutenberg` mode is a stub that just prints the URL). Chapter split regex can produce empty chapters — verify after import (known issue in repo README).
- **In the manifest but not imported:** `huckleberry-finn`, `swiss-family-robinson` — quick wins next ingest run.
- Legal note already tracked in `SHIP_PLAN.md`: strip Project Gutenberg headers/trademark before commercial redistribution.

## Curation TODO

- [x] Fill "On device?" from the device library audit *(2026-08-07)*
- [ ] Ingest priority order for missing titles: K–2 read-alouds first (Peter Rabbit, Three Little Pigs, English Fairy Tales — the K–2 shelf is thinnest: only Aesop today), then Heidi/Pinocchio, then the 9–12 shelf (empty today).
- [ ] Verify Gutenberg numbers at ingest time; prefer illustrated/children's editions for K–2.
- [ ] Reading-level labels: bands above are conventional placements; curriculum lead adjusts per child (child's-pace stance — bands describe books, not children).
