"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 1: MAX-MIN AND BINARY SEARCH (DIVIDE AND CONQUER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import time
import random

# ======================================================================================
# PART 1: MAXIMUM AND MINIMUM FINDING
# ======================================================================================

class MaxMinStats:
    def __init__(self):
        self.comparisons = 0

def linear_max_min(arr):
    """
    Standard Naive Linear Max-Min
    Worst-case comparisons: 2n - 2 (or 2n - 3)
    """
    if not arr:
        return None, None, 0
    n = len(arr)
    comparisons = 0
    min_val = arr[0]
    max_val = arr[0]
    
    for i in range(1, n):
        comparisons += 1
        if arr[i] < min_val:
            min_val = arr[i]
        comparisons += 1
        if arr[i] > max_val:
            max_val = arr[i]
            
    return min_val, max_val, comparisons


def max_min_dc_recursive(arr, low, high, stats):
    """
    Divide and Conquer Max-Min (Tournament Method)
    Recurrence: T(n) = 2T(n/2) + 2 for n > 2
                T(2) = 1
                T(1) = 0
    Total comparisons = 3n/2 - 2 (for n being a power of 2)
    A 25% reduction over naive linear search!
    """
    # Base Case 1: Exactly 1 element
    if low == high:
        return arr[low], arr[low]
    
    # Base Case 2: Exactly 2 elements (1 comparison)
    if high == low + 1:
        stats.comparisons += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Divide step
    mid = (low + high) // 2
    
    # Conquer step
    min1, max1 = max_min_dc_recursive(arr, low, mid, stats)
    min2, max2 = max_min_dc_recursive(arr, mid + 1, high, stats)
    
    # Combine step: 2 comparisons
    stats.comparisons += 1
    final_min = min1 if min1 < min2 else min2
    
    stats.comparisons += 1
    final_max = max1 if max1 > max2 else max2
    
    return final_min, final_max


def max_min_divide_and_conquer(arr):
    """Wrapper for D&C Max-Min with statistics tracking"""
    if not arr:
        return None, None, 0
    stats = MaxMinStats()
    min_val, max_val = max_min_dc_recursive(arr, 0, len(arr) - 1, stats)
    return min_val, max_val, stats.comparisons


# ======================================================================================
# PART 2: BINARY SEARCH
# ======================================================================================

def standard_binary_search(arr, target):
    """
    Standard Iterative Binary Search
    Time Complexity: Theta(log n)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons


def lower_bound_binary_search(arr, target):
    """
    Modified Binary Search for First Occurrence (KartIQ lower-bound requirement)
    Handles duplicate keys deterministically in Theta(log n) time.
    """
    low = 0
    high = len(arr) - 1
    result = -1
    comparisons = 0
    trace = []
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        trace.append((low, high, mid, arr[mid]))
        if arr[mid] == target:
            result = mid
            # Continue searching the left subarray to find earlier occurrences
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return result, comparisons, trace


# ======================================================================================
# DEMONSTRATION & VERIFICATION HARNESS
# ======================================================================================

def run_q1_demo():
    print("=" * 75)
    print("QUESTION 1: DIVIDE AND CONQUER MAX-MIN & BINARY SEARCH")
    print("=" * 75)
    
    # 1. Max-Min Verification on Sample Data
    sample_a = [12, 5, 8, 20, 3, 15]
    print(f"\n--- 1. Max-Min Tournament Execution ---")
    print(f"Sample Input Array: {sample_a}")
    
    lin_min, lin_max, lin_cmp = linear_max_min(sample_a)
    dc_min, dc_max, dc_cmp = max_min_divide_and_conquer(sample_a)
    
    print(f"Linear Search   -> Min: {lin_min}, Max: {lin_max}, Comparisons: {lin_cmp}")
    print(f"D&C (Tournament)-> Min: {dc_min}, Max: {dc_max}, Comparisons: {dc_cmp}")
    print(f"Theoretical D&C Bound (3n/2 - 2): {1.5 * len(sample_a) - 2:.1f} comparisons")
    
    # 2. Binary Search Verification
    sorted_a = [2, 4, 6, 8, 10, 12]
    target = 8
    print(f"\n--- 2. Binary Search Execution ---")
    print(f"Sorted Array: {sorted_a}")
    print(f"Search Target: {target}")
    idx, bs_cmp = standard_binary_search(sorted_a, target)
    print(f"Target {target} found at Index: {idx} in {bs_cmp} comparisons.")
    
    # 3. Duplicate Handling (Lower-Bound First Occurrence)
    dup_orders = [101, 102, 102, 103, 105, 105, 105, 108]
    dup_target = 105
    print(f"\n--- 3. Lower-Bound Binary Search (Duplicate Timestamps) ---")
    print(f"Order Timestamps: {dup_orders}")
    print(f"Target Timestamp: {dup_target}")
    first_idx, dup_cmp, trace = lower_bound_binary_search(dup_orders, dup_target)
    print(f"First Occurrence Index: {first_idx} (Value: {dup_orders[first_idx]})")
    print(f"Search Trace (low, high, mid, val): {trace}")
    
    # 4. Comparative Benchmark Across Input Sizes
    print(f"\n--- 4. Benchmarking Max-Min: Naive vs Divide-and-Conquer ---")
    sizes = [16, 64, 256, 1024, 4096, 16384, 65536]
    print(f"{'Input Size (n)':<15} | {'Linear Cmps':<14} | {'D&C Cmps':<14} | {'Savings (%)':<12} | {'Linear Time(ms)':<16} | {'D&C Time(ms)':<14}")
    print("-" * 95)
    
    benchmark_results = []
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
        # Linear
        t0 = time.perf_counter()
        _, _, l_cmp = linear_max_min(arr)
        t_lin = (time.perf_counter() - t0) * 1000.0
        
        # D&C
        t0 = time.perf_counter()
        _, _, d_cmp = max_min_divide_and_conquer(arr)
        t_dc = (time.perf_counter() - t0) * 1000.0
        
        savings = ((l_cmp - d_cmp) / l_cmp) * 100.0
        print(f"{n:<15} | {l_cmp:<14} | {d_cmp:<14} | {savings:6.2f}%      | {t_lin:12.4f} ms   | {t_dc:10.4f} ms")
        benchmark_results.append({
            'n': n, 'l_cmp': l_cmp, 'd_cmp': d_cmp, 'savings': savings,
            't_lin': t_lin, 't_dc': t_dc
        })
        
    print("\n[SUCCESS] Q1 Implementation & Empirical Verification Complete.")
    return benchmark_results

if __name__ == "__main__":
    run_q1_demo()
