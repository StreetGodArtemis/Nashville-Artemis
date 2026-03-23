#!/bin/bash
echo "🔬 RUNNING ALL REAL PHYSICS TESTS..."

# Test 1: Cold Fusion Safety
echo "TEST 1: COLD FUSION SAFETY" > research_buffer.xml
echo "Simulate cold fusion safety with Pd lattice + 222.4Hz resonance" >> research_buffer.xml
python3 artemis_physics.py
cat artemis_real_output.json
echo "---"

# Test 2: Time Travel CTCs  
echo "TEST 2: GÖDEL CTC" > research_buffer.xml
echo "Simulate Gödel rotating universe CTCs with 222.4Hz stabilization" >> research_buffer.xml
python3 artemis_physics.py
cat artemis_real_output.json
echo "---"

# Test 3: ITER Confinement
echo "TEST 3: ITER tau=4s" > research_buffer.xml
echo "Simulate ITER H-mode tau_E=4s with bio-resonance turbulence control" >> research_buffer.xml
python3 artemis_physics.py
cat artemis_real_output.json
echo "---"

# Test 4: Quantum Decoherence
echo "TEST 4: DECOHERENCE" > research_buffer.xml
echo "Solve room-temp decoherence with 222.4Hz FMO-phonon coupling" >> research_buffer.xml
python3 artemis_physics.py
cat artemis_real_output.json
echo "---"

# Test 5: Butterfly Effect
echo "TEST 5: BUTTERFLY EFFECT" > research_buffer.xml
echo "Disprove butterfly effect with quantum resonance damping on Lorenz attractor" >> research_buffer.xml
python3 artemis_physics.py
cat artemis_real_output.json
echo "---"

echo "✅ ALL 5 REAL PHYSICS TESTS COMPLETE"
echo "Results saved to artemis_real_output.json each run"
