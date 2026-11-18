# CSA0608 – Design and Analysis of Algorithms

**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Department:** Department of Computer Science and Engineering  
**Student Name:** Sanjai S  
**Register Number:** 192511018  

---

## 📚 Repository Overview

This repository hosts coursework, laboratory programs, continuous assessments, and comprehensive capstone project assignments for **CSA0608 – Design and Analysis of Algorithms**.

```text
CSA0608-DAA/
│
├── CO1_Assignment/                     # Assignment 1: Large-Scale Student Record Retrieval (Tasks 1-12)
│   ├── Task_1_Algorithm_Design/        # Three distinct search strategies & pseudocode
│   ├── Task_2_Basic_Operation/         # Basic operations identification & justification
│   ├── Task_3_Mathematical_Complexity/ # Mathematical derivations of T(n) & preprocessing P(n)
│   ├── Task_4_Case_Analysis/           # Best-, average-, and worst-case mathematical analysis
│   ├── Task_5_Asymptotic_Analysis/     # Growth analysis using Big-O, Big-Omega, Big-Theta
│   ├── Task_6_Recurrence_Formulation/  # Formal recurrence formulation T(n) = T(n/2) + c
│   ├── Task_7_Recurrence_Solution/     # Expansion, Master Theorem, & Induction proofs
│   ├── Task_8_Implementation_Testing/  # Python source code, test cases, and benchmarks
│   ├── Task_9_Experimental_Performance/# Empirical measurements (N=1,000 to 1,000,000)
│   ├── Task_10_Theory_vs_Experiment/   # Comparison of theoretical models vs physical execution
│   ├── Task_11_Final_Recommendation/   # Technically justified baseline recommendation
│   ├── Task_12_Design_Challenge/       # Day-4 Design Challenge (50,000 req/hr on 1,000,000 records)
│   ├── Report/                         # Master reports (.docx, .md), screenshots, graphs, & analysis
│   └── README.md                       # Comprehensive CO1 assignment documentation
│
├── CO2_Assignment/                     # Assignment 2: Brute-Force & Exhaustive Search (Q1-Q7)
│   ├── Q1_Sorting_Algorithms/          # Selection, Bubble, and Insertion Sort adaptivity
│   ├── Q2_Sequential_Search/           # Tool tracking boundaries & multi-facility explosion
│   ├── Q3_Brute_Force_String_Matching/ # Structural work variance (20.0x) under fixed (n, m)
│   ├── Q4_Brute_Force_Closest_Pair/    # n(n-1)/2 pair derivation & 50 ms real-time SLA breach
│   ├── Q5_Brute_Force_Convex_Hull/     # Half-plane derivation, collinear filter & correctness proof
│   ├── Q6_Exhaustive_Search/           # 0/1 Knapsack 2^n enumeration & 5.0 s dispatch boundary
│   ├── Q7_Day4_Design_Challenge/       # Adaptive-Axis Sweep-Window Redesign (384.9x speedup)
│   ├── Final_Report/                   # Master reports (.docx, .md) following SIMATS Capstone format
│   └── README.md                       # Comprehensive CO2 assignment documentation
│
├── CO3_Assignment/                     # Assignment 3: Divide and Conquer (Pair Work, Q1-Q7)
│   ├── Q1_MaxMin_Binary_Search/        # Tournament Max-Min (3n/2 - 2) & Lower-Bound Binary Search
│   ├── Q2_MergeSort_QuickSort/         # Decomposition quality: Stable Merge Sort vs Median-of-3 Introsort
│   ├── Q3_Karatsuba_Multiplication/    # Fast multiplication Theta(n^1.585), 91.7% mult reduction
│   ├── Q4_Strassen_Matrix_Multiplication/# Strassen Theta(n^2.807), 73.7% mult reduction on 1024x1024
│   ├── Q5_Divide_Conquer_Closest_Pair/ # Geometric strip bounding (7 neighbors) & O(n log n) scaling
│   ├── Q6_Advanced_Divide_Conquer/     # Median of Medians (BFPRT O(n)) & Meet in the Middle (2^(n/2))
│   ├── Q7_Day4_Design_Challenge/       # KartIQ Retail Platform: 10M orders, 100K live leaderboard
│   ├── Final_Report/                   # Master reports (.docx, .md) & Student_Contribution_Record.docx
│   └── README.md                       # Comprehensive CO3 assignment documentation
│
├── CO4_Assignment_4A/                  # Assignment 4A: Algorithmic Design Through Pseudocode (CO4)
│   ├── Source_Code/
│   │   ├── Task_1/                     # Fractional Knapsack: 6 Deficiencies Diagnosed & Repaired
│   │   ├── Task_2/                     # Job Sequencing with Deadlines: Latest-Slot Greedy & Challenge ($210)
│   │   ├── Task_3/                     # 0/1 Knapsack DP: Recurrence, Table Desk-Check & Backtracking ({Q, R})
│   │   ├── Task_4/                     # Word Break Forensics: Prefix-Chaining Defect & Surgical Fix
│   │   ├── Task_5/                     # Shortest Paths: Dijkstra, Bellman-Ford & Floyd-Warshall APSP
│   │   └── Task_6/                     # Day-4 Design Challenge: Energy-Aware Scheduling DP (Value = 200)
│   ├── Report/                         # PDF Report (CO4_Assignment_4A_Report.pdf), DOCX & MD Reports
│   └── README.md                       # Comprehensive CO4 assignment documentation
│
├── CSA0608 CO AND ASSESSMENT/          # Course Outcome briefs, assignments, and case studies
└── CSA0608 LAB PROGRAMS/               # Laboratory topic implementations & manuals
```

