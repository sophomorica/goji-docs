#!/usr/bin/env python3
"""
End-to-end School Day check against the LOCAL stack, over the real wire.

Unlike `goji_computer/backend/tests/integration/test_school_day_e2e_mock.py`
(which calls an in-process MockFamilyCloud), every step here is a real HTTP
request: parent -> Supabase PostgREST/RPC, device -> Supabase edge functions,
child -> Flask kiosk API. That is what makes it able to catch contract drift,
RLS/grant problems and edge-function bugs that the hermetic mock cannot see.

Prerequisite: scripts/local-stack-up.sh

    scripts/local_school_day_smoke.py
    scripts/local_school_day_smoke.py --keep    # leave the day open for the UI
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

SB_URL = os.environ.get("SB_URL", "http://127.0.0.1:54321")
SB_ANON = os.environ["SB_ANON"]
DEVICE_URL = os.environ.get("GOJI_BACKEND_URL", "http://127.0.0.1:5000")
EMAIL = os.environ.get("GOJI_TEST_EMAIL", "parent@goji.test")
PASSWORD = os.environ.get("GOJI_TEST_PASSWORD", "gojitest123")
COMPUTER_DIR = os.environ["GOJI_COMPUTER_DIR"]

failures: list[str] = []
step_no = 0


def request(method, url, body=None, headers=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            return resp.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode()
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, raw


def parent(method, path, body=None, jwt=None, prefer=None):
    headers = {"apikey": SB_ANON}
    if jwt:
        headers["Authorization"] = f"Bearer {jwt}"
    if prefer:
        headers["Prefer"] = prefer
    return request(method, f"{SB_URL}{path}", body, headers)


def step(msg):
    global step_no
    step_no += 1
    print(f"\n[{step_no}] {msg}")


def check(label, ok, detail=""):
    print(f"    {'PASS' if ok else 'FAIL'}  {label}{f'  ({detail})' if detail else ''}")
    if not ok:
        failures.append(label)
    return ok


def sync_once(label=""):
    """Run one real sync cycle as the device would."""
    env = dict(os.environ)
    env_file = os.path.join(COMPUTER_DIR, "backend", ".env.local-cloud")
    with open(env_file) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k] = v
    out = subprocess.run(
        [os.path.join(COMPUTER_DIR, "backend", ".venv", "bin", "python"),
         "-m", "sync.agent", "--once"],
        cwd=os.path.join(COMPUTER_DIR, "backend"),
        env=env, capture_output=True, text=True, timeout=180,
    )
    summary = {}
    for line in out.stderr.splitlines() + out.stdout.splitlines():
        if "Sync cycle done:" in line:
            try:
                summary = json.loads(line.split("Sync cycle done:", 1)[1].strip()
                                     .replace("'", '"').replace("True", "true")
                                     .replace("False", "false").replace("None", "null"))
            except json.JSONDecodeError:
                pass
    print(f"    sync{f' ({label})' if label else ''}: "
          f"pulled={summary.get('pulled')} pushed={summary.get('pushed')} "
          f"status_pushed={summary.get('status_pushed')} "
          f"school_acked={summary.get('school_acked')} "
          f"messages_pulled={summary.get('messages_pulled')}")
    return summary


def device_get(path):
    return request("GET", f"{DEVICE_URL}{path}")


def device_post(path, body=None):
    return request("POST", f"{DEVICE_URL}{path}", body if body is not None else {})


def make_plan(jwt, family_id, child_id, title, tasks):
    _, rows = parent("POST", "/rest/v1/plans?select=id", {
        "family_id": family_id, "child_id": child_id,
        "title": title, "status": "draft", "position": 0,
    }, jwt, prefer="return=representation")
    plan_id = rows[0]["id"]
    parent("POST", "/rest/v1/plan_tasks", [
        {"plan_id": plan_id, "position": i, "status": "pending", **t}
        for i, t in enumerate(tasks)
    ], jwt)
    return plan_id


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true",
                    help="leave a school day open for manual UI testing")
    args = ap.parse_args()

    print("=" * 68)
    print("Goji local School Day smoke — real HTTP across cloud, device, kiosk")
    print("=" * 68)

    # ---------------------------------------------------------------- parent
    step("Parent signs in to the local cloud")
    request("POST", f"{SB_URL}/auth/v1/signup",
            {"email": EMAIL, "password": PASSWORD}, {"apikey": SB_ANON})
    code, tok = request("POST", f"{SB_URL}/auth/v1/token?grant_type=password",
                        {"email": EMAIL, "password": PASSWORD}, {"apikey": SB_ANON})
    if not check("parent authenticated", code == 200 and tok and "access_token" in tok,
                 f"HTTP {code}"):
        return 1
    jwt = tok["access_token"]

    code, family_id = parent("POST", "/rest/v1/rpc/bootstrap_family",
                             {"p_family_name": "Family"}, jwt)
    check("bootstrap_family", code == 200 and isinstance(family_id, str), f"HTTP {code}")

    code, parents = parent("GET", "/rest/v1/parents?select=id,family_id", jwt=jwt)
    check("parent can read parents (RLS recursion regression)", code == 200, f"HTTP {code}")
    parent_id = parents[0]["id"] if code == 200 and parents else None

    code, children = parent("GET", "/rest/v1/children?select=id,display_name", jwt=jwt)
    check("parent can read children", code == 200 and children, f"HTTP {code}")
    if not children:
        return 1
    child_id = children[0]["id"]

    # ---------------------------------------------------------------- pairing
    step("Pair the Goji (device-register -> device-claim -> device-poll)")
    code, device = device_get("/api/device")
    check("device reachable", code == 200, f"HTTP {code}")
    check("device in live sync mode", device.get("sync_mode") == "live",
          device.get("sync_mode"))

    if device.get("claimed"):
        print("    device already paired — reusing")
    else:
        code, _ = device_post("/api/device/register-cloud")
        check("device-register", code == 200, f"HTTP {code}")
        pairing_code = device_get("/api/device")[1]["pairing_code"]
        code, claimed = request("POST", f"{SB_URL}/functions/v1/device-claim",
                                {"pairing_code": pairing_code},
                                {"apikey": SB_ANON, "Authorization": f"Bearer {jwt}"})
        check("parent device-claim", code == 200, f"HTTP {code}")
        code, device = device_post("/api/device/poll-claim")
        check("device applied the claim", code == 200 and device.get("claimed"),
              f"HTTP {code}")
    check("device bound to the family", device.get("family_id") == family_id)

    # ------------------------------------------------------- draft invisible
    step("Parent drafts a plan (drafts must NOT reach the device)")
    plan_id = make_plan(jwt, family_id, child_id, "Tuesday school day", [
        {"kind": "app_time", "title": "Math practice",
         "verify_json": {"app": "math", "min_duration_s": 120}},
        {"kind": "freeform", "title": "Tidy your desk", "verify_json": {}},
    ])
    check("draft plan created", bool(plan_id))
    sync_once("draft only")
    code, today = device_get("/api/plans/today?user_id=1")
    check("device has no plan while it is a draft",
          code == 200 and not (today.get("plan") or {}).get("cloud_id"))
    check("School Mode off before Start",
          not (today.get("school") or {}).get("active"))

    # ------------------------------------------------------------ start day
    step("Parent taps Start (rpc start_school_day)")
    code, started = parent("POST", "/rest/v1/rpc/start_school_day",
                           {"p_plan_id": plan_id}, jwt)
    check("start_school_day", code == 200 and started.get("status") == "pending_start",
          f"HTTP {code} {started}")

    step("Device syncs: pulls the plan and acks the session to active")
    s = sync_once("start")
    check("plan pulled", s.get("pulled") == 1, str(s.get("pulled")))
    check("session acked", s.get("school_acked") == 1, str(s.get("school_acked")))

    code, today = device_get("/api/plans/today?user_id=1")
    plan = today.get("plan") or {}
    school = today.get("school") or {}
    check("kiosk shows the plan", plan.get("cloud_id") == plan_id)
    check("School Mode is active on the kiosk", school.get("active") is True)
    check("allowed apps limited to the plan", set(school.get("allowed_apps") or []) == {"hub", "math"},
          str(school.get("allowed_apps")))
    code, status = device_get("/api/school/status?user_id=1")
    check("/api/school/status agrees", code == 200 and status.get("active") is True)

    # ----------------------------------------------------------- parent msg
    step("Parent sends a message; the Goji picks it up and the kid reacts")
    code, msg = parent("POST", "/rest/v1/messages?select=id",
                       {"family_id": family_id, "child_id": child_id,
                        "from_parent_id": parent_id, "body": "Proud of you today"},
                       jwt, prefer="return=representation")
    check("message inserted", code == 201, f"HTTP {code} {msg}")
    s = sync_once("messages")
    check("message pulled to the device", s.get("messages_pulled") == 1,
          str(s.get("messages_pulled")))
    check("message acked", s.get("messages_acked") == 1, str(s.get("messages_acked")))
    code, msgs = device_get("/api/messages?user_id=1")
    bodies = [m.get("body") for m in (msgs.get("messages") if isinstance(msgs, dict) else msgs) or []]
    check("kiosk shows the message", "Proud of you today" in bodies, str(bodies))
    code, rows = parent("GET", f"/rest/v1/messages?child_id=eq.{child_id}"
                                "&select=body,delivered_at", jwt=jwt)
    check("parent sees it was delivered",
          code == 200 and rows and rows[0].get("delivered_at") is not None)

    # ------------------------------------------------------------ kid works
    step("Kid does the work on the Goji")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    code, _ = device_post("/api/activity?user_id=1", {"events": [{
        "app": "math", "event_type": "app.session", "duration_s": 130,
        "subject_type": "drill", "subject_id": "addition", "occurred_at": now,
    }]})
    check("math session recorded", code == 201, f"HTTP {code}")

    code, today = device_get("/api/plans/today?user_id=1")
    tasks = {t["title"]: t for t in (today.get("plan") or {}).get("tasks", [])}
    check("math task auto-verified from app time",
          tasks.get("Math practice", {}).get("status") == "done"
          and tasks["Math practice"].get("completed_how") == "auto",
          str(tasks.get("Math practice", {}).get("status")))

    freeform_id = tasks.get("Tidy your desk", {}).get("id")
    code, confirmed = device_post(f"/api/plans/tasks/{freeform_id}/confirm?user_id=1")
    check("kid self-confirms the freeform task", code == 200, f"HTTP {code}")

    # Assert on the confirm response, not a re-fetch: finishing the last task
    # flips the plan to `completed`, so /api/plans/today immediately advances to
    # the next active plan and would no longer describe the day just finished.
    done_tasks = (confirmed.get("plan") or {}).get("tasks", [])
    check("every task on the plan is done",
          bool(done_tasks) and all(t["status"] == "done" for t in done_tasks),
          str([(t["title"], t["status"]) for t in done_tasks]))

    code, today = device_get("/api/plans/today?user_id=1")
    check("School Mode released itself when the plan finished",
          not (today.get("school") or {}).get("active"))

    # -------------------------------------------------------- parent sees it
    step("Device pushes results; parent sees the finished day")
    s = sync_once("completion")
    check("activity uploaded", (s.get("pushed") or 0) >= 1, str(s.get("pushed")))
    check("task status pushed", (s.get("status_pushed") or 0) >= 2,
          str(s.get("status_pushed")))

    code, rows = parent("GET", f"/rest/v1/plans?id=eq.{plan_id}&select=status,completed_at",
                        jwt=jwt)
    check("cloud plan is completed", code == 200 and rows
          and rows[0]["status"] == "completed", str(rows))

    code, rows = parent("GET", f"/rest/v1/plan_tasks?plan_id=eq.{plan_id}"
                                "&select=title,status,completed_how&order=position", jwt=jwt)
    check("both tasks done in the cloud",
          code == 200 and all(r["status"] == "done" for r in rows) and len(rows) == 2,
          str(rows))
    check("completion method survived the wire",
          {r["title"]: r["completed_how"] for r in rows}
          == {"Math practice": "auto", "Tidy your desk": "self_confirm"}, str(rows))

    code, rows = parent("GET", f"/rest/v1/school_sessions?plan_id=eq.{plan_id}"
                                "&select=status,ended_how", jwt=jwt)
    check("session completed via all_tasks_done",
          code == 200 and rows and rows[0]["status"] == "completed"
          and rows[0]["ended_how"] == "all_tasks_done", str(rows))

    code, rows = parent("GET", f"/rest/v1/activity_events?child_id=eq.{child_id}"
                                "&select=app,duration_s", jwt=jwt)
    check("parent sees the kid's activity", code == 200 and rows, str(rows))

    code, summary = parent("POST", "/rest/v1/rpc/child_progress_summary",
                           {"p_child_id": child_id, "p_days": 7}, jwt)
    check("child_progress_summary RPC works", code == 200 and summary
          and summary.get("event_count", 0) >= 1, f"HTTP {code}")

    # ---------------------------------------------------------- release path
    step("Second day, ended early by the parent (rpc release_school_day)")
    plan2 = make_plan(jwt, family_id, child_id, "Half day", [
        {"kind": "app_time", "title": "Typing drill",
         "verify_json": {"app": "typing", "min_duration_s": 600}},
    ])
    parent("POST", "/rest/v1/rpc/start_school_day", {"p_plan_id": plan2}, jwt)
    sync_once("start day 2")
    code, today = device_get("/api/plans/today?user_id=1")
    check("School Mode active again", (today.get("school") or {}).get("active") is True)

    if args.keep:
        print("\n    --keep: leaving this school day open for manual UI testing")
    else:
        code, released = parent("POST", "/rest/v1/rpc/release_school_day",
                                {"p_child_id": child_id}, jwt)
        check("release_school_day", code == 200
              and released.get("status") == "pending_release", f"HTTP {code} {released}")
        sync_once("release")
        code, today = device_get("/api/plans/today?user_id=1")
        check("School Mode off after parent release",
              not (today.get("school") or {}).get("active"))
        code, rows = parent("GET", f"/rest/v1/school_sessions?plan_id=eq.{plan2}"
                                    "&select=status,ended_how", jwt=jwt)
        check("session recorded as parent_release",
              code == 200 and rows and rows[0]["status"] == "released"
              and rows[0]["ended_how"] == "parent_release", str(rows))

    print("\n" + "=" * 68)
    if failures:
        print(f"{len(failures)} FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"All {step_no} steps passed — cloud, device and kiosk agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
