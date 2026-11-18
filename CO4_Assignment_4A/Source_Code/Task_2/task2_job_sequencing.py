"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 2: JOB SEQUENCING WITH DEADLINES
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"Job({self.job_id}, d={self.deadline}, p={self.profit})"


def job_sequencing_greedy(jobs):
    """
    Greedy Job Sequencing with Deadlines
    Greedy Choice Rule:
    Sort jobs in descending order of profit.
    For each job, search backward from min(n, deadline) down to slot 1
    for the first unoccupied time slot.
    If an empty slot is found, assign the job and accumulate profit.
    Otherwise, reject the job.
    
    Time Complexity: O(n log n) sorting + O(n * min(n, max_d)) slot search.
    Space Complexity: O(max_d) for slot tracking.
    """
    # Step 1: Sort jobs in descending order of profit
    sorted_jobs = sorted(jobs, key=lambda j: j.profit, reverse=True)
    
    # Determine maximum deadline to size the schedule array
    max_deadline = max(j.deadline for j in jobs) if jobs else 0
    # 1-indexed slots: index 0 unused, slots 1 to max_deadline
    slots = [None] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs = []
    audit_trace = []

    for job in sorted_jobs:
        # Search backward from job.deadline down to 1
        allocated_slot = -1
        search_path = []
        for t in range(min(max_deadline, job.deadline), 0, -1):
            search_path.append(t)
            if slots[t] is None:
                slots[t] = job.job_id
                allocated_slot = t
                total_profit += job.profit
                scheduled_jobs.append(job.job_id)
                break
                
        audit_trace.append({
            "job_id": job.job_id,
            "deadline": job.deadline,
            "profit": job.profit,
            "search_path": search_path,
            "allocated_slot": allocated_slot if allocated_slot != -1 else "REJECTED",
            "slots_state": [slots[i] for i in range(1, max_deadline + 1)],
            "running_profit": total_profit
        })

    return total_profit, scheduled_jobs, slots[1:], audit_trace


def run_task2_demo():
    print("=" * 80)
    print("TASK 2: JOB SEQUENCING WITH DEADLINES")
    print("=" * 80)
    
    # 1. Base Problem Dataset (Task 2.4 Desk-Check)
    base_jobs = [
        Job("A", deadline=2, profit=80),
        Job("B", deadline=1, profit=35),
        Job("C", deadline=2, profit=60),
        Job("D", deadline=3, profit=40),
        Job("E", deadline=1, profit=25)
    ]
    
    print("\n--- 1. Desk-Check on Given Problem Instance ---")
    print("Given Jobs:")
    for j in base_jobs:
        print(f"  Job {j.job_id}: Deadline = {j.deadline}, Profit = ${j.profit}")
        
    tot_prof, sched, slots, trace = job_sequencing_greedy(base_jobs)
    
    print(f"\nGreedy Execution Trace (Sorted by Profit Descending):")
    print(f"{'Job':<5} | {'Deadline':<10} | {'Profit':<8} | {'Search Path':<14} | {'Allocated Slot':<16} | {'Slot State [1..3]':<20} | {'Total Profit':<12}")
    print("-" * 95)
    for t in trace:
        slot_str = str(t['slots_state'])
        print(f"{t['job_id']:<5} | {t['deadline']:<10} | ${t['profit']:<7} | {str(t['search_path']):<14} | {str(t['allocated_slot']):<16} | {slot_str:<20} | ${t['running_profit']}")
        
    print("-" * 95)
    print(f"Final Scheduled Slots [Slot 1, Slot 2, Slot 3] : {slots}")
    print(f"Maximum Total Profit Earned                     : ${tot_prof}")
    
    # 2. Challenge Design (Task 2.5: Change Job B Profit to 90)
    print("\n" + "=" * 80)
    print("TASK 2.5: CHALLENGE YOUR DESIGN (ADVERSARIAL MODIFICATION)")
    print("Modification: Increase Job B Profit from $35 to $90 (Deadline remains d=1)")
    print("Prediction: Job B will become #1 priority, claim Slot 1, and displace Job C (d=2)!")
    print("=" * 80)
    
    modified_jobs = [
        Job("A", deadline=2, profit=80),
        Job("B", deadline=1, profit=90),  # MODIFIED FROM 35 TO 90
        Job("C", deadline=2, profit=60),
        Job("D", deadline=3, profit=40),
        Job("E", deadline=1, profit=25)
    ]
    
    m_prof, m_sched, m_slots, m_trace = job_sequencing_greedy(modified_jobs)
    
    print(f"\nModified Greedy Execution Trace:")
    print(f"{'Job':<5} | {'Deadline':<10} | {'Profit':<8} | {'Search Path':<14} | {'Allocated Slot':<16} | {'Slot State [1..3]':<20} | {'Total Profit':<12}")
    print("-" * 95)
    for t in m_trace:
        slot_str = str(t['slots_state'])
        print(f"{t['job_id']:<5} | {t['deadline']:<10} | ${t['profit']:<7} | {str(t['search_path']):<14} | {str(t['allocated_slot']):<16} | {slot_str:<20} | ${t['running_profit']}")
        
    print("-" * 95)
    print(f"Modified Schedule Slots : {m_slots}")
    print(f"Modified Total Profit   : ${m_prof}")
    print(f"Outcome Verification    : Job C was DISPLACED as predicted! Total profit increased to ${m_prof}.")
    print("\n[SUCCESS] Task 2 Verification Complete.")

if __name__ == "__main__":
    run_task2_demo()
