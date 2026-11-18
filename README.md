# CSA0608 – Design and Analysis of Algorithms

**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Department:** Computer Science and Engineering  
**Student Name:** Sanjai S  
**Register Number:** 192511018  

---

## 📚 Repository Overview

This repository hosts coursework, laboratory programs, continuous assessments, and comprehensive capstone project assignments for **CSA0608 – Design and Analysis of Algorithms**.

```
CSA0608-DAA/
│
├── CO1_Assignment/                     # Capstone Assignment 1: Large-Scale Student Record Retrieval
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
│   └── README.md                       # Comprehensive assignment documentation
│
├── CSA0608 CO AND ASSESSMENT/          # Course Outcome briefs, assignments, and case studies
└── CSA0608 LAB PROGRAMS/               # Laboratory topic implementations & manuals
```

---

## 🏆 Featured Submission: CO1 Assignment
- **Title:** *Design, Analyse and Validate an Efficient Search Strategy for a Large-Scale Student Record System*
- **Directory:** [`CO1_Assignment/`](CO1_Assignment/)
- **Master Report (.docx):** [`CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.docx`](CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.docx)
- **Master Report (.md):** [`CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.md`](CO1_Assignment/Report/Documentation/CSA0608_CO1_Assignment_Report.md)
- **Experimental Highlights:**
  - Evaluated on $1\,000 \to 10\,000 \to 100\,000 \to 1\,000\,000$ student records.
  - Linear Search: $1\,000\,000$ comparisons ($31.89$ ms).
  - Iterative & Recursive Binary Search: **20 comparisons** ($7.00$ $\mu\text{s}$) — a **$50\,000\times$ speedup**.
  - Day-4 Challenge: Modified to a **Hybrid In-Memory Hash Index + Sorted View** sustaining $50\,000$ requests/hour in $0.17$ s total CPU time.

---

## 💻 Quick Start & Verification
```powershell
# Run unit tests
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/test_cases.py

# Run benchmark suite across 1,000 to 1,000,000 records
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/benchmark.py
```
