#!/usr/bin/env bash
# Checkout the three private product repos next to goji-docs.
#
# Cloud Agent git clone of private siblings is often blocked unless those
# remotes are added to the environment. `gh api …/tarball` works when the
# session token can read sophomorica/{kodi-computer,goji-cloud,goji-learner-app}.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

clone_tarball() {
  local repo="$1" dest="$2"
  if [ -d "$dest/.git" ] || [ -f "$dest/README.md" ] || [ -f "$dest/CLAUDE.md" ]; then
    echo "skip $dest (already present)"
    return 0
  fi
  echo "fetching $repo → $dest"
  mkdir -p "$dest"
  gh api "repos/sophomorica/${repo}/tarball/main" | tar -xz -C "$dest" --strip-components=1
}

clone_tarball kodi-computer goji_computer
clone_tarball goji-cloud goji_cloud
clone_tarball goji-learner-app goji_learner_app
echo "done"
