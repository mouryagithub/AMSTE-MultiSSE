#!/bin/bash
set -e

echo "=== 1. Checking Environment Inside Container ==="
python3 --version
clang-14 --version | head -n 1
llvm-config-14 --version
meson --version
ninja --version

echo ""
echo "=== 2. Running Meson Setup ==="
cd /mnt/d/Major_Project/parrot
# Clean previous build dir if exists
rm -rf build

# Run Meson setup for AUTOSAR apps with ARM enabled
meson setup build --native-file native-debian.ini -Dbuild_autosar_apps=true -Denable_arm=true

echo ""
echo "=== 3. Meson Setup Succeeded! ==="
