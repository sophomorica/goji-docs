# Goji curriculum — planning home

**This is the place.** When someone says *“Goji computer,”* *curriculum,* *lesson plans,* *teaching animations,* *skills,* *Virginia SOLs,* *where the child stands,* or *Claude Design for learning* — start here.

**How humans get here:** open the company **hub** and say it in plain English. They do **not** need this path. Hub agents are instructed (`hub/CLAUDE.md`, `hub/GOJI.md`) to open this folder automatically.

**Mac mini:** hub is at `~/nr/hub`; this curriculum tree is at `~/nr/products/goji_learner/curriculum/`. Open Grok on **`~/nr/hub`** and say “Goji curriculum.” Human guide: `hub/FOR_CURRICULUM_LEAD.md`.

Status: **planning / organization** · vision locked in intent 2026-08-05 · **math 6–8 first slice on `main` 2026-08-12** (`goji-docs` #3)  
Scope: **K–12**, pillars **reading · writing · math**, offline-first Goji computer + parent metrics  
**Curriculum lead:** family curriculum owner (works with agents in this folder)  
**Product/engineering:** Patrick · pilot path still in `TODO.md` / child repos  

**Agents: do not look in `goji_computer/` for the 6–8 math slice.** It lives here (`subjects/math/`, `skills/math-6.md` / `math-7.md`). Device modules and parent `catalog_v1.json` have **not** been regenerated for `obj.math.68.*`.  

---

## North star (short)

The Goji computer is a **self-contained learning machine**.  
The parent app shows **exactly where each child stands** (especially reading, writing, math) and runs the **school day**.  
Curriculum is **skills covered** (Virginia expectations as checklist) + **teach → practice → comprehension**, with **Claude Design** animations and **local data** (Gutenberg books, Kiwix/Wikipedia, item banks) hydrating tools on the device.  
Optional **Grok** helps parents plan and generate — it does not replace on-device tools.

Full write-up: **[VISION.md](./VISION.md)** (read this in any curriculum session).

### The three pillars

| Pillar | Purpose |
|--------|---------|
| **Reading** | Access to information |
| **Writing** | Learn how to think |
| **Math** | Learn how to think straight |

Everything else (history, science, coding, …) builds on these.

---

## Map (new session order)

| Doc | Use when |
|-----|----------|
| **[VISION.md](./VISION.md)** | Paradigm, pillars, parent metrics, VA skills, Gutenberg/Kiwix, phases |
| **[TOOLS.md](./TOOLS.md)** | What the computer already has vs tools to invent |
| **[ANIMATIONS.md](./ANIMATIONS.md)** | Claude Design pipeline + ID mapping |
| **[QUIZZES.md](./QUIZZES.md)** | Comprehension checks, generation later |
| **[INTEGRATION.md](./INTEGRATION.md)** | **Anchor books, app chains, Kiwix research pairings** — how everything connects |
| **[PARENT_STANDING.md](./PARENT_STANDING.md)** | "Where the child stands" metrics spec (per pillar) |
| **[skills/](./skills/)** | **VA SOL coverage checklist** (math K–8 + HS courses, English 1–12, science, history — verified) |
| **[subjects/](./subjects/)** | Pillar subjects — math K–2 + 3–5 + **6–8 first slice**; reading/writing spines authored |
| **[bands/](./bands/)** | K–2 … 9–12 notes |
| **[assets/animations/](./assets/animations/)** | Animation registry (briefs; generation pending) |
| **[assets/templates/](./assets/templates/)** | Objective / lesson / animation brief templates |

### Product context (outside this folder)

| Doc | Why |
|-----|-----|
| [`../CLAUDE.md`](../CLAUDE.md) | Multi-repo map |
| [`../PARENT_APP_PRODUCT.md`](../PARENT_APP_PRODUCT.md) | School Day, wizard, dashboard (engineering SoT for app) |
| [`../MATH_MODULE_TASKS_PLAN.md`](../MATH_MODULE_TASKS_PLAN.md) | Module-scoped math tasks |
| [`../TODO.md`](../TODO.md) | Pilot / ship features |
| `../goji_computer/` | Device implementation + seed data (coding/typing, books, research/Kiwix path) |

---

## Working agreements

1. **Planning lives here; code lives in product repos.**  
2. **Pillars first** — reading, writing, math get curriculum priority.  
3. **Teach → practice → check** in every lesson plan.  
4. **Maximize existing tools**; gaps go in `TOOLS.md`.  
5. **Every animation and quiz maps to an objective/skill ID.**  
6. **Offline-first on the kid device**; Grok/generation is parent/cloud-side.  
7. **Vehicle + data** — prefer hydrating stable tools over new apps per skill.  
8. **Child’s pace** — trajectories and days adapt to the learner.  
9. Don’t re-litigate School Mode / sync here — use parent product + `SYNC_API.md`.

---

## How to use this in conversation

| Someone says | Agent does |
|--------------|------------|
| Curriculum / Goji learning vision | `VISION.md` + this README |
| Animations / Claude Design | `ANIMATIONS.md` + register in INDEX |
| Skills / Virginia / grade requirements | `VISION.md` §5; subject OBJECTIVES; plan catalog work |
| Parent sees progress / standing | `VISION.md` §6 + `PARENT_APP_PRODUCT.md` |
| What tools exist / what to build | `TOOLS.md` |
| Books / Gutenberg / classics | `subjects/reading/` + vision §7; audit backlog |
| Kiwix / Wikipedia lessons | Vision §7; research tool; quiz blueprints |
| First strand to fill | Pick pillar × band; use templates |

---

## Folder tree

```
curriculum/
├── README.md              ← you are here
├── VISION.md              ← full paradigm (pillars, parent, VA, offline knowledge)
├── TOOLS.md
├── ANIMATIONS.md
├── QUIZZES.md
├── subjects/              ← math, reading, writing (+ supporting)
├── bands/
└── assets/
    ├── animations/        ← INDEX + briefs
    └── templates/
```

**Next for curriculum lead:** pick a first pillar strand, or start a Virginia skills catalog worksheet for one grade — agents will help either way inside this tree.
