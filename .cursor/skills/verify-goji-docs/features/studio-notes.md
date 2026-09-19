# Studio notes

Notes on keeps the design rationale under each phone. Screens only hides those notes so the phones sit on the board alone.

## Sub-features

- `notes-on` shows the note cards under the slots.
- `notes-off` hides the note cards and keeps the phones.
- `notes-pressed` reflects the active choice on the segmented control.

## How to get to it (user POV)

- Choose **Notes on** in the studio bar.
- Choose **Screens only** in the studio bar.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- The studio board is loaded and zoom is closed.

- **Confirm default.** Notes start on. Run `scripts/verify drive studio-notes`. `#noteseg button[data-notes="on"]` has `aria-pressed="true"` and a note containing `Why:` is visible.
- **Hide notes.** Choose **Screens only**. The driver clicks `#noteseg button[data-notes="off"]`. That button has `aria-pressed="true"`, the on button has `aria-pressed="false"`, and `#board` has class `notes-off`.
- **Restore notes.** Choose **Notes on**. The on button returns to `aria-pressed="true"` and a `Why:` note is visible again.
- **Proof.** `before.png` is Notes on. `after.png` is Screens only. `state.txt` records both `aria-pressed` values.

## Gotchas

- The phones stay in the DOM when notes hide. Assert note visibility or `#board.notes-off`, not phone count.
- `#noteseg` is the only notes control. Phone-chrome buttons do not toggle notes.
