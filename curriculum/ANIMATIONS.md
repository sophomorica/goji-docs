# Teaching animations — pipeline & mapping

Status: **conventions for planning** · 2026-08-05

Teaching animations explain **principles** (place value, fractions as parts of a whole, main idea vs detail, etc.). They are produced largely with **Claude Design** (and similar), then mapped into the Goji curriculum so they are never orphan media.

---

## 1. Goals

- Every animation has a stable **ID** and links to **≥1 objective**.
- Authoring can be rich (Claude Design); **on-device playback** stays Pi-cheap and skippable.
- Agents and humans can say: “animation for `MATH-K2-PV-03`” and find brief + file + lesson.

---

## 2. ID scheme

```
anim.<subject>.<band>.<strand>.<nn>
```

Examples:

| ID | Meaning |
|----|---------|
| `anim.math.k2.place-value.01` | K–2 place value, first clip |
| `anim.math.35.fractions.02` | Grades 3–5 fractions |
| `anim.reading.k2.phonics.01` | Early phonics |

**Objective IDs** (separate namespace — see subject OBJECTIVES):

```
obj.<subject>.<band>.<strand>.<nn>
```

Example: `obj.math.k2.place-value.03`

One animation may support multiple objectives; one objective may have multiple animations (intro / re-teach / extension).

---

## 3. Authoring pipeline (Claude Design → curriculum)

```
1. Objective exists (or draft) in subjects/<subject>/OBJECTIVES.md
2. Copy assets/templates/animation-brief.md
3. Fill brief: learning goal, script beats, on-screen text, duration target, brand notes
4. Generate in Claude Design
5. Export + store asset path (see §5)
6. Register row in assets/animations/INDEX.md
7. Link from lesson plan (template field: animations[])
```

**Brand constraints** (from product design): calm motion, no confetti cascades, seal/red-cream system when UI chrome appears, respect reduced-motion. Kid teaching clips should feel **warm and clear**, not gamer/HUD.

---

## 4. On-device delivery (proposed 2026-08-21: **self-contained HTML lesson packages** — see [`LESSON_PACKAGES.md`](./LESSON_PACKAGES.md); table kept for history)

| Option | Pros | Cons |
|--------|------|------|
| Short WebM/MP4 | Easy from Design exports | Size on SD; decode cost on Pi |
| Lottie / SVG motion | Small, crisp | Not every Design export converts cleanly |
| Storyboard stills + Svelte steps | Cheapest on Pi; full control | More engineering |
| Parent-side preview only at first | Unblocks authoring | No kid playback yet |

**Default while planning:** author against briefs + INDEX; **do not** bulk-commit large binaries into `goji-docs`. Note external/export paths in INDEX.

When we pick a format, record the decision here and in VISION open questions.

---

## 5. Where files live

| Kind | Location |
|------|----------|
| Briefs + INDEX | `curriculum/assets/animations/` (this repo) |
| Working exports (large) | Local folder or drive **outside** git, e.g. `~/nr-assets/goji-animations/` (suggested; create when first clip lands) |
| Shipped assets (later) | Catalog sync and/or `goji_computer` seed path TBD |

Suggested local layout (not required until first export):

```
~/nr-assets/goji-animations/
  anim.math.k2.place-value.01/
    brief.md          # optional copy
    source.*          # Design export
    preview.*
    ship.*            # chosen runtime format
```

---

## 6. Brief quality bar

A brief is ready when it answers:

1. **What must the child understand after watching?** (one sentence)
2. **Objective IDs** covered
3. **Beats** (0–15s, 15–30s, …) with visuals + narration/text
4. **Max length** (target ≤ 60–90s for intro clips)
5. **What practice comes next** on Goji (math module, flashcards, …)
6. **Misconceptions** to avoid reinforcing

Template: [`assets/templates/animation-brief.md`](./assets/templates/animation-brief.md)

---

## 7. Linking to lessons

In each lesson plan:

```markdown
## Media
- anim.math.k2.place-value.01 — intro (required)
- anim.math.k2.place-value.02 — re-teach if quiz < 70% (optional)
```

School Day integration (future): task type “watch animation” or embed step in a **lesson player**. Until then, PDFs can embed stills / QR to local path is **not** preferred — keep offline package design intentional.

---

## 8. Session checklist (when user brings a new Design export)

- [ ] Assign / confirm animation ID  
- [ ] Link objective(s)  
- [ ] Write or update brief  
- [ ] INDEX row  
- [ ] Note lesson plan(s)  
- [ ] Flag if a new **tool** is required for playback (`TOOLS.md` §6)  
