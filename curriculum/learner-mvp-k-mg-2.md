# Learner MVP — one skill, one sit-through (K.MG.2)

Status: **locked slice 2026-08-25** (Charlie correction) · planning SoT lives in `curriculum/`  
Skill: Virginia SOL **K.MG.2** plane figures (circle, triangle, square, rectangle)  
Objective / lesson / animation IDs: `obj.math.k2.shapes.01` · `lesson.math.k2.shapes.01` · `anim.math.k2.shapes.01`  
**Coverage: gap. Do not flip.** The catalog row in [`skills/math-k.md`](./skills/math-k.md) stays **gap** until a human sits through the teach.

School owns the pack. Goji plays it (parent app + computer). This repo does **not** author shapes, cards, or lesson copy.

---

## Ownership

| Who | Owns | Does not |
|-----|------|----------|
| **Goji School** | K.MG.2 fixture: v2 HTML (stroke / trace / tap / draw), 8-card practice spec, check bar | Learner software, parent app, computer player product |
| **Goji** | Parent app + computer path that *plays* that one cached pack | Curriculum / teach HTML |
| **This doc + sit-through page** | Product loop for tonight: pace + one audit row + evidence | A factory, a player product, a second skill |

School fixture (source of truth — **link only, do not scrape into a new lesson**):

- [K.MG.2 fixture pack](https://docs.google.com/document/d/16QD419w2BoWjIzEnlVLoV6GtcKWtnwo3yaeIfRiYdkU/edit)
- [proof pack v2 (hands-on)](https://docs.google.com/document/d/1i0WSoBVeZZoClJ3xxIwheJ1heW0caA6bJi7If-yUA9w/edit)

Handed into this repo as [`learner-mvp/pack.json`](./learner-mvp/pack.json). The sit-through page **plays that pack**. It does not invent teach HTML, voice, or a second skill.

---

## Four product layers

Tonight is one child, one cached pack, one result. Not a dashboard and not siblings.

| Layer | Tonight | Later (not this PR) |
|-------|---------|---------------------|
| **1. School pack** | Fixture in `pack.json`. Teach file is School’s v2 HTML. | Same pack cached on the computer |
| **2. Computer** | Desktop sit-through loads that HTML folder. Loop: **lesson → write/print engage → real check**. | Computer player runs the cached pack. **Not built here.** |
| **3. Parent app** | Same sit-through page: **pace** (this skill now / hold) + **one audit row** (skill, attempted, passed, confidence) + check evidence | Flutter surfaces the same one row |
| **4. Cloud** | `localStorage` stands in: one child, one result | One child, one result on the family project. Route any wire through `goji_cloud/SYNC_API.md` first. No store, no IAP, no siblings |

If the check is **not confident**, the parent **does not see passed**.

---

## Teach — load School’s v2 HTML (do not rewrite)

**File they own:** [`proof-k-mg-2/index.html`](./proof-k-mg-2/index.html) (relative path the loader opens)

If that file is already in this repo, the sit-through page iframes it. If it is missing, **do not rewrite the teach.** The sit-through page is the loader: it points at that relative path and keeps the parent-audit shell. Drop School’s existing v2 file as-is into `curriculum/proof-k-mg-2/index.html`, or use **Load School HTML**. Desktop browser is enough. There is no player product and no invented voice.

Hands-on (School): each shape stroke-draws, then the child traces / taps / draws.

| Shape | Child does |
|-------|------------|
| Circle | Trace around twice. No corners. |
| Triangle | Tap 3 corners, draw the sides. |
| Square | Tap 4 corners, draw the square. |
| Rectangle | Tap 4 corners, draw the rectangle. |

**HTML finished** = all four shapes completed.  
Construct (build a shape) is **off-device optional**. Not required to pass.

Browser voice in the School HTML, if any, is a stand-in. **Not Eve.**

---

## Practice — School’s 8-card spec only (no seed pipeline)

Parent authors deck **`math-k2-shapes-plane`** in the sit-through audit / flashcard UI (same page). This repo does not seed a pipeline or rewrite Memory.

Spec: **4 picture→name + 4 name→picture**, one pair per shape. Pictures are plain figures; square = equal sides; rectangle = clearly wider than tall. Parent types the four names; the page does not invent card copy.

| # | Front | Back |
|---|-------|------|
| 1 | Picture of a circle | circle |
| 2 | Picture of a triangle | triangle |
| 3 | Picture of a square | square |
| 4 | Picture of a rectangle | rectangle |
| 5 | Word circle | picture of a circle |
| 6 | Word triangle | picture of a triangle |
| 7 | Word square | picture of a square |
| 8 | Word rectangle | picture of a rectangle |

**Check run** = the 8 cards plus **2 random repeats** (10 items). Gate: **9/10**.

Author tonight, then drill the 10-item run. That is the pack, not a new flashcard product.

---

## Check bar — all three, or not passed

| Piece | Gate |
|-------|------|
| Teach | HTML finished (all four shapes) |
| Practice | 9/10 on the 10-item run (8 + 2 repeats) |
| Journal | One sentence: “This is a ___ because …” with a **true** attribute: round / three corners / four same sides / two long and two short |
| Parent | Pass or Not yet |

Any piece fail → audit row is **not passed**.  
A lucky tap cannot pass: the practice run is several items (10). If the check is not a real 10-item run, **confidence stays not confident** and the Passed cell is hidden (`—`).

---

## Parent surfaces tonight (one page, not a dashboard)

Open [`learner-mvp/index.html`](./learner-mvp/index.html) (see that folder’s README).

1. **Pace:** this skill now / hold.  
2. **One audit row:** skill · attempted · passed · confidence. Passed is visible only when the check is confident.  
3. **Evidence:** HTML finished, flashcard 9/10, journal sentence, parent Pass / Not yet.  
4. Persist locally (`localStorage`). **Do not write a covered flag** into any catalog.

---

## Out of this slice

Eve / voice · second skill · `english-k.md` · factory · clocks / patterns · science / history packs · Bluetooth · store / IAP · Speed Read / Memory / Tutor · siblings · standing dashboard · coverage flip · inventing or rewriting School’s teach HTML · scraping the School Docs into a new lesson · building a computer player product.

---

## Catalog

`skills/math-k.md` K.MG.2 stays **gap**. Sitting through tonight does not flip coverage. A human still has to sit the teach before anyone changes that row.
