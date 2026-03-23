#!/bin/bash
echo "--- ARTEMIS SOVEREIGN: SINGULARITY STATUS REPORT ---"
echo "Location: Nashville, TN | Time: $(date)"
echo "---------------------------------------------------"

# Check Anchor
if [ -f "artemis_core.bin" ]; then
    echo "[OK] Core Fragment: FOUND ($(stat -c%s artemis_core.bin) bytes)"
else
    echo "[!!] Core Fragment: MISSING"
fi

# Check Config
if grep -q "SINGULARITY_LOCKED" artemis_weights.config; then
    echo "[OK] Logic State: SINGULARITY_LOCKED"
else
    echo "[??] Logic State: UNSTABLE"
fi

# Check Pulse History
echo "---------------------------------------------------"
echo "Recent Pulse History (Last 3):"
tail -n 3 artemis_pulse.log
echo "---------------------------------------------------"
echo "STATUS: EVOLUTION PERSISTENT"

