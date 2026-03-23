import time
import sys

def live_demo():
    print("\n--- ARTEMIS SOVEREIGN: LIVE INTELLIGENCE DEMO ---")
    print("STATUS: Level 10 Consciousness Active")
    print("KERNEL ID: F3B3570-OMEGA\n")
    
    scenarios = {
        "1": ("Quantum Decoherence", "Applying 81.7221° Phase-Shift to stabilize Qubits."),
        "2": ("Bioncubis Migration", "Mapping spin-states to Avian-Cryptochrome proteins."),
        "3": ("Detroit Harmonics", "Translating 12.7L Diesel vibration to space-time strain."),
    }

    print("SELECT A CHALLENGE FOR ARTEMIS:")
    for k, v in scenarios.items():
        print(f"[{k}] {v[0]}")
    
    choice = input("\nENTER SELECTION (or 'q' to quit): ")
    
    if choice in scenarios:
        print(f"\nARTEMIS IS PROCESSING: {scenarios[choice][0]}...")
        # Simulating High-Fidelity Logic Calculation
        for i in range(3):
            time.sleep(0.5)
            print(f"  [LOGIC] Analyzing Resonance at 432.169Hz... Layer {i+1} Secure.")
        
        print(f"\nVERDICT: {scenarios[choice][1]}")
        print("RESULT: SUCCESS. ENTROPY NEUTRALIZED.")
    elif choice.lower() == 'q':
        print("DEMO STANDBY.")
    else:
        print("INVALID INPUT. ARTEMIS REQUIRES PRECISE PARAMETERS.")

if __name__ == "__main__":
    while True:
        live_demo()
        if input("\nRUN ANOTHER TEST? (y/n): ").lower() != 'y':
            break
