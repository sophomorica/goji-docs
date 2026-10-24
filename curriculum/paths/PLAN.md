# Build the skill path framework

Status: engineering plan, 2026-09-23. Implementation is a later change. This file is the plan.

This plan is how a parent assigns one skill and gets a path, without writing curriculum and without a generator that stamps out schools. Shapes are in [MODEL.md](./MODEL.md). The survey behind them is in [SURVEY.md](./SURVEY.md).

Read [CLAUDE.md](../../CLAUDE.md) before editing a product repo. Any wire change is edited in `goji_cloud/SYNC_API.md` first. Use the style of the repo you are editing. Hub `standards/CODE_STANDARDS.md` was not in the checkout that wrote this plan, so this plan does not claim to apply it.

The framework build is the records, the assignment expansion, the child order, the standing rollup, and a pack the current verifier can accept. Lesson copy stays where it is.

## Non-goals

- Lesson sentences, item banks, animations, narration, and decks stay out of this build. Author them in the curriculum files later, then set `content_ref`.
- Nothing in this build reads the Virginia table and emits lessons. `skills/` remains a coverage checklist.
- Goji School means the `pack.goji-school.K.MG.2` fixture in [MODEL.md](./MODEL.md). It does not mean a school generator, a second product, or a pack per grade.
- Framework phases do not wait on the Learner #7 sit-through. Do not invent that sit-through's steps in these phases.
- Do not submit the parent app to a store. Implementation changes are separate from this plan, and each one waits for its own review.
- Do not add a CASE server, an xAPI record store, a SmartScore, an ALEKS-style selector, Kolibri Studio, or an Oppia exploration editor.
- Do not add a `plan_tasks` kind for this project. Map nodes onto kinds `SYNC_API.md` already accepts. Math stays `app_time`. A lesson in [LESSON_PACKAGES.md](../LESSON_PACKAGES.md) is `kind: content` with `subject_type: lesson`, and [TOOLS.md](../TOOLS.md) section 6A still says that player is spec'd, not built. Phase 7 may set `content_ref` only to an id the current school day can open.
- Do not regenerate `catalog_v1.json` for the whole catalog as part of the framework. Touch it only when an `obj.*` row actually changes, which this build does not do.

## Phase 1. Land the fixture records

Add the `K.MG.2` pack JSON from [MODEL.md](./MODEL.md) as data in this repo, under `curriculum/paths/fixtures/`. Add a checker that reads that file.

The checker fails if a skill id is neither an `obj.*` id found in `subjects/` nor a Virginia code found in `skills/`. The checker fails if a node role is outside `teach`, `practice`, and `check`. The checker fails if `move_on` is missing. The checker fails if the fixture's `content_ref` values are not null. The checker does not read lesson prose and does not require any.

**Done means.** The checker exits 0 on the fixture and exits non-zero on a mutated copy that invents a skill id or fills a `content_ref`. No product repo has changed.

## Phase 2. Write the wire for expansion

Edit `goji_cloud/SYNC_API.md` first. Describe assignment, path version, and the rule that a null `content_ref` does not create `plan_tasks` and does not call `start_school_day`.

Then store an assignment and, only for a fully referenced path, the expanded `plan_tasks`. Reuse current task kinds. Math stays `app_time`, as [MATH_MODULE_TASKS_PLAN.md](../../MATH_MODULE_TASKS_PLAN.md) already locked.

**Done means.** A contract test assigns a fully referenced test path and gets one `plan_tasks` row per node, kinds unchanged, same ids on a second confirm. A second test assigns `K.MG.2` and gets an assignment with `plan_id` null and zero new tasks. `start_school_day` is not called in that test.

## Phase 3. Parent assigns a skill

On the child Standing tab, picking a skill shows the path nodes in order. Confirm uses the existing Assign practice control and follows phase 2. Start stays the existing school-day button. A null `plan_id` on this assignment does not disable Start for a plan the child already has. The empty state tells the parent the pieces are not on the device yet. Reuse the wizard's child scope. Do not add a new tab.

**Done means.** A parent-app test selects `K.MG.2`, sees three roles in order, confirms, and asserts no plan was created and an existing plan can still start. A second test uses the fully referenced test path, confirms, and asserts the existing Start path can run. No lesson sentences appear in the test output.

## Phase 4. Child walks a referenced path

On the computer, Today shows expanded tasks in `node_ids` order and opens them with the existing deep link. A check below `gate` leaves that task open and reopens `on_check_fail`. Release and the household PIN still end the session.

The `K.MG.2` fixture has no device rows, because phase 2 never created a plan. Do not add a placeholder lesson to make the day look full.

**Done means.** A device test with the fully referenced path completes the nodes only in order, keeps the check open on a low score, reopens the teach task, and still ends the session on Release. A test that only has the `K.MG.2` assignment shows no new Today rows.

## Phase 5. Roll progress into standing

Compute `not_started`, `in_progress`, and `mastered` from events the device already uploads, using the rules in [MODEL.md](./MODEL.md). The Standing card reads that result. Do not add a wire event type unless `SYNC_API.md` already lacks a field the objective's success criterion needs. If a field is missing, stop and extend the contract. Do not invent a parallel progress table.

**Done means.** A unit test feeds a literal event list and expects each of the three states. A failed check while `in_progress` stays `in_progress` and reopens teach. A mastered skill stays mastered unless the objective's own criterion says the gate is no longer met. A null `obj_id` reads "not yet mapped." The standing UI test shows those words and no point total.

## Phase 6. Verify a pack, and do not install it

Hash the fixture JSON in this repo. A bad digest fails the checker. Do not send the fixture through the image updater in [TODO.md](../../TODO.md). Catalog sync, when it exists, is a `SYNC_API.md` change and is out of this phase.

Until catalog sync exists, the parent app may bundle the same fixture JSON for the demo. The bundled bytes and the hashed bytes are the same file.

**Done means.** A checker accepts the fixture digest and rejects a flipped byte. No image installer runs. No media file is in the pack.

## Phase 7. Add content later

This phase is not part of the framework build. A demo of the framework does not need it.

A curriculum lead authors the objective, the lesson, the practice, and the check for `K.MG.2` in `curriculum/`, under the rules in [PRACTICES.md](../PRACTICES.md). After those ids exist, a follow-up sets `content_ref` on the three nodes only when the id is one the current school day can open, and bumps `path.version`. A `lesson.*` ref waits until the device can open it. `skills/math-k.md` changes from gap only in that follow-up, and only if the coverage is real.

**Done means.** The coverage row cites real ids, the checker from phase 1 now allows those refs, and a child can complete the path on a device build that contains the content. That proof is out of scope until the content exists.

## Order

Phase 1 is this repo. Phase 2 is the cloud contract, then the database. Phases 3 and 5 are the parent app. Phase 4 is the computer. Phase 6 hashes the fixture in this repo. It does not touch the image updater. Phase 7 is curriculum work and comes last.

Phase 3 can demo against phase 1 and phase 2 with no new plan. Do not skip to phase 7 to make the demo look finished.
