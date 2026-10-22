# Task: ship interactive lesson packages on the Goji computer (K–4), starting from the finished exemplar

You are working in `~/Desktop/active/products/goji_learner/` (the `goji-docs` repo with the three product repos cloned as siblings: `goji_computer/`, `goji_cloud/`, `goji_learner_app/`). Read `CLAUDE.md` first and obey its cross-repo rules — especially: the sync contract in `goji_cloud/SYNC_API.md` is edited before either side implements it; nothing cloud/app-related goes into `goji_computer/`; no secrets in any repo; `GOJI_*` env vars only; tests green before "done".

## Context (already done — do not redo)

- Spec: `curriculum/LESSON_PACKAGES.md` — package format, `lesson.json` manifest, player ⇄ package postMessage contract (§4), sync-contract additions (§5), authoring bar (§6), batch plan (§7), engineering tickets (§8). Treat it as the design; implement it, don't re-litigate it.
- Exemplar package: `curriculum/assets/lessons/lesson.science.k2.living.01/` — `index.html` (works stand-alone in a browser), `lesson.json`, `assets.json`, `media/` (22 generated WebP images present; clips and voice not yet generated).
- Curriculum files for the exemplar: `curriculum/subjects/science/{OBJECTIVES.md,quiz-blueprints.md,lessons/lesson.science.k2.living.01.md}`, `curriculum/assets/animations/anim.science.k2.living.01.md` + INDEX row, `curriculum/skills/science-k.md` (K.6 = partial).
- Asset pipeline: `curriculum/tools/lesson_assets/gen_assets.py` + `style.json` + `README.md`. Key is in `goji_learner/.env` as `XAI_API_KEY` (the script finds it). Needs `pip3 install pillow` for WebP optimize.
- House rules for content: `curriculum/PRACTICES.md` (one objective per lesson K–5, anchor book, measurable gate, named misconceptions, IDs are law, honest statuses, audit checklist §4).

## Phase 1 — finish the exemplar's media (30 min, ≈ $5 of API)

1. `cd curriculum/tools/lesson_assets && pip3 install pillow`
2. `python3 gen_assets.py lesson.science.k2.living.01 --only images` → regenerates only `card_cloud` (its prompt was fixed; the bad render is in `media/_rejected/`). Also move `media/src/card_seed.png` and `media/img/card_seed.webp` to `media/_rejected/` first so the seed is redone with its sprout.
3. `python3 gen_assets.py lesson.science.k2.living.01 --only clips,voice` → five 6-second image-to-video clips + ~30 MP3 narration lines. Video requests poll asynchronously; expect 1–3 min per clip.
4. Open `index.html` in a browser and play through all four stages. Review against `tools/lesson_assets/README.md` "Review loop": wolf stays on-model in every clip; no camera moves/cuts; no faces on river/cloud/fire; narration pacing OK for age 5 (adjust `tts_speed` in `style.json` or add `[pause]` tags in `assets.json` and rerun `--force --only voice` if not). Regenerate any bad clip by deleting its MP4 and rerunning `--only clips`.
5. Write a short review note at `curriculum/assets/lessons/lesson.science.k2.living.01/REVIEW.md`: what was regenerated, what was tuned in prompts/style, final media size. Commit `assets.json`/`style.json` changes; `media/` is gitignored (keep it that way).

## Phase 2 — make packages playable and assignable (engineering, ~2–4 days)

Implement `LESSON_PACKAGES.md` §4, §5, §8 exactly. Order matters.

**2a. Contract first — `goji_cloud/SYNC_API.md`**
Add, additively: plan task `kind: content`, `verify_json: { "subject_type": "lesson", "lesson_id": "<lesson.id>", "min_score": <int> }`; completion rule `completed_how: "lesson_check"` when the device receives `lesson.complete` with `score >= min_score`; activity event `lesson.completed` (`app: "lessons"`, `subject_type: "lesson"`, `subject_id: <lesson.id>`, payload `{quiz_id, score, total, objectives[], attempt}`, `duration_s`), latest-by-`occurred_at` display rule; catalog table `catalog_lessons` (id, title, subject, band, objectives, va_sol, duration_min, version) generated from `lesson.json` files. Then the Supabase migration + RLS in `goji_cloud/supabase/` following existing catalog tables' patterns; edge function `plans-pull` must pass the new `verify_json` fields through verbatim (check it already does — the journal `prompt` fields set the precedent).

