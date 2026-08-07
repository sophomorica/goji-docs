# Virginia skills catalog — coverage checklist

Status: **complete catalogs 2026-08-07** · Math K–8 + Algebra I/Geometry/Algebra II · English 1–12 — all verified against fetched VDOE sources  
This is the coverage checklist from VISION.md §5: for each grade × pillar, the finite list of skills Virginia expects, and **what on Goji covers each one**.

**Provenance:** every SOL code and statement in these files was verified against fetched official VDOE documents (2023 Mathematics SOLs; 2024 English SOLs — "Understanding the Standards" grade docs), not written from memory. Source URLs are noted per file. When VDOE revises standards, re-verify before editing.

## Coverage statuses

| Status | Meaning |
|--------|---------|
| **covered** | A Goji objective + lesson + check exists (IDs linked) |
| **partial** | Goji objective covers a subset; gap described |
| **planned** | Objective IDs assigned, lessons not yet authored |
| **gap** | Nothing on Goji yet — candidate for next strand or TOOLS.md backlog |
| **off-device** | Deliberately parent-led / physical (e.g. handwriting, measuring real objects); Goji may hold the record, not the activity |

Rule from the vision: every skill ends up covered by **some combination** of animation, lesson, practice tool, quiz, book — or an explicit gap row. No silent omissions.

## Files

**K–2**

| File | Scope |
|------|-------|
| [`math-k.md`](./math-k.md) | Kindergarten math (2023 SOLs) |
| [`math-1.md`](./math-1.md) | Grade 1 math |
| [`math-2.md`](./math-2.md) | Grade 2 math |
| [`english-1.md`](./english-1.md) | Grade 1 English — reading + writing pillars |
| [`english-2.md`](./english-2.md) | Grade 2 English — reading + writing pillars |

**3–5**

| File | Scope |
|------|-------|
| [`math-3.md`](./math-3.md) | Grade 3 math (12 standards) |
| [`math-4.md`](./math-4.md) | Grade 4 math (18 standards) |
| [`math-5.md`](./math-5.md) | Grade 5 math (14 standards) |
| [`english-3.md`](./english-3.md) | Grade 3 English |
| [`english-4.md`](./english-4.md) | Grade 4 English (media messages begin) |
| [`english-5.md`](./english-5.md) | Grade 5 English |

**6–8**

| File | Scope |
|------|-------|
| [`math-6.md`](./math-6.md) | Grade 6 math (15 standards) |
| [`math-7.md`](./math-7.md) | Grade 7 math (15 standards) |
| [`math-8.md`](./math-8.md) | Grade 8 math (16 standards — Algebra I on-ramp) |
| [`english-6.md`](./english-6.md) | Grade 6 English (FFR/FFW defer to K–5 from here) |
| [`english-7.md`](./english-7.md) | Grade 7 English |
| [`english-8.md`](./english-8.md) | Grade 8 English (MLA/APA begins) |

**High school** — English 9–12 catalogs exist; HS math is course-structured (see [`GRADUATION.md`](./GRADUATION.md))

| File | Scope |
|------|-------|
| [`math-algebra1.md`](./math-algebra1.md) | Algebra I |
| [`math-geometry.md`](./math-geometry.md) | Geometry |
| [`math-algebra2.md`](./math-algebra2.md) | Algebra II |
| [`english-9.md`](./english-9.md) | Grade 9 English (9–12 reading rows ingest-blocked) |
| [`english-10.md`](./english-10.md) | Grade 10 English — world literature |
| [`english-11.md`](./english-11.md) | Grade 11 English — American literature + workplace docs |
| [`english-12.md`](./english-12.md) | Grade 12 English — British literature + technical writing |

Sources: K–2 files cite per-grade "Understanding the Standards" docs; grades 3–8 math cite the 2023 K–12 math SOL doc (…/48908/…) and grades 3–12 English cite the 2024 K–12 English SOL doc (…/53643/…), both fetched 2026-08-07 via archive.

**Science (2018 SOLs — current for K–Physics; 2025 expansion covers only additional HS courses)** — delivery per PRACTICES.md §6: Kiwix-anchored units + PDF lessons + quizzes; labs/hands-on off-device, parent-led

