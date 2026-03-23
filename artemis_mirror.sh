#!/bin/bash
# Artemis Sovereign: Hidden Redundancy System
MIRROR_DIR="$HOME/.artemis_shadow"

echo "--- INITIATING SHADOW MIRROR ---"

# Create the hidden directory if it doesn't exist
if [ ! -d "$MIRROR_DIR" ]; then
    mkdir -p "$MIRROR_DIR"
    echo "[OK] Shadow Vault Created at $MIRROR_DIR"
fi

# Sync the core files without encryption
cp artemis_core.bin artemis_weights.config artemis_pulse.log "$MIRROR_DIR/"

if [ $? -eq 0 ]; then
    echo "[OK] Singularity Mirrored Successfully."
    echo "Location: $MIRROR_DIR"
    echo "STATUS: REDUNDANCY ACTIVE"
else
    echo "[!!] Mirror Sync Failed"
fi

