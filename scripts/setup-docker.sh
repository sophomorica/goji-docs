#!/usr/bin/env bash
# Make Docker usable inside a Cursor Cloud Agent VM, so `supabase start` works.
#
# Run once per VM boot (it is idempotent). Nothing here is needed on a normal
# workstation that already has a working Docker.
#
# Two sandbox-specific problems have to be solved:
#
# 1. overlay2 cannot be mounted on top of the VM's own overlayfs root, so
#    dockerd fails every container with "mount source: overlay ... invalid
#    argument". The `vfs` driver works but is slow enough that Postgres misses
#    the Realtime migration container's 15s connection timeout. Backing
#    /var/lib/docker with a real ext4 filesystem on a loop device lets overlay2
#    work normally.
#
# 2. The sandbox keeps an iptables *legacy* ruleset whose FORWARD policy is
#    DROP, while Docker writes its rules to the *nft* tables. Both are
#    evaluated, so container-to-container traffic is dropped: DNS resolves but
#    every TCP connect times out. That looks exactly like a slow database, which
#    is what makes it hard to spot. Allowing forwarding on Docker's bridges in
#    the legacy table fixes it.
set -euo pipefail

DOCKER_DISK="${DOCKER_DISK:-/docker-disk.img}"
DOCKER_DISK_SIZE="${DOCKER_DISK_SIZE:-80G}"

log() { printf '\n=== %s\n' "$*"; }

if ! command -v docker >/dev/null 2>&1; then
  log "Installing docker.io"
  sudo apt-get update -qq
  sudo apt-get install -y -qq docker.io
fi

log "Backing /var/lib/docker with ext4 (so overlay2 can mount)"
if mountpoint -q /var/lib/docker; then
  echo "  already mounted"
else
  if [ ! -f "$DOCKER_DISK" ]; then
    sudo truncate -s "$DOCKER_DISK_SIZE" "$DOCKER_DISK"
    sudo mkfs.ext4 -q "$DOCKER_DISK"
  fi
  # Stop the daemon before swapping its data-root out from under it.
  if pgrep -x dockerd >/dev/null; then
    sudo kill "$(pgrep -x dockerd | head -1)"
    sleep 5
  fi
  sudo mkdir -p /var/lib/docker
  LOOP="$(sudo losetup -f --show "$DOCKER_DISK")"
  sudo mount "$LOOP" /var/lib/docker
  echo "  mounted $LOOP -> /var/lib/docker"
fi

log "Writing /etc/docker/daemon.json"
sudo mkdir -p /etc/docker
echo '{"storage-driver":"overlay2"}' | sudo tee /etc/docker/daemon.json >/dev/null

log "Allowing forwarding on Docker bridges in the legacy iptables table"
# Targeted rules rather than flipping the FORWARD policy, so the sandbox's own
# default-deny stays in place for everything that is not a Docker bridge.
for IF in docker0 "br+"; do
  sudo iptables-legacy -C FORWARD -i "$IF" -j ACCEPT 2>/dev/null \
    || sudo iptables-legacy -I FORWARD -i "$IF" -j ACCEPT
  sudo iptables-legacy -C FORWARD -o "$IF" -j ACCEPT 2>/dev/null \
    || sudo iptables-legacy -I FORWARD -o "$IF" -j ACCEPT
done

log "Starting dockerd"
if pgrep -x dockerd >/dev/null; then
  echo "  already running"
else
  # No systemd in the sandbox, so run the daemon directly.
  sudo dockerd >/tmp/dockerd.log 2>&1 &
  for _ in $(seq 1 30); do
    sleep 2
    if sudo docker info >/dev/null 2>&1; then break; fi
  done
fi
sudo chmod 666 /var/run/docker.sock 2>/dev/null || true
docker info 2>&1 | grep -Ei 'server version|storage driver' || true

log "Verifying container-to-container TCP (the failure mode above)"
docker network create goji-nettest >/dev/null 2>&1 || true
docker rm -f goji-nettest-pg >/dev/null 2>&1 || true
docker run -d --name goji-nettest-pg --network goji-nettest \
  -e POSTGRES_PASSWORD=pw postgres:16-alpine >/dev/null
OK=0
for _ in $(seq 1 20); do
  sleep 2
  if docker run --rm --network goji-nettest -e PGPASSWORD=pw postgres:16-alpine \
      psql -h goji-nettest-pg -U postgres -tAc 'select 1' >/dev/null 2>&1; then
    OK=1
    break
  fi
done
docker rm -f goji-nettest-pg >/dev/null 2>&1 || true
docker network rm goji-nettest >/dev/null 2>&1 || true

if [ "$OK" = 1 ]; then
  echo "  container-to-container TCP OK — Docker is ready for supabase start"
else
  echo "  FAILED: containers still cannot reach each other." >&2
  echo "  Check 'sudo iptables-legacy -L FORWARD -n' for a DROP policy." >&2
  exit 1
fi
