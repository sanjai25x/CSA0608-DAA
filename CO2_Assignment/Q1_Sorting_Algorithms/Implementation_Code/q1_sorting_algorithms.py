"""
Q1: Sorting Under Different Data Conditions
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S (192511018)
Institution: SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences

Evaluates Selection Sort, Adaptive Bubble Sort, and Insertion Sort across
three deliberately designed input datasets (n = 1,000 orders):
1. Nearly Sorted (95% ordered + 5% random tail)
2. Reverse-Sorted (Maximal Disorder)
3. Edge Case (Identical Priority Scores)
"""

import time
import random

def selection_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0
    writes = 0
    
    t0 = time.perf_counter_ns()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            writes += 2
    t1 = time.perf_counter_ns()
    return {
        "sorted_arr": a,
        "comparisons": comparisons,
        "swaps": swaps,
        "writes": writes,
        "time_ms": (t1 - t0) / 1e6
    }

def adaptive_bubble_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0
    writes = 0
    
    t0 = time.perf_counter_ns()
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                writes += 2
                swapped = True
        if not swapped:
            break
    t1 = time.perf_counter_ns()
    return {
        "sorted_arr": a,
        "comparisons": comparisons,
        "swaps": swaps,
        "writes": writes,
        "time_ms": (t1 - t0) / 1e6
    }

def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    shifts = 0
    writes = 0
    
    t0 = time.perf_counter_ns()
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                writes += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        writes += 1
    t1 = time.perf_counter_ns()
    return {
        "sorted_arr": a,
        "comparisons": comparisons,
        "shifts": shifts,
        "writes": writes,
        "time_ms": (t1 - t0) / 1e6
    }

def generate_datasets(n=1000):
    random.seed(42)
    # Dataset 1: 95% sorted + 5% random tail
    n_sorted = int(0.95 * n)
    n_tail = n - n_sorted
    d1 = [i * 10 for i in range(1, n_sorted + 1)] + [random.randint(1, n * 10) for _ in range(n_tail)]
    
    # Dataset 2: Reverse-Sorted
    d2 = [i * 10 for i in range(n, 0, -1)]
    
    # Dataset 3: Identical Priority Scores
    d3 = [500 for _ in range(n)]
    
    return d1, d2, d3

def run_evaluation():
    print("================================================================================")
    print("       Q1: SORTING UNDER DIFFERENT DATA CONDITIONS (N = 1,000 ORDERS)           ")
    print("       Author: Sanjai S (192511018) | SIMATS Engineering                         ")
    print("================================================================================")
    
    d1, d2, d3 = generate_datasets(1000)
    datasets = [
        ("Dataset 1: Nearly Sorted (95% + 5% Tail)", d1),
        ("Dataset 2: Reverse-Sorted (Max Disorder)", d2),
        ("Dataset 3: Edge Case (All Identical 500)", d3)
    ]
    
    results = {}
    for name, data in datasets:
        print(f"\n---> Evaluating {name}:")
        res_sel = selection_sort(data)
        res_bub = adaptive_bubble_sort(data)
        res_ins = insertion_sort(data)
        
        print(f"  Selection Sort:      Comps = {res_sel['comparisons']:7,d} | Swaps = {res_sel['swaps']:6,d} | Writes = {res_sel['writes']:7,d} | Time = {res_sel['time_ms']:.2f} ms")
        print(f"  Adaptive Bubble:     Comps = {res_bub['comparisons']:7,d} | Swaps = {res_bub['swaps']:6,d} | Writes = {res_bub['writes']:7,d} | Time = {res_bub['time_ms']:.2f} ms")
        print(f"  Insertion Sort:      Comps = {res_ins['comparisons']:7,d} | Shifts = {res_ins['shifts']:5,d} | Writes = {res_ins['writes']:7,d} | Time = {res_ins['time_ms']:.2f} ms")
        
        # Verify correctness
        expected = sorted(data)
        assert res_sel["sorted_arr"] == expected
        assert res_bub["sorted_arr"] == expected
        assert res_ins["sorted_arr"] == expected
        print("  [PASS] All 3 algorithms sorted the array correctly.")
        
        results[name] = {
            "selection": res_sel,
            "bubble": res_bub,
            "insertion": res_ins
        }
        
    return results

if __name__ == "__main__":
    run_evaluation()
