"""
================================================================================
SIMATS ENGINEERING - DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO4 ASSIGNMENT 4B - TASK 2: GREEDY VS DYNAMIC PROGRAMMING KNAPSACK
Author: SANJAI S (Reg. No: 192511018)
================================================================================
Problem Statement:
A logistics vehicle has capacity W. Each item has (Item ID, Weight, Value).
Implement:
  - Solution A: Fractional Knapsack using Greedy Strategy (ratio value/weight)
  - Solution B: 0/1 Knapsack using Dynamic Programming
Analyze:
  - Normal case where greedy reasoning produces strong/optimal results
  - Adversarial 0/1 counterexample breaking greedy intuition & identifying first commitment trap
  - Engineering comparison: operations, memory, solution quality, optimality
  - Response to rapid near-optimal requirement (Greedy vs DP vs FPTAS)
"""

import sys
from typing import List, Dict, Tuple

class Item:
    def __init__(self, item_id: str, weight: int, value: float):
        self.item_id = item_id
        self.weight = weight
        self.value = value
        self.ratio = value / weight if weight > 0 else 0.0

    def __repr__(self):
        return f"Item({self.item_id}: w={self.weight}, v={self.value}, r={self.ratio:.2f})"

def fractional_knapsack_greedy(items: List[Item], capacity: int) -> Dict:
    """
    Solution A: Fractional Knapsack using Greedy Strategy.
    Sorts items by value-to-weight ratio in descending order.
    Returns selected items/fractions, total value, total weight, and operation counts.
    """
    comp_count = 0
    # Sorting items by ratio descending
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    # n log n comparisons estimated
    n = len(items)
    comp_count += int(n * (len(items).bit_length())) # approx comparisons for sorting
    
    current_weight = 0
    total_value = 0.0
    selections = []
    
    for item in sorted_items:
        comp_count += 1
        if current_weight + item.weight <= capacity:
            # Take full item
            current_weight += item.weight
            total_value += item.value
            selections.append({
                'item_id': item.item_id,
                'weight_taken': item.weight,
                'fraction': 1.0,
                'value_gained': item.value,
                'type': 'FULL'
            })
        else:
            # Take fractional slice
            remain = capacity - current_weight
            if remain > 0:
                fraction = remain / item.weight
                val = item.value * fraction
                current_weight += remain
                total_value += val
                selections.append({
                    'item_id': item.item_id,
                    'weight_taken': remain,
                    'fraction': fraction,
                    'value_gained': val,
                    'type': f"FRACTION ({fraction:.2%})"
                })
            break # Knapsack full
            
    memory_bytes = sys.getsizeof(sorted_items) + sum(sys.getsizeof(x) for x in selections)
    
    return {
        'total_value': total_value,
        'total_weight': current_weight,
        'capacity': capacity,
        'selections': selections,
        'comparisons': comp_count,
        'memory_bytes': memory_bytes
    }

def knapsack_01_dp(items: List[Item], capacity: int) -> Dict:
    """
    Solution B: 0/1 Knapsack using Dynamic Programming.
    DP Table: DP[i][w] = max value using subset of first i items with capacity w.
    Returns optimal value, selected item IDs, DP table, and operation count.
    """
    n = len(items)
    DP = [[0.0] * (capacity + 1) for _ in range(n + 1)]
    eval_count = 0
    
    # Fill DP Table
    for i in range(1, n + 1):
        item = items[i - 1]
        w_i = item.weight
        v_i = item.value
        for w in range(capacity + 1):
            eval_count += 1
            if w_i <= w:
                # Option 1: Exclude item vs Option 2: Include item
                if DP[i - 1][w] >= DP[i - 1][w - w_i] + v_i:
                    DP[i][w] = DP[i - 1][w]
                else:
                    DP[i][w] = DP[i - 1][w - w_i] + v_i
            else:
                DP[i][w] = DP[i - 1][w]

    # Item reconstruction backtracking
    w_rem = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if DP[i][w_rem] != DP[i - 1][w_rem]:
            item = items[i - 1]
            selected_items.append(item)
            w_rem -= item.weight
    
    selected_items.reverse()
    total_val = DP[n][capacity]
    total_wt = sum(it.weight for it in selected_items)
    
    # Memory estimation
    memory_bytes = sys.getsizeof(DP) + sum(sys.getsizeof(row) for row in DP)

    return {
        'total_value': total_val,
        'total_weight': total_wt,
        'capacity': capacity,
        'selected_items': selected_items,
        'operations': eval_count,
        'memory_bytes': memory_bytes,
        'dp_table': DP
    }

