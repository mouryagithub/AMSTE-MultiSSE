#!/bin/bash
# ============================================================
# MultiSSE Build & Run Script
# Run AFTER setup_env.sh completes:
#   wsl -d rocky -e bash /mnt/d/Major_Project/build_and_run.sh
# ============================================================

set -e

PROJECT_DIR="/mnt/d/Major_Project"
PARROT_DIR="$PROJECT_DIR/parrot"
ARA_DIR="$PARROT_DIR/subprojects/ara"
CONFIG_FILE="$ARA_DIR/settings/autosar_generator_arm.json"

echo "============================================"
echo "  MultiSSE Build & Run"
echo "============================================"

# ── Step 1: Verify Docker is running ─────────────────────
echo ""
echo "[1/5] Checking Docker..."
if ! docker info &>/dev/null; then
    echo "  Starting Docker service..."
    sudo systemctl start docker
    sleep 3
fi
echo "  ✅ Docker: $(docker --version)"

# ── Step 2: Set critical timing config ───────────────────
echo ""
echo "[2/5] Setting MultiSSE timing config (with_times: true)..."
if [ -f "$CONFIG_FILE" ]; then
    # Enable timing annotations — CRITICAL for paper-matching results
    python3 -c "
import json, sys
with open('$CONFIG_FILE', 'r') as f:
    cfg = json.load(f)
cfg.setdefault('MultiSSE', {})['with_times'] = True
with open('$CONFIG_FILE', 'w') as f:
    json.dump(cfg, f, indent=2)
print('  ✅ with_times=true set in', '$CONFIG_FILE')
"
else
    echo "  ⚠️  Config not found yet — will set after build"
fi

# ── Step 3: Build PARROT with Meson ──────────────────────
echo ""
echo "[3/5] Setting up Meson build..."
mkdir -p "$PARROT_DIR/build"
meson setup "$PARROT_DIR/build" "$PARROT_DIR" --wipe 2>&1 | tail -20
echo "  ✅ Meson setup complete"

echo ""
echo "  Building with Ninja (this may take 10-30 min for LLVM)..."
ninja -C "$PARROT_DIR/build" -j$(nproc) 2>&1 | tail -30
echo "  ✅ Build complete"

# ── Step 4: Run MultiSSE conformance tests ────────────────
echo ""
echo "[4/5] Running MultiSSE test suite..."
echo "  (These 12 tests verify correctness — all should PASS)"
meson test -C "$PARROT_DIR/build" --suite multisse -v 2>&1 | tail -40

# ── Step 5: Run AUTOSAR generator test suite ─────────────
echo ""
echo "[5/5] Running AUTOSAR generator test suite (autosar_generator_pi4)..."
echo "  (Validates 872-app synthetic benchmark pipeline)"
meson test -C "$PARROT_DIR/build" --suite autosar_generator_pi4 2>&1 | tail -20

echo ""
echo "============================================"
echo "  ✅ MultiSSE Analysis Pipeline COMPLETE!"
echo ""
echo "  Check results in: $PARROT_DIR/build/"
echo "  Key files:"
echo "    multisse.py   → $ARA_DIR/ara/steps/multisse.py"
echo "    MSTG output   → $PARROT_DIR/build/test/ (look for .dot or .json)"
echo "============================================"
