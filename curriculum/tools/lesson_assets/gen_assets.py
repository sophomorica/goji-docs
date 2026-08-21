#!/usr/bin/env python3
"""
Goji lesson-asset pipeline — Grok Imagine (images + video) and Grok TTS.

Reads  assets/lessons/<lesson.id>/assets.json  (+ tools/lesson_assets/style.json)
Writes assets/lessons/<lesson.id>/media/{img,clip,voice}/*  and  media/index.js

Usage
  export XAI_API_KEY=...            # or put it in goji_learner/.env  (XAI_API_KEY=...)
  python3 gen_assets.py lesson.science.k2.living.01              # everything (skips existing files)
  python3 gen_assets.py lesson.science.k2.living.01 --only images,voice
  python3 gen_assets.py lesson.science.k2.living.01 --dry-run   # prompts + cost estimate, no calls
  python3 gen_assets.py lesson.science.k2.living.01 --mock      # placeholder files, no calls (for HTML wiring)
  python3 gen_assets.py lesson.science.k2.living.01 --force --only clips   # regenerate clips

Stdlib only — no pip installs. Idempotent: an asset is regenerated only if missing or --force.
AI generation happens here, at authoring time, on the parent/cloud side (CLAUDE.md rule 2).
The Pi only ever receives the finished files.
"""
import argparse, base64, json, os, sys, time, zlib, struct, urllib.request, urllib.error
from pathlib import Path

API = "https://api.x.ai/v1"
HERE = Path(__file__).resolve().parent
CURRICULUM = HERE.parent.parent
LESSONS = CURRICULUM / "assets" / "lessons"

# ---------- pricing (docs.x.ai/developers/pricing, 2026-08) — estimate only ----------
PRICE_IMG = {"1k": 0.04, "2k": 0.08}
PRICE_VID_PER_S = {"480p": 0.08, "720p": 0.15, "1080p": 0.25}
PRICE_TTS_PER_CHAR = 15.0 / 1_000_000


