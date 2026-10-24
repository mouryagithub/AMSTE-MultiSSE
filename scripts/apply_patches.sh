#!/usr/bin/env bash
# Script to apply all upstream ARA and MultiSSE bug fixes
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PATCH_FILE="$ROOT_DIR/patches/ara_multisse_fixes.patch"

if [ -f "$PATCH_FILE" ] && [ -d "$ROOT_DIR/parrot/subprojects/ara" ]; then
    echo "Applying MultiSSE fixes to parrot/subprojects/ara..."
    cd "$ROOT_DIR/parrot/subprojects/ara"
    git apply "$PATCH_FILE" || git apply --check "$PATCH_FILE" || echo "Patches already applied or conflict."
    echo "Successfully updated ARA."
fi
