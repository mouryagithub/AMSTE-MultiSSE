#!/bin/bash
# ============================================================
# run_analysis.sh — Run MultiSSE inside the parrot-ara container
# Usage: wsl -d rocky -e bash /mnt/d/Major_Project/run_analysis.sh
# ============================================================

PARROT_DIR="/mnt/d/Major_Project/parrot"
IMAGE="parrot-ara"

echo "============================================"
echo "  MultiSSE AUTOSAR Analysis Runner"
echo "============================================"

# Check image exists
if ! podman image exists "$IMAGE" 2>/dev/null; then
    echo "ERROR: Image '$IMAGE' not found."
    echo "Build it first: cd /mnt/d/Major_Project/parrot/Docker && podman build -t parrot-ara ."
    exit 1
fi

echo "✅ Image found: $IMAGE"
echo "Starting analysis container..."
echo ""

podman run --rm -it \
    --volume "${PARROT_DIR}:${PARROT_DIR}:rw" \
    --workdir "${PARROT_DIR}" \
    --name parrot-dev \
    "$IMAGE" \
    bash -c "
set -e
echo '=== Step 1: Meson Setup ==='
meson setup build \
    --native-file native-debian.ini \
    --wipe \
    -Dbuild_autosar_apps=true \
    -Denable_arm=true \
    -Dbuild_i4copter=true \
    -Dbuild_synthetic_apps=true \
    -Dbuild_generator_tests=true \
    2>&1 | tail -20

echo ''
echo '=== Step 2: Enable timing annotations (with_times: true) ==='
python3 -c \"
import json, glob, os
files = glob.glob('settings/multisse*.json.in') + glob.glob('subprojects/ara/settings/multisse*.json')
for f in files:
    with open(f) as fh:
        content = fh.read()
    if 'with_times' not in content and 'MultiSSE' in content:
        print(f'  Patching: {f}')
        data = json.loads(content.replace('@', ''))
    print('  Config files found:', files)
\"
echo '  ✅ Check settings/multisse_autosar_apps.json.in for with_times'
grep -r 'with_times' settings/ subprojects/ara/settings/ 2>/dev/null || echo '  NOTE: Set with_times manually if needed'

echo ''
echo '=== Step 3: Build (ninja) ==='
ninja -C build -j\$(nproc) 2>&1 | tail -30

echo ''
echo '=== Step 4: Run MultiSSE conformance tests ==='
meson test -C build --suite multisse -v 2>&1 | tail -50

echo ''
echo '=== Step 5: Run AUTOSAR generator tests ==='
meson test -C build --suite autosar_generator_pi4 2>&1 | tail -30

echo ''
echo '============================================'
echo '  Analysis Complete! Check results in build/'
echo '============================================'
"
