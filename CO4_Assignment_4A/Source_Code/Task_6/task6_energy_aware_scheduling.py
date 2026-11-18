"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 6: DESIGN CHALLENGE - ENERGY-AWARE JOB SCHEDULING (WEIGHTED INTERVAL SCHEDULING)
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import bisect

class EnergyJob:
    def __init__(self, job_id, start, finish, value):
        self.job_id = job_id
        self.start = start
        self.finish = finish
        self.value = value

    def __repr__(self):
        return f"{self.job_id}[{self.start}-{self.finish}, v={self.value}]"


def find_latest_non_conflicting(jobs, i):
    """
    Binary search to find the latest job j < i such that jobs[j].finish <= jobs[i].start.
    Returns 1-based index j, or 0 if no compatible job exists.
    Time Complexity: O(log n)
    """
    start_time = jobs[i - 1].start
    # Binary search over finish times of preceding jobs (indices 0 to i-2)
    low = 0
    high = i - 2
    best_idx = -1
    
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid].finish <= start_time:
            best_idx = mid
            low = mid + 1  # Seek latest compatible job
        else:
            high = mid - 1
            
    return best_idx + 1  # Convert to 1-based index (0 means none)


def weighted_interval_scheduling(job_list):
    """
    Dynamic Programming for Weighted Interval Scheduling
    Solves Task 6 Energy-Aware Cloud Data Centre Scheduling.
    
    Time Complexity: O(n log n) sorting + O(n log n) binary search = O(n log n)
    Space Complexity: O(n) for DP table and predecessors
    """
    # Step 1: Sort jobs by finish time
    sorted_jobs = sorted(job_list, key=lambda j: j.finish)
    n = len(sorted_jobs)
    
    # Step 2: Compute predecessor p(i) for each job
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = find_latest_non_conflicting(sorted_jobs, i)
        
    # Step 3: Compute DP states
    DP = [0] * (n + 1)
    decision = [""] * (n + 1)
    
    for i in range(1, n + 1):
        job = sorted_jobs[i - 1]
        exclude_val = DP[i - 1]
        include_val = job.value + DP[p[i]]
        
        if include_val > exclude_val:
            DP[i] = include_val
            decision[i] = f"INCLUDE {job.job_id} ({job.value} + DP[{p[i]}]={include_val})"
        else:
            DP[i] = exclude_val
            decision[i] = f"EXCLUDE {job.job_id} (Keep DP[{i-1}]={exclude_val})"
            
    max_energy_saving = DP[n]
    
    # Step 4: Backtrack to reconstruct selected jobs
    selected_jobs = []
    curr = n
    while curr > 0:
        job = sorted_jobs[curr - 1]
        if job.value + DP[p[curr]] > DP[curr - 1]:
            selected_jobs.append(job)
            curr = p[curr]
        else:
            curr = curr - 1
            
    selected_jobs.reverse()
    return max_energy_saving, selected_jobs, sorted_jobs, p, DP, decision


def run_task6_demo():
    print("=" * 85)
    print("TASK 6: DESIGN CHALLENGE - ENERGY-AWARE CLOUD JOB SCHEDULING")
    print("=" * 85)
    
    # 1. Given Problem Instance (8 Jobs)
    base_jobs = [
        EnergyJob("J1", start=1, finish=3, value=20),
        EnergyJob("J2", start=2, finish=5, value=50),
        EnergyJob("J3", start=4, finish=6, value=30),
        EnergyJob("J4", start=6, finish=8, value=40),
        EnergyJob("J5", start=5, finish=9, value=60),
        EnergyJob("J6", start=8, finish=10, value=30),
        EnergyJob("J7", start=9, finish=11, value=50),
        EnergyJob("J8", start=11, finish=13, value=40)
    ]
    
    print("\n--- 1. Stage 5: Desk-Check on Given 8-Job Problem Instance ---")
    print("Given Waiting Jobs:")
    for j in base_jobs:
        print(f"  {j.job_id}: [{j.start} -> {j.finish}], Energy Saving Value = {j.value}")
        
    opt_val, selected, sorted_j, p_vals, dp_vals, decs = weighted_interval_scheduling(base_jobs)
    
    print("\nFinish-Sorted Jobs with Predecessor p(i) and DP State Transitions:")
    print(f"{'i':<3} | {'Job ID':<8} | {'Interval':<12} | {'Value':<8} | {'p(i)':<6} | {'DP[p(i)]':<10} | {'DP[i-1]':<10} | {'DP[i]':<8} | {'Decision'}")
    print("-" * 95)
    for i in range(1, len(sorted_j) + 1):
        j = sorted_j[i - 1]
        p_i = p_vals[i]
        print(f"{i:<3} | {j.job_id:<8} | [{j.start:>2}, {j.finish:>2}]       | {j.value:<8} | {p_i:<6} | {dp_vals[p_i]:<10} | {dp_vals[i-1]:<10} | {dp_vals[i]:<8} | {decs[i]}")
        
    print("-" * 95)
    print(f"Maximum Total Energy-Saving Value : {opt_val}")
    print(f"Selected Compatible Jobs         : {[j.job_id for j in selected]}")
    print("Execution Verification of Selected Schedule:")
    for j in selected:
        print(f"  Execute {j.job_id}: Time [{j.start} -> {j.finish}], Energy Saved = {j.value}")
        
    # Check non-overlap
    for k in range(len(selected) - 1):
        assert selected[k].finish <= selected[k+1].start, "Overlap detected!"
    print("  Constraint Check: All selected jobs are strictly NON-OVERLAPPING. PASS!")

    # 2. Stage 6: Attack Your Own Design (Adversarial 5-Job Instance)
    print("\n" + "=" * 85)
    print("STAGE 6: ATTACK YOUR OWN DESIGN (ADVERSARIAL 5-JOB DATASET)")
    print("Constructed to challenge greedy heuristics (Earliest Finish, Max Value traps)")
    print("=" * 85)
    
    adv_jobs = [
        EnergyJob("A1", start=1, finish=4, value=10),   # Earliest finish time trap
        EnergyJob("A2", start=3, finish=8, value=100),  # Highest single value trap
        EnergyJob("A3", start=2, finish=5, value=60),   # Optimal choice 1
        EnergyJob("A4", start=5, finish=9, value=60),   # Optimal choice 2
        EnergyJob("A5", start=9, finish=12, value=50)   # Optimal choice 3
    ]
    
    print("Adversarial Jobs:")
    for j in adv_jobs:
        print(f"  {j.job_id}: [{j.start} -> {j.finish}], Value = {j.value}")
        
    adv_opt, adv_sel, _, _, _, _ = weighted_interval_scheduling(adv_jobs)
    
    print("\nHeuristic Analysis on Adversarial Set:")
    print("  • Greedy by Earliest Finish Time (picks A1): A1(10) + A4(60) + A5(50) = 120 (SUBOPTIMAL)")
    print("  • Greedy by Highest Value (picks A2)      : A2(100) + A5(50) = 150        (SUBOPTIMAL)")
    print(f"  • Our Dynamic Programming Engine          : {[j.job_id for j in adv_sel]} = {adv_opt} (OPTIMAL!)")
    print(f"\nConclusion: Dynamic Programming successfully resisted both greedy traps and achieved the true global maximum of {adv_opt}!")
    print("\n[SUCCESS] Task 6 Design Challenge Verification Complete.")

if __name__ == "__main__":
    run_task6_demo()
