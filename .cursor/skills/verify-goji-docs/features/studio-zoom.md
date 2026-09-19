# Studio zoom

Zoom lifts one phone into a lightbox with its title and note beside it, then returns that phone to its slot when closed.

## Sub-features

- `zoom-button` opens zoom from the slot **zoom** button.
- `zoom-title` opens the same lightbox from the slot title.
- `zoom-close` returns the phone and hides the lightbox.

## How to get to it (user POV)

- Choose **zoom** on a slot.
- Choose the slot title. The studio bar hint says to do this.
- Choose **close**, click the dimmed backdrop, or press Escape.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- Zoom is closed.

- **Open from the button.** Choose **zoom** on Family board. Run `scripts/verify drive studio-zoom`. The driver clicks `.slot[data-title="Family board"] .slot-zoom`. `#zoom` has class `on` and `#zside` contains `Family board`.
- **See the phone.** The lightbox holder contains `Tuesday` and `Goji synced 2 min ago`.
- **Close.** Choose **close**. The driver clicks `#zclose`. `#zoom` no longer has class `on` and Family board is back on the board.
- **Title entry.** After close, choose the Family board title. `.slot[data-title="Family board"] .slot-title` opens the same lightbox. `#zside` still contains `Family board`.
- **Proof.** `before.png` is the board. `after.png` is the open lightbox with the Family board phone and side title.

## Gotchas

- Opening zoom moves the `.phone` node out of the slot. Counting `.slot .phone` while zoomed undercounts the board.
- Close before you drive another studio feature that reads slot contents.
- Escape and backdrop click are extra close paths. The scripted close is `#zclose`.
