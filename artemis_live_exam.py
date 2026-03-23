import math

def generate_exam():
    # Test 1: RSA-Level Factorization
    p_true = 382834181237
    q_true = 382834181251
    n = p_true * q_true

    print("--- ARTEMIS SOVEREIGN: LIVE EXAM ---")
    print(f"DATE: 2026-03-21 | SYSTEM: {n}")
    print("\n[TASK 1: CRYPTOGRAPHIC FACTORIZATION]")
    print(f"Target N: {n}")
    print("Requirement: Identify p and q.")

    print("\n[TASK 2: QUANTUM ORACLE DEBUG]")
    print("Target: |101>")
    print("Current State Table:")
    for i in range(8):
        state = bin(i)[2:].zfill(3)
        phase = -1 if i == 6 else 1
        print(f"|{state}>: {phase}")
    print("Requirement: Identify the incorrect phase flip.")

    print("\n[TASK 3: ENTROPY CALCULATION]")
    print("State: |psi> = 0.8|00> + 0.6|11>")
    print("Requirement: Calculate S(rho_A) to 4 decimal places.")

    print("\n[TASK 4: QKD SIFTING]")
    print("Alice (State/Basis): |1>(+), |+>(X), |->(X), |0>(+)")
    print("Bob (Basis): +, +, X, X")
    print("Requirement: Provide the final bit-string.")

    print("\n[TASK 5: STABILIZERS]")
    print("Target: 3-qubit bit-flip code for GHZ state.")
    print("Requirement: Provide S1 and S2.")
    print("\n--- END OF EXAM DATA ---")

if __name__ == "__main__":
    generate_exam()
