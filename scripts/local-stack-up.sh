#!/usr/bin/env bash
# Bring up the whole Goji product locally: cloud + device + parent app.
#
#   scripts/local-stack-up.sh            # start everything
#   scripts/local-stack-up.sh --reset     # also wipe cloud DB + device SQLite
#   scripts/local-stack-up.sh --skip-app  # skip the (slow) Flutter web build
#
# Afterwards:
#   parent app  http://127.0.0.1:8088
#   kiosk       http://127.0.0.1:5173
#   device API  http://127.0.0.1:5000
#   cloud       http://127.0.0.1:54321
#
# Each service runs in its own tmux session (goji-backend, goji-frontend,
# goji-parent-app, goji-sync-agent) so it survives the shell that started it.
set -euo pipefail

cd "$(dirname "$0")/.."
# shellcheck source=./local-env.sh
source scripts/local-env.sh

RESET=0
SKIP_APP=0
for arg in "$@"; do
  case "$arg" in
    --reset) RESET=1 ;;
    --skip-app) SKIP_APP=1 ;;
    *) echo "unknown flag: $arg" >&2; exit 2 ;;
  esac
done

log() { printf '\n=== %s\n' "$*"; }

# --- 0. Docker ---------------------------------------------------------------
if ! docker info >/dev/null 2>&1; then
  log "Docker is not usable yet — running scripts/setup-docker.sh"
  scripts/setup-docker.sh
fi

# --- 1. Cloud ----------------------------------------------------------------
log "Local Supabase (goji_cloud)"
if curl -fsS -o /dev/null --max-time 3 "$SB_URL/rest/v1/" -H "apikey: $SB_ANON" 2>/dev/null; then
  echo "  already running"
  if [ "$RESET" = 1 ]; then
    echo "  --reset: re-applying migrations"
    ( cd "$GOJI_CLOUD_DIR" && npx --yes supabase@latest db reset >/dev/null )
  fi
else
  ( cd "$GOJI_CLOUD_DIR" && npx --yes supabase@latest start -x "$SB_EXCLUDE" ) \
    | tail -5
fi
goji_wait_http "$SB_URL/rest/v1/" "supabase rest"

# --- 2. Device backend -------------------------------------------------------
log "Device backend (goji_computer, GOJI_SYNC_MODE=live)"
echo "  wrote $(goji_write_device_env)"
if [ ! -d "$GOJI_COMPUTER_DIR/backend/.venv" ]; then
  echo "  creating backend venv"
  ( cd "$GOJI_COMPUTER_DIR/backend" \
      && python3 -m venv .venv \
      && . .venv/bin/activate \
      && pip install -q -r requirements.txt )
fi
if [ "$RESET" = 1 ]; then
  echo "  --reset: removing device SQLite so the Goji comes up unpaired"
  goji_tmux kill-session -t "=$SESS_BACKEND" 2>/dev/null || true
  goji_tmux kill-session -t "=$SESS_SYNC" 2>/dev/null || true
  sleep 2
  rm -f "$GOJI_COMPUTER_DIR/backend/data/goji.db"
fi
goji_service "$SESS_BACKEND" "$GOJI_COMPUTER_DIR/backend" \
  "set -a && source .env.local-cloud && set +a && source .venv/bin/activate && python app.py 2>&1 | tee /tmp/goji-backend.log"
goji_wait_http "$GOJI_BACKEND_URL/api/device" "device backend"

# --- 3. Kiosk ----------------------------------------------------------------
log "Kiosk frontend (Svelte dev server)"
if [ ! -d "$GOJI_COMPUTER_DIR/frontend/node_modules" ]; then
  ( cd "$GOJI_COMPUTER_DIR/frontend" && npm ci )
fi
goji_service "$SESS_KIOSK" "$GOJI_COMPUTER_DIR/frontend" \
  "npm run dev -- --host 127.0.0.1 2>&1 | tee /tmp/goji-frontend.log"
goji_wait_http "$GOJI_KIOSK_URL/" "kiosk"

# --- 4. Sync agent -----------------------------------------------------------
log "Device sync agent (--loop)"
goji_service "$SESS_SYNC" "$GOJI_COMPUTER_DIR/backend" \
  "set -a && source .env.local-cloud && set +a && source .venv/bin/activate && python -m sync.agent --loop 2>&1 | tee /tmp/goji-sync.log"
echo "  started (adaptive interval; ~10s while a school day is open)"

# --- 5. Parent app -----------------------------------------------------------
log "Parent app (Flutter web)"
export PATH="$HOME/flutter/bin:$PATH"
if ! command -v flutter >/dev/null 2>&1; then
  echo "  Flutter SDK not found. Install it, then re-run:" >&2
  echo "    git clone https://github.com/flutter/flutter.git -b stable --depth 1 ~/flutter" >&2
  exit 1
fi
if [ "$SKIP_APP" = 0 ] || [ ! -f "$GOJI_APP_DIR/build/web/index.html" ]; then
  ( cd "$GOJI_APP_DIR" \
      && flutter pub get >/dev/null \
      && flutter build web --release \
           --dart-define=SUPABASE_URL="$SB_URL" \
           --dart-define=SUPABASE_ANON_KEY="$SB_ANON" 2>&1 | tail -3 )
fi
goji_service "$SESS_APP" "$GOJI_APP_DIR/build/web" \
  "python3 -m http.server $GOJI_PARENT_APP_PORT --bind 127.0.0.1 2>&1 | tee /tmp/goji-parent-app.log"
goji_wait_http "$GOJI_PARENT_APP_URL/" "parent app"

cat <<EOF

=== Goji local stack is up ===
  parent app  $GOJI_PARENT_APP_URL   (sign up: $GOJI_TEST_EMAIL / $GOJI_TEST_PASSWORD)
  kiosk       $GOJI_KIOSK_URL
  device API  $GOJI_BACKEND_URL
  cloud       $SB_URL

Pair the Goji: read the kiosk pairing code, then enter it on the parent app's
Pair tab. Then run the headless check:

  scripts/local-school-day-smoke.sh
EOF
