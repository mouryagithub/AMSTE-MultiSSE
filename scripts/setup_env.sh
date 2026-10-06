#!/bin/bash
# ============================================================
# MultiSSE Environment Setup Script
# Run this inside WSL2 Rocky Linux:
#   wsl -d rocky -e bash /mnt/d/Major_Project/setup_env.sh
# ============================================================

set -e  # Exit on any error

PROJECT_DIR="/mnt/d/Major_Project"
PARROT_DIR="$PROJECT_DIR/parrot"
DOCKER_DATA_DIR="$PROJECT_DIR/docker-data"

echo "============================================"
echo "  MultiSSE Environment Setup"
echo "  Project dir: $PROJECT_DIR"
echo "============================================"

# ── Step 1: Enable systemd if not already ──────────────────
echo ""
echo "[1/7] Checking systemd..."
if [ "$(ps -p 1 -o comm=)" != "systemd" ]; then
    echo "  systemd NOT running. Enabling via /etc/wsl.conf..."
    sudo tee /etc/wsl.conf > /dev/null <<'EOF'
[boot]
systemd=true
EOF
    echo "  ✅ wsl.conf written. You MUST restart WSL2:"
    echo "     Run in PowerShell: wsl --shutdown"
    echo "     Then re-run this script."
    exit 0
else
    echo "  ✅ systemd is running"
fi

# ── Step 2: Install Docker CE ──────────────────────────────
echo ""
echo "[2/7] Installing Docker CE..."
if command -v docker &>/dev/null; then
    echo "  ✅ Docker already installed: $(docker --version)"
else
    echo "  Adding Docker CE repo..."
    sudo dnf config-manager --add-repo \
        https://download.docker.com/linux/rhel/docker-ce.repo -y
    echo "  Installing Docker packages..."
    sudo dnf install -y docker-ce docker-ce-cli containerd.io \
        docker-buildx-plugin docker-compose-plugin
    echo "  ✅ Docker installed"
fi

# ── Step 3: Configure Docker data-root to D:\ ─────────────
echo ""
echo "[3/7] Configuring Docker to store data on D:\\..."
mkdir -p "$DOCKER_DATA_DIR"
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json > /dev/null <<EOF
{
  "data-root": "$DOCKER_DATA_DIR"
}
EOF
echo "  ✅ Docker data-root set to $DOCKER_DATA_DIR"

# ── Step 4: Start and enable Docker ───────────────────────
echo ""
echo "[4/7] Starting Docker service..."
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker "$USER"
echo "  ✅ Docker service running"
docker --version

# ── Step 5: Install build dependencies ────────────────────
echo ""
echo "[5/7] Installing build tools (git, meson, ninja, python3)..."
sudo dnf install -y git meson ninja-build python3 python3-pip \
    gcc gcc-c++ cmake make wget curl
echo "  ✅ Build tools installed"

# ── Step 6: Clone PARROT repository ───────────────────────
echo ""
echo "[6/7] Cloning PARROT repository..."
if [ -d "$PARROT_DIR/.git" ]; then
    echo "  PARROT already cloned. Pulling latest..."
    git -C "$PARROT_DIR" pull
else
    echo "  Cloning from GitHub..."
    git clone --recurse-submodules \
        https://github.com/luhsra/parrot.git \
        "$PARROT_DIR"
fi
echo "  ✅ PARROT cloned to $PARROT_DIR"

# ── Step 7: Initialize submodules ─────────────────────────
echo ""
echo "[7/7] Initializing all Meson subprojects (ARA, LLVM, dOSEK, Trampoline)..."
git -C "$PARROT_DIR" submodule update --init --recursive
echo "  ✅ All subprojects initialized"

# ── Done ──────────────────────────────────────────────────
echo ""
echo "============================================"
echo "  ✅ Environment setup COMPLETE!"
echo ""
echo "  Next steps:"
echo "  1. newgrp docker  (apply docker group without logout)"
echo "  2. cd $PARROT_DIR"
echo "  3. Run: bash /mnt/d/Major_Project/build_and_run.sh"
echo "============================================"
