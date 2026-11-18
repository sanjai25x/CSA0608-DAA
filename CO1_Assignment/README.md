# CSA0608 – Design and Analysis of Algorithms
## Assignment 1 – Course Outcome 1 (CO1)
### Design, Analyse and Validate an Efficient Search Strategy for a Large-Scale Student Record System

**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Department:** Computer Science and Engineering  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  

---

## 📌 Repository Organization

This repository is organized strictly according to the course submission requirements:

```
CO1_Assignment/
│
├── Task_1_Algorithm_Design/               # Algorithm designs, pseudocode, strategies
├── Task_2_Basic_Operation/                 # Identification and justification of basic operations
├── Task_3_Mathematical_Complexity/         # Mathematical derivations and formulas
├── Task_4_Case_Analysis/                   # Best, average, and worst-case analysis
├── Task_5_Asymptotic_Analysis/             # Asymptotic bounds (O, Ω, Θ) and growth rates
├── Task_6_Recurrence_Formulation/          # Formal recurrence formulation from code
├── Task_7_Recurrence_Solution/             # Iteration, Master Theorem, and Induction proofs
├── Task_8_Implementation_Testing/          # Testing architecture and documentation
│   └── Source_Code/                        # Python implementations & benchmarks
│       ├── linear_search.py
│       ├── iterative_binary_search.py
│       ├── recursive_binary_search.py
│       ├── hash_search.py
│       ├── test_cases.py
│       ├── benchmark.py
│       └── benchmark_results.json
├── Task_9_Experimental_Performance/        # Experimental tables, measurements, and figures
├── Task_10_Theory_vs_Experiment/           # Critical theory vs empirical behavior comparison
├── Task_11_Final_Recommendation/           # Technically justified baseline recommendation
├── Task_12_Design_Challenge/               # Complete Day-4 Challenge (Parts A, B, C, D)
├── Report/
│   ├── Source_Code_Screenshots/            # Rendered source code screenshots
│   ├── Output_Screenshots/                 # Terminal benchmark & test execution screenshots
│   ├── Analysis/                           # In-depth theoretical and architectural documents
│   ├── Tables_and_Graphs/                  # High-resolution matplotlib empirical plots
│   └── Documentation/                      # Master Capstone Report (.docx & .md)
│       ├── CSA0608_CO1_Assignment_Report.docx
│       └── CSA0608_CO1_Assignment_Report.md
└── README.md                               # This documentation file
```

---

## 🚀 Key Theoretical and Empirical Highlights

### 1. Algorithmic Complexity Comparison

| Algorithm | Strategy | Best Case | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Iterative Linear Search** | Sequential Scan | $\Theta(1)$ | $\Theta(n)$ | $\Theta(n)$ | $\Theta(1)$ |
| **Iterative Binary Search** | Iterative Divide-and-Conquer | $\Theta(1)$ | $\Theta(\log n)$ | $\Theta(\log n)$ | $\Theta(1)$ |
| **Recursive Binary Search** | Recursive Divide-and-Conquer | $\Theta(1)$ | $\Theta(\log n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ stack |
| **Hash Table Lookup** | Direct Addressing / Hashing | $\Theta(1)$ | Expected $\Theta(1)$ | $O(n)$ | $\Theta(n)$ |

### 2. Experimental Benchmark Results (Worst-Case Target Key $n$)

| Dataset Size ($n$) | Linear Search Comps | Linear Time (s) | Binary Search Comps | Binary Time (s) | Hash Table Comps | Hash Time (s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1,000** | $1\,000$ | $0.00005218$ s | $10$ | $0.00000218$ s | $1$ | $0.00000080$ s |
| **10,000** | $10\,000$ | $0.00036506$ s | $14$ | $0.00000228$ s | $1$ | $0.00000100$ s |
| **100,000** | $100\,000$ | $0.00349770$ s | $17$ | $0.00002724$ s | $1$ | $0.00000140$ s |
| **1,000,000** | $1\,000\,000$ | $0.03189313$ s | **20** | **0.00000700 s** | **1** | **0.00000340 s** |

*Verification:*  
- At $n = 1\,000\,000$, Linear Search requires **$1\,000\,000$ comparisons**, whereas Binary Search requires only **$20$ comparisons**—a **$50\,000 \times$ reduction** in basic operations!

---

## ⚡ Day-4 Design Challenge Summary
**Scenario:** The university needs to process **50,000 search requests per hour** on a database containing **1,000,000 student records**, with new records added **only once per day**.

### Hourly Workload Comparison:
- **Linear Search:** $50\,000 \times 1\,000\,000 = \mathbf{50 \text{ Billion comparisons/hour}}$, taking $\approx 13.3$ minutes of 100% single-core CPU time.
- **Iterative Binary Search:** $50\,000 \times 20 = \mathbf{1 \text{ Million comparisons/hour}}$, taking $0.35$ seconds of CPU time.
- **Hash Table Search:** $50\,000 \times 1 = \mathbf{50\,000 \text{ comparisons/hour}}$, taking $0.17$ seconds of CPU time.

**Decision: MODIFY** to a **High-Performance Hybrid Architecture**:
- In-memory Hash Table index for $O(1)$ point lookups.
- Sorted array view retained for range queries and cohort reports.
- Off-peak daily batch updates ($< 1.5$ ms insertion time).

---

## 🛠️ Reproducibility and Execution

### Running Unit Tests:
```powershell
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/test_cases.py
```

### Running Experimental Benchmarks:
```powershell
python CO1_Assignment/Task_8_Implementation_Testing/Source_Code/benchmark.py
```

### Regenerating Visual Plots:
```powershell
python CO1_Assignment/generate_graphs_and_visuals.py
```

### Regenerating Master Capstone Report (.docx):
```powershell
python CO1_Assignment/generate_capstone_report_docx.py
```
