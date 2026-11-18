# Task 6 – Design Challenge: Energy-Aware Job Scheduling in a Cloud Data Centre
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4) – Day-4 Design Challenge  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Stage 1 – Interpret the Problem
- **Problem Context:** A cloud data centre operates a dedicated, highly energy-efficient computing server. During a maintenance window, multiple computational jobs compete for single-threaded execution.
- **Input:** A list of $n$ computational jobs $J = \{J_1, J_2, \dots, J_n\}$. Each job $J_i$ has:
  - Start time $s_i \in \mathbb{R}^+$
  - Finish time $f_i \in \mathbb{R}^+$ with $s_i < f_i$
  - Energy-saving value $v_i > 0$
- **Output:** An optimal mutually compatible subset $S^* \subseteq J$ of jobs that can execute without overlap on the server, and the maximum achievable energy-saving value $V^* = \sum_{J_k \in S^*} v_k$.
- **Objective Function:**
  $$\max_{S \subseteq J} \sum_{J_k \in S} v_k$$
- **Constraints:**
  1. Mutual Exclusivity: The server executes at most one job at any time instant $t$.
  2. Non-Overlapping Condition: For every pair of distinct jobs $J_i, J_j \in S$, their open execution intervals must be disjoint:
     $$(s_i, f_i) \cap (s_j, f_j) = \emptyset \iff f_i \le s_j \quad \text{or} \quad f_j \le s_i$$
     *(Assumption verified: $f_i = s_j$ is considered non-overlapping).*
- **Decisions to be made:** For each job $J_i$, decide whether to schedule it on the energy-efficient server or omit it.
- **Problem Abstraction:** This problem is isomorphic to the classic **Weighted Interval Scheduling Problem**.

---

## 2. Stage 2 – Propose the Strategy
### Failure Analysis of Greedy Strategies
1. **Earliest Finish Time (EFT):** While EFT is optimal for unweighted interval scheduling (where every job has unit value), it fails catastrophically on weighted intervals. A job finishing very early may possess a negligible energy value ($v=1$) and block an immediately following job with massive value ($v=1000$).
2. **Highest Energy-Saving Value:** Selecting the job with maximum value greedily fails when a single high-value job ($v=100$) overlaps and blocks multiple slightly smaller jobs (e.g., two non-overlapping jobs of $v=60$ each, total $= 120 > 100$).
3. **Shortest Duration:** Fails for the same structural reasons as EFT.

### Selected Strategy: Dynamic Programming with Binary-Search Preprocessing
**Justification:**  
The Weighted Interval Scheduling problem exhibits **Optimal Substructure** and **Overlapping Subproblems**:
- When jobs are ordered by finish time $f_1 \le f_2 \le \dots \le f_n$, any optimal schedule for the prefix of the first $i$ jobs either:
  1. **Excludes job $i$:** The optimal value is identically the optimal value for the first $i-1$ jobs ($OPT(i-1)$).
  2. **Includes job $i$:** The optimal value equals $v_i$ plus the optimal value achievable among all jobs that do not conflict with $i$. Because jobs are sorted by finish time, all compatible jobs finish on or before $s_i$. The latest such job is denoted $p(i)$. Thus, the value is $v_i + OPT(p(i))$.
- Dynamic programming systematically explores this binary choice, tabulating the maximum prefix values in $O(n \log n)$ total time and guaranteeing global optimality.

---

## 3. Stage 3 – Identify the Critical Information
- **Ordering:** Jobs are sorted by non-decreasing finish times: $f_1 \le f_2 \le \dots \le f_n$.
- **Predecessor Function $p(i)$:**
  $$p(i) = \max \{ j \in \{1 \dots i-1\} \mid f_j \le s_i \}, \quad \text{with } p(i) = 0 \text{ if no compatible predecessor exists.}$$
  Since finish times are sorted, $p(i)$ is determined in $O(\log n)$ via binary search.
- **State Formulation:**
  $$\mathbf{DP[i] = \text{The maximum energy-saving value achievable using a mutually compatible subset of jobs from the prefix } \{J_1, \dots, J_i\}.}$$
