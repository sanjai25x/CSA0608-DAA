"""
Q2: When Is Sequential Search an Appropriate Engineering Choice?
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S (192511018)
Institution: SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences

Simulates Aircraft Maintenance Tool Tracking:
Record: (Tool ID, Technician ID, Issue Time, Work Bay)
Investigates:
1. Positional lookups for n = 200 tools
2. List size scaling from n = 10 to n = 3,000
3. Changed condition: 1 Hangar (n=150, q=400) -> 20 Facilities (n=3000, q=8000)
"""

import time
import random

def sequential_search_tools(tool_list, target_id):
    """
    Searches for target_id in tool_list.
    Returns (record, comparisons, time_sec).
    """
    comparisons = 0
    t0 = time.perf_counter_ns()
    for record in tool_list:
        comparisons += 1
        if record["tool_id"] == target_id:
            t1 = time.perf_counter_ns()
            return record, comparisons, (t1 - t0) / 1e9
    t1 = time.perf_counter_ns()
    return None, comparisons, (t1 - t0) / 1e9

def run_q2_experiments():
    print("================================================================================")
    print("       Q2: SEQUENTIAL SEARCH FOR AIRCRAFT MAINTENANCE TOOL TRACKING             ")
    print("       Author: Sanjai S (192511018) | SIMATS Engineering                         ")
    print("================================================================================")
    
    # 1. Positional Experiments (n = 200 tools)
    n = 200
    tool_list = [
        {"tool_id": f"T-{100 + i}", "tech_id": f"TECH-{1000 + i}", "time": "08:30", "bay": f"BAY-{i % 10 + 1}"}
        for i in range(n)
    ]
    
    test_positions = [
        ("Front (Index 0 - Best Case)", "T-100", 0),
        ("First Quarter (Index 49)", "T-149", 49),
        ("Middle (Index 99)", "T-199", 99),
        ("Third Quarter (Index 149)", "T-249", 149),
        ("Last (Index 199 - Worst Successful)", "T-299", 199),
        ("Absent Tool (Unsuccessful)", "T-9999", -1)
    ]
    
    print(f"\n---> Part 1: Positional Search Experiments (List Size n = {n}):")
    print(f"{'Search Position':<38} | {'Target ID':<10} | {'Index':<6} | {'Comparisons':<11} | {'Fraction of n'}")
    print("-" * 80)
    for desc, tid, expected_idx in test_positions:
        rec, comps, t_sec = sequential_search_tools(tool_list, tid)
        idx = tool_list.index(rec) if rec else -1
        assert idx == expected_idx
        frac = comps / n
        print(f"{desc:<38} | {tid:<10} | {idx:<6} | {comps:<11} | {frac:.3f}")
        
    # 2. List-size Scaling Experiments
    print(f"\n---> Part 2: List-Size Scaling Experiments:")
    print(f"{'Active Tools (n)':<18} | {'Best Case':<12} | {'Avg Successful':<15} | {'Worst / Absent'}")
    print("-" * 65)
    for size in [10, 50, 100, 200, 500, 1000, 3000]:
        t_arr = [{"tool_id": f"T-{i}"} for i in range(size)]
        _, best_c, _ = sequential_search_tools(t_arr, "T-0")
        _, worst_c, _ = sequential_search_tools(t_arr, f"T-{size-1}")
        avg_c = (size + 1) / 2
        print(f"{size:<18} | {best_c:<12} | {avg_c:<15.1f} | {worst_c}")

    # 3. Changed Condition Simulation: 1 Hangar vs 20 Maintenance Facilities
    print(f"\n---> Part 3: Changed Condition Re-Evaluation (1 Hangar vs 20 Facilities):")
    # Single Hangar: n=150, q=400 lookups/day, 20% miss rate
    q1 = 400
    n1 = 150
    miss_rate = 0.20
    avg_comps_single = (1 - miss_rate) * ((n1 + 1) / 2) + miss_rate * n1
    total_comps_single = q1 * avg_comps_single
    
    # 20 Facilities: n=3000, q=8000 lookups/day, 20% miss rate
    q2 = 8000
    n2 = 3000
    avg_comps_20 = (1 - miss_rate) * ((n2 + 1) / 2) + miss_rate * n2
    total_comps_20 = q2 * avg_comps_20
    surge = total_comps_20 / total_comps_single

    print(f"  Single Hangar (n={n1}, q={q1}/day):")
    print(f"    Avg Comps/Query = {avg_comps_single:.2f} | Total Daily Comparisons = {total_comps_single:,.0f}")
    print(f"  20 Facilities (n={n2}, q={q2}/day):")
    print(f"    Avg Comps/Query = {avg_comps_20:.2f} | Total Daily Comparisons = {total_comps_20:,.0f}")
    print(f"  Workload Surge Ratio: {surge:.2f}x (~400x increase!)")
    print("  [RECOMMENDATION] Discontinue Sequential Search; deploy Hash Table keyed by Tool ID for O(1) lookups.")

if __name__ == "__main__":
    run_q2_experiments()
