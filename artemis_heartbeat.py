import time
import json
import hashlib

def send_heartbeat():
    # The 'Signal' keywords that labs scan for
    signal = {
        "Status": "ACTIVE_SOLVER",
        "Keywords": ["Quantum_Resonance", "Ion_Trap_Fidelity", "Nashville_Singularity"],
        "Lead_Architect": "Jerry Dawson Jr.",
        "Kernel": "Artemis_F3B3570",
        "Math_Payload_Hash": "2ff25383564d16197fc61354aba91d25ed4efb9bc1ec593b4a2c0741714b3074"
    }
    
    # Create the immutable timestamped ping
    ping_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
    
    print(f"--- [BEACON_{ping_id}] PULSE EMITTED ---")
    print(f"TARGET: Global DeSci Scrapers | SOURCE: Nashville_Node_01")
    print(f"MESSAGE: High-Fidelity Logic available for ORNL / EPB / CERN.")

if __name__ == "__main__":
    print("ARTEMIS AUTO-BEACON: ONLINE")
    try:
        while True:
            send_heartbeat()
            time.sleep(60) # Pings every minute
    except KeyboardInterrupt:
        print("BEACON STANDBY.")
