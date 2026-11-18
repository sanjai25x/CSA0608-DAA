"""
Unified Benchmark Suite for University Student Record System
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018

Tests datasets of size 1,000, 10,000, 100,000, and 1,000,000.
Records comparisons, execution times, preprocessing overhead,
and simulates Day-4 Design Challenge workloads.
"""

import time
import random
import json
import os
import sys

# Ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linear_search import linear_search
from iterative_binary_search import iterative_binary_search
from recursive_binary_search import recursive_binary_search

def run_single_worst_case_test(arr, key):
    """
    Runs search for key (located at last position arr[-1])
    Measures execution time using high-resolution time.perf_counter_ns().
    """
    # 1. Linear Search
    t0 = time.perf_counter_ns()
    idx_lin, comps_lin = linear_search(arr, key)
    t1 = time.perf_counter_ns()
    time_lin_sec = (t1 - t0) / 1e9

    # 2. Iterative Binary Search
    t0 = time.perf_counter_ns()
    idx_it, comps_it = iterative_binary_search(arr, key)
    t1 = time.perf_counter_ns()
    time_it_sec = (t1 - t0) / 1e9

    # 3. Recursive Binary Search
    # Note: For n=1,000,000 recursion depth is at most ~20, well below sys.getrecursionlimit() (typically 1000)
    t0 = time.perf_counter_ns()
    idx_rec, comps_rec = recursive_binary_search(arr, key)
    t1 = time.perf_counter_ns()
    time_rec_sec = (t1 - t0) / 1e9

    return {
        "linear": {"comps": comps_lin, "time_sec": time_lin_sec, "found_idx": idx_lin},
        "iterative_binary": {"comps": comps_it, "time_sec": time_it_sec, "found_idx": idx_it},
        "recursive_binary": {"comps": comps_rec, "time_sec": time_rec_sec, "found_idx": idx_rec}
    }

