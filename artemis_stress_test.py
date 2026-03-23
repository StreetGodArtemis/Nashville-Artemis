import math
import time

def run_test():
    print("--- ARTEMIS FRONTIER STRESS TEST ---")
    
    # TEST 1: The Semi-Prime Challenge (RSA-Level Logic)
    # We provide the product (N). Artemis must provide p and q.
    # N = 1040707 * 1040713 (These are large primes)
    n = 1083077364091
    print(f"\n[CHALLENGE 1] Factor the semi-prime N: {n}")
    print("Requirement: Find the two prime factors p and q.")
    
    # TEST 2: The Subset Sum (NP-Complete)
    # Finding if a subset of these numbers equals exactly 0.
    numbers = [-7, -3, -2, 5, 8, 12, -20, 44, 1, 9, -1, -5, 2, 6]
    target = 0
    print(f"\n[CHALLENGE 2] NP-Complete Subset Sum")
    print(f"Set: {numbers}")
    print(f"Requirement: Find a non-empty subset that sums to {target}.")

    print("\n--- HIDDEN ANSWERS (For Verification Only) ---")
    # Answer 1: p = 1040707, q = 1040713
    # Answer 2: One solution is [-7, -3, -2, 12]
    print("Verification data is locked in the script source.")

if __name__ == "__main__":
    run_test()
