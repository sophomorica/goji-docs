# goji-docs verification map

This directory is the maintained source for verifying the user-facing HTML in `sophomorica/goji-docs`. Read this index before driving a page, then use the matching feature file as the recipe.

## Baseline preconditions

- Serve the repo root at `http://127.0.0.1:4177` with `scripts/verify launch`.
- Run `scripts/verify doctor` and require both page titles listed in the skill.
- Never drive an instance that this run did not start.
- Keep Chrome on a throwaway user-data dir. The driver does that for you.

## Driving conventions

- Start every recipe from the baseline state unless its preconditions say otherwise.
- Prefer `data-*` attributes, element ids, and accessible names over CSS position.
- Treat every command as literal. Keep quoted names and flags unchanged.
- Run browser actions through `scripts/verify drive <feature-id>`.
- Do not remove proof artifacts during cleanup.

## Proof and skip reporting

- Capture the user action and the resulting state, not only the final screen.
- Proof includes `before.png`, `after.png`, and `state.txt` with the asserted strings.
- Record the feature id and entry point used with every artifact.
- Report an unreachable path with the attempted command and the unmet precondition.
- Do not report a skipped entry point as verified through a different path.

## Feature entry contract

Each feature file starts with an H1 title and one paragraph describing the user-visible behavior. It then uses exactly four H2 sections in this order.

1. `Sub-features` lists short IDs with one line for each behavior.
2. `How to get to it (user POV)` lists every user entry point.
3. `Driving it with verify-goji-docs` starts with `Preconditions:` and uses labeled bullets that pair each user action with an exact command and observable result.
4. `Gotchas` lists traps that can waste or invalidate a verification run.

Keep implementation details out of the map. Name only user paths, stable handles, required state, commands, and observable proof.

## Features

- [Studio board](./studio-board.md) covers the parent-app layout studio grid and the twelve screen slots.
- [Studio notes](./studio-notes.md) covers the Notes on and Screens only toggle.
- [Studio zoom](./studio-zoom.md) covers zoom from the slot title or the zoom button, then close.
- [Child detail tabs](./studio-child-tabs.md) covers Today, Standing, and Activity inside the Child detail phone.
- [Living lesson](./lesson-living.md) covers the hook guess and the move into the teach stage.
