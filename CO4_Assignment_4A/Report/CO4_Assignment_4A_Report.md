# ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE
## Optimization Problems via Greedy Strategies and Dynamic Programming

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Course Outcome 4 (CO4) – Assignment 4A  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Date:** November 2026  

---

## BONAFIDE CERTIFICATE & DECLARATION
This is to certify that this report is a bonafide record of independent work done by SANJAI S (192511018) under Course Outcome 4 (CO4) in CSA0608 at SIMATS Engineering. All algorithm models, mathematical state definitions, recurrence derivations, pseudocode conforming to the SIMATS Engineering Handbook, desk-checks, forensic defect diagnoses, and Day-4 design challenge solutions were developed and validated independently.

---

## 1. TASK 1: ALGORITHM DESIGN REVIEW – FRACTIONAL KNAPSACK
- **Deficiencies Diagnosed:**
  1. Undefined inputs/outputs (P, W, V, C).
  2. Ambiguous selection criterion ('arrange'/'best' hides greedy density rule v_i/w_i).
  3. Missing feasibility and capacity tracking (C_rem).
  4. Failure to handle package divisibility (fractional allocation f = C_rem / w_i).
  5. Missing loop advancement (infinite loop).
  6. Unspecified result construction.
- **Repaired Pseudocode:** Computes density R[i] = V[i]/W[i], sorts descendingly, fills complete items, divides first overflowing item, terminates.
- **Design Defence:** Qualifies as pseudocode by using language-independent mathematical abstractions without syntactic boilerplate, while remaining mathematically deterministic and unambiguous.

---

## 2. TASK 2: JOB SEQUENCING WITH DEADLINES
- **Greedy Hypothesis:** Sort jobs descending by profit, and allocate each job to the latest unoccupied slot t <= d_i. Deferring slot commitment preserves earlier slots for jobs with tighter deadlines.
- **Desk-Check Trace:** On jobs {A(80,d=2), B(35,d=1), C(60,d=2), D(40,d=3), E(25,d=1)}:
  - Job A -> Slot 2 ($80)
  - Job C -> Slot 1 ($140)
  - Job D -> Slot 3 ($180)
  - Jobs B and E are rejected. Total Profit = **$180**.
- **Adversarial Modification Challenge:** Increasing Job B profit to 90 causes B to claim Slot 1, preempting and displacing Job C. New schedule: [B, A, D], Total Profit = **$210** (Verified!).

---

## 3. TASK 3: DYNAMIC PROGRAMMING – 0/1 KNAPSACK
- **State Definition:** DP[i][w] = Maximum total value achievable using a subset of items {1...i} under weight capacity w.
- **Recurrence:**
  - If w_i > w: DP[i][w] = DP[i-1][w]
  - If w_i <= w: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)
- **Desk-Check (Capacity W = 7):** On items P(2,12), Q(3,20), R(4,25), S(5,30):
  - Optimal Value DP[4][7] = **$45**.
  - Backtracking reconstructs **{Q, R}** (weight = 3+4=7 kg, value = 20+25=$45).
- **Dependency:** State DP[i][w] depends on DP[i-1][w] and DP[i-1][w-w_i] from row i-1, mandating forward row iteration i=1...n.

---

## 4. TASK 4: PSEUDOCODE FORENSICS – WORD BREAK
- **Defect:** Checks only whether substring(Text, j, i) is in Dictionary, ignoring whether the preceding prefix ending at j was segmentable (DP[j] == TRUE).
- **Counterexample:** Text = "abcat", Dict = {"cat"}. Ground truth is FALSE. Faulty code sets DP[5] <- TRUE because "cat" is in Dict, ignoring DP[2]=FALSE. Returns TRUE (False Positive!).
- **Surgical Repair:** `IF (DP[j] == TRUE) AND (substring(Text, j, i) is in Dictionary) THEN DP[i] <- TRUE; BREAK; END IF`. Regression on "applepie" verified.

---

## 5. TASK 5: SHORTEST PATHS – DIJKSTRA, BELLMAN-FORD, FLOYD-WARSHALL
- **Dijkstra:** Greedily extracts unvisited vertex with min tentative distance and relaxes outgoing edges. Result from A: A:0, B:4, C:6, D:7, E:10.
- **Negative Edges & Bellman-Ford:** Negative edges violate Dijkstra's greedy finalizing assumption. Bellman-Ford performs |V|-1 relaxation rounds and detects negative cycles on the |V|-th pass.
- **Floyd-Warshall (APSP):** State D^(k)[i][j] = shortest path from i to j using intermediate vertices from {1...k}. Transition: min(D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j]).

---

## 6. TASK 6: DAY-4 DESIGN CHALLENGE – ENERGY-AWARE SCHEDULING
- **Problem Abstraction:** Weighted Interval Scheduling.
- **Strategy:** Greedy by finish time or value fails on weighted intervals. Dynamic Programming with binary search for latest non-conflicting job p(i) guarantees global optimality in O(n log n) time.
- **Desk-Check (8 Jobs):** DP states lead to optimal value **200**. Backtracking reconstructs **{J2, J5, J7, J8}** with zero interval overlap.
- **Adversarial Trap Immunity:** Evaluated on {A1[1,4]v=10, A2[3,8]v=100, A3[2,5]v=60, A4[5,9]v=60, A5[9,12]v=50}. Greedy EFT gets 120; Greedy Value gets 150; our DP engine achieves optimal **170** ({A3, A4, A5}), proving complete immunity to local traps.

---

## 7. COMPARATIVE SUMMARY MATRIX

| Task | Paradigm | Complexity | Key Algorithmic Principle |
| :--- | :--- | :--- | :--- |
| **Task 1: Fractional Knapsack** | Greedy | O(n log n) | Divisibility enables greedy ratio choice. |
| **Task 2: Job Sequencing** | Greedy | O(n^2) / O(n log n) | Latest-slot commitment preserves earlier flexibility. |
| **Task 3: 0/1 Knapsack** | Dynamic Programming | Theta(n W) | Indivisibility requires evaluating include vs exclude. |
| **Task 4: Word Break** | Dynamic Programming | O(n^2) | Prefix state chaining (DP[j]==True) ensures correctness. |
| **Task 5: Shortest Paths** | Greedy / DP | O(V^2) / O(VE) / O(V^3) | Non-negative greedy vs repeated relaxation vs all-pairs DP. |
| **Task 6: Cloud Scheduling** | Dynamic Programming | O(n log n) | Binary search predecessor p(i) + DP solves weighted intervals. |
