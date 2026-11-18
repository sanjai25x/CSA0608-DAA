# CSA0608 – Design and Analysis of Algorithms
## Course Outcome 3 (CO3) Assignment & Capstone Case Study: Divide and Conquer Algorithms

**Institution:** Department of Computer Science and Engineering, SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences (SIMATS), Chennai – 602105  
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 3 – CO3 (Divide and Conquer)  
**Mode:** Pair Work Collaboration (2 Students per Group)  
**Total Marks:** 50 Marks  

---

### Student Details & Role Allocation
- **Student A (Primary Lead):** SANJAI S (Reg. No: **192511018**)  
  *Responsibilities:* Tournament Max-Min, Quick Sort Partitioning & Worst-Case Derivations, Karatsuba Recurrence & Analysis, Strassen Intermediate Multiplication Proofs, Closest Pair Strip Bounding Proof, Median of Medians (BFPRT), Day-4 Proposal (Module 1 & 4A Lead).
- **Student B (Pair Collaborator):** PAIR PARTNER (Reg. No: **192511025**)  
  *Responsibilities:* Lower-Bound Binary Search, Merge Sort Stability & External Runs, Karatsuba Thresholding & Naive Simulator, Matrix Padding & Hybrid Strassen Tuning, Coordinate Presorting Pipeline, Meet-in-the-Middle Subset Sum, Day-4 Proposal (Module 2, 3 & 4B Lead).

---

## 1. Repository Organization

```text
CO3_Assignment/
│
├── Q1_MaxMin_Binary_Search/
│   ├── Implementation_Code/
│   │   └── q1_maxmin_binary_search.py
│   ├── Output_Screenshots/
│   │   ├── q1_execution_terminal.png
│   │   └── q1_maxmin_comparison_graph.png
│   └── Pseudocode/
│       └── q1_pseudocode.md
│
├── Q2_MergeSort_QuickSort/
│   ├── Implementation_Code/
│   │   └── q2_mergesort_quicksort.py
│   ├── Output_Screenshots/
│   │   ├── q2_execution_terminal.png
│   │   └── q2_sorting_distribution_benchmarks.png
│   └── Pseudocode/
│       └── q2_pseudocode.md
│
├── Q3_Karatsuba_Multiplication/
│   ├── Implementation_Code/
│   │   └── q3_karatsuba.py
│   ├── Output_Screenshots/
│   │   ├── q3_execution_terminal.png
│   │   └── q3_karatsuba_vs_naive_operations.png
│   └── Pseudocode/
│       └── q3_pseudocode.md
│
├── Q4_Strassen_Matrix_Multiplication/
│   ├── Implementation_Code/
│   │   └── q4_strassen.py
│   ├── Output_Screenshots/
│   │   ├── q4_execution_terminal.png
│   │   └── q4_strassen_multiplication_savings.png
│   └── Pseudocode/
│       └── q4_pseudocode.md
│
├── Q5_Divide_Conquer_Closest_Pair/
│   ├── Implementation_Code/
│   │   └── q5_closest_pair_dc.py
│   ├── Output_Screenshots/
│   │   ├── q5_closest_pair_scaling_graph.png
│   │   └── q5_execution_terminal.png
│   └── Pseudocode/
│       └── q5_pseudocode.md
│
├── Q6_Advanced_Divide_Conquer/
│   ├── Implementation_Code/
│   │   └── q6_advanced_dc.py
│   ├── Median_of_Medians/
│   │   └── median_of_medians.py
│   ├── Meet_in_the_Middle/
│   │   └── meet_in_the_middle.py
│   ├── Output_Screenshots/
│   │   ├── q6_advanced_dc_scaling_comparison.png
│   │   └── q6_execution_terminal.png
│   └── Pseudocode/
│       └── q6_pseudocode.md
│
├── Q7_Day4_Design_Challenge/
│   ├── Implementation_Code/
│   │   └── q7_day4_challenge.py
│   ├── Joint_Final_Design/
│   │   └── joint_design_specification.md
│   ├── Output_Screenshots/
│   │   ├── q7_execution_terminal.png
│   │   └── q7_kartiq_performance_improvements.png
│   ├── Pseudocode/
│   │   └── q7_pseudocode.md
│   ├── Student_A_Initial_Design/
│   │   └── student_a_proposal.md
│   └── Student_B_Initial_Design/
│       └── student_b_proposal.md
│
├── Final_Report/
│   ├── CO3_Assignment_Report.docx
│   ├── CO3_Assignment_Report.md
│   └── Student_Contribution_Record.docx
│
└── README.md
```

