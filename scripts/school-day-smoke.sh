#!/usr/bin/env bash
# Hermetic + optional live School Day smoke for Cloud Agents.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="${HOME}/flutter/bin:${PATH}"

echo "=== 1. Hermetic mock (no network) ==="
cd "$ROOT/goji_computer/backend"
# shellcheck disable=SC1091
source .venv/bin/activate
python -m sync.mock_family_cloud
python -m pytest tests/integration/test_school_day_e2e_mock.py -q --tb=line

echo "=== 2. Computer unit gate (optional quick) ==="
# Keep smoke fast — full suite is separate
python -m pytest tests/test_school_day.py -q --tb=line

if [ -f .env ] && grep -q 'GOJI_SYNC_MODE=live' .env; then
  echo "=== 3. Live sync configured (GOJI_SYNC_MODE=live) ==="
  echo "Pair via POST /api/device/register-cloud + parent device-claim + poll-claim,"
  echo "then create draft plan → start_school_day RPC → python -m sync.agent --once"
else
  echo "=== 3. Live sync not configured (stub mode) — set SUPABASE_* / GOJI_CLOUD_* secrets ==="
fi

echo "school-day-smoke: OK"
