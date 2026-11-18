# CSA0608 – Design and Analysis of Algorithms

**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Department:** Department of Computer Science and Engineering  
**Student Name:** Sanjai S  
**Register Number:** 192511018  

---

## 📚 Repository Overview

This repository hosts coursework, laboratory programs, continuous assessments, and comprehensive capstone project assignments for **CSA0608 – Design and Analysis of Algorithms**.

```
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

---

## 💻 Quick Start & Verification
```powershell
# Run CO1 benchmarks
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/benchmark.py

# Run CO2 Day-4 Closest Pair Redesign validation
python CO2_Assignment/Q7_Day4_Design_Challenge/Implementation_Code/q7_closest_pair_redesign.py
```
