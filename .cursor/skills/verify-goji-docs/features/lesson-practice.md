# Living practice

After the four signs, the lesson asks the child to sort a tree, a rock, and a child with the signs still showing. A still tree dropped into Not living gets the stillness hint.

## Sub-features

- `teach-ready` enables Your turn when the river test finishes.
- `guided-tree` opens practice on Tree with the four signs visible.
- `still-hint` explains a wrong Not living drop.

## How to get to it (user POV)

- Open the living lesson.
- Tap **Wolf**, then **Let's find out →**.
- Wait until **Your turn →** enables, then choose it.
- On Tree, choose **Not living**.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- The lesson starts on stage `s0`.
- Chrome is in reduced motion, so the teach stage finishes in a few seconds.

- **Reach teach.** Choose **Wolf**, then **Let's find out →**. Run `scripts/verify drive lesson-practice`. The driver clicks `[data-guess="wolf"]` and `#hookNext`.
- **Enter practice.** Wait until `#teachNext` is enabled, then choose **Your turn →**. `#s2` is active, the lead contains `four signs`, the card name is `Tree`, `#signstrip` is visible, and the picture is an SVG.
- **Miss on purpose.** Choose **Not living**. The driver clicks `[data-tap="dead"]`. The feedback contains `still` and `grow`.
- **Proof.** `before.png` is the hook with Wolf selected. `after.png` is the guided sort after the miss.

## Gotchas

- `#teachNext` stays disabled until the river stamp. Do not click it early.
- The first card is Tree, and Tree is living. **Not living** is the miss this map checks.
- `?stage=practice` opens the sort directly for author preview. This drive does not use it.
