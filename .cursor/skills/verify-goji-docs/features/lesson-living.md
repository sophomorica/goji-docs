# Living lesson

Living or not living walks a K–2 science lesson from a wolf-or-river hook into the four signs of life. This map covers the hook and the arrival on teach. Practice and check are later work.

## Sub-features

- `hook-guess` selects Wolf or River and enables the next button.
- `hook-next` moves the lesson into the teach stage.
- `teach-heading` shows The four signs of life after the hook.

## How to get to it (user POV)

- Open `http://127.0.0.1:4177/curriculum/assets/lessons/lesson.science.k2.living.01/index.html`.
- Tap **Wolf** or **River**.
- Choose **Let's find out →**.

## Driving it with verify-goji-docs

Preconditions:

- Doctor reports both page titles.
- The lesson starts on stage `s0`.

- **Open the lesson.** Load the lesson URL. Run `scripts/verify drive lesson-living`. The document title is `Living or not living? — Goji` and `#s0` is the active stage.
- **Guess wolf.** Choose **Wolf**. The driver clicks `[data-guess="wolf"]`. That pick has class `sel` and `#hookNext` is enabled.
- **Enter teach.** Choose **Let's find out →**. The driver clicks `#hookNext`. `#s1` is the active stage and the heading contains `The four signs of life`.
- **Proof.** `before.png` is the hook with Wolf selected. `after.png` is the teach stage. `state.txt` records the active stage id and the teach heading.

## Gotchas

- `#hookNext` stays disabled until a pick is selected. Click the card, not the next button first.
- Teach autoplays for about 22 seconds unless Chrome reports reduced motion. Arrival on `#s1` is enough for this feature. Do not wait for **Your turn →** unless you are extending the map.
- Generated `media/` files are optional. Missing clips fall back to inline SVG. That is not a failure.
- `lesson.json` is the catalog manifest. It does not appear on the kid-facing page. Do not treat a JSON read as proof.
