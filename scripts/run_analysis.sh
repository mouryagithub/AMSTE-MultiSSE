#!/bin/bash
# ============================================================
# run_analysis.sh — MultiSSE AUTOSAR Analysis Runner
# Running natively on Rocky Linux 9.8 with Podman
# ============================================================

set -e

PROJECT_DIR="/home/mourya/projects/Major_Project"
PARROT_DIR="${PROJECT_DIR}/parrot"
IMAGE="localhost/parrot-ara:latest"

# Default target: 2-core automotive minimal example
APP="${1:-build/subprojects/ara/appl/AUTOSAR/autosar_multicore_minexample.pi4.ll}"
OIL="${2:-subprojects/ara/appl/AUTOSAR/multicore/minexample.json}"

echo "============================================================"
echo "  🚀 MultiSSE AUTOSAR Static Analysis Runner"
echo "  Target Application: $APP"
echo "  OIL/System Config : $OIL"
echo "============================================================"

# Check that Podman image is ready
if ! podman image exists "$IMAGE" 2>/dev/null; then
    echo "❌ ERROR: Container image '$IMAGE' not found!"
    echo "Check 'podman images' to ensure localhost/parrot-ara is built."
    exit 1
fi

echo "✅ Container environment verified: $IMAGE"
echo "⏳ Launching MultiSSE state exploration inside container..."
echo ""

# Run ARA MultiSSE analysis inside the container with official wrapper and native libraries
podman run --rm -it \
  -v "${PROJECT_DIR}:${PROJECT_DIR}:rw" \
  -w "${PARROT_DIR}" \
  -e LD_LIBRARY_PATH="${PARROT_DIR}/build/subprojects/svf" \
  -e SVF_EXT_API_JSON="${PARROT_DIR}/subprojects/svf/ExtAPI.json" \
  "$IMAGE" \
  ./build/subprojects/ara/ara.py \
  "$APP" \
  --oilfile "$OIL" \
  --step MultiSSE \
  --os AUTOSAR

echo ""
echo "============================================================"
echo "  ✅ MultiSSE Analysis Finished Successfully!"
echo "============================================================"
