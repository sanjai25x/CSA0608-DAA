"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 4: STRASSEN MATRIX MULTIPLICATION (DIVIDE AND CONQUER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import time
import random

class MatrixStats:
    def __init__(self):
        self.scalar_mults = 0
        self.scalar_adds = 0

def matrix_add(A, B, stats=None):
    n = len(A)
    m = len(A[0])
    if stats:
        stats.scalar_adds += n * m
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def matrix_sub(A, B, stats=None):
    n = len(A)
    m = len(A[0])
    if stats:
        stats.scalar_adds += n * m
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]

def conventional_matrix_mult(A, B, stats=None):
    n = len(A)
    p = len(B)
    m = len(B[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            for j in range(m):
                if stats:
                    stats.scalar_mults += 1
                    stats.scalar_adds += 1
                C[i][j] += A[i][k] * B[k][j]
    return C

def split_matrix(A):
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def merge_matrix(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom

def strassen_recursive(A, B, threshold=2, stats=None):
    n = len(A)
    if n <= threshold:
        return conventional_matrix_mult(A, B, stats)
    
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    # Strassen's 7 products
    M1 = strassen_recursive(matrix_add(A11, A22, stats), matrix_add(B11, B22, stats), threshold, stats)
    M2 = strassen_recursive(matrix_add(A21, A22, stats), B11, threshold, stats)
    M3 = strassen_recursive(A11, matrix_sub(B12, B22, stats), threshold, stats)
    M4 = strassen_recursive(A22, matrix_sub(B21, B11, stats), threshold, stats)
    M5 = strassen_recursive(matrix_add(A11, A12, stats), B22, threshold, stats)
    M6 = strassen_recursive(matrix_sub(A21, A11, stats), matrix_add(B11, B12, stats), threshold, stats)
    M7 = strassen_recursive(matrix_sub(A12, A22, stats), matrix_add(B21, B22, stats), threshold, stats)
    
    # Quadrant reconstruction
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4, stats), M5, stats), M7, stats)
    C12 = matrix_add(M3, M5, stats)
    C21 = matrix_add(M2, M4, stats)
    C22 = matrix_add(matrix_add(matrix_sub(M1, M2, stats), M3, stats), M6, stats)
    
    return merge_matrix(C11, C12, C21, C22)

def pad_matrix_power_of_two(A):
    n = len(A)
    m = len(A[0])
    target = 1
    while target < max(n, m):
        target *= 2
    padded = [[0] * target for _ in range(target)]
    for i in range(n):
        for j in range(m):
            padded[i][j] = A[i][j]
    return padded, n, m

def unpad_matrix(A, n, m):
    return [row[:m] for row in A[:n]]

def strassen_multiply(A, B, threshold=2):
    n = len(A)
    m = len(B[0])
    # Pad to power of 2 if necessary
    is_pow2 = (n & (n - 1) == 0) and (n == len(B)) and (n == len(B[0]))
    stats = MatrixStats()
    if is_pow2:
        res = strassen_recursive(A, B, threshold, stats)
        return res, stats.scalar_mults, stats.scalar_adds
    else:
        padded_A, rA, cA = pad_matrix_power_of_two(A)
        padded_B, rB, cB = pad_matrix_power_of_two(B)
        res_padded = strassen_recursive(padded_A, padded_B, threshold, stats)
        res = unpad_matrix(res_padded, rA, cB)
        return res, stats.scalar_mults, stats.scalar_adds

def run_q4_demo():
    print("=" * 80)
    print("QUESTION 4: STRASSEN MATRIX MULTIPLICATION (DIVIDE AND CONQUER)")
    print("=" * 80)
    
    # 1. Sample 1: Assignment PDF Sample
    A1 = [[1, 2], [3, 4]]
    B1 = [[5, 6], [7, 8]]
    print(f"\n--- 1. Verification on Course Sample 1 (2x2) ---")
    print(f"Matrix A: {A1}")
    print(f"Matrix B: {B1}")
    C1_conv = conventional_matrix_mult(A1, B1)
    C1_stras, m_cnt, a_cnt = strassen_multiply(A1, B1, threshold=1)
    print(f"Conventional Multiplication Result: {C1_conv}")
    print(f"Strassen Multiplication Result   : {C1_stras}")
    print(f"Verification: {'MATCH' if C1_conv == C1_stras else 'ERROR'}")
    
    # 2. Sample 2: Case Study Sample (KartIQ 2x2)
    A2 = [[1, 7], [3, 5]]
    B2 = [[1, 3], [7, 5]]
    print(f"\n--- 2. Verification on KartIQ Case Study Sample (2x2) ---")
    print(f"Matrix A: {A2}")
    print(f"Matrix B: {B2}")
    C2_conv = conventional_matrix_mult(A2, B2)
    C2_stras, _, _ = strassen_multiply(A2, B2, threshold=1)
    print(f"Conventional: {C2_conv}")
    print(f"Strassen    : {C2_stras} (Expected: [[50, 38], [38, 34]])")
    
    # 3. Asymptotic Operation Comparison Table (n = 2 to n = 1024)
    print(f"\n--- 3. Theoretical Operation Count Comparison (Conventional vs Strassen) ---")
    print(f"{'Dimension (n)':<15} | {'Conventional (n^3)':<22} | {'Strassen (7^k)':<20} | {'Mult Reduction':<15}")
    print("-" * 76)
    for k in range(1, 11):
        dim = 2 ** k
        conv_mult = dim ** 3
        stras_mult = 7 ** k
        reduc = ((conv_mult - stras_mult) / conv_mult) * 100.0
        print(f"{dim:<15} | {conv_mult:<22} | {stras_mult:<20} | {reduc:6.2f}%")
        
    # 4. Empirical Wall-Clock Benchmarks on Power-of-Two Matrices
    print(f"\n--- 4. Empirical Benchmark: Conventional vs Pure Strassen vs Hybrid Strassen ---")
    print(f"{'Dimension (n)':<15} | {'Conventional (ms)':<20} | {'Pure Strassen (ms)':<20} | {'Hybrid (th=16)(ms)':<20}")
    print("-" * 78)
    
    bench_dims = [4, 8, 16, 32, 64]
    results = []
    for d in bench_dims:
        mat_a = [[random.randint(1, 10) for _ in range(d)] for _ in range(d)]
        mat_b = [[random.randint(1, 10) for _ in range(d)] for _ in range(d)]
        
        # Conventional
        t0 = time.perf_counter()
        _ = conventional_matrix_mult(mat_a, mat_b)
        t_conv = (time.perf_counter() - t0) * 1000.0
        
        # Pure Strassen (threshold = 2)
        t0 = time.perf_counter()
        _ = strassen_multiply(mat_a, mat_b, threshold=2)
        t_pure = (time.perf_counter() - t0) * 1000.0
        
        # Hybrid Strassen (threshold = 16)
        t0 = time.perf_counter()
        _ = strassen_multiply(mat_a, mat_b, threshold=16)
        t_hyb = (time.perf_counter() - t0) * 1000.0
        
        print(f"{d:<15} | {t_conv:16.4f} ms | {t_pure:16.4f} ms | {t_hyb:16.4f} ms")
        results.append({'dim': d, 't_conv': t_conv, 't_pure': t_pure, 't_hyb': t_hyb})
        
    print("\n[SUCCESS] Q4 Implementation & Empirical Verification Complete.")
    return results

if __name__ == "__main__":
    run_q4_demo()
