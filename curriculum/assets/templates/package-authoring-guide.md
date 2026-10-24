# Lesson package authoring guide (agents) — the unit of work

Status: working guide 2026-08-24 · Companion to `LESSON_PACKAGES.md` (the spec) and `PRACTICES.md` (the law).
Exemplar: `assets/lessons/lesson.science.k2.living.01/` — copy its architecture, not its content.

The K–4 science wave is **merged** (2026-08-24): write new units straight into `OBJECTIVES.md`, `quiz-blueprints.md`, `INDEX.md`, and `skills/`. Use `_fragments/` only when several agents are authoring in parallel and would collide on those shared files.

## 0. What one "unit" ships

For an assigned skill row (e.g. Science K.7), you produce ALL of:

| # | Deliverable | Path | Contention |
|---|------------|------|-----------|
| 1 | Objective row (+ strand section if new) | `curriculum/_fragments/<lesson.id>/objective.md` | fragment — merged later |
| 2 | Lesson plan | `curriculum/subjects/<subject>/lessons/<lesson.id>.md` | direct write (own file) |
| 3 | Quiz blueprint section | `curriculum/_fragments/<lesson.id>/quiz.md` | fragment |
| 4 | Package | `curriculum/assets/lessons/<lesson.id>/{lesson.json,assets.json,index.html}` | direct write |
| 5 | Animation brief | `curriculum/assets/animations/anim.<...>.md` | direct write (own file) |
| 6 | INDEX row | `curriculum/_fragments/<lesson.id>/index-row.md` (one `\|`-row, status `shipped-inline`) | fragment |
| 7 | Skills flip | `curriculum/_fragments/<lesson.id>/skills-flip.md` (skills file name, SOL row key, full replacement text for the "What covers it" and "Status" cells) | fragment |

Formats: objective row columns = `ID | Statement | Success criteria | Prereqs | Practice tools | Animations | Quiz | VA | Status`; quiz blueprint = YAML block + numbered gold items with the misconception each distractor encodes (see `subjects/science/quiz-blueprints.md`); lesson plan template = `assets/templates/lesson-plan.md` (follow `lesson.science.k2.living.01.md` for tone/detail); brief template = `assets/templates/animation-brief.md` with "Claude Design" fields = "n/a — inline in package".

Status honesty (PRACTICES §3.10): objective/lesson status is `ready (package authored; player pending — TOOLS.md §6A)`. Skills flip is `partial` or `covered` with an honest note ("lesson authored <date>; kid playback blocked on lesson player; parent-quiz bridge available"). Never plain "covered" while the player is unshipped.

## 1. IDs are law

- IDs are ASSIGNED in your work order — never invent different ones. `lesson.id` = folder name = plan ID; `obj./quiz./anim.` share the stem.
- If your work order says an objective already exists (math "planned" rows), reference it; do NOT author a duplicate.
- Every ID you reference must resolve (audit checklist §4). Cross-band prereqs allowed.

## 2. The lesson design bar (this is the product)

- **Four stages** `hook → teach → practice → check` (LESSON_PACKAGES §6). Hook ≤20s poses a real question and captures a guess that the result screen revisits. Teach ≤90s: beats with captions + narration + one animated scene per beat; must land the principle, not trivia. Practice ≥6 interactions with instant, misconception-aware feedback (wrong answer names WHY via the specific error, then re-queues). Check 3–5 items, every distractor encodes a named misconception; pass gate in `lesson.json` (K–2: 4/5).
- **One objective per lesson (K–5).** A fat SOL may split into two lessons (your work order says so).
- **Interaction fits the content.** Do not clone the sort mechanic blindly. Pick per topic: sort/bins, sequence-the-steps, drag-to-label a scene, tap-the-map, timeline order, match pairs, build/assemble, observe-and-predict. Keep the mechanic touch-first (targets ≥64px), single-item-at-a-time where possible, and misconception-aware.
- **Misconceptions drive everything**: named in the objective row, encoded in practice feedback and check distractors, listed in the brief's "must not show".
- **Anchor-tied** where the work order names one (Aesop animal, book setting); otherwise explicitly "anchor: n/a" with the research hand-off named (Kiwix topic → journal sentence).
- **Remediation is specific**: the result screen's retry path replays teach; the plan's "If not yet" names an exact easier step.
- **Age-fit language**: K–2 body text ≥28px, one short sentence at a time, every instruction has a read-aloud 🔊; 3–5 may use two-sentence captions, still read-aloud on instructions.

