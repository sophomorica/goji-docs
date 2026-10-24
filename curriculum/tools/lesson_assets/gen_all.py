#!/usr/bin/env python3
"""Batch media generation queue for all lesson packages.

Run this on a machine with network access to api.x.ai and XAI_API_KEY in
goji_learner/.env (gen_assets.py finds it). Idempotent: only generates what's
missing; safe to re-run after interruptions.

Usage:
  python3 gen_all.py --dry-run              # list packages + estimated cost, no calls
  python3 gen_all.py                        # IMAGES ONLY for every package (default tier)
  python3 gen_all.py --tier voice           # images + narration (TTS is ~5 cents/lesson)
  python3 gen_all.py --tier full            # images + voice + video clips (the $ tier)
  python3 gen_all.py --match history        # only lesson ids containing "history"
  python3 gen_all.py --limit 10             # first N pending packages

Tiers map to gen_assets.py --only flags:
  images -> images | voice -> images,voice | full -> (everything)
"""
import argparse, os, subprocess, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.normpath(os.path.join(HERE, "..", "..", "assets", "lessons"))

def packages(match):
    out = []
    for d in sorted(os.listdir(LESSONS)):
        p = os.path.join(LESSONS, d)
        if d.startswith("lesson.") and os.path.isdir(p) and os.path.isfile(os.path.join(p, "assets.json")):
            if match and match not in d: continue
            out.append(d)
    return out

def estimate(lid):
    try: A = json.load(open(os.path.join(LESSONS, lid, "assets.json")))
    except Exception: return (0,0,0)
    n_img = len(A.get("images", [])) + len(A.get("characters", {}))
    secs = sum(c.get("seconds", 6) for c in A.get("clips", []))
    chars = sum(len(v.get("text","")) for v in A.get("voice", []))
    return n_img, secs, chars

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["images","voice","full"], default="images")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--match", default="")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    pkgs = packages(a.match)
    if a.limit: pkgs = pkgs[:a.limit]
    only = {"images":"images", "voice":"images,voice", "full":None}[a.tier]
    tot_i = tot_s = tot_c = 0
    for lid in pkgs:
        i, s, c = estimate(lid); tot_i += i; tot_s += s; tot_c += c
    cost_img = tot_i * 0.04
    cost_clip = tot_s * 0.08   # 480p; x ~2 for 720p per pricing
    cost_tts = tot_c / 1_000_000 * 15
    print(f"{len(pkgs)} packages · ~{tot_i} images (${cost_img:.0f}) · {tot_s}s clips (${cost_clip:.0f}-${tot_s*0.17:.0f}) · TTS ${cost_tts:.2f}")
    tier_cost = {"images": cost_img, "voice": cost_img + cost_tts, "full": cost_img + cost_tts + cost_clip}[a.tier]
    print(f"tier '{a.tier}' estimated spend if nothing exists yet: ~${tier_cost:.0f}\n")
    if a.dry_run:
        for lid in pkgs:
            i, s, c = estimate(lid)
            print(f"  {lid}: {i} imgs, {s}s clip, {c} tts chars")
        return
    fails = []
    for n, lid in enumerate(pkgs, 1):
        print(f"[{n}/{len(pkgs)}] {lid}")
        cmd = [sys.executable, os.path.join(HERE, "gen_assets.py"), lid]
        if only: cmd += ["--only", only]
        r = subprocess.run(cmd)
        if r.returncode != 0:
            fails.append(lid)
            print(f"  !! failed (continuing)")
    print(f"\ndone. {len(pkgs)-len(fails)} ok, {len(fails)} failed" + (": " + ", ".join(fails) if fails else ""))

if __name__ == "__main__":
    main()
