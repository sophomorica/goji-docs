# Goji curriculum — vision

Status: **north star (locked intent)** · updated 2026-08-05 · Living doc  
**Curriculum owner (planning & content):** Wife / family curriculum lead (works with agents here)  
**Product / engineering owner:** Patrick  

When she (or any session) talks about Goji curriculum, animations, skills, or “where does the child stand,” **this folder is the place** — start at [`README.md`](./README.md), then this file.

---

## 1. One-line job

Make the **Goji computer** a **self-contained, all-purpose learning machine** for a student — offline-first — while the **Goji parent app** gives parents **clear, trustworthy visibility** into where each child stands (especially **reading, writing, math**) and the power to **run a school day** from that picture.

---

## 2. The three pillars (learning paradigm)

These are non-negotiable. **Everything else sits on top of them.**

| Pillar | Why it exists | What “done well” means |
|--------|---------------|------------------------|
| **Reading** | Access to information | Child can get ideas *in* from text (and eventually rich offline sources) |
| **Writing** | Learn how to **think** | Child can get ideas *out* — organize mind, argue, reflect, explain |
| **Math** | Learn how to think **straight** | Precision, structure, honesty with quantity and logic |

With those three tools **well harnessed**, the child can follow curiosity into history, science, physics, language arts, coding, languages — whatever. Domain content (history, science, …) is **downstream**: it rides on literacy + clear thinking, and is fed by offline knowledge stores (books, Kiwix/Wikipedia, PDFs), not by treating every subject as equal “pillars.”

```
        Curiosity domains
     (history, science, CS, …)
                 ▲
                 │  built on
     ┌───────────┼───────────┐
     │           │           │
 Reading     Writing       Math
 (access)    (think)    (think straight)
```

**Subjects folders** under `subjects/` still include coding/typing/etc. as **tools and pathways** — not as co-equal pillars. Pillar work gets priority in curriculum planning.

---

## 3. Pedagogy: mainstream bones, avant-garde vehicle

We stay **on track with what works in teaching research and practice**, without becoming a clone of a textbook publisher:

| Pattern | On Goji |
|---------|---------|
| **Teach** | Principle first — often a **Claude Design** teaching animation / component, or short lesson media |
| **Practice** | Games and tools that **facilitate learning** (math drills, typing, spelling, flashcards, coding challenges) |
| **Comprehension / check** | Quizzes, writing responses, retells, accuracy gates — prove it stuck |

**Child’s pace** is the product stance: progress and school days adapt to the learner, not a factory bell. Avant-garde = **device + parent remote + offline knowledge + animated teaching objects + metrics parents can act on** — not gimmicks that abandon teach → practice → check.

Agents and curriculum authors should name the pattern in lesson plans (teach / practice / check steps). See lesson template.

---

## 4. Claude Design → curriculum media

We design **animated objects and components** (Claude Design and similar) that **plug into** lessons:

- Lesson can **kick off** with a teaching animation  
- Animations map to **skill / objective IDs** (never orphan clips)  
- Ship format on Pi is still open; authoring pipeline is in [`ANIMATIONS.md`](./ANIMATIONS.md)  
- Registry: [`assets/animations/INDEX.md`](./assets/animations/INDEX.md)

---

## 5. Skills catalog (Virginia, K–12)

We live in **Virginia**. For each grade K–12 and each domain, there is a **finite set of skills** students are expected to learn (SOLs and related expectations as the **coverage checklist**).

**Curriculum lead work (later, her lane):**

1. **Catalog** those skills by grade × domain (start with the three pillars).  
2. Ensure each skill is **covered** by some combination of: animation, lesson, practice tool, quiz, book, or explicit “gap / build tool.”  
3. Prefer a **vehicle + data** model: build stable tool surfaces on the computer; **hydrate** them with skill data, item banks, book lists, animation IDs — not a new app per skill.

IDs in this repo can start Goji-native (`obj.math.…`) and later gain a **Virginia / SOL crosswalk** field on each objective. Alignment is intentional; we are not shipping a public standards product first.

---

## 6. Parent app vision (metrics + school day)

The parent app is already the **school-day remote + trust dashboard** (see `PARENT_APP_PRODUCT.md`). Curriculum vision extends what “trust” means:

Parent opens app → family linked to Goji + **child profiles** → for a child they can see, at a glance:

- **Where they stand in reading comprehension** (and related literacy metrics)  
- **Where they stand in writing**  
- **Where they stand in math**  
- Supporting signals: **books read**, time/accuracy on tools, quiz scores, trajectory vs grade expectations  

Then they **organize a day** from that picture: “they need *this*” → assign School Day → Start → child works on the computer → proof flows back.

**Enrichment (cloud / Grok):** Grok (or similar) via API keys can help **articulate recommendations** — which tools, which quizzes, how to phrase the day — from the same metrics and skill map. Generation and advice stay **parent/cloud-side**; the **Pi stays offline-first** and runs **baked-in tools** hydrated by **local data**.

Target mental model:

> Tools on the computer are the **engine**.  
> Skills, books, animations, item banks are the **fuel**.  
> Parent app is the **instrument panel + day planner**.  
> Optional Grok is the **co-pilot**, not the engine.

---

## 7. Computer as all-in-one learning system

### Learning-facilitating surfaces

Math tools, reading, writing, spelling quizzes, typing + typing games, flashcards, coding challenges, teaching animations, comprehension checks — all in service of the pillars and curiosity domains.

