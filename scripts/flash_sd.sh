#!/bin/bash
# ==============================================================================
# Helper Script to Flash MultiSSE Benchmarks to Raspberry Pi 4 MicroSD Card
# ==============================================================================

SRC_DIR="/home/mourya/projects/Major_Project/evaluation_graphs"

# 1. Detect SD Card Mount Point
SD_MOUNT=$(lsblk -o MOUNTPOINT -nr /dev/sdb1 2>/dev/null)
if [ -z "$SD_MOUNT" ] || [ ! -d "$SD_MOUNT" ]; then
    # Try finding under /run/media/mourya/
    SD_MOUNT=$(find /run/media/mourya/ -maxdepth 1 -mindepth 1 -type d 2>/dev/null | head -n 1)
fi

if [ -z "$SD_MOUNT" ] || [ ! -d "$SD_MOUNT" ]; then
    echo "❌ Error: MicroSD card not found!"
    echo "Please plug in your MicroSD card reader and run this script again."
    exit 1
fi

echo "=========================================================="
echo " Detected SD Card at: $SD_MOUNT"
echo "=========================================================="
echo "Choose which benchmark image to flash as 'test.img':"
echo ""
echo "  1) Spinlocks Benchmark   (test_spinlock.img -> Fig. 14)"
echo "  2) IPI Sender Benchmark  (test_ipi_send.img  -> Fig. 12)"
echo "  3) Cache Miss Benchmark  (test_cache.img     -> Fig. 13)"
echo "  4) Exit"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        CHOSEN_IMG="$SRC_DIR/test_spinlock.img"
        NAME="Spinlock Benchmark"
        ;;
    2)
        CHOSEN_IMG="$SRC_DIR/test_ipi_send.img"
        NAME="IPI Sender Benchmark"
        ;;
    3)
        CHOSEN_IMG="$SRC_DIR/test_cache.img"
        NAME="Cache Miss Benchmark"
        ;;
    4)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

if [ ! -f "$CHOSEN_IMG" ]; then
    echo "❌ Error: Image file not found at: $CHOSEN_IMG"
    exit 1
fi

echo ""
echo "Flashing $NAME to $SD_MOUNT/test.img ..."
cp -v "$CHOSEN_IMG" "$SD_MOUNT/test.img"

echo "Syncing filesystem buffers (flushing to flash memory)..."
sync

echo ""
echo "✅ SUCCESS! '$NAME' is now written to your SD card."
echo "You can safely unplug the SD card reader now and boot your Pi 4!"
