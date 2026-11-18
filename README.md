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
├── CO4_Assignment_4B/                  # Assignment 4B: Algorithm Engineering: Implement, Test, Debug & Optimise
│   ├── Source_Code/
│   │   ├── Task_1/                     # Word Wrap DP Layout Engine: Cubic Penalty, Multi-Width & Guards
│   │   ├── Task_2/                     # Fractional vs 0/1 Knapsack: Adversarial Commitment Trap & FPTAS
│   │   ├── Task_3/                     # Network Routing Engine: Dijkstra Failure, Bellman-Ford & Floyd-Warshall
│   │   ├── Task_4/                     # Assembly Line Scheduling DP: Stay vs Transfer Trace & Disruption
│   │   ├── Task_5/                     # Kruskal vs Prim vs Boruvka MST: Stressed Multiple MST Proof
│   │   └── Task_6/                     # Held-Karp TSP DP: Bitmask Engine, Brute Force Validation & Benchmark
│   ├── Report/                         # Official PDF (CO4_Assignment_4B_Report.pdf), DOCX & MD Reports
│   └── README.md                       # Comprehensive CO4 Assignment 4B documentation
│
├── CSA0608 CO AND ASSESSMENT/          # Course Outcome briefs, assignments, and case studies
└── CSA0608 LAB PROGRAMS/               # Laboratory topic implementations & manuals
```

---

## 🎯 Course Outcomes & Assignments

| Assignment | Course Outcome | Focus & Paradigm | Status | Key Deliverables |
| :--- | :--- | :--- | :---: | :--- |
| **CO1 Assignment** | **CO1** | Mathematical Analysis of Algorithms & Recurrences | **Completed** | Full derivation, experimental tests on 1M records, Design Challenge, PDF/Word/MD reports |
| **CO2 Assignment** | **CO2** | Brute Force, Exhaustive Search, Adaptivity & Convex Hull | **Completed** | 7 Questions, Sweepline optimization, 384.9x speedup, PDF/Word/MD reports |
| **CO3 Assignment** | **CO3** | Divide and Conquer Paradigms & Lower Bounds | **Completed** | Karatsuba, Strassen, Closest Pair, Median-of-Medians, KartIQ Day-4 System, PDF/Word/MD |
| **CO4 Assignment 4A** | **CO4 (Part I)** | Algorithmic Design Through Pseudocode | **Completed** | Diagnostic review, job sequencing, knapsack DP, word break forensics, energy-aware DP, PDF/Word/MD |
| **CO4 Assignment 4B** | **CO4 (Part II)** | Algorithm Engineering: Implement, Test, Debug & Optimise | **Completed** | Word wrap DP, Knapsack trap, Routing engine, Assembly line, MST triad, Held-Karp TSP, PDF/Word/MD |

---

## 🚀 Key Coursework Achievements

1. **Large-Scale Asymptotic Modeling:** Mathematically evaluated and benchmarked binary search across $10^6$ records, proving $O(\log n)$ scalability under high-throughput request rates.
2. **Brute Force & Algorithmic Adaptivity:** Diagnosed worst-case bottlenecks across sorting, searching, and geometric algorithms, redesigning the Day-4 nearest-neighbor radar with a 384.9x faster adaptive-axis window.
3. **Advanced Divide and Conquer:** Implemented sub-cubic matrix multiplication (Strassen $O(n^{2.807})$), fast integer arithmetic (Karatsuba $O(n^{1.585})$), linear-time median selection ($O(n)$ BFPRT), and sub-millisecond closest pair detection.
4. **Algorithmic Design Through Pseudocode:** Identified and repaired anti-patterns in greedy and dynamic programming formulations, applying formal verification, invariant modeling, and state-transition desk-checks.
5. **Algorithm Engineering & Adversarial Verification:** Engineered production-grade implementations of Word Wrap DP, Fractional vs 0/1 Knapsack with an adversarial counterexample exposing the greedy commitment trap, robust multi-protocol routing with negative cycle detection, assembly line scheduling under mechanical disruptions, multiple MST verification across Kruskal/Prim/Borůvka, and Held-Karp bitmask TSP with brute-force validation and growth benchmarking.

---
*Maintained by Sanjai S (192511018) | Department of Computer Science and Engineering, SIMATS Engineering.*
