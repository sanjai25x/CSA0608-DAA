"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 6: ADVANCED DIVIDE AND CONQUER - MEET IN THE MIDDLE
STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import time
import bisect
import random

def brute_force_subset_sum(arr, target):
    """
    Exhaustive search evaluating all 2^n subsets.
    Time Complexity: Theta(2^n)
    """
    n = len(arr)
    # Generate all subset sums iteratively
    sums = {0}
    for x in arr:
        sums |= {s + x for s in list(sums)}
        if target in sums:
            return True, len(sums)
    return (target in sums), len(sums)

def meet_in_the_middle_subset_sum(arr, target):
    """
    Meet in the Middle Divide and Conquer:
    Divides array of size n into two halves of size n/2.
    Generates 2^(n/2) subset sums for each half.
    Sorts one half and uses binary search:
    Time Complexity: O(2^(n/2) * n)
    Space Complexity: O(2^(n/2))
    Exponential speedup from 2^n to 2^(n/2)!
    """
    n = len(arr)
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Generate subset sums of left half (2^(n/2))
    s1 = {0}
    for x in left:
        s1 |= {s + x for s in list(s1)}
        
    # Generate subset sums of right half (2^(n/2))
    s2 = {0}
    for x in right:
        s2 |= {s + x for s in list(s2)}
        
    # Sort right sums for binary search
    s2_sorted = sorted(s2)
    
    # Check if target - s1 exists in s2 via binary search
    for s in s1:
        needed = target - s
        idx = bisect.bisect_left(s2_sorted, needed)
        if idx < len(s2_sorted) and s2_sorted[idx] == needed:
            return True, len(s1), len(s2)
            
    return False, len(s1), len(s2)

def run_meet_in_the_middle_demo():
    print("=" * 75)
    print("SUBMODULE: MEET IN THE MIDDLE (SUBSET SUM PROBLEM)")
    print("=" * 75)
    
    sample_a = [3, 4, 7, 2, 9]
    target = 11
    print(f"Sample Input Array: {sample_a}")
    print(f"Target Sum: {target}")
    
    exists_bf, bf_subsets = brute_force_subset_sum(sample_a, target)
    exists_mim, len_s1, len_s2 = meet_in_the_middle_subset_sum(sample_a, target)
    
    print(f"Brute Force Result       : Exists = {exists_bf} (Subsets evaluated: {bf_subsets})")
    print(f"Meet-in-the-Middle Result: Exists = {exists_mim} (|S1|={len_s1}, |S2|={len_s2})")
    
    # Empirical Benchmark Showing 2^n vs 2^(n/2)
    print(f"\n--- Complexity Divergence: 2^n Brute Force vs 2^(n/2) Meet in the Middle ---")
    print(f"{'Array Size (n)':<15} | {'Naive Subsets (2^n)':<22} | {'MitM Subsets 2*(2^(n/2))':<25} | {'Speedup Factor':<15}")
    print("-" * 80)
    
    for n in [10, 14, 18, 22, 26, 30, 36, 40]:
        bf_states = 2 ** n
        mim_states = 2 * (2 ** (n // 2))
        speedup = bf_states / mim_states
        print(f"{n:<15} | {bf_states:<22,d} | {mim_states:<25,d} | {speedup:12,.1f}x")
        
    # Wall clock test
    print(f"\n--- Empirical Runtime Comparison ---")
    print(f"{'Array Size (n)':<15} | {'Target':<10} | {'Brute Force (ms)':<20} | {'Meet-in-the-Middle (ms)':<22}")
    print("-" * 72)
    
    for n in [10, 14, 18, 22, 24]:
        arr = [random.randint(1, 100) for _ in range(n)]
        tgt = sum(arr[:n//3])  # Guaranteed subset sum
        
        t0 = time.perf_counter()
        _ = brute_force_subset_sum(arr, tgt)
        t_bf = (time.perf_counter() - t0) * 1000.0
        
        t0 = time.perf_counter()
        _ = meet_in_the_middle_subset_sum(arr, tgt)
        t_mim = (time.perf_counter() - t0) * 1000.0
        
        print(f"{n:<15} | {tgt:<10} | {t_bf:16.4f} ms | {t_mim:16.4f} ms")

if __name__ == "__main__":
    run_meet_in_the_middle_demo()