---

## 🏆 Featured Submissions

### 1. CO1 Assignment: Search Strategy for Student Records
- **Directory:** [`CO1_Assignment/`](CO1_Assignment/)
- **Master Report (.docx):** [`CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.docx`](CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.docx)
- **Highlights:** Evaluated $1\,000 \to 1\,000\,000$ records. Binary Search demonstrated **20 comparisons** vs Linear Search's $1\,000\,000$ comparisons ($50\,000\times$ speedup). Day-4 Challenge modified to a Hybrid In-Memory Hash Index sustaining $50\,000$ requests/hour in $0.17$ s CPU time.

### 2. CO2 Assignment: Brute-Force and Exhaustive Search
- **Directory:** [`CO2_Assignment/`](CO2_Assignment/)
- **Master Report (.docx):** [`CO2_Assignment/Final_Report/CO2_Assignment_Report.docx`](CO2_Assignment/Final_Report/CO2_Assignment_Report.docx)
- **Highlights:**
  - **Q1 Sorting:** Insertion Sort cuts comparisons by 94.8% and runs $10.4\times$ faster on nearly sorted streams.
  - **Q2 Tool Tracking:** 20-facility expansion causes a $398.94\times$ comparison surge; resolved via Hash Table index.
  - **Q3 String Matching:** Fixed dimensions ($n=10,000, m=20$) show a $20.0\times$ work variance ($9,981 \to 199,620$ comps).
  - **Q4 Closest Pair:** Brute force breaches the 50 ms SLA at $n = 1,000$ drones ($805$ ms at $n = 4,000$).
  - **Q5 Convex Hull:** Derived from the half-plane separation principle; eliminates collinear subsegments and near-edge traps.
  - **Q6 0/1 Knapsack:** Proved greedy heuristic suboptimal (+10 value); determined $n_{\text{max}} = 22$ under a 5.0 s dispatch SLA.
  - **Q7 Day-4 Challenge:** Adaptive-Axis Sweep-Window Redesign achieves a **$384.9\times$ speedup** at $n = 4,000$ drones ($2.12$ ms latency, $23\times$ below SLA).

