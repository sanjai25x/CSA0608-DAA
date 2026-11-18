# CSA0608 – Design and Analysis of Algorithms
## Assignment 4A (Part I): Algorithmic Design Through Pseudocode (CO4)

**Institution:** Department of Computer Science and Engineering, SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences (SIMATS), Chennai – 602105  
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: **192511018**)  
**Mode:** Individual Submission | **Total Marks:** 50 Marks  

---

## 1. Repository Organization

```text
CO4_Assignment_4A/
│
├── Source_Code/
│   ├── Task_1/
│   │   ├── task1_fractional_knapsack.py        # Python verification & simulation
│   │   ├── task1_pseudocode.md                 # Diagnosis, repaired pseudocode & design defence
│   │   └── task1_execution_terminal.png        # Execution output screenshot
│   │
│   ├── Task_2/
│   │   ├── task2_job_sequencing.py             # Greedy job sequencing & challenge code
│   │   ├── task2_pseudocode.md                 # Requirement model, greedy rule & desk-check
│   │   └── task2_execution_terminal.png        # Execution output screenshot
│   │
│   ├── Task_3/
│   │   ├── task3_knapsack_dp.py                # 0/1 Knapsack DP with backtracking reconstruction
│   │   ├── task3_pseudocode.md                 # State definition, recurrence & dependency analysis
│   │   ├── task3_dp_table_visualization.png    # DP state matrix heatmap
│   │   └── task3_execution_terminal.png        # Execution output screenshot
│   │
│   ├── Task_4/
│   │   ├── task4_word_break_forensics.py       # Forensics on faulty WordBreak & regression test
│   │   ├── task4_pseudocode.md                 # Exact defect, counterexample & surgical fix
│   │   └── task4_execution_terminal.png        # Execution output screenshot
│   │
│   ├── Task_5/
│   │   ├── task5_shortest_paths.py             # Dijkstra, Bellman-Ford, and Floyd-Warshall
│   │   ├── task5_pseudocode.md                 # Non-negative greedy, negative edge breakdown & APSP
│   │   ├── task5_graph_visualization.png       # Graph topology diagram
│   │   └── task5_execution_terminal.png        # Execution output screenshot
│   │
│   └── Task_6/
│       ├── task6_energy_aware_scheduling.py    # Weighted Interval Scheduling DP & attack test
│       ├── task6_pseudocode.md                 # Stages 1 to 6 complete design challenge
│       ├── task6_scheduling_visualization.png  # Optimal Gantt-style schedule chart
│       └── task6_execution_terminal.png        # Execution output screenshot
│
├── Report/
│   ├── CO4_Assignment_4A_Report.pdf            # PDF Report (Mandated Submission File)
│   ├── CO4_Assignment_4A_Report.docx           # Comprehensive Word Document Report
│   └── CO4_Assignment_4A_Report.md             # Markdown Report
│
└── README.md
```

---

## 2. Summary of Tasks & Algorithmic Results

| Task | Competency Assessed | Strategy / Paradigm | Key Algorithmic Finding |
| :--- | :--- | :--- | :--- |
| **Task 1** | **Algorithm Design Review** | Greedy (Fractional Knapsack) | Diagnosed 6 deficiencies in junior engineer's code. Repaired with value/weight density ordering ($v_i/w_i$), tracking $C_{\text{rem}}$, and fractional division. |
| **Task 2** | **Requirement to Greedy Pseudocode** | Greedy (Job Sequencing) | Modeled constraints, formulated latest-slot greedy rule. Desk-checked on 5 jobs ($\text{Profit} = \$180$). Adversarial modification (Job B profit $= 90$) displaces Job C ($\text{Profit} = \$210$). |
| **Task 3** | **Recurrence to Executable Logic** | Dynamic Programming (0/1 Knapsack) | State $DP[i][w] = \max(DP[i-1][w], DP[i-1][w-w_i] + v_i)$. Desk-checked on 4 items ($W=7$), backtracking selected $\{Q, R\}$ ($\text{Value} = \$45$). Proved forward row dependency. |
| **Task 4** | **Pseudocode Forensics** | DP Debugging (Word Break) | Located missing prefix check. Designed counterexample `Text = "abcat"`, `Dict = {"cat"}` producing False Positive. Surgically added `DP[j] == TRUE` fix. Verified regression on `"applepie"`. |
| **Task 5** | **Graph Optimization Reasoning** | Greedy vs Repeated Relaxation vs APSP | Non-negative Dijkstra from A gives distances `A:0, B:4, C:6, D:7, E:10`. Negative weights break greedy finalizing; Bellman-Ford performs $|V|-1$ passes. Floyd computes APSP via intermediate sets in $\Theta(V^3)$. |
| **Task 6** | **Day-4 Design Challenge** | Dynamic Programming (Weighted Interval) | Modeled cloud data centre energy-aware scheduling. Proved greedy fails. Formulated binary search for $p(i)$ and $DP[i] = \max(DP[i-1], v_i + DP[p(i)])$. Selected $\{J2, J5, J7, J8\}$ ($\text{Energy Saved} = 200$). Proved immunity against adversarial traps ($\text{Value} = 170$). |

---

## 3. How to Run the Source Code & Verify Results

Execute any of the task scripts using Python 3:
```bash
# Task 1: Fractional Knapsack Review
python CO4_Assignment_4A/Source_Code/Task_1/task1_fractional_knapsack.py

# Task 2: Job Sequencing with Deadlines
python CO4_Assignment_4A/Source_Code/Task_2/task2_job_sequencing.py

# Task 3: 0/1 Knapsack Dynamic Programming
python CO4_Assignment_4A/Source_Code/Task_3/task3_knapsack_dp.py

# Task 4: Word Break Forensics
python CO4_Assignment_4A/Source_Code/Task_4/task4_word_break_forensics.py

# Task 5: Shortest Path Algorithms
python CO4_Assignment_4A/Source_Code/Task_5/task5_shortest_paths.py

# Task 6: Day-4 Design Challenge (Energy-Aware Cloud Scheduling)
python CO4_Assignment_4A/Source_Code/Task_6/task6_energy_aware_scheduling.py
```

---

## 4. Reports & Submissions
- **Official Submission PDF:** `Report/CO4_Assignment_4A_Report.pdf`
- **Comprehensive Word Report:** `Report/CO4_Assignment_4A_Report.docx`
- **Full Markdown Documentation:** `Report/CO4_Assignment_4A_Report.md`
