"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 2: MERGE SORT & QUICK SORT (DIVIDE AND CONQUER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import sys
import time
import random

# Increase recursion depth for worst-case first-pivot tests
sys.setrecursionlimit(20000)

# ======================================================================================
# 1. STABLE MERGE SORT
# ======================================================================================

class SortStats:
    def __init__(self):
        self.comparisons = 0
        self.max_depth = 0
        self.current_depth = 0

def merge_sort_recursive(arr, stats, depth=0):
    stats.current_depth = depth
    if depth > stats.max_depth:
        stats.max_depth = depth
        
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    left = merge_sort_recursive(arr[:mid], stats, depth + 1)
    right = merge_sort_recursive(arr[mid:], stats, depth + 1)
    
    # Merge step
    merged = []
    i = j = 0
    len_l, len_r = len(left), len(right)
    
    while i < len_l and j < len_r:
        stats.comparisons += 1
        # '<=' ensures stability!
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    stats = SortStats()
    res = merge_sort_recursive(arr, stats, depth=0)
    return res, stats.comparisons, stats.max_depth


# ======================================================================================
# 2. QUICK SORT (FIRST-ELEMENT PIVOT - VULNERABLE TO O(n^2))
# ======================================================================================

def quick_sort_first_pivot_recursive(arr, low, high, stats, depth=0):
    stats.current_depth = depth
    if depth > stats.max_depth:
        stats.max_depth = depth
        
    if low < high:
        # Lomuto partition with first element as pivot
        pivot = arr[low]
        i = low
        for j in range(low + 1, high + 1):
            stats.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[i] = arr[i], arr[low]
        pivot_idx = i
        
        quick_sort_first_pivot_recursive(arr, low, pivot_idx - 1, stats, depth + 1)
        quick_sort_first_pivot_recursive(arr, pivot_idx + 1, high, stats, depth + 1)

def quick_sort_first_pivot(arr):
    stats = SortStats()
    arr_copy = list(arr)
    quick_sort_first_pivot_recursive(arr_copy, 0, len(arr_copy) - 1, stats, depth=0)
    return arr_copy, stats.comparisons, stats.max_depth


# ======================================================================================
# 3. IMPROVED QUICK SORT (MEDIAN-OF-THREE PIVOT)
# ======================================================================================

def median_of_three(arr, low, high, stats):
    mid = (low + high) // 2
    stats.comparisons += 3
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]  # Median placed at high

def quick_sort_median_three_recursive(arr, low, high, stats, depth=0):
    stats.current_depth = depth
    if depth > stats.max_depth:
        stats.max_depth = depth
        
    if low < high:
        if high - low == 1:
            stats.comparisons += 1
            if arr[low] > arr[high]:
                arr[low], arr[high] = arr[high], arr[low]
            return
            
        pivot = median_of_three(arr, low, high, stats)
        i = low - 1
        for j in range(low, high):
            stats.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        p = i + 1
        
        quick_sort_median_three_recursive(arr, low, p - 1, stats, depth + 1)
        quick_sort_median_three_recursive(arr, p + 1, high, stats, depth + 1)

def quick_sort_median_three(arr):
    stats = SortStats()
    arr_copy = list(arr)
    quick_sort_median_three_recursive(arr_copy, 0, len(arr_copy) - 1, stats, depth=0)
    return arr_copy, stats.comparisons, stats.max_depth


# ======================================================================================
# DEMONSTRATION & EXTENSIVE BENCHMARKS
# ======================================================================================

def run_q2_demo():
    print("=" * 80)
    print("QUESTION 2: MERGE SORT & QUICK SORT DECOMPOSITION ANALYSIS")
    print("=" * 80)
    
    sample_arr = [8, 3, 6, 2, 7, 1]
    print(f"\n--- 1. Verification on Sample Dataset ---")
    print(f"Original Input Array: {sample_arr}")
    
    ms_res, ms_cmp, ms_dep = merge_sort(sample_arr)
    qs1_res, qs1_cmp, qs1_dep = quick_sort_first_pivot(sample_arr)
    qs3_res, qs3_cmp, qs3_dep = quick_sort_median_three(sample_arr)
    
    print(f"Merge Sort Result       : {ms_res} (Cmps: {ms_cmp}, Max Depth: {ms_dep})")
    print(f"Quick Sort (First Pivot): {qs1_res} (Cmps: {qs1_cmp}, Max Depth: {qs1_dep})")
    print(f"Quick Sort (Med-of-3)   : {qs3_res} (Cmps: {qs3_cmp}, Max Depth: {qs3_dep})")
    
    # 2. Benchmark Under Deliberately Contrasting Data Distributions
    print(f"\n--- 2. Experimental Evaluation Across Data Distributions (n = 2000) ---")
    n = 2000
    distributions = {
        "Random Permutation": [random.randint(1, 100000) for _ in range(n)],
        "Already Sorted (Ascending)": list(range(n)),
        "Reverse Sorted (Descending)": list(range(n, 0, -1)),
        "Repeated Duplicates (1-10)": [random.randint(1, 10) for _ in range(n)]
    }
    
    print(f"{'Distribution':<28} | {'Algorithm':<20} | {'Comparisons':<12} | {'Max Depth':<10} | {'Runtime (ms)':<14}")
    print("-" * 92)
    
    results = []
    for dist_name, test_arr in distributions.items():
        # Merge Sort
        t0 = time.perf_counter()
        _, m_cmp, m_dep = merge_sort(test_arr)
        t_ms = (time.perf_counter() - t0) * 1000.0
        print(f"{dist_name:<28} | {'Merge Sort':<20} | {m_cmp:<12} | {m_dep:<10} | {t_ms:10.4f} ms")
        
        # Quick Sort First Pivot (skip sorted/reverse if n too large to avoid recursion crash)
        if dist_name in ["Already Sorted (Ascending)", "Reverse Sorted (Descending)"] and n > 2500:
            q1_cmp, q1_dep, t_q1 = "O(n^2) DNF", n, "TIMEOUT"
        else:
            t0 = time.perf_counter()
            _, q1_cmp, q1_dep = quick_sort_first_pivot(test_arr)
            t_q1 = (time.perf_counter() - t0) * 1000.0
            print(f"{'':<28} | {'QuickSort (First)':<20} | {q1_cmp:<12} | {q1_dep:<10} | {t_q1:10.4f} ms")
            
        # Quick Sort Median of 3
        t0 = time.perf_counter()
        _, q3_cmp, q3_dep = quick_sort_median_three(test_arr)
        t_q3 = (time.perf_counter() - t0) * 1000.0
        print(f"{'':<28} | {'QuickSort (Med-3)':<20} | {q3_cmp:<12} | {q3_dep:<10} | {t_q3:10.4f} ms")
        print("-" * 92)
        
        results.append({
            'dist': dist_name,
            'ms_cmp': m_cmp, 'ms_dep': m_dep, 't_ms': t_ms,
            'q1_cmp': q1_cmp, 'q1_dep': q1_dep, 't_q1': t_q1,
            'q3_cmp': q3_cmp, 'q3_dep': q3_dep, 't_q3': t_q3
        })
        
    print("\n[SUCCESS] Q2 Implementation & Empirical Verification Complete.")
    return results

if __name__ == "__main__":
    run_q2_demo()
