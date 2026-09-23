# Studio walk

Show a family walks one phone at a time: the family glance, Eli's day, where he stands, then the living lesson on the Goji.

## Sub-features

- `walk-open` opens the walk on the family board.
- `walk-day` moves to Eli's today checklist.
- `walk-standing` shows reading, writing, and math.
- `walk-lesson` plays Living or not living inside the walk.
- `walk-close` returns every phone to the board and restores Today.

## How to get to it (user POV)

- Choose **Show a family** in the studio bar.
- Choose **Next** to move through the day, standing, and the lesson.
- Choose **close** or **Done** to leave. **Back** steps backward.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- The walk is closed.

- **Open the walk.** Choose **Show a family**. Run `scripts/verify drive studio-walk`. The driver clicks `#walkgo`. `#walk` has class `on`, the title is `Six children. One look.`, and the phone shows `Tuesday` and `Halfway`.
- **See the day.** Choose **Next**. The driver clicks `#wnext`. The title is `One red button.` and the phone shows `Today's plan · 3 of 5 done` and `Release day`.
- **See standing.** Choose **Next** again. The phone shows `Where Eli stands` and `Needs help`.
- **Play the lesson.** Choose **Next** again. The title is `Living or not living.` and the frame title is `Living or not living? — Goji` with `Which one is alive?` visible.
- **Close.** Choose **close**. The driver clicks `#wclose`. `#walk` no longer has class `on`, Family board shows `Tuesday`, and Child detail's Today tab is selected.
- **Proof.** `before.png` is the board. `after.png` is the lesson step of the walk.

## Gotchas

- The walk moves a `.phone` node, the same way zoom does. Close it before counting phones on the board.
- The lesson frame loads only on the last step. Do not assert the lesson on the glance step.
- Closing from an earlier step still returns the phone and selects Today.