### Reward / pure-fun games

Some games will be **reward-only** (fun unlock, post–School Mode play). Keep them **separate** from learning-facilitating games so metrics stay honest. (Standing locks / reward pools are product-later; principle is already noted in parent product docs.)

### Offline knowledge stores (huge product leverage)

| Store | Role |
|-------|------|
| **Project Gutenberg lineup** | Core **classic reading** path by grade/readability — Black Beauty, Treasure Island, Poe, etc. **Audit** what is already on the device; curate grade-level lists in curriculum docs |
| **Kiwix (full Wikipedia offline)** | History, science, and domain lessons; source material to **augment lessons** and (cloud/parent-side or local templates) help **build quizzes** without live internet on the kid path |
| **PDF catalog / notebooks / research app** | Structured lessons and student projects |

Self-contained means: after setup, a student can learn **for a long time** without treating the open web as required infrastructure.

---

## 8. System shape (target)

```
     Virginia / grade skill catalog (coverage checklist)
                         │
                         ▼
              Goji objectives (pillars first)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   Teach media      Practice tools    Checks / quizzes
   (Claude Design    (math, typing,    (comprehension,
    animations)       games, …)         writing, scores)
        │                │                │
        └────────────────┼────────────────┘
                         ▼
              Local data hydration
         (books, Kiwix, banks, progress)
                         │
           ┌─────────────┴─────────────┐
           ▼                           ▼
    Goji computer                  Parent app
    (do the work)            (see standing + run day)
           │                           │
           └───────── sync ────────────┘
                    (+ optional Grok
                     recommend / generate)
```

**Authoring loop (curriculum lead + agents + Claude Design):**

1. Catalog / map skills (VA) → objectives for a strand.  
2. Lesson plans: teach → practice → comprehension.  
3. Produce animations → register IDs.  
4. Quiz / check blueprints; classic book or Kiwix topic if relevant.  
5. Only then ask engineering to seed data or build missing tools.

---

## 9. Phases (planning — not a ship schedule)

| Phase | Goal | Exit criteria |
|-------|------|----------------|
| **P0 Organize** | This folder, tools inventory, templates, vision | ✅ 2026-08-05 |
| **P1 First pillar strand** | One pillar × one band (objectives + 5–10 lessons) | ✅ 2026-08-07 — math K–2 (5 objectives, 5 lessons in `subjects/math/lessons/`) |
| **P2 Media pilot** | Claude Design animations mapped; playback approach decided | Briefs + INDEX ✅ 2026-08-07 (3 briefs); **format decision still open** |
| **P3 Skills coverage map** | VA skill catalog started for pillars (even one grade) | ✅ 2026-08-07 — `skills/` (K–2 math + G1–2 English, VDOE-verified) |
| **P4 Gutenberg audit** | Inventory on-device classics + grade reading lists | ✅ 2026-08-07 — `subjects/reading/reading-lists.md` (13 on device) |
| **P5 Practice + quiz + metrics story** | Blueprint for parent “standing” per pillar | ✅ 2026-08-07 — `PARENT_STANDING.md` + quiz blueprints; eng later |
| **P6 Device integration** | Seed / player / deep-links / richer parent metrics | Product repos |
| **P7 Expand** | More grades, Kiwix-augmented domain units | Repeat |

**Does not replace** pilot path (School Day e2e, pairing, sync). Curriculum planning can advance in **this repo** while the pilot ships.

---

## 10. What is pillar vs supporting

| Priority | Area | Role |
|----------|------|------|
| **Pillar** | Reading | Access |
| **Pillar** | Writing | Thinking out loud on the page |
| **Pillar** | Math | Thinking straight |
| Supporting tool | Typing | Fluency for writing/reading on a computer |
| Supporting tool | Coding | Optional pathway; already strong seed content |
| Supporting knowledge | History, science, … | Via books + Kiwix + projects once pillars work |
| Shell | School Mode, Today, parent Start/Release | Delivery and proof |

---

## 11. Non-goals (near term)

- Shipping all K–12 VA skills before one vertical works end-to-end.  
- On-device LLM calls for the child (cloud/parent-side only).  
- Large animation binaries in `goji-docs` git.  
- Treating reward games as academic proof.  
- Replacing the parent product SoT (`PARENT_APP_PRODUCT.md`) from this folder.  
- Dual-editing curriculum “truth” inside `goji_computer` without updating `curriculum/`.

---

## 12. Open questions

- [ ] First vertical for her: which pillar × which grades first?  
- [ ] Animation ship format on Pi?  
- [ ] How formal is the VA SOL crosswalk in v1 IDs?  
- [ ] Gutenberg grade bands — who sets reading-level labels?  
- [ ] Which parent metrics are v1 vs later for “trajectory to requirements”?  
- [ ] Grok recommendation UX: suggest day vs generate quiz items vs both?

Capture decisions here when locked.

---

## 13. Session note for agents

If the user is the **curriculum lead** (or says they are working on curriculum/animations/skills):

1. Read `curriculum/README.md` + this file.  
2. Do not re-litigate the three pillars.  
3. Prefer teach → practice → comprehension in every lesson.  
4. Map work to objectives/skills; register animations.  
5. Use Gutenberg / Kiwix as first-class content sources in plans.  
6. Separate **learning games** from **reward games** when discussing design.  
7. Engineering gaps go in [`TOOLS.md`](./TOOLS.md); don’t invent architecture in lesson prose.
