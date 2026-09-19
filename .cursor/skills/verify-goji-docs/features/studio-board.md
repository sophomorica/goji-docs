# Studio board

The layout studio shows twelve parent-app screens on one board so a reviewer can compare pairing, family, standing, tasks, content, settings, and the design system without opening the Flutter app.

## Sub-features

- `board-open` loads the studio at the repo root HTML file.
- `board-slots` shows every named screen slot on one scroll.
- `board-hint` keeps the zoom hint visible in the studio bar.

## How to get to it (user POV)

- Open `http://127.0.0.1:4177/PARENT_APP_LAYOUT_STUDIO.html` in a browser.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- No zoom overlay is open.

- **Open studio.** Load the studio URL. Run `scripts/verify drive studio-board`. The document title is `goji parent app — layout studio`.
- **See the board.** Read the slot titles. `state.txt` lists `Pair gate (unpaired)`, `Family board`, `Child detail`, `Skill heat map`, `Evidence sheet`, `Plan the day`, `Add task sheet`, `Household tasks board`, `Child task list`, `Messages`, `Content`, `Settings`, and `Design system`.
- **See the hint.** The studio bar contains `click a screen title to zoom`.
- **Proof.** `after.png` shows the studio bar lockup and at least the first two phone slots.

## Gotchas

- Serving from a subdirectory 404s the lesson path later. Launch from the repo root.
- A zoomed slot moves its phone node into `#zoom`. Close zoom before you count board slots.
- The document title uses an em dash. Assert the exact title string from the HTML.
