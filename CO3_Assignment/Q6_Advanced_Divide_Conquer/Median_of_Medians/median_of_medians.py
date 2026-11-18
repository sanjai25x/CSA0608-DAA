"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 6: ADVANCED DIVIDE AND CONQUER - MEDIAN OF MEDIANS (BFPRT)
STUDENT A: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import time
import random

class SelectionStats:
    def __init__(self):
        self.comparisons = 0
        self.max_depth = 0

def median_of_medians_select(arr, k, stats=None, depth=0):
    """
    Blum-Floyd-Pratt-Rivest-Tarjan (BFPRT) Algorithm
    Guarantees deterministic O(n) worst-case time complexity.
    Recurrence: T(n) <= T(n/5) + T(7n/10) + c*n
    Since 1/5 + 7/10 = 9/10 < 1, T(n) = O(n)!
    """
    if stats:
        if depth > stats.max_depth:
            stats.max_depth = depth
            
    n = len(arr)
    # Base case for small inputs
    if n <= 5:
        sorted_small = sorted(arr)
        if stats:
            stats.comparisons += n * (n - 1) // 2
        return sorted_small[k - 1]
    
    # Step 1: Divide array into blocks of 5 and find each block's median
    medians = []
    for i in range(0, n, 5):
        block = arr[i:i + 5]
        block.sort()
        if stats:
            stats.comparisons += len(block) * (len(block) - 1) // 2
        medians.append(block[len(block) // 2])
        
    # Step 2: Recursively determine the median of medians
    mom_pivot = median_of_medians_select(medians, (len(medians) + 1) // 2, stats, depth + 1)
    
    # Step 3: 3-way Partition around the chosen pivot
    left = []
    equal = []
    right = []
    for x in arr:
        if stats:
            stats.comparisons += 1
        if x < mom_pivot:
            left.append(x)
        elif x == mom_pivot:
            equal.append(x)
        else:
            right.append(x)
            
    # Step 4: Recurse into the subproblem containing the kth element
    len_left = len(left)
    len_equal = len(equal)
    
    if k <= len_left:
        return median_of_medians_select(left, k, stats, depth + 1)
    elif k <= len_left + len_equal:
        return mom_pivot
    else:
        return median_of_medians_select(right, k - len_left - len_equal, stats, depth + 1)

def quickselect_randomized(arr, k, stats=None):
    """Randomized Quickselect: Average O(n), Worst-case O(n^2)"""
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quickselect_randomized(left, k, stats)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return quickselect_randomized(right, k - len(left) - len(equal), stats)

def run_median_of_medians_demo():
    print("=" * 75)
    print("SUBMODULE: MEDIAN OF MEDIANS (DETERMINISTIC O(n) SELECTION)")
    print("=" * 75)
    
    sample_a = [7, 2, 9, 4, 1, 6, 3, 8, 5]
    k = 5
    print(f"Sample Input Array: {sample_a}")
    print(f"Finding {k}-th Smallest Element...")
    
    stats = SelectionStats()
    ans = median_of_medians_select(sample_a, k, stats)
    print(f"Result: {k}-th Smallest = {ans}")
    print(f"True Sorted Array: {sorted(sample_a)}")
    print(f"Comparisons: {stats.comparisons}, Max Recursion Depth: {stats.max_depth}")
    
    # Benchmark across sizes n
    print(f"\n--- Empirical Scaling of Median of Medians vs Randomized Selection ---")
    print(f"{'Input Size (n)':<15} | {'k Target':<12} | {'MoM Time (ms)':<16} | {'Rand Select(ms)':<16} | {'Built-in Sort(ms)':<18}")
    print("-" * 85)
    
    for n in [100, 1000, 5000, 20000, 50000]:
        test_arr = [random.randint(1, 1000000) for _ in range(n)]
        k_target = n // 2  # Find true median
        
        # MoM
        t0 = time.perf_counter()
        r1 = median_of_medians_select(test_arr, k_target)
        t_mom = (time.perf_counter() - t0) * 1000.0
        
        # Randomized
        t0 = time.perf_counter()
        r2 = quickselect_randomized(test_arr, k_target)
        t_rand = (time.perf_counter() - t0) * 1000.0
        
        # Builtin sort
        t0 = time.perf_counter()
        r3 = sorted(test_arr)[k_target - 1]
        t_sort = (time.perf_counter() - t0) * 1000.0
        
        assert r1 == r2 == r3, "Mismatch in results!"
        print(f"{n:<15} | {k_target:<12} | {t_mom:12.4f} ms | {t_rand:12.4f} ms | {t_sort:12.4f} ms")

if __name__ == "__main__":
    run_median_of_medians_demo()
