#!/usr/bin/env bash
# Idempotent Cloud Agent install for goji-docs multi-repo workspace.
# Expects sibling checkouts at goji_computer/, goji_learner_app/, goji_cloud/
# (prefer adding those repos to the environment; otherwise clones via GITHUB_TOKEN).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export PATH="${HOME}/flutter/bin:${PATH}"

clone_sibling() {
  local repo="$1" dest="$2" branch="${3:-main}"
  if [ -d "$dest/.git" ]; then
    echo "OK $dest already present"
    return 0
  fi
  if [ -z "${GITHUB_TOKEN:-}" ]; then
    echo "WARN: $dest missing and GITHUB_TOKEN unset — add sibling repos to the Cloud environment" >&2
    return 1
  fi
  echo "Cloning sophomorica/$repo → $dest (branch $branch)"
  GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null \
    git clone --depth 1 -b "$branch" \
      "https://x-access-token:${GITHUB_TOKEN}@github.com/sophomorica/${repo}.git" \
      "$dest"
}

# Prefer environment multi-repo checkout; fall back to clone.
clone_sibling kodi-computer goji_computer main || true
clone_sibling goji-learner-app goji_learner_app main || \
  clone_sibling goji-learner-app goji_learner_app feat/school-day-parent || true
clone_sibling goji-cloud goji_cloud main || \
  clone_sibling goji-cloud goji_cloud feat/school-day-sync-contract || true

# System packages (idempotent)
if ! python3 -c "import venv" 2>/dev/null; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3.12-venv
fi

# Flutter SDK
if [ ! -x "${HOME}/flutter/bin/flutter" ]; then
  git clone https://github.com/flutter/flutter.git -b stable --depth 1 "${HOME}/flutter"
fi
grep -q 'flutter/bin' "${HOME}/.bashrc" 2>/dev/null || \
  echo 'export PATH="$HOME/flutter/bin:$PATH"' >> "${HOME}/.bashrc"
flutter --version >/dev/null
flutter config --no-analytics >/dev/null || true

# goji_computer
if [ -d goji_computer/backend ]; then
  python3 -m venv goji_computer/backend/.venv
  # shellcheck disable=SC1091
  source goji_computer/backend/.venv/bin/activate
  pip install -q -r goji_computer/backend/requirements.txt
  deactivate
  if [ -f goji_computer/backend/package.json ]; then
    (cd goji_computer/backend && npm install --silent)
  fi
  (cd goji_computer/frontend && npm install --silent)
fi

# Parent app
if [ -d goji_learner_app ]; then
  (cd goji_learner_app && flutter pub get)
fi

# Wire cloud secrets into gitignored .env files when present
write_envs() {
  local url="${SUPABASE_URL:-}"
  local anon="${SUPABASE_ANON_KEY:-}"
  local cloud_url="${GOJI_CLOUD_URL:-}"
  local cloud_anon="${GOJI_CLOUD_ANON_KEY:-}"
  if [ -z "$url" ] || [ -z "$anon" ]; then
    echo "INFO: SUPABASE_URL / SUPABASE_ANON_KEY not set — parent app live mode skipped"
    return 0
  fi
  if [ -z "$cloud_url" ]; then
    cloud_url="${url%/}/functions/v1"
  fi
  if [ -z "$cloud_anon" ]; then
    cloud_anon="$anon"
  fi
  if [ -d goji_learner_app ]; then
    cat > goji_learner_app/.env <<ENV
SUPABASE_URL=${url}
SUPABASE_ANON_KEY=${anon}
ENV
    echo "Wrote goji_learner_app/.env"
  fi
  if [ -d goji_computer/backend ]; then
    cat > goji_computer/backend/.env <<ENV
GOJI_SYNC_MODE=live
GOJI_CLOUD_URL=${cloud_url}
GOJI_CLOUD_ANON_KEY=${cloud_anon}
GOJI_SYNC_INTERVAL_S=20
GOJI_SYNC_INTERVAL_ACTIVE_S=10
ENV
    echo "Wrote goji_computer/backend/.env (live sync)"
  fi
}
write_envs

echo "cloud-agent-install: done"
