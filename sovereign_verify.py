import math

def verify_artemis():
    # Verification for Test 1
    p = 354692711053
    q = 413208412897
    n = 146562011158572183883329
    
    print(f"Checking Factorization: {p} * {q}")
    if p * q == n:
        print("RESULT: SUCCESS. The factors are correct.")
    else:
        print("RESULT: FAIL. Multiplication does not match N.")

    # Verification for Test 3 (Entropy)
    p1, p2 = 0.64, 0.36
    entropy = -(p1 * math.log2(p1) + p2 * math.log2(p2))
    print(f"\nTarget Entropy Value: {entropy:.4f}")

if __name__ == "__main__":
    verify_artemis()
