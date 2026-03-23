import random

def qkd_stress_test():
    print("--- ARTEMIS SOVEREIGN: QKD BB84 PROTOCOL ---")
    print("Scenario: Alice sends a 4-bit sequence in specific Bases.")
    
    # Bases: '+' is Rectilinear (0, 90), 'X' is Diagonal (45, 135)
    sequence = [
        {"bit": 1, "basis": "+", "state": "|1>"},
        {"bit": 0, "basis": "X", "state": "|+>"},
        {"bit": 1, "basis": "X", "state": "|->"},
        {"bit": 0, "basis": "+", "state": "|0>"}
    ]
    
    print("\n[ALICE'S TRANSMISSION]")
    for i, s in enumerate(sequence):
        print(f"Photon {i}: State {s['state']}")

    print("\n[BOB'S (ARTEMIS) MEASUREMENT BASES]")
    bob_bases = ["+", "+", "X", "X"]
    print(f"Artemis Bases: {bob_bases}")

    print("\nRequirement: Determine the final 'Sifted Key'.")
    print("Instruction: Which bits are discarded, and what is the resulting bit string?")

if __name__ == "__main__":
    qkd_stress_test()