def greedy_01_heuristic(items: List[Item], capacity: int) -> Dict:
    """
    Evaluates what a purely greedy value-to-weight heuristic would select
    under strict 0/1 (no fraction) constraints.
    """
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    cur_wt = 0
    tot_val = 0.0
    chosen = []
    rejected_due_to_capacity = []
    
    for it in sorted_items:
        if cur_wt + it.weight <= capacity:
            cur_wt += it.weight
            tot_val += it.value
            chosen.append(it)
        else:
            rejected_due_to_capacity.append(it)
            
    return {
        'total_value': tot_val,
        'total_weight': cur_wt,
        'chosen': chosen,
        'rejected': rejected_due_to_capacity
    }

def run_task2():
    print("=" * 80)
    print("     CO4 ASSIGNMENT 4B - TASK 2: GREEDY VS DYNAMIC PROGRAMMING KNAPSACK")
    print("=" * 80)
    
    # -------------------------------------------------------------------------
    # 2.1 Normal Case
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("TASK 2.1: NORMAL CASE EVALUATION")
    print("=" * 75)
    print("Scenario: Divisible logistical freight (Fractional Knapsack formulation).")
    print("Vehicle Capacity: 60 kg")
    
    normal_items = [
        Item("PKG-A", weight=10, value=60.0),   # ratio 6.0
        Item("PKG-B", weight=20, value=100.0),  # ratio 5.0
        Item("PKG-C", weight=30, value=120.0),  # ratio 4.0
        Item("PKG-D", weight=15, value=45.0),   # ratio 3.0
        Item("PKG-E", weight=25, value=50.0),   # ratio 2.0
    ]
    
    print("\nInput Freight Item Catalog:")
    print(f"{'Item ID':<8} | {'Weight (kg)':<12} | {'Value ($)':<10} | {'Ratio ($/kg)':<12}")
    print("-" * 50)
    for it in normal_items:
        print(f"{it.item_id:<8} | {it.weight:<12} | {it.value:<10.1f} | {it.ratio:<12.2f}")
        
    frac_res = fractional_knapsack_greedy(normal_items, capacity=60)
    print(f"\n--- Greedy Fractional Knapsack Execution Result ---")
    print(f"Optimal Value Achieved: ${frac_res['total_value']:.2f}")
    print(f"Total Weight Loaded   : {frac_res['total_weight']} / {frac_res['capacity']} kg")
    print(f"{'Item ID':<8} | {'Weight Taken':<14} | {'Fraction':<16} | {'Value Gained ($)'}")
    print("-" * 55)
    for sel in frac_res['selections']:
        print(f"{sel['item_id']:<8} | {sel['weight_taken']:<14.1f} | {sel['type']:<16} | ${sel['value_gained']:.2f}")
    print("\nGreedy Decision Sequence Observation:")
    print("  1. Sorted items by ratio: PKG-A (6.0) > PKG-B (5.0) > PKG-C (4.0) > PKG-D (3.0) > PKG-E (2.0).")
    print("  2. Committed 100% of PKG-A (wt: 10, val: 60), remaining capacity = 50 kg.")
    print("  3. Committed 100% of PKG-B (wt: 20, val: 100), remaining capacity = 30 kg.")
    print("  4. Committed 100% of PKG-C (wt: 30, val: 120), remaining capacity = 0 kg.")
    print("  Conclusion: Greedy strategy achieves mathematically optimal solution with zero fractional waste.")

    # -------------------------------------------------------------------------
    # 2.2 Break the Greedy Intuition (Adversarial 0/1 Counterexample)
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("TASK 2.2: BREAKING GREEDY INTUITION (0/1 KNAPSACK ADVERSARIAL COUNTEREXAMPLE)")
    print("=" * 75)
    print("Vehicle Capacity W = 50 kg (Strictly indivisible packages).")
    
    adv_items = [
        Item("ITEM-1", weight=10, value=60.0),   # ratio = 6.00
        Item("ITEM-2", weight=20, value=100.0),  # ratio = 5.00
        Item("ITEM-3", weight=30, value=120.0),  # ratio = 4.00
    ]
    
    print("\nStudent-Designed Adversarial Dataset:")
    print(f"{'Item ID':<8} | {'Weight (kg)':<12} | {'Value ($)':<10} | {'Ratio ($/kg)':<12}")
    print("-" * 50)
    for it in adv_items:
        print(f"{it.item_id:<8} | {it.weight:<12} | {it.value:<10.1f} | {it.ratio:<12.2f}")
        
    greedy_01_res = greedy_01_heuristic(adv_items, capacity=50)
    dp_01_res = knapsack_01_dp(adv_items, capacity=50)
    
    print(f"\n[A] Greedy Heuristic Execution (0/1 Rule):")
    print(f"  Items Selected : {[it.item_id for it in greedy_01_res['chosen']]}")
    print(f"  Total Weight   : {greedy_01_res['total_weight']} kg (Capacity = 50 kg, Unused = {50 - greedy_01_res['total_weight']} kg)")
    print(f"  Total Value    : ${greedy_01_res['total_value']:.2f}")
    print(f"  Items Rejected : {[it.item_id for it in greedy_01_res['rejected']]}")
    
    print(f"\n[B] Dynamic Programming Exact Execution (0/1 Rule):")
    print(f"  Items Selected : {[it.item_id for it in dp_01_res['selected_items']]}")
    print(f"  Total Weight   : {dp_01_res['total_weight']} kg (Capacity = 50 kg, Unused = {50 - dp_01_res['total_weight']} kg)")
    print(f"  Total Value    : ${dp_01_res['total_value']:.2f}")

    print("\n>>> IDENTIFICATION OF THE FIRST GREEDY COMMITMENT TRAP:")
    print("  * Step 1: Greedy observes ITEM-1 has the highest ratio (6.00 $/kg).")
    print("  * Step 2: Greedy commits ITEM-1 (weight 10 kg, value $60). Capacity left = 40 kg.")
    print("  * Step 3: Greedy commits ITEM-2 (weight 20 kg, value $100). Capacity left = 20 kg.")
    print("  * Step 4: Greedy evaluates ITEM-3 (weight 30 kg). It CANNOT fit in 20 kg space!")
    print("  * TRAP EXPOSED: The initial commitment to ITEM-1 (10 kg) left an awkward residual")
    print("    capacity of 20 kg, preventing the inclusion of the large high-value ITEM-3 (30 kg).")
    print("    Optimal combination {ITEM-2, ITEM-3} achieves $220.00 at full 50 kg capacity.")
    print(f"    Suboptimality Gap: ${dp_01_res['total_value'] - greedy_01_res['total_value']:.2f} "
          f"({((dp_01_res['total_value'] - greedy_01_res['total_value']) / dp_01_res['total_value'])*100:.1f}% value loss)!")

    # -------------------------------------------------------------------------
    # 2.3 Engineering Comparison
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("TASK 2.3: ENGINEERING COMPARISON (GREEDY VS DYNAMIC PROGRAMMING)")
    print("=" * 75)
    frac_ops_str = f"{frac_res['comparisons']} sort/scan ops"
    dp_ops_str = f"{dp_01_res['operations']} table state evaluations"
    frac_mem_str = f"{frac_res['memory_bytes']} bytes"
    dp_mem_str = f"{dp_01_res['memory_bytes']} bytes"

    print(f"{'Performance Metric':<26} | {'Greedy Strategy (Sol A)':<24} | {'Dynamic Programming (Sol B)'}")
    print("-" * 80)
    print(f"{'Theoretical Time':<26} | {'O(n log n)':<24} | {'O(n * W)'}")
    print(f"{'Computational Work (Ops)':<26} | {frac_ops_str:<24} | {dp_ops_str}")
    print(f"{'Theoretical Space':<26} | {'O(1) auxiliary':<24} | {'O(n * W) table (or O(W))'}")
    print(f"{'Memory Consumed (Est)':<26} | {frac_mem_str:<24} | {dp_mem_str}")
    print(f"{'Optimality Guarantee':<26} | {'Exact (Fractional only)':<24} | {'Exact Mathematical Optimum (0/1)'}")
    print(f"{'Subproblem Overlap':<26} | {'None (Irrevocable choice)':<24} | {'Exhaustive memoized reuse'}")
    print(f"{'Sensitivity to Capacity W':<26} | {'Independent of W':<24} | {'Directly scales with W (Pseudo-poly)'}")
    print("-" * 80)

    # -------------------------------------------------------------------------
    # 2.4 Changed Requirement (Rapid Decision / Near-Optimal)
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("TASK 2.4: CHANGED REQUIREMENT ANALYSIS")
    print("=" * 75)
    print("Management Mandate: 'Extremely quick decision required; near-optimal is acceptable.'")
    print("\nAlgorithmic Engineering Trade-off Evaluation:")
    print("1. Why Pure DP Fails under Millisecond Real-Time Latency:")
    print("   - As capacity W scales to 100,000 units and n = 5,000 items, DP table requires")
    print("     5,000 * 100,000 = 500,000,000 cell operations (~500 MB memory). Execution exceeds")
    print("     the real-time dispatch threshold by multiple seconds.")
    print("2. The Modified Greedy Heuristic (Greedy-2 / Modified Greedy):")
    print("   - Take max(Value(Greedy 0/1), Value(Single Max-Value Item)).")
    print("   - Guarantee: Mathematically proven 2-approximation (at least 50% of optimal value).")
    print("   - Execution time: O(n log n), executing in < 2 milliseconds for n = 10,000 items.")
    print("3. Fully Polynomial Time Approximation Scheme (FPTAS):")
    print("   - Scales values by factor K = (epsilon * V_max) / n, running DP on scaled values.")
    print("   - Produces a (1 - epsilon)-optimal solution in O(n^3 / epsilon) time.")
    print("4. Final Recommendation:")
    print("   - For high-throughput dispatch systems (50,000 queries/hour), deploy the Modified Greedy")
    print("     Heuristic for instant O(n log n) sub-millisecond response with guaranteed bounded error.")

if __name__ == "__main__":
    run_task2()
