#!/usr/bin/env bash
# Per-boot reconciliation — ensure PATH and env files; do not start long-running servers
# (those belong in environment terminals).
set -euo pipefail
export PATH="${HOME}/flutter/bin:${PATH}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Re-apply secrets → .env on each boot (secrets are injected per pod)
if [ -x scripts/cloud-agent-install.sh ]; then
  # Only the env-writing portion: re-run write by sourcing install's end — call install
  # is idempotent and fast when deps exist.
  scripts/cloud-agent-install.sh
fi

echo "cloud-agent-start: ready (start backend/frontend/flutter via terminals)"
