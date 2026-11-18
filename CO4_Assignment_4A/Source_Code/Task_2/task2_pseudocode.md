# Task 2 – From Business Requirement to Greedy Pseudocode: Job Sequencing with Deadlines
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Task 2.1 – Model the Requirement

| Component | Technical Specification |
| :--- | :--- |
| **Input** | A list of $n$ independent computational jobs $J = \{J_1, J_2, \dots, J_n\}$, where each job $J_i = (\text{id}_i, d_i, p_i)$ has an integer deadline $d_i \ge 1$, profit $p_i \ge 0$, and requires exactly 1 time slot. |
| **Output** | An ordered schedule array $S[1 \dots M]$ mapping discrete time slots $t \in \{1 \dots M\}$ (where $M = \max_{i} d_i$) to scheduled job IDs, and the maximum total profit $\Pi = \sum_{t=1}^M \text{profit}(S[t])$. |
| **Objective** | $\max \sum_{i \in \text{Scheduled}} p_i$ subject to all scheduled jobs meeting their deadlines. |
| **Constraints** | 1. Processing unit constraint: Each job consumes exactly 1 unit slot.<br>2. Capacity constraint: At most one job per time slot $t$.<br>3. Deadline feasibility: Job $J_i$ scheduled at slot $t$ must satisfy $1 \le t \le d_i$.<br>4. Uniqueness constraint: Each job is scheduled at most once. |
| **Decision to be made** | For each job, decide whether to accept or reject it, and if accepted, select the exact slot $t \in [1, d_i]$ to maximize residual schedule flexibility. |
| **Information required** | The availability state of time slots $t \le d_i$ within the global schedule array. |

---

## 2. Task 2.2 – Formulate a Greedy Hypothesis
**Greedy-Choice Rule:**  
*"Sort all incoming jobs in descending order of profit, and greedily allocate each candidate job to the latest unoccupied discrete time slot $t \le d_i$."*

**Justification:**  
Prioritizing the highest profit jobs captures maximum immediate revenue. Placing each selected job into the latest possible feasible slot ($t = d_i$ or nearest preceding open slot) defers resource commitment as late as possible, preserving earlier time slots for subsequent candidate jobs that have stricter, earlier deadlines.

---

## 3. Task 2.3 – Design the Algorithm (Complete Pseudocode)

```text
ALGORITHM JobSequencingWithDeadlines(Jobs, n)
    // Purpose: Maximizes total profit for jobs completed within deadlines
    // Inputs:
    //   Jobs[1...n] : Array of job records with fields (id, deadline, profit)
    //   n           : Total number of jobs (integer >= 1)
    // Outputs:
    //   Schedule[1...max_deadline] : Array of assigned job IDs per slot
    //   total_profit : Maximum total profit accumulated

    // Step 1: Sort jobs in descending order of profit
    SORT Jobs in descending order according to Jobs[i].profit

    // Step 2: Determine maximum deadline to size the schedule array
    max_deadline <- 0
    FOR i <- 1 TO n DO
        IF Jobs[i].deadline > max_deadline THEN
            max_deadline <- Jobs[i].deadline
        END IF
    END FOR

    // Step 3: Initialize time slot array
    Create array Schedule[1...max_deadline]
    FOR t <- 1 TO max_deadline DO
        Schedule[t] <- NULL             // NULL represents an empty, available slot
    END FOR

    total_profit <- 0

    // Step 4: Greedy Slot Assignment
    FOR i <- 1 TO n DO
        // Scan backwards from min(max_deadline, Jobs[i].deadline) down to 1
        limit <- MIN(max_deadline, Jobs[i].deadline)
        slot_found <- FALSE

        FOR t <- limit DOWNTO 1 DO
            IF Schedule[t] == NULL THEN
                Schedule[t] <- Jobs[i].id
                total_profit <- total_profit + Jobs[i].profit
                slot_found <- TRUE
                BREAK                   // Exit backward scan; job placed
            END IF
        END FOR
        // If slot_found is FALSE, job cannot be scheduled feasibly and is rejected
    END FOR

    RETURN (Schedule, total_profit)
END ALGORITHM
```

---

## 4. Task 2.4 – Desk-Check on Given Problem Instance

**Given Dataset:**
- Job A: $d = 2, p = 80$
- Job B: $d = 1, p = 35$
- Job C: $d = 2, p = 60$
- Job D: $d = 3, p = 40$
- Job E: $d = 1, p = 25$

**Execution Trace:**
1. **Sorted Jobs by Profit:** A (80, d=2), C (60, d=2), D (40, d=3), B (35, d=1), E (25, d=1).  
2. **Max Deadline:** $M = 3$. Slot array initialized: `[Slot 1: NULL, Slot 2: NULL, Slot 3: NULL]`.  
3. **Job A ($d=2, p=80$):** Checks Slot 2 $\rightarrow$ NULL $\rightarrow$ Assign A to Slot 2. `Schedule = [-, A, -]`, Profit = 80.  
4. **Job C ($d=2, p=60$):** Checks Slot 2 $\rightarrow$ Occupied (A) $\rightarrow$ Checks Slot 1 $\rightarrow$ NULL $\rightarrow$ Assign C to Slot 1. `Schedule = [C, A, -]`, Profit = 140.  
5. **Job D ($d=3, p=40$):** Checks Slot 3 $\rightarrow$ NULL $\rightarrow$ Assign D to Slot 3. `Schedule = [C, A, D]`, Profit = 180.  
6. **Job B ($d=1, p=35$):** Checks Slot 1 $\rightarrow$ Occupied (C) $\rightarrow$ No slots $\le 1$ remain $\rightarrow$ REJECTED.  
7. **Job E ($d=1, p=25$):** Checks Slot 1 $\rightarrow$ Occupied (C) $\rightarrow$ No slots $\le 1$ remain $\rightarrow$ REJECTED.  

**Final State:**
- **Schedule:** Slot 1: Job C | Slot 2: Job A | Slot 3: Job D
- **Total Profit Earned:** **$180**

---

## 5. Task 2.5 – Challenge Your Design (Adversarial Input Modification)

**Modification:** Change Job B's profit from **$35 to $90** (Deadline remains $d=1$).

1. **Prediction:**  
   The schedule will fundamentally change. Job B will now rank #1 overall with $p=90$, preempting Slot 1 before Job C is evaluated. When Job C ($d=2$) is evaluated, Slot 2 will be taken by Job A and Slot 1 will be taken by Job B, causing Job C to be completely displaced and rejected.
2. **Affected Decision:**  
   The allocation decision at Step 1 (Job B claims Slot 1) and the feasibility test for Job C at Step 3 (which now fails).
3. **Trace of Relevant Decisions:**  
   - Sorted order: B (90, d=1), A (80, d=2), C (60, d=2), D (40, d=3), E (25, d=1).  
   - Job B claims Slot 1: `[B, -, -]`, Profit = 90.  
   - Job A claims Slot 2: `[B, A, -]`, Profit = 170.  
   - Job C ($d=2$): Slot 2 occupied (A), Slot 1 occupied (B) $\rightarrow$ REJECTED!  
   - Job D claims Slot 3: `[B, A, D]`, Profit = 210.  
   - Job E is rejected.  
4. **Conclusion:**  
   Prediction was exactly correct. The final schedule becomes `[Slot 1: B, Slot 2: A, Slot 3: D]` yielding total profit **$210**.