def load_env_key():
    k = os.environ.get("XAI_API_KEY")
    if k:
        return k
    for p in [CURRICULUM.parent / ".env", CURRICULUM / ".env", Path.cwd() / ".env"]:
        if p.exists():
            for line in p.read_text().splitlines():
                if line.strip().startswith("XAI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


class XAI:
    def __init__(self, key):
        self.key = key

    def _req(self, method, path, body=None, raw=False, timeout=180):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(API + path, data=data, method=method,
                                     headers={"Authorization": f"Bearer {self.key}",
                                              "Content-Type": "application/json"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    b = r.read()
                    return b if raw else json.loads(b)
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors="replace")[:400]
                if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                    time.sleep(3 * (attempt + 1)); continue
                raise SystemExit(f"xAI {method} {path} -> HTTP {e.code}: {msg}")
            except urllib.error.URLError as e:
                if attempt < 3:
                    time.sleep(3 * (attempt + 1)); continue
                raise

    @staticmethod
    def _data_uri(png_path):
        return "data:image/png;base64," + base64.b64encode(Path(png_path).read_bytes()).decode()

    def image(self, model, prompt, aspect, resolution, ref_png=None):
        if ref_png:
            body = {"model": model, "prompt": prompt, "response_format": "b64_json",
                    "images": [{"type": "image_url", "url": self._data_uri(ref_png)}],
                    "aspect_ratio": aspect, "resolution": resolution}
            out = self._req("POST", "/images/edits", body)
        else:
            body = {"model": model, "prompt": prompt, "n": 1, "response_format": "b64_json",
                    "aspect_ratio": aspect, "resolution": resolution}
            out = self._req("POST", "/images/generations", body)
        d = out["data"][0] if "data" in out else out
        if d.get("b64_json"):
            return base64.b64decode(d["b64_json"])
        return urllib.request.urlopen(d["url"], timeout=120).read()

    def video(self, model, prompt, png_path, seconds, resolution, aspect):
        body = {"model": model, "prompt": prompt, "duration": seconds, "resolution": resolution,
                "aspect_ratio": aspect, "image": {"url": self._data_uri(png_path)}}
        sub = self._req("POST", "/videos/generations", body)
        rid = sub.get("request_id") or sub.get("id")
        if not rid:
            raise SystemExit(f"video submit: no request_id in {sub}")
        t0 = time.time()
        while True:
            st = self._req("GET", f"/videos/{rid}")
            s = st.get("status")
            if s == "done":
                return urllib.request.urlopen(st["video"]["url"], timeout=300).read()
            if s in ("failed", "expired"):
                raise SystemExit(f"video {rid} {s}: {st}")
            if time.time() - t0 > 900:
                raise SystemExit(f"video {rid} timed out")
            time.sleep(8)

    def tts(self, text, voice, language, speed):
        body = {"text": text, "voice_id": voice, "language": language, "speed": speed,
                "output_format": {"codec": "mp3", "sample_rate": 24000, "bit_rate": 64000}}
        return self._req("POST", "/tts", body, raw=True)


# ---------- mock placeholders (no API) ----------
def mock_png(w=512, h=512, rgb=(232, 214, 184)):
    raw = b"".join(b"\x00" + bytes(rgb) * w for _ in range(h))
    def chunk(t, d): return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lesson")
    ap.add_argument("--only", default="images,clips,voice")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    only = set(a.only.split(","))

    ldir = LESSONS / a.lesson
    man = json.loads((ldir / "assets.json").read_text())
    style = json.loads((ldir / man["style"]).resolve().read_text()) if man.get("style") else json.loads((HERE / "style.json").read_text())
    media = ldir / "media"
    for sub in ("img", "clip", "voice"):
        (media / sub).mkdir(parents=True, exist_ok=True)

    key = None if (a.dry_run or a.mock) else load_env_key()
    if not (a.dry_run or a.mock) and not key:
        sys.exit("XAI_API_KEY not set (env var or goji_learner/.env). Use --dry-run to preview.")
    xai = XAI(key) if key else None

    def prompt_for(item, kind):
        p = style["prefix"] + " " + item["prompt"]
        p += style["card_suffix"] if kind == "card" else style["scene_suffix"]
        return p + style["suffix"]

    cost = 0.0
    produced = {"img": {}, "clip": {}, "voice": {}}
    res = style.get("image_resolution", "1k")

    def need(path):
        return a.force or not path.exists() or path.stat().st_size == 0

    def write(path, data):
        path.write_bytes(data); print(f"  wrote {path.relative_to(ldir)} ({len(data)//1024} KB)")

    # ---- characters (reference sheets) ----
    refs = {}
    if "images" in only:
        for cid, c in man.get("characters", {}).items():
            out = media / "img" / f"ref_{cid}.png"; refs[cid] = out
            p = prompt_for(c, c.get("kind", "card"))
            print(f"[char] {cid}: {p[:110]}…")
            cost += PRICE_IMG[res]
            if a.dry_run: continue
            if need(out):
                write(out, mock_png() if a.mock else xai.image(style["image_model"], p, "1:1", res))

        # ---- images ----
        for it in man.get("images", []):
            kind = it.get("kind", "card"); aspect = "1:1" if kind == "card" else style.get("video_aspect", "16:9")
            out = media / "img" / f"{it['id']}.png"; produced["img"][it["id"]] = f"media/img/{it['id']}.png"
            ref = refs.get(it.get("ref")) if it.get("ref") else None
            p = prompt_for(it, kind)
            if ref: p = "Keep this exact wolf character (same colours, markings, proportions). " + p
            print(f"[img] {it['id']} ({kind}{', ref '+it['ref'] if ref else ''}): {p[:100]}…")
            cost += PRICE_IMG[res]
            if a.dry_run: continue
            if need(out):
                if ref and not ref.exists():
                    sys.exit(f"reference {ref} missing — run images for characters first")
                w = 512 if kind == "card" else 768
                write(out, mock_png(w, int(w * (9/16)) if kind != "card" else w) if a.mock
                      else xai.image(style["image_model"], p, aspect, res, ref_png=ref))

    # ---- clips (image → video) ----
    if "clips" in only:
        vres = style.get("video_resolution", "720p")
        for c in man.get("clips", []):
            src = media / "img" / f"{c['from']}.png"
            out = media / "clip" / f"{c['id']}.mp4"; produced["clip"][c["id"]] = f"media/clip/{c['id']}.mp4"
            p = style["video_prefix"] + " " + c["prompt"]
            print(f"[clip] {c['id']} ← {c['from']} {c['seconds']}s @{vres}: {p[:90]}…")
            cost += PRICE_VID_PER_S[vres] * c["seconds"]
            if a.dry_run: continue
            if need(out):
                if a.mock:
                    print("  (mock: no placeholder video written; HTML falls back to SVG animation)")
                    produced["clip"].pop(c["id"]); continue
                if not src.exists(): sys.exit(f"clip source {src} missing — run --only images first")
                write(out, xai.video(style["video_model"], p, src, c["seconds"], vres, style.get("video_aspect", "16:9")))

    # ---- voice ----
    if "voice" in only:
        for v in man.get("voice", []):
            out = media / "voice" / f"{v['id']}.mp3"; produced["voice"][v["id"]] = f"media/voice/{v['id']}.mp3"
            print(f"[voice] {v['id']}: {v['text'][:80]}")
            cost += PRICE_TTS_PER_CHAR * len(v["text"])
            if a.dry_run: continue
            if need(out):
                if a.mock:
                    produced["voice"].pop(v["id"]); continue
                write(out, xai.tts(v["text"], style.get("tts_voice", "luna"), style.get("tts_language", "en"), style.get("tts_speed", 1.0)))

    # ---- index.js (what the HTML actually loads; only lists files that exist) ----
    if not a.dry_run:
        for kind in produced:
            produced[kind] = {k: v for k, v in produced[kind].items() if (ldir / v).exists()}
        produced["style"] = style["name"]; produced["generated"] = time.strftime("%Y-%m-%d")
        (media / "index.js").write_text("window.GOJI_MEDIA=" + json.dumps(produced) + ";\n")
        print(f"\nindex.js: {len(produced['img'])} images, {len(produced['clip'])} clips, {len(produced['voice'])} voice lines")
    print(f"\nEstimated API cost for a full run: ${cost:.2f}")


if __name__ == "__main__":
    main()