**2b. Device — `goji_computer/`**
- Seed path: `backend/seed_data/lessons/<lesson.id>/{index.html,lesson.json,media/…}`. Write a script `scripts/sync_lessons.py` that copies packages from `../curriculum/assets/lessons/` into the seed path (this is the only allowed direction: curriculum → device seed; never the reverse).
- Flask: `backend/routes/lessons.py` — `GET /api/lessons` (list from `lesson.json` manifests), `GET /api/lessons/<id>/<path:file>` (serve package files), `POST /api/lessons/<id>/complete` (persist attempt; emit `lesson.completed` into the sync outbox the same way `quiz.submitted` is emitted — find that code and mirror it). Register the blueprint in `routes/__init__.py`. Tests in `backend/tests/` for all three.
- Kiosk: `frontend/src/components/LessonPlayer.svelte` — hub app id `lessons`, tile in the hub's `lazyApps` (look at how `MyApps.svelte` sandboxes user HTML and reuse that iframe mechanism). The iframe loads `/api/lessons/<id>/index.html` (so relative `media/` paths resolve). Listen for `lesson.ready | lesson.stage | lesson.check | lesson.complete` messages; post `player.config { reduced_motion }` on ready; progress dots for stages; an always-visible Exit control; on `lesson.complete` call the `POST …/complete` route and show the Goji "done" chrome. School Day integration: a `content/lesson` task launches the player with that `lesson_id` and is marked done on a passing `lesson.complete` (mirror how `pdf` tasks navigate with `navigateTo(appId, intent)` and how `quiz` tasks complete). Vitest unit tests + one Playwright e2e (import `test` from `./fixtures`) that plays the exemplar through to completion with the check answered correctly and asserts the task flips to done.
- Follow `NAMING.md`, `docs/BRAND.md`, and `../../hub/standards/` for code standards; run `python -m pytest tests/` and `npm run test:run` green.

**2c. Parent app — `goji_learner_app/`**
- School Day wizard: new task slot `kind: lesson` with a picker fed by `catalog_lessons` (title, band, duration, objectives); writes the `verify_json` shape from 2a.
- Standing: consume `lesson.completed` events in `lib/standing/` so a passing score marks the lesson's objectives covered on the heat map; extend `assets/curriculum/catalog_v1.json` with `obj.science.k2.living.01` / `lesson.science.k2.living.01` and update its count test (`test/standing_catalog*_test.dart`).
- `flutter test` green. Update `PARENT_APP_PRODUCT.md` only with the minimal note that a `lesson` task type exists (don't redesign the wizard).

**2d. Docs**
Update `curriculum/TOOLS.md` §6A row to "shipped", `curriculum/ANIMATIONS.md` §4 to "decided: HTML packages (see LESSON_PACKAGES.md)", and `LESSON_PACKAGES.md` status line from "proposal" to "implemented <date>". Add a line to `TODO.md`.

## Phase 3 — batch the rest of K Science (content, after Phase 1 is approved)

For each remaining K Science standard in `curriculum/skills/science-k.md` (K.2, K.3, K.4, K.5, K.7, K.8, K.9, K.10, K.11; K.1 stays partial/parent-led), produce the full unit of work, modelled line-for-line on the exemplar:

1. Objective row in `subjects/science/OBJECTIVES.md` (`obj.science.k2.<strand>.<nn>`, measurable gate, prereqs, VA code, misconceptions).
2. Lesson plan `subjects/science/lessons/lesson.science.k2.<strand>.<nn>.md` from `assets/templates/lesson-plan.md`: four stages, anchor = current Aesop animal where it fits (K.7 basic needs/life cycles rides the animal-of-the-week slot; K.9/K.10 use the weather/observation journal; K.2/K.3/K.5/K.8 pair an on-device teach+practice+check with a parent-led hands-on step), research hand-off, specific remediation.
3. Quiz blueprint (5 items, each distractor names its misconception) in `subjects/science/quiz-blueprints.md`.
4. Package folder `assets/lessons/<lesson.id>/` with `lesson.json`, `assets.json` (one recurring character max, reuse `ref_wolf` style conventions, badges/cards/scenes/clips/voice), and `index.html` — copy the exemplar's HTML and change only content, keeping the player bridge, media loader, fallbacks, read-aloud buttons, touch sizes and the 4/5 gate. Run `gen_assets.py <id> --dry-run` and sanity-check prompts, then generate (`≈$5.50` each) and review as in Phase 1.
5. Animation brief + INDEX row (`status: shipped-inline`), flip the `skills/science-k.md` row to `partial` or `covered` with an honest note, and fill the matching row in the Google Sheet tracker (Objective ID, Lesson ID, Teach media = "lesson package", Check = "built-in 5-item check").
6. Run PRACTICES §4 audit checklist on the batch and fix findings before committing.

Do K.7 first (closest to the exemplar), then K.9, then the rest. Stop and ask if a standard cannot be made to terminate in a measurable on-device check — mark it blocked rather than inventing a tool.

## Definition of done

- Phase 1: exemplar plays end-to-end with real art, clips and voice; REVIEW.md written.
- Phase 2: a parent can assign `lesson.science.k2.living.01` from the app, a child launches it from the Goji hub, passes the check, the task flips to done, and the parent sees the objective covered; all test suites green; SYNC_API.md updated first.
- Phase 3: nine more K Science packages generated, reviewed, audited, and reflected in `skills/` and the tracker.

Report back with: what shipped, what's blocked and why, API spend, and any deviations from `LESSON_PACKAGES.md` (with reasons).
