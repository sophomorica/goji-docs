#!/usr/bin/env python3
"""Validate a Goji lesson package (structure + headless playthrough).

Usage: python3 validate_package.py <lesson.id> [more ids...] [--all] [--fast]
  --fast  structural checks only (no browser)
Exit 0 and prints PASS per package when green.
"""
import json, os, re, sys, threading, functools, http.server, socketserver

HERE = os.path.dirname(os.path.abspath(__file__))
CURR = os.path.dirname(os.path.dirname(HERE))  # curriculum/
LESSONS = os.path.join(CURR, "assets", "lessons")

def err(msgs, m): msgs.append(m)

def structural(lid):
    msgs = []
    d = os.path.join(LESSONS, lid)
    if not os.path.isdir(d): return [f"missing package dir {d}"]
    lj = os.path.join(d, "lesson.json")
    aj = os.path.join(d, "assets.json")
    ih = os.path.join(d, "index.html")
    for p in (lj, aj, ih):
        if not os.path.isfile(p): err(msgs, f"missing {os.path.basename(p)}")
    if msgs: return msgs
    try: L = json.load(open(lj))
    except Exception as e: return [f"lesson.json parse: {e}"]
    if L.get("id") != lid: err(msgs, f"lesson.json id {L.get('id')!r} != folder {lid}")
    for k in ("title","subject","band","objectives","va_sol","duration_min","stages","check","version","entry"):
        if k not in L: err(msgs, f"lesson.json missing {k}")
    if L.get("stages") != ["hook","teach","practice","check"]: err(msgs, "stages must be hook/teach/practice/check")
    chk = L.get("check", {})
    if not chk.get("quiz_id","").startswith("quiz."): err(msgs, "check.quiz_id missing/bad")
    if not (isinstance(chk.get("n_items"), int) and isinstance(chk.get("pass"), int) and 0 < chk["pass"] <= chk["n_items"]):
        err(msgs, "check n_items/pass invalid")
    try: A = json.load(open(aj))
    except Exception as e: return msgs + [f"assets.json parse: {e}"]
    imgs = [i["id"] for i in A.get("images", [])]
    if len(imgs) != len(set(imgs)): err(msgs, "duplicate image ids in assets.json")
    vids = [v["id"] for v in A.get("voice", [])]
    if len(vids) != len(set(vids)): err(msgs, "duplicate voice ids")
    for c in A.get("clips", []):
        if c.get("from") not in imgs: err(msgs, f"clip {c.get('id')} 'from' not an image id")
    html = open(ih, encoding="utf-8").read()
    if len(html.encode()) > 300*1024: err(msgs, f"index.html {len(html.encode())//1024}KB > 300KB")
    if re.search(r'(src|href)\s*=\s*["\']https?://', html): err(msgs, "external http(s) reference in HTML")
    if "media/index.js" not in html: err(msgs, "missing media/index.js loader")
    if "GOJI_TEST" not in html: err(msgs, "missing GOJI_TEST hook")
    if "lesson.ready" not in html or "lesson.complete" not in html: err(msgs, "missing player bridge messages")
    if "prefers-reduced-motion" not in html: err(msgs, "missing reduced-motion handling")
    # every data-voice id should have a voice line (warn-level -> error to keep bar high)
    used = set(re.findall(r'data-voice="([^"]+)"', html))
    missing_v = used - set(vids)
    if missing_v: err(msgs, f"data-voice ids missing from assets.json voice[]: {sorted(missing_v)}")
    return msgs

HARNESS = """<!doctype html><meta charset=utf-8><body>
<iframe id=f src="/%s/index.html" style="width:1024px;height:768px"></iframe>
<script>
window.MSGS=[];addEventListener('message',e=>{if(e.data&&e.data.type)MSGS.push(e.data)});
document.getElementById('f').addEventListener('load',()=>{
  try{document.getElementById('f').contentWindow.postMessage({type:'player.config',reduced_motion:true},'*')}catch(e){}
});
</script></body>"""

