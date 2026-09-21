---
name: verify-goji-docs
description: >-
  Drive the goji-docs HTML surfaces the way a user does: the parent-app
  layout studio and the Living or not living lesson package. Use when
  proving a docs or curriculum HTML change, running /verify-goji-docs,
  or checking layout-studio or lesson-package behavior. Do not use this
  skill to drive the Goji kiosk, the Flutter parent app, or Supabase.
---

# Verify goji-docs

This repo is product SoT markdown plus two in-repo HTML pages. Those pages are the only user-facing surfaces you can launch from this checkout. Sibling remotes (`goji_computer/`, `goji_learner_app/`, `goji_cloud/`) are out of scope.

Read `features/README.md` before you drive. Use the matching feature file as the recipe. Drive one mapped entry point per proof. Do not treat a convenient nearby click as coverage for a different entry.

Repo root is the directory that contains `PARENT_APP_LAYOUT_STUDIO.html` and `curriculum/`.

## Launch

Start a disposable HTTP server that you own. Do not attach to a server you did not start.

```bash
.cursor/skills/verify-goji-docs/scripts/verify launch
```

Ready when the script prints `ready` and `http://127.0.0.1:4177` answers. Override the bind with `VERIFY_PORT` and the state directory with `VERIFY_ROOT` (default `/tmp/goji-docs-verify`).

A second launch on the same `VERIFY_ROOT` exits 1 while the first process is still alive. Use a different `VERIFY_ROOT` and `VERIFY_PORT` for a side-by-side run.

Teardown is Cleanup, not a second launch.

## Doctor

Run this first whenever anything looks off, and again after a failed drive.

```bash
.cursor/skills/verify-goji-docs/scripts/verify doctor
```

Doctor is read-only. It checks that the recorded PID is alive, that PID owns `VERIFY_PORT`, and that both pages return 200 with their titles:

- `/PARENT_APP_LAYOUT_STUDIO.html` contains `goji parent app — layout studio`
- `/curriculum/assets/lessons/lesson.science.k2.living.01/index.html` contains `Living or not living? — Goji`

Exit 0 only when every check passes. Do not drive a failing instance.

## Drive

Chrome CDP through `scripts/drive.mjs`. Prefer the IDs, `data-*` attributes, and accessible names in the feature files. Do not click by coordinates.

```bash
.cursor/skills/verify-goji-docs/scripts/verify drive studio-zoom
```

Replace `studio-zoom` with a feature id from `features/README.md`. The driver starts its own headless Chrome, uses a throwaway user-data dir, and kills that Chrome when the drive ends. It never opens the operator's Chrome profile.

Stable handles:

- Studio notes. `#noteseg button[data-notes="on"]` and `[data-notes="off"]`
- Studio zoom. `.slot[data-title="Family board"] .slot-zoom` and `#zclose`
- Child tabs. `.slot[data-title="Child detail"] button[data-pane="p-standing"]`
- Lesson hook. `[data-guess="wolf"]` then `#hookNext`

## Evidence

Write proof under `$VERIFY_EVIDENCE_DIR/<run-id>/` (default `/tmp/goji-docs-verify/evidence/<run-id>/`). Cleanup must not delete that tree.

Each drive writes:

- `action.json` with the feature id, URL, commands, and observed text
- `before.png` and `after.png` for the user action and the resulting state
- `state.txt` with the title plus the asserted strings

Proof rules:

- Exercise the real page in Chrome. Do not curl a title and call the feature done.
- Capture the action and the resulting state, not only the last frame.
- Assert visible text or `aria-*` values the user can see. Do not assert class names alone.
- These pages have no network writes. Side effects are DOM state only (pressed toggles, zoom overlay, active lesson stage).
- Record the feature id and the entry point on every artifact.

## Cleanup

```bash
.cursor/skills/verify-goji-docs/scripts/verify cleanup
```

Sends TERM, then KILL, to the HTTP PID recorded at launch. Removes `$VERIFY_ROOT/run`. Leaves `$VERIFY_EVIDENCE_DIR` in place. Never kill by process name.

If a drive started Chrome and the driver aborted, `drive.mjs` still kills that Chrome. `cleanup` does not search for leftover Chrome.

After cleanup, confirm the evidence directory still exists and still holds `after.png`.

## Helpers

All helpers live in `.cursor/skills/verify-goji-docs/scripts/` and are executable.

| Command | What it does |
|---|---|
| `scripts/verify launch` | Bind `127.0.0.1:$VERIFY_PORT` to the repo root and write the PID file |
| `scripts/verify doctor` | Read-only health check |
| `scripts/verify drive <feature-id>` | Doctor, then run `drive.mjs` for that feature |
| `scripts/verify cleanup` | Stop the server this run started |
| `scripts/self-test` | Launch, doctor, drive `studio-zoom`, cleanup, then assert evidence survived |

Environment:

- `VERIFY_PORT` default `4177`
- `VERIFY_ROOT` default `/tmp/goji-docs-verify`
- `VERIFY_EVIDENCE_DIR` default `$VERIFY_ROOT/evidence`
- `VERIFY_REPO_ROOT` default the repo root discovered from the script path
- `CHROME_BIN` default `/opt/google/chrome/chrome` when that binary exists. Do not use `/usr/local/bin/google-chrome` on this image. That wrapper pins port 9222 and the shared user profile.

## Out of scope

Do not clone sibling product remotes from this skill. Do not start the Flask kiosk, the Flutter app, or a local Supabase stack. Those apps have their own checkouts.