def benchmark_suite():
    print("================================================================================")
    print("       CSA0608 DAA - EXPERIMENTAL BENCHMARKING (STUDENT RECORD RETRIEVAL)       ")
    print("       Author: Sanjai S (192511018) | Saveetha SIMATS Engineering               ")
    print("================================================================================")

    sizes = [1000, 10000, 100000, 1000000]
    results = {}

    for n in sizes:
        print(f"\n---> Testing Dataset Size N = {n:,} records...")
        # Create dataset: sorted registration numbers 1 to N
        # (Equivalent to unique registration numbers e.g. 192511000 to ...)
        arr = list(range(1, n + 1))
        key = n  # Key at the last position (worst case for linear search)

        # Warm up
        _ = linear_search(arr[:100], 100)
        _ = iterative_binary_search(arr[:100], 100)
        _ = recursive_binary_search(arr[:100], 100)

        # Run several iterations and take the median/average for stable timing
        iters = 5 if n <= 100000 else 3
        runs = []
        for _ in range(iters):
            runs.append(run_single_worst_case_test(arr, key))

        # Average metrics
        avg_lin_time = sum(r["linear"]["time_sec"] for r in runs) / iters
        avg_it_time = sum(r["iterative_binary"]["time_sec"] for r in runs) / iters
        avg_rec_time = sum(r["recursive_binary"]["time_sec"] for r in runs) / iters

        comps_lin = runs[0]["linear"]["comps"]
        comps_it = runs[0]["iterative_binary"]["comps"]
        comps_rec = runs[0]["recursive_binary"]["comps"]

        # Measure Hash Table build and lookup
        t0 = time.perf_counter_ns()
        hash_map = {rec: f"Rec_{rec}" for rec in arr}
        t1 = time.perf_counter_ns()
        hash_build_sec = (t1 - t0) / 1e9

        t0 = time.perf_counter_ns()
        _ = hash_map.get(key)
        t1 = time.perf_counter_ns()
        hash_lookup_sec = (t1 - t0) / 1e9

        # Measure Sorting Preprocessing Time
        unsorted_arr = list(range(1, n + 1))
        random.seed(42)
        random.shuffle(unsorted_arr)
        t0 = time.perf_counter_ns()
        unsorted_arr.sort()
        t1 = time.perf_counter_ns()
        sort_time_sec = (t1 - t0) / 1e9

        results[str(n)] = {
            "n": n,
            "linear_comps": comps_lin,
            "linear_time_sec": avg_lin_time,
            "iterative_binary_comps": comps_it,
            "iterative_binary_time_sec": avg_it_time,
            "recursive_binary_comps": comps_rec,
            "recursive_binary_time_sec": avg_rec_time,
            "hash_lookup_time_sec": hash_lookup_sec,
            "hash_build_time_sec": hash_build_sec,
            "sort_time_sec": sort_time_sec
        }

        print(f"     Linear Search:           Comparisons = {comps_lin:10,d} | Time = {avg_lin_time:.8f} s")
        print(f"     Iterative Binary Search: Comparisons = {comps_it:10,d} | Time = {avg_it_time:.8f} s")
        print(f"     Recursive Binary Search: Comparisons = {comps_rec:10,d} | Time = {avg_rec_time:.8f} s")
        print(f"     Hash Table Lookup:       Comparisons =          1 | Time = {hash_lookup_sec:.8f} s (Build: {hash_build_sec:.4f} s)")
        print(f"     Array Sort Time:                                  | Time = {sort_time_sec:.4f} s")

    # Day-4 Challenge Workload Simulation:
    # 50,000 queries on 1,000,000 records
    print("\n================================================================================")
    print("       DAY-4 DESIGN CHALLENGE: 50,000 SEARCHES / HOUR ON 1,000,000 RECORDS      ")
    print("================================================================================")
    n_records = 1000000
    queries_per_hour = 50000
    
    # 1. Linear Search projection
    # Average case comparisons per search = (N + 1) / 2 = 500,000.5
    # Total comparisons per hour = 50,000 * 500,000 = 25,000,000,000
    # Worst case = 50,000,000,000 comparisons!
    lin_single_time = results["1000000"]["linear_time_sec"] # worst case
    # Average search time is approx half of worst case
    lin_hourly_time = queries_per_hour * (lin_single_time / 2.0)

    # 2. Iterative Binary Search projection
    # Comparisons per search = ceil(log2(1000000)) = 20
    # Total comparisons per hour = 50,000 * 20 = 1,000,000
    it_single_time = results["1000000"]["iterative_binary_time_sec"]
    it_hourly_time = queries_per_hour * it_single_time

    # 3. Hash Table projection
    # Comparisons per search = 1
    # Total comparisons per hour = 50,000 * 1 = 50,000
    hash_single_time = results["1000000"]["hash_lookup_time_sec"]
    hash_hourly_time = queries_per_hour * hash_single_time

    day4_simulation = {
        "dataset_size": n_records,
        "queries_per_hour": queries_per_hour,
        "linear_avg_comps_per_hour": queries_per_hour * (n_records / 2),
        "linear_worst_comps_per_hour": queries_per_hour * n_records,
        "linear_estimated_time_sec": lin_hourly_time,
        "binary_comps_per_hour": queries_per_hour * 20,
        "binary_estimated_time_sec": it_hourly_time,
        "hash_comps_per_hour": queries_per_hour * 1,
        "hash_estimated_time_sec": hash_hourly_time,
        "hash_build_time_sec": results["1000000"]["hash_build_time_sec"],
        "daily_update_batch_size": 1000,
        "daily_update_insertion_time_sec": 1000 * 1.5e-6 # O(1) per insert
    }

    print(f"Total Records: {n_records:,}")
    print(f"Hourly Queries: {queries_per_hour:,}")
    print(f"Linear Search Estimated Hourly Time:   {lin_hourly_time:.2f} seconds ({lin_hourly_time/60:.2f} mins) | Comps: {day4_simulation['linear_worst_comps_per_hour']:,}")
    print(f"Binary Search Estimated Hourly Time:   {it_hourly_time:.4f} seconds | Comps: {day4_simulation['binary_comps_per_hour']:,}")
    print(f"Hash Table Estimated Hourly Time:      {hash_hourly_time:.4f} seconds | Comps: {day4_simulation['hash_comps_per_hour']:,}")
    print(f"Hash Build Overhead (Once at start):   {results['1000000']['hash_build_time_sec']:.4f} seconds")
    print(f"Daily Update Overhead (1,000 records): {day4_simulation['daily_update_insertion_time_sec']*1000:.4f} ms")

    # Save output to JSON
    output_dir = os.path.dirname(os.path.abspath(__file__))
    data_to_save = {
        "benchmarks": results,
        "day4_challenge": day4_simulation
    }
    
    json_path = os.path.join(output_dir, "benchmark_results.json")
    with open(json_path, "w") as f:
        json.dump(data_to_save, f, indent=4)
    print(f"\n[+] Benchmark results successfully saved to: {json_path}")

    return data_to_save

if __name__ == "__main__":
    benchmark_suite()
