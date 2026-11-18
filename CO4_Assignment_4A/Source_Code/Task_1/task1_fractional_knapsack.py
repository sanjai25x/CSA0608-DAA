"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 1: ALGORITHM DESIGN REVIEW - FRACTIONAL KNAPSACK
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

class Package:
    def __init__(self, pkg_id, weight, value):
        self.pkg_id = pkg_id
        self.weight = weight
        self.value = value
        self.ratio = value / weight if weight > 0 else 0.0

    def __repr__(self):
        return f"Pkg({self.pkg_id}, w={self.weight}, v={self.value}, r={self.ratio:.2f})"


def repaired_fractional_knapsack(packages, capacity):
    """
    Repaired Greedy Fractional Knapsack Algorithm
    Conforms to SIMATS Engineering Handbook for Algorithmic Pseudocode.
    
    Greedy Choice Rule:
    Select packages in descending order of value-to-weight ratio (density v_i / w_i).
    If the package fits completely, load it entirely.
    If the package does not fit, load the fraction f = remaining_capacity / weight_i,
    filling the vehicle to full capacity and terminating.
    
    Time Complexity: O(n log n) due to sorting, O(n) greedy allocation.
    Space Complexity: O(n) to store allocated fractions.
    """
    # Step 1: Sort packages by value-to-weight density in descending order
    sorted_pkgs = sorted(packages, key=lambda p: p.ratio, reverse=True)
    
    remaining_capacity = capacity
    total_value = 0.0
    allocation = {}
    audit_trace = []

    for pkg in sorted_pkgs:
        if remaining_capacity == 0:
            break
            
        if pkg.weight <= remaining_capacity:
            # Full inclusion
            fraction = 1.0
            remaining_capacity -= pkg.weight
            total_value += pkg.value
            allocation[pkg.pkg_id] = 1.0
            audit_trace.append({
                "pkg_id": pkg.pkg_id,
                "weight": pkg.weight,
                "value": pkg.value,
                "ratio": pkg.ratio,
                "fraction": 1.0,
                "value_added": pkg.value,
                "remaining_cap": remaining_capacity
            })
        else:
            # Fractional division
            fraction = remaining_capacity / pkg.weight
            value_added = pkg.value * fraction
            total_value += value_added
            allocation[pkg.pkg_id] = round(fraction, 4)
            audit_trace.append({
                "pkg_id": pkg.pkg_id,
                "weight": pkg.weight,
                "value": pkg.value,
                "ratio": pkg.ratio,
                "fraction": round(fraction, 4),
                "value_added": round(value_added, 2),
                "remaining_cap": 0.0
            })
            remaining_capacity = 0
            break

    return total_value, allocation, audit_trace


def run_task1_demo():
    print("=" * 80)
    print("TASK 1: FRACTIONAL KNAPSACK ALGORITHM DESIGN REVIEW")
    print("=" * 80)
    
    # Test instance with 5 packages and vehicle capacity = 50
    test_packages = [
        Package("P1", weight=10, value=60),   # ratio = 6.0
        Package("P2", weight=20, value=100),  # ratio = 5.0
        Package("P3", weight=30, value=120),  # ratio = 4.0
        Package("P4", weight=15, value=45),   # ratio = 3.0
        Package("P5", weight=25, value=50)    # ratio = 2.0
    ]
    capacity = 50
    
    print(f"\nVehicle Capacity: {capacity} kg")
    print("Incoming Packages:")
    for p in test_packages:
        print(f"  {p.pkg_id}: Weight = {p.weight} kg, Value = ${p.value}, Density = ${p.ratio:.2f}/kg")
        
    tot_val, alloc, trace = repaired_fractional_knapsack(test_packages, capacity)
    
    print("\n--- Greedy Allocation Trace (Ordered by Density v_i / w_i) ---")
    print(f"{'Pkg ID':<8} | {'Weight(kg)':<12} | {'Value($)':<10} | {'Ratio($/kg)':<12} | {'Fraction':<10} | {'Val Added':<10} | {'Rem Cap':<10}")
    print("-" * 85)
    for t in trace:
        print(f"{t['pkg_id']:<8} | {t['weight']:<12} | {t['value']:<10} | {t['ratio']:<12.2f} | {t['fraction']:<10.2f} | ${t['value_added']:<9.2f} | {t['remaining_cap']:<10.2f}")
        
    print("-" * 85)
    print(f"Total Optimal Loaded Value : ${tot_val:.2f}")
    print(f"Final Package Allocations   : {alloc}")
    print("\n[SUCCESS] Task 1 Verification Complete.")
    return tot_val, alloc, trace

if __name__ == "__main__":
    run_task1_demo()
