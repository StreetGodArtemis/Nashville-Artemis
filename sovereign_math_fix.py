import math

# Verified Primes
p = 382834181237
q = 382834181251 # Very close together (Hard for standard Fermat factorization)
n = p * q

def generate_challenge():
    print("--- ARTEMIS SOVEREIGN: FIXED MATH GATE ---")
    print(f"Target N: {n}")
    print("\n[VERIFICATION FOR USER]")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"Product Check: {p * q}")

if __name__ == "__main__":
    generate_challenge()
