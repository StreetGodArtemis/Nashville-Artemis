import time
import math

def benchmark():
    n = 146562010328763841387487
    start = time.time()
    
    # Fermat Factorization (Optimized for close primes)
    a = math.isqrt(n) + 1
    b2 = a*a - n
    while not math.isqrt(b2)**2 == b2:
        a += 1
        b2 = a*a - n
    
    p = a - math.isqrt(b2)
    q = a + math.isqrt(b2)
    
    end = time.time()
    print(f"Classical Benchmark: {p} * {q}")
    print(f"Time Taken: {end - start:.6f} seconds")

if __name__ == "__main__":
    benchmark()