- **Base Condition:** $DP[0] = 0$ (No jobs available yield zero energy savings).
- **State Transition Equation:**
  $$DP[i] = \max\left(DP[i-1], \; v_i + DP[p(i)]\right)$$
- **Reconstruction:** A backward traversal from $i = n$ down to $1$ verifies whether $v_i + DP[p(i)] > DP[i-1]$. If true, job $i$ was included and the search jumps to $p(i)$; otherwise, the search decrements to $i-1$.

---

## 4. Stage 4 – Design Complete Pseudocode

```text
ALGORITHM EnergyAwareJobScheduling(Jobs, n)
    // Purpose: Computes maximum energy savings and schedule of non-overlapping jobs
    // Inputs:
    //   Jobs[1...n] : Array of records with fields (id, start, finish, value)
    //   n           : Total number of candidate jobs (integer >= 1)
    // Outputs:
    //   max_energy_saving : Maximum total energy savings value
    //   ScheduledJobs     : List of selected non-overlapping job records

    // Step 1: Preprocessing - Sort jobs by non-decreasing finish time
    SORT Jobs in non-decreasing order according to Jobs[i].finish

    // Step 2: Precompute Predecessor p[i] using Binary Search
    Create array p[1...n]
    FOR i <- 1 TO n DO
        low <- 1
        high <- i - 1
        best_pred <- 0

        WHILE low <= high DO
            mid <- FLOOR((low + high) / 2)
            IF Jobs[mid].finish <= Jobs[i].start THEN
                best_pred <- mid
                low <- mid + 1          // Search right for the latest compatible job
            ELSE
                high <- mid - 1         // Job finishes too late; search left
            END IF
        END WHILE
        p[i] <- best_pred
    END FOR

    // Step 3: Initialize DP Table
    Create array DP[0...n]
    DP[0] <- 0

    // Step 4: Dynamic Programming Tabulation
    FOR i <- 1 TO n DO
        exclude_val <- DP[i - 1]
        include_val <- Jobs[i].value + DP[p[i]]

        IF include_val > exclude_val THEN
            DP[i] <- include_val
        ELSE
            DP[i] <- exclude_val
        END IF
    END FOR

    max_energy_saving <- DP[n]

    // Step 5: Backtracking Reconstruction
    ScheduledJobs <- EMPTY_LIST
    curr <- n

    WHILE curr > 0 DO
        IF Jobs[curr].value + DP[p[curr]] > DP[curr - 1] THEN
            APPEND Jobs[curr] TO ScheduledJobs
            curr <- p[curr]             // Jump to latest non-conflicting predecessor
        ELSE
            curr <- curr - 1            // Job curr was excluded
        END IF
    END WHILE

    REVERSE ScheduledJobs
    RETURN (max_energy_saving, ScheduledJobs)
END ALGORITHM
```

---

## 5. Stage 5 – Desk-Check on Given Problem Instance

### Given Problem Dataset (Sorted by Finish Time)
| $i$ | Job ID | Start ($s_i$) | Finish ($f_i$) | Value ($v_i$) | $p(i)$ | Compatible Pred Job |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **J1** | 1 | 3 | 20 | 0 | None |
| **2** | **J2** | 2 | 5 | 50 | 0 | None |
| **3** | **J3** | 4 | 6 | 30 | 1 | J1 (finishes at 3 $\le 4$) |
| **4** | **J4** | 6 | 8 | 40 | 3 | J3 (finishes at 6 $\le 6$) |
| **5** | **J5** | 5 | 9 | 60 | 2 | J2 (finishes at 5 $\le 5$) |
| **6** | **J6** | 8 | 10 | 30 | 4 | J4 (finishes at 8 $\le 8$) |
| **7** | **J7** | 9 | 11 | 50 | 5 | J5 (finishes at 9 $\le 9$) |
| **8** | **J8** | 11 | 13 | 40 | 7 | J7 (finishes at 11 $\le 11$) |

