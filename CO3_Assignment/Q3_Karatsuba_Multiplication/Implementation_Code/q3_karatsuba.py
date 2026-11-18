"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 3: KARATSUBA MULTIPLICATION (DIVIDE AND CONQUER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import time
import random

class KaratsubaStats:
    def __init__(self):
        self.mult_count = 0
        self.add_count = 0
        self.max_depth = 0

def naive_multiply_digit_by_digit(x, y):
    """
    Simulates grade-school O(n^2) digit multiplication.
    Tracks scalar single-digit multiplications and additions.
    """
    sx = str(abs(x))
    sy = str(abs(y))
    len_x, len_y = len(sx), len(sy)
    
    mult_count = len_x * len_y
    add_count = len_x * len_y + (len_x + len_y)
    
    # Python native big-int multiplication for actual product
    prod = x * y
    return prod, mult_count, add_count


def karatsuba_recursive(x, y, stats, depth=0):
    if depth > stats.max_depth:
        stats.max_depth = depth
        
    # Base case: small numbers (<= 1 digit)
    if x < 10 or y < 10:
        stats.mult_count += 1
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m
    
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    
    # 3 recursive multiplications instead of 4!
    ac = karatsuba_recursive(a, c, stats, depth + 1)
    bd = karatsuba_recursive(b, d, stats, depth + 1)
    
    stats.add_count += 2
    sum_a_b = a + b
    sum_c_d = c + d
    
    ad_plus_bc = karatsuba_recursive(sum_a_b, sum_c_d, stats, depth + 1) - ac - bd
    stats.add_count += 2  # Subtractions
    
    stats.add_count += 2  # Polynomial reconstruction additions
    product = ac * (p * p) + ad_plus_bc * p + bd
    return product


def karatsuba(x, y):
    stats = KaratsubaStats()
    prod = karatsuba_recursive(x, y, stats, depth=0)
    return prod, stats.mult_count, stats.add_count, stats.max_depth


def hybrid_karatsuba_recursive(x, y, threshold=32):
    """
    Practical Hybrid Karatsuba: falls back to native/naive multiplication
    when number of digits falls below threshold.
    """
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    if n <= threshold:
        return x * y
        
    m = n // 2
    p = 10 ** m
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    
    ac = hybrid_karatsuba_recursive(a, c, threshold)
    bd = hybrid_karatsuba_recursive(b, d, threshold)
    ad_bc = hybrid_karatsuba_recursive(a + b, c + d, threshold) - ac - bd
    return ac * (p * p) + ad_bc * p + bd


def run_q3_demo():
    print("=" * 80)
    print("QUESTION 3: KARATSUBA MULTIPLICATION (DIVIDE AND CONQUER)")
    print("=" * 80)
    
    # 1. Sample Verification
    x, y = 1234, 5678
    print(f"\n--- 1. Verification on Sample Problem ---")
    print(f"Inputs: x = {x}, y = {y}")
    prod_naive, n_mult, n_add = naive_multiply_digit_by_digit(x, y)
    prod_karat, k_mult, k_add, k_depth = karatsuba(x, y)
    
    print(f"Naive Product    : {prod_naive} (Multiplications: {n_mult}, Additions: {n_add})")
    print(f"Karatsuba Product: {prod_karat} (Multiplications: {k_mult}, Additions: {k_add}, Depth: {k_depth})")
    print(f"Mathematical Verification: {x} * {y} = {x * y} -> {'MATCH' if prod_karat == x * y else 'ERROR'}")
    
    # 2. Asymptotic Operations Benchmark across Digit Lengths
    print(f"\n--- 2. Multiplication Operation Count Comparison Across Digit Counts (n) ---")
    print(f"{'Digits (n)':<12} | {'Naive Mults (n^2)':<18} | {'Karatsuba Mults (n^1.585)':<25} | {'Mult Reduction':<15}")
    print("-" * 75)
    
    digit_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    op_results = []
    for d in digit_sizes:
        num1 = int("".join([str(random.randint(1, 9)) for _ in range(d)]))
        num2 = int("".join([str(random.randint(1, 9)) for _ in range(d)]))
        
        _, n_m, _ = naive_multiply_digit_by_digit(num1, num2)
        _, k_m, _, _ = karatsuba(num1, num2)
        
        reduction = ((n_m - k_m) / n_m) * 100.0 if n_m > 0 else 0
        print(f"{d:<12} | {n_m:<18} | {k_m:<25} | {reduction:6.2f}%")
        op_results.append({'digits': d, 'naive_mult': n_m, 'karatsuba_mult': k_m, 'reduction': reduction})
        
    # 3. Practical Runtime Benchmark (Finding Crossover Threshold)
    print(f"\n--- 3. Wall-Clock Execution Time & Crossover Analysis ---")
    print(f"{'Digits (n)':<12} | {'Pure Karatsuba(ms)':<20} | {'Hybrid (th=32)(ms)':<20} | {'Python Native (ms)':<20}")
    print("-" * 76)
    
    run_sizes = [16, 64, 256, 512, 1024, 2048]
    for d in run_sizes:
        num1 = int("".join([str(random.randint(1, 9)) for _ in range(d)]))
        num2 = int("".join([str(random.randint(1, 9)) for _ in range(d)]))
        
        # Pure Karatsuba
        t0 = time.perf_counter()
        _ = karatsuba(num1, num2)
        t_pure = (time.perf_counter() - t0) * 1000.0
        
        # Hybrid Karatsuba
        t0 = time.perf_counter()
        _ = hybrid_karatsuba_recursive(num1, num2, threshold=32)
        t_hyb = (time.perf_counter() - t0) * 1000.0
        
        # Native
        t0 = time.perf_counter()
        _ = num1 * num2
        t_nat = (time.perf_counter() - t0) * 1000.0
        
        print(f"{d:<12} | {t_pure:16.4f} ms | {t_hyb:16.4f} ms | {t_nat:16.6f} ms")
        
    print("\n[SUCCESS] Q3 Implementation & Empirical Verification Complete.")
    return op_results

if __name__ == "__main__":
    run_q3_demo()
