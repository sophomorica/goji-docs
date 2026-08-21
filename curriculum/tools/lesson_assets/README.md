# lesson_assets — Grok Imagine + Grok TTS pipeline for lesson packages

Turns a lesson's `assets.json` into illustrations, short teach clips, and narration, baked into the package's `media/` folder. The HTML lesson loads `media/index.js` and uses whatever exists; anything missing falls back to the built-in SVG/emoji/browser-speech — so a package always runs, generated or not.

```
assets/lessons/<lesson.id>/
  index.html      ← lesson (reads media/index.js)
  lesson.json     ← package manifest (LESSON_PACKAGES.md §3)
  assets.json     ← WHAT to generate (prompts, clips, voice lines)   ← curriculum authors edit this
  media/          ← generated; gitignored; shipped via seed pipeline
    index.js      ← { img:{id:path}, clip:{}, voice:{} } — only lists files that exist
    img/*.png  clip/*.mp4  voice/*.mp3
tools/lesson_assets/
  style.json      ← ONE shared art/voice preset for all K–4 (storybook watercolor, voice "luna")
  gen_assets.py   ← the generator (stdlib only)
```

## Run

```bash
# key: env var, or a line  XAI_API_KEY=...  in goji_learner/.env (gitignored — rule 4)
cd curriculum/tools/lesson_assets
python3 gen_assets.py lesson.science.k2.living.01 --dry-run      # see prompts + cost, no calls
python3 gen_assets.py lesson.science.k2.living.01                # generate everything missing
python3 gen_assets.py lesson.science.k2.living.01 --only voice   # just narration
python3 gen_assets.py lesson.science.k2.living.01 --force --only images   # redo the art
```

Then open `assets/lessons/<id>/index.html`. Idempotent: rerunning only fills gaps; delete a file (or `--force`) to regenerate it.

## How consistency works

1. `characters.*` are generated first as reference sheets (`media/img/ref_<name>.png`).
2. Any image with `"ref": "<name>"` goes through the **edit** endpoint with that sheet as a reference image, prompt prefixed "Keep this exact character…" — so the wolf on the hook card, the teach clips and the sort card are the same wolf.
3. `clips[]` are **image-to-video** from the matching still (`from`), 6 s, loopable, camera locked — the still is the poster, the clip plays muted under the narration.
4. `voice[]` lines are TTS with the shared voice; speech tags (`[pause]`, `<emphasis>`, `<soft>`) are allowed in `text`.
5. `style.json` carries the prompt prefix/suffix and the "must not" list (no faces on objects, no text, no borders). Change the style once → regenerate every lesson with `--force`.

## Cost (docs.x.ai/developers/pricing, Aug 2026)

Images $0.04 (1k) / $0.08 (2k) · video $0.08/s (480p) – $0.25/s (1080p) · TTS $15 per 1M chars.  
The exemplar is ≈ **$5.50** at 720p (23 images, 5×6 s clips, ~30 lines); ≈ $3.40 at 480p. 125 K–4 lessons ≈ $700 at 720p.

## Review loop (what a human checks before a package ships)

- Character drift (is it still the same wolf?) → regenerate that image with `--force` after tightening the prompt.
- Anything with a face that shouldn't have one (river, cloud, fire) → misconception risk, regenerate.
- Clip motion calm? No camera moves/cuts? → tweak the clip prompt.
- Narration pacing for a 5-year-old → adjust `tts_speed` in style.json or add `[pause]`.
- `respect_moderation` flags are not surfaced yet — if the API returns a moderated/blank image, rerun.

## Rules this respects

- Generation is parent/cloud-side at authoring time; the Pi gets files only (CLAUDE.md rule 2).
- Binaries stay out of git (`assets/lessons/.gitignore` ignores `*/media/`); they ship with the image / catalog sync (ANIMATIONS.md §5). Keep `assets.json` in git — it's the source.
- No secrets in the repo: key comes from env or a gitignored `.env`.