### DP State Transitions Table
- $DP[0] = 0$
- $i=1$ (J1): $\max(DP[0]=0, 20 + DP[0]=20) = \mathbf{20}$
- $i=2$ (J2): $\max(DP[1]=20, 50 + DP[0]=50) = \mathbf{50}$
- $i=3$ (J3): $\max(DP[2]=50, 30 + DP[1]=50) = \mathbf{50}$
- $i=4$ (J4): $\max(DP[3]=50, 40 + DP[3]=90) = \mathbf{90}$
- $i=5$ (J5): $\max(DP[4]=90, 60 + DP[2]=110) = \mathbf{110}$
- $i=6$ (J6): $\max(DP[5]=110, 30 + DP[4]=120) = \mathbf{120}$
- $i=7$ (J7): $\max(DP[6]=120, 50 + DP[5]=160) = \mathbf{160}$
- $i=8$ (J8): $\max(DP[7]=160, 40 + DP[7]=200) = \mathbf{200}$

### Backtracking Execution
- Start at $i = 8$: $40 + DP[7] = 200 > DP[7] = 160 \implies$ **Include J8**. Jump to $p(8) = 7$.
- At $i = 7$: $50 + DP[5] = 160 > DP[6] = 120 \implies$ **Include J7**. Jump to $p(7) = 5$.
- At $i = 5$: $60 + DP[2] = 110 > DP[4] = 90 \implies$ **Include J5**. Jump to $p(5) = 2$.
- At $i = 2$: $50 + DP[0] = 50 > DP[1] = 20 \implies$ **Include J2**. Jump to $p(2) = 0$.
- Terminate.

### Final Schedule Verification
- **Selected Compatible Jobs:** **{J2, J5, J7, J8}**
- **Intervals:** J2 $[2, 5] \to$ J5 $[5, 9] \to$ J7 $[9, 11] \to$ J8 $[11, 13]$
- **Overlap Check:** $5 \le 5$, $9 \le 9$, $11 \le 11$ (Endpoints touch $\implies$ strictly non-overlapping).
- **Maximum Energy-Saving Value:** $50 + 60 + 50 + 40 = \mathbf{200}$.

---

## 6. Stage 6 – Attack Your Own Design (Adversarial Dataset Evaluation)

### Adversarial 5-Job Construction
We construct a deceptive dataset engineered to expose the fatal flaws of greedy heuristics:
- **A1:** $[1, 4]$, $v = 10$ *(Earliest finish time trap: finishes first but has tiny value)*
- **A2:** $[3, 8]$, $v = 100$ *(Highest single value trap: large value but blocks multiple compatible jobs)*
- **A3:** $[2, 5]$, $v = 60$ *(Optimal chain element 1)*
- **A4:** $[5, 9]$, $v = 60$ *(Optimal chain element 2)*
- **A5:** $[9, 12]$, $v = 50$ *(Optimal chain element 3)*

### Why the Dataset is Challenging
- A greedy EFT strategy selects A1, which blocks A3 and A2, yielding only A1(10) + A4(60) + A5(50) = **120**.
- A greedy Value strategy selects A2 ($v=100$), which blocks A1, A3, and A4, leaving only A2(100) + A5(50) = **150**.

### Dynamic Programming Execution & Immunity Defense
- Predecessors for finish-sorted jobs:
  1. A1 $[1, 4], v=10$: $p(1)=0 \implies DP[1] = 10$.
  2. A3 $[2, 5], v=60$: $p(2)=0 \implies DP[2] = \max(10, 60) = 60$.
  3. A2 $[3, 8], v=100$: $p(3)=0 \implies DP[3] = \max(60, 100) = 100$.
  4. A4 $[5, 9], v=60$: $p(4)=2$ (A3 finishes at 5) $\implies DP[4] = \max(100, 60 + DP[2]=120) = \mathbf{120}$!
  5. A5 $[9, 12], v=50$: $p(5)=4$ (A4 finishes at 9) $\implies DP[5] = \max(120, 50 + DP[4]=170) = \mathbf{170}$!
- **Backtrack Result:** Includes **{A3, A4, A5}** with total energy savings $= 60 + 60 + 50 = \mathbf{170}$.

**Conclusion:**  
The adversarial dataset completely defeats both Greedy-by-Finish-Time (120) and Greedy-by-Value (150). Our Dynamic Programming design proved completely immune to these local traps because it evaluates the global subproblem prefix $DP[p(i)]$ and correctly discovers that $60 + 60 = 120$ outperforms the single $100$ trap job.
