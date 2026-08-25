#!/usr/bin/env bash
# Thin wrapper: load the local stack config, then run the smoke check.
#   scripts/local-school-day-smoke.sh [--keep]
set -euo pipefail
cd "$(dirname "$0")/.."
# shellcheck source=./local-env.sh
source scripts/local-env.sh
goji_write_device_env >/dev/null
exec python3 scripts/local_school_day_smoke.py "$@"
