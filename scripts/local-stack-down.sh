#!/usr/bin/env bash
# Stop the local Goji stack.
#
#   scripts/local-stack-down.sh            # stop device + app, leave cloud up
#   scripts/local-stack-down.sh --all      # also stop the Supabase containers
#
# Kills only the tmux sessions this harness created, by name. It never uses
# `pkill -f`, which would be able to match unrelated processes.
set -euo pipefail

cd "$(dirname "$0")/.."
# shellcheck source=./local-env.sh
source scripts/local-env.sh

for s in "$SESS_SYNC" "$SESS_BACKEND" "$SESS_KIOSK" "$SESS_APP"; do
  if goji_tmux has-session -t "=$s" 2>/dev/null; then
    goji_tmux kill-session -t "=$s"
    echo "stopped $s"
  fi
done

if [ "${1:-}" = "--all" ]; then
  echo "stopping Supabase containers"
  ( cd "$GOJI_CLOUD_DIR" && npx --yes supabase@latest stop ) | tail -3
fi