### 3. CO3 Assignment: Divide and Conquer Algorithms (Pair Work)
- **Directory:** [`CO3_Assignment/`](CO3_Assignment/)
- **Master Report (.docx):** [`CO3_Assignment/Final_Report/CO3_Assignment_Report.docx`](CO3_Assignment/Final_Report/CO3_Assignment_Report.docx)
- **Contribution Record (.docx):** [`CO3_Assignment/Final_Report/Student_Contribution_Record.docx`](CO3_Assignment/Final_Report/Student_Contribution_Record.docx)
- **Pair Team:** Student A: SANJAI S (192511018) | Student B: PAIR PARTNER (192511025)
- **Highlights:**
  - **Q1 Max-Min & Binary Search:** Tournament method achieves exact $\frac{3n}{2} - 2$ comparisons (**25.00% reduction** over linear); Lower-Bound Binary Search resolves duplicates in $\le 24$ steps.
  - **Q2 Decomposition Quality:** Quick Sort first-pivot experiences catastrophic quadratic degradation on sorted data ($1.99\text{M}$ comparisons, depth 1999); solved by Median-of-Three Introsort ($20,892$ comparisons, depth 10).
  - **Q3 Karatsuba Multiplication:** 3-multiplication recurrence $\Theta(n^{1.585})$ saves **91.69%** scalar multiplications for 1024-digit integers.
  - **Q4 Strassen Matrix Multiplication:** 7-product formulation $\Theta(n^{2.8074})$ eliminates **73.69%** scalar multiplications on $1024 \times 1024$ recommendation matrices.
  - **Q5 Closest Pair:** Geometric circle packing bounds strip neighbors to $\le 7$ points, providing $O(n \log n)$ scaling and a **99.88% reduction** in distance evaluations.
  - **Q6 Advanced D&C:** Deterministic linear-time BFPRT selection ($O(n)$) and Meet-in-the-Middle subset sum yielding a **$524,288\times$ state space reduction**.
  - **Q7 Day-4 Challenge (KartIQ Engine):** Synthesized multi-pipeline D&C engine handling 10M orders, 100K live leaderboards, instantaneous retrieval, and recommendation matrix updates.

### 4. CO4 Assignment 4A: Algorithmic Design Through Pseudocode
- **Directory:** [`CO4_Assignment_4A/`](CO4_Assignment_4A/)
- **Official Submission PDF:** [`CO4_Assignment_4A/Report/CO4_Assignment_4A_Report.pdf`](CO4_Assignment_4A/Report/CO4_Assignment_4A_Report.pdf)
- **Master Report (.docx):** [`CO4_Assignment_4A/Report/CO4_Assignment_4A_Report.docx`](CO4_Assignment_4A/Report/CO4_Assignment_4A_Report.docx)
- **Highlights:**
  - **Task 1 Fractional Knapsack:** Diagnosed 6 deficiencies in junior engineer's logic; repaired with $v_i/w_i$ greedy density sorting and fractional division.
  - **Task 2 Job Sequencing:** Modeled requirements, proved latest-slot greedy rule; desk-checked 5 jobs ($\text{Profit} = \$180$); verified adversarial modification where Job B displaces Job C ($\text{Profit} = \$210$).
  - **Task 3 0/1 Knapsack DP:** Derived state $DP[i][w]$ and recurrence; desk-checked on 4 items ($W=7$ kg) selecting $\{Q, R\}$ ($\text{Value} = \$45$); proved row dependency order.
  - **Task 4 Word Break Forensics:** Pinpointed missing prefix segmentability check; crafted adversarial counterexample `"abcat"` with `{"cat"}` causing false positive; provided minimal fix and regression test.
  - **Task 5 Shortest Paths:** Dijkstra non-negative design ($A:0, B:4, C:6, D:7, E:10$); analyzed negative edge greedy failure; formulated Bellman-Ford repeated relaxation and Floyd-Warshall APSP intermediate state transition.
  - **Task 6 Day-4 Design Challenge:** Weighted Interval Scheduling for cloud server energy savings. Formulated binary search for $p(i)$ and DP state $DP[i] = \max(DP[i-1], v_i + DP[p(i)])$. Selected $\{J2, J5, J7, J8\}$ ($\text{Energy Saved} = 200$); proved complete immunity against adversarial greedy traps.

---

## 💻 Quick Start & Verification
```powershell
# Run CO1 benchmarks
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/benchmark.py

# Run CO2 Day-4 Closest Pair Redesign validation
python CO2_Assignment/Q7_Day4_Design_Challenge/Implementation_Code/q7_closest_pair_redesign.py

# Run CO3 Day-4 KartIQ Divide-and-Conquer Engine validation
python CO3_Assignment/Q7_Day4_Design_Challenge/Implementation_Code/q7_day4_challenge.py

# Run CO4 Day-4 Energy-Aware Cloud Scheduling validation
python CO4_Assignment_4A/Source_Code/Task_6/task6_energy_aware_scheduling.py
```