## 3. Package HTML rules (copy from the exemplar)

Open `assets/lessons/lesson.science.k2.living.01/index.html` and reuse verbatim its: player bridge (`post()`, `player.config` listener, `lesson.ready/stage/check/complete` messages), speech helper (`say(txt,id)` voice-file-else-speechSynthesis), media loader (`GOJI_MEDIA`, `img()/clip()/vo()`, `showBeat()` clip>still>SVG fallback), stage machine + progress dots, reduced-motion handling, result ring + gate + finish flow, base CSS tokens (cream/ink/seal-red palette). Change the content: stages, scenes, items, quiz.

Hard rules:
- Self-contained: no CDN, no webfonts, no fetch, no storage. Only `media/…` relative refs. HTML < 300 KB.
- Inline SVG fallback for EVERY visual so the package fully works with no `media/` folder present.
- No faces/eyes on non-living things in your SVGs. Calm motion, no confetti; `prefers-reduced-motion` collapses animation to stepped stills (exemplar's `later()` pattern).
- Touch: pointer events (not mouse-only), tap alternative for every drag.
- Every quiz item posts `{id, correct, chosen}`; practice posts its telemetry in `lesson.check`'s `practice` field like the exemplar.
- **Test hook (new, required)** — before the closing `})();` add:

```js
window.GOJI_TEST={go,quiz:()=>QUIZ,autoCheck:function(pass=true){go(3);return new Promise(res=>{const step=()=>{if(document.getElementById('result').style.display!=='none'){res({score});return;}const q=QUIZ[qi];const want=pass?q.a:((q.a+1)%q.o.length);document.querySelectorAll('#opts .opt')[want].click();setTimeout(()=>{document.getElementById('qNext').click();setTimeout(step,50);},40);};setTimeout(step,150);})}};
```

Adapt names if your check uses different variables — the CONTRACT is: `GOJI_TEST.go(n)` jumps stages; `GOJI_TEST.autoCheck(true)` answers every item correctly and lands on the result screen; `autoCheck(false)` answers wrong. The validator depends on it. Keep `#finish` clickable on pass and hidden/absent on fail-gate, exemplar-style.

## 4. `lesson.json` + `assets.json`

`lesson.json`: exemplar shape exactly (id/title/subject/band/grade_hint/objectives/va_sol/duration_min/anchor/stages/check/animations/reduced_motion/version/entry).

`assets.json` (this session: prompts are authored NOW, generated later when budget lands — write them as if generation runs tomorrow):
- `"style": "../../../tools/lesson_assets/style.json"`.
- ≤1 recurring character (`characters.<name>` + `"ref"` on images that must stay on-model). History figures: use period-appropriate storybook depiction, no photoreal, no named-likeness claims beyond standard historical portraiture.
- Images: `hook_*`, `teach_*` (one per teach beat, kind `scene`), `card_*` (practice/check items, kind `card`), `badge_*` (concept emblems). ~15–25 images. Prompts concrete and style-free (style.json carries style); include "no creatures"/"clearly a toy"-type misconception guards.
- Clips: ≤5, each `from` a teach image, 6s, calm loopable motion described.
- Voice: one line per `data-voice`/`say()` id used in the HTML — hook, each teach beat, sort intro/done, each feedback id, each `q<n>`, each `why_*` (if used), pass/retry/done. `[pause]`/`<emphasis>` allowed.
- Media budget note: images land first (`gen_all.py` default `--only images`); design teach beats so stills alone carry the lesson (clips are enrichment).

## 5. Validate before you report done

```bash
cd /home/claude/work/goji/curriculum && python3 tools/lesson_assets/validate_package.py <lesson.id>
```

Must print `PASS`. It checks manifests, IDs, size, self-containment, then plays the package headless: load w/o console errors, `lesson.ready`, stage walk, `autoCheck(true)` → `lesson.check` full score + `lesson.complete` on finish, `autoCheck(false)` → gate holds. Fix and re-run until green. Also self-run the PRACTICES §4 checklist on your batch and state the result in your final report.