| File | Scope |
|------|-------|
| [`science-k.md`](./science-k.md) | Kindergarten science (11 standards) |
| [`science-1.md`](./science-1.md) | Grade 1 science (8 standards) |
| [`science-2.md`](./science-2.md) | Grade 2 science (8 standards) |
| [`science-3.md`](./science-3.md) | Grade 3 science (8 standards — jungle-book anchor synergy) |
| [`science-4.md`](./science-4.md) | Grade 4 science (8 standards — solar system, Oz weather unit) |
| [`science-5.md`](./science-5.md) | Grade 5 science (9 standards — energy year) |
| [`science-6.md`](./science-6.md) | Grade 6 science (9 standards — atoms, watersheds) |
| [`science-7-life.md`](./science-7-life.md) | Grade 7 Life Science (11 standards — call-of-wild anchor synergy) |
| [`science-8-physical.md`](./science-8-physical.md) | Grade 8 Physical Science (9 standards — most drill-compatible) |
| [`science-biology.md`](./science-biology.md) | Biology (8 standards — lab-credit constraint noted) |
| [`science-chemistry.md`](./science-chemistry.md) | Chemistry (7 standards — lab-credit constraint noted) |
| [`science-earth.md`](./science-earth.md) | Earth Science (12 standards — most on-device-deliverable lab science) |
| [`science-physics.md`](./science-physics.md) | Physics (9 standards — sequence after Algebra II) |

Science sources: each file cites its per-grade/course 2018 Science SOL doc on doe.virginia.gov (ids: K 23733, G1 23721, G2 23723, G3 23725, G4 23727, G5 23729, G6 23731, LS 23715, PS 23717, BIO 15700, CH 15704, ES 15708, PH 23719), all fetched 2026-08-07 via archive. Laboratory-science graduation credits (×3, two disciplines) are tracked in [`GRADUATION.md`](./GRADUATION.md).

**History & Social Science (2023 SOLs) + Economics & Personal Finance (2019 SOLs)** — delivery per PRACTICES.md §6: Kiwix-anchored units + PDF lessons + quizzes via the research→notebooks chain; primary sources ride the reader (federalist-papers ingest underway) and the informational-reading objectives (`obj.reading.*.info.*`).

**2023 structure note:** each grade is a named course — Grade 4 = Virginia Studies (VS), 5 = US History to 1865 (USI), 6 = US History 1865–Present (USII), 7 = Civics & Economics (CE), 8 = World Geography (WG); high school: 9 = World History to 1500 (WHI), 10 = World History 1500–Present (WHII), 11 = VA/US History (VUS), 12 = VA/US Government (GOVT). K–3 standards carry Civics/Geography/Economics/History strand labels; grades 4–12 have a course-wide Skills standard plus numbered standards (strand "—" in the tables).

| File | Scope |
|------|-------|
| [`history-k.md`](./history-k.md) | Kindergarten — Community (8 standards + Skills) |
| [`history-1.md`](./history-1.md) | Grade 1 — Commonwealth of Virginia (8 + Skills) |
| [`history-2.md`](./history-2.md) | Grade 2 — United States of America (13 + Skills) |
| [`history-3.md`](./history-3.md) | Grade 3 — The World (10 + Skills — **Egypt unit is the INTEGRATION §4 worked example**) |
| [`history-4-va-studies.md`](./history-4-va-studies.md) | Grade 4 — Virginia Studies, VS (13 + Skills) |
| [`history-5-us1.md`](./history-5-us1.md) | Grade 5 — US History to 1865, USI (9 + Skills) |
| [`history-6-us2.md`](./history-6-us2.md) | Grade 6 — US History 1865–Present, USII (9 + Skills — call-of-wild Klondike synergy) |
| [`history-7-civics.md`](./history-7-civics.md) | Grade 7 — Civics & Economics, CE (14 + Skills — Federalist 10/51 named in-standard) |
| [`history-8-world-geo.md`](./history-8-world-geo.md) | Grade 8 — World Geography, WG (17 + Skills — nine templated region units) |
| [`history-9-whg1.md`](./history-9-whg1.md) | Grade 9 — World History to 1500, WHI (13 + Skills) |
| [`history-10-whg2.md`](./history-10-whg2.md) | Grade 10 — World History 1500–Present, WHII (12 + Skills) |
| [`history-11-vus.md`](./history-11-vus.md) | Grade 11 — VA/US History, VUS (17 + Skills — usual verified-credit course) |
| [`history-12-govt.md`](./history-12-govt.md) | Grade 12 — VA/US Government, GOVT (14 + Skills — Federalist reading spine) |
| [`econ-personal-finance.md`](./econ-personal-finance.md) | Economics & Personal Finance, EPF (18 standards — **the separate 1-credit graduation requirement**, 2019 SOLs) |

History/EPF sources: the 13 HSS courses cite the combined 2023 History and Social Science SOL doc (…/58926/…, April 2023); EPF cites the 2019 Economics and Personal Finance SOLs (…/2004/…, Oct 17 2019) — both fetched 2026-08-07 via archive. The History & Social Sciences ×3 credits (1 verified) and the EPF credit are tracked in [`GRADUATION.md`](./GRADUATION.md).

## How objectives relate

Goji objective IDs (`obj.math.k2.…`) are the native spine; the SOL code is the **crosswalk** column on each objective (see `subjects/*/OBJECTIVES.md`). One objective can serve several SOL sub-skills; one SOL can need several objectives. The catalog is the completeness check, not the teaching unit.