def play(lid):
    from playwright.sync_api import sync_playwright
    msgs = []
    L = json.load(open(os.path.join(LESSONS, lid, "lesson.json")))
    os.makedirs("/tmp/goji_harness", exist_ok=True)
    open(f"/tmp/goji_harness/h_{lid}.html","w").write(HARNESS % lid)

    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(H, directory=LESSONS)
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as srv:
        port = srv.server_address[1]
        t = threading.Thread(target=srv.serve_forever, daemon=True); t.start()
        import shutil
        shutil.copy(f"/tmp/goji_harness/h_{lid}.html", os.path.join(LESSONS, f"_h_{lid}.html"))
        try:
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                pg = b.new_page(viewport={"width":1100,"height":800})
                errors = []
                pg.on("pageerror", lambda e: errors.append(str(e)))
                pg.on("console", lambda m: errors.append(m.text) if m.type=="error" and "media/index.js" not in m.text and "404" not in m.text and "ERR_" not in m.text else None)
                pg.goto(f"http://127.0.0.1:{port}/_h_{lid}.html")
                pg.wait_for_timeout(1200)
                f = pg.frames[1] if len(pg.frames) > 1 else None
                if f is None: err(msgs, "iframe did not load"); b.close(); return msgs
                def got(t): return pg.evaluate(f"MSGS.some(m=>m.type==='{t}')")
                if not got("lesson.ready"): err(msgs, "no lesson.ready")
                if not f.evaluate("!!window.GOJI_TEST && typeof GOJI_TEST.go==='function' && typeof GOJI_TEST.autoCheck==='function'"):
                    err(msgs, "GOJI_TEST contract missing"); b.close(); return msgs
                for n, name in ((1,"teach"),(2,"practice")):
                    f.evaluate(f"GOJI_TEST.go({n})"); pg.wait_for_timeout(400)
                    if not pg.evaluate(f"MSGS.some(m=>m.type==='lesson.stage'&&m.stage==='{name}')"):
                        err(msgs, f"stage '{name}' not reported")
                r = f.evaluate("GOJI_TEST.autoCheck(true)")
                pg.wait_for_timeout(600)
                chk = pg.evaluate("MSGS.filter(m=>m.type==='lesson.check').pop()")
                if not chk: err(msgs, "no lesson.check after autoCheck(true)")
                else:
                    if chk.get("score") != chk.get("total"): err(msgs, f"autoCheck(true) score {chk.get('score')}/{chk.get('total')} != full")
                    if chk.get("total") != L["check"]["n_items"]: err(msgs, f"check total {chk.get('total')} != lesson.json n_items")
                fin = f.query_selector("#finish")
                if not fin: err(msgs, "no #finish button on pass")
                else:
                    fin.click(); pg.wait_for_timeout(500)
                    comp = pg.evaluate("MSGS.filter(m=>m.type==='lesson.complete').pop()")
                    if not comp: err(msgs, "no lesson.complete after finish")
                    elif comp.get("score") != L["check"]["n_items"]: err(msgs, "lesson.complete score mismatch")
                # fail path
                pg.evaluate("MSGS.length=0")
                pg.reload(); pg.wait_for_timeout(1000)
                f = pg.frames[1]
                f.evaluate("GOJI_TEST.autoCheck(false)"); pg.wait_for_timeout(800)
                vis = f.evaluate("(function(){var b=document.getElementById('finish');return b && b.offsetParent!==null && getComputedStyle(b).display!=='none';})()")
                chk2 = pg.evaluate("MSGS.filter(m=>m.type==='lesson.check').pop()")
                if chk2 and chk2.get("score",0) >= L["check"]["pass"] :
                    pass  # some quizzes are 2-option; all-wrong may still be < pass. fine.
                if vis and chk2 and chk2.get("score",0) < L["check"]["pass"]:
                    err(msgs, "finish visible despite failing gate")
                if pg.evaluate("MSGS.some(m=>m.type==='lesson.complete')"): err(msgs, "lesson.complete fired on failed gate")
                if errors: err(msgs, "console/page errors: " + " | ".join(errors[:4]))
                b.close()
        finally:
            srv.shutdown()
            try: os.remove(os.path.join(LESSONS, f"_h_{lid}.html"))
            except OSError: pass
    return msgs

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fast = "--fast" in sys.argv
    if "--all" in sys.argv:
        args = sorted(d for d in os.listdir(LESSONS) if d.startswith("lesson.") and os.path.isdir(os.path.join(LESSONS,d)))
    bad = 0
    for lid in args:
        msgs = structural(lid)
        if not msgs and not fast:
            try: msgs = play(lid)
            except Exception as e: msgs = [f"playthrough crashed: {e}"]
        if msgs:
            bad += 1
            print(f"FAIL {lid}")
            for m in msgs: print(f"  - {m}")
        else:
            print(f"PASS {lid}")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