---

## 2. Summary of Questions and Mathematical Results

| Question | Problem & Algorithm | Recurrence Relation | Asymptotic Complexity | Key Benchmark Finding |
| :--- | :--- | :--- | :--- | :--- |
| **Q1** | **Tournament Max-Min & Binary Search** | $T(n) = 2T(n/2) + 2$ | $\Theta(n)$, $1.5n - 2$ cmps | Exactly **25.00% comparison savings** over linear search; Binary Search finds duplicates in $\le 24$ steps. |
| **Q2** | **Merge Sort vs Quick Sort** | $T(n) = 2T(n/2) + \Theta(n)$ | $\Theta(n \log n)$ stable | Merge Sort maintains depth 11 and stability; Quick Sort with first pivot degrades to $O(n^2)$ (1.99M comparisons) on sorted data. |
| **Q3** | **Karatsuba Integer Multiplication** | $T(n) = 3T(n/2) + O(n)$ | $\Theta(n^{1.585})$ | Reduces scalar multiplications by **91.69%** for 1024-digit integers ($87,129$ vs $1,048,576$). |
| **Q4** | **Strassen Matrix Multiplication** | $T(n) = 7T(n/2) + \Theta(n^2)$ | $\Theta(n^{2.8074})$ | Cuts scalar multiplications by **73.69%** for $1024 \times 1024$ matrices ($282.5\text{M}$ vs $1.074\text{B}$). |
| **Q5** | **Closest Pair of Points** | $T(n) = 2T(n/2) + O(n)$ | $\Theta(n \log n)$ | Reduces distance computations by **99.88%** at $n = 2000$ points ($2,248$ vs $1,999,000$). |
| **Q6** | **Advanced D&C (BFPRT & MitM)** | $T(n) \le T(n/5) + T(7n/10) + cn$ | $\Theta(n)$ / $O(2^{n/2} \cdot n)$ | Deterministic linear selection; Meet-in-the-Middle delivers a **$524,288\times$ state space reduction** at $n = 40$. |
| **Q7** | **Day 4 Challenge (KartIQ Platform)** | Multi-pipeline synthesis | Full Platform Engine | Solves 10M order consolidation, 100K live leaderboards, instantaneous lookup, and recommendations. |

---

## 3. How to Run the Source Code & Verify Results

### Prerequisites
- Python 3.10+
- Dependencies: `matplotlib`, `python-docx`
```bash
pip install matplotlib python-docx
```

### Execution Commands
Navigate to the root directory and execute any module:
```bash
# 1. Run Question 1: Max-Min & Binary Search
python CO3_Assignment/Q1_MaxMin_Binary_Search/Implementation_Code/q1_maxmin_binary_search.py

# 2. Run Question 2: Merge Sort & Quick Sort
python CO3_Assignment/Q2_MergeSort_QuickSort/Implementation_Code/q2_mergesort_quicksort.py

# 3. Run Question 3: Karatsuba Multiplication
python CO3_Assignment/Q3_Karatsuba_Multiplication/Implementation_Code/q3_karatsuba.py

# 4. Run Question 4: Strassen Matrix Multiplication
python CO3_Assignment/Q4_Strassen_Matrix_Multiplication/Implementation_Code/q4_strassen.py

# 5. Run Question 5: Closest Pair of Points
python CO3_Assignment/Q5_Divide_Conquer_Closest_Pair/Implementation_Code/q5_closest_pair_dc.py

# 6. Run Question 6: Advanced Divide and Conquer
python CO3_Assignment/Q6_Advanced_Divide_Conquer/Implementation_Code/q6_advanced_dc.py

# 7. Run Question 7: Day 4 Design Challenge
python CO3_Assignment/Q7_Day4_Design_Challenge/Implementation_Code/q7_day4_challenge.py
```

---

## 4. Documentation & Capstone Reports
- **Complete Word Capstone Report:** `Final_Report/CO3_Assignment_Report.docx` (Structured strictly according to the SIMATS Engineering Capstone format).
- **Student Contribution Record:** `Final_Report/Student_Contribution_Record.docx` (Complete responsibility matrix for Student A and Student B).
- **Master Markdown Report:** `Final_Report/CO3_Assignment_Report.md`.
