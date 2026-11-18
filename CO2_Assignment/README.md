# CSA0608 – Design and Analysis of Algorithms
## Assignment 2 – Course Outcome 2 (CO2)
### Brute-Force and Exhaustive-Search Strategies: Design, Analysis, and Optimisation for High-Throughput Systems

**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Department:** Department of Computer Science and Engineering  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  

---

## 📌 Repository Organization

This directory is organized strictly according to the assignment requirements:

```text
CO2_Assignment/
│
├── Q1_Sorting_Algorithms/
│   ├── Pseudocode/                     # Pseudocode for Selection, Bubble, and Insertion Sort
│   ├── Implementation_Code/            # Python implementation (q1_sorting_algorithms.py)
│   └── Output_Screenshots/             # Output screenshot & comparison/writes charts
│
├── Q2_Sequential_Search/
│   ├── Pseudocode/                     # Pseudocode for Sequential & Hash Tool Tracking
│   ├── Implementation_Code/            # Python implementation (q2_sequential_search.py)
│   └── Output_Screenshots/             # Positional search output & scaling charts
│
├── Q3_Brute_Force_String_Matching/
│   ├── Pseudocode/                     # Pseudocode for Sliding Window String Matcher
│   ├── Implementation_Code/            # Python implementation (q3_string_matching.py)
│   └── Output_Screenshots/             # Execution output & work variance charts
│
├── Q4_Brute_Force_Closest_Pair/
│   ├── Pseudocode/                     # Pseudocode & mathematical pair-count derivation
│   ├── Implementation_Code/            # Python implementation (q4_closest_pair.py)
│   └── Output_Screenshots/             # Execution output & quadratic SLA breach charts
│
├── Q5_Brute_Force_Convex_Hull/
│   ├── Pseudocode/                     # Geometric derivation, pseudocode & correctness proof
│   ├── Implementation_Code/            # Python implementation (q5_convex_hull.py)
│   └── Output_Screenshots/             # Boundary visualization & cubic growth charts
│
├── Q6_Exhaustive_Search/
│   ├── Pseudocode/                     # Bitmask combinatorial enumeration pseudocode
│   ├── Implementation_Code/            # Python implementation (q6_exhaustive_search.py)
│   └── Output_Screenshots/             # Execution output & combinatorial SLA boundary charts
│
├── Q7_Day4_Design_Challenge/
│   ├── Pseudocode/                     # Adaptive-Axis Sweep-Window Redesign pseudocode
│   ├── Implementation_Code/            # Python implementation (q7_closest_pair_redesign.py)
│   └── Output_Screenshots/             # Validation output & 384.9x speedup charts
│
├── Final_Report/
│   ├── CO2_Assignment_Report.docx       # Master Capstone Report (Word docx, 1.55 MB)
│   └── CO2_Assignment_Report.md         # Master Capstone Report (Markdown)
│
└── README.md                            # Comprehensive CO2 documentation (this file)
```

---

## 🚀 Key Theoretical and Empirical Highlights (Q1 to Q7)

### Q1: Sorting Under Different Data Conditions (n = 1,000 Orders)
- **Nearly Sorted (95% + 5% tail):** Insertion Sort executes in **26,085 comparisons** ($1.95$ ms), outperforming Selection Sort (499,500 comps, $16.18$ ms) and Adaptive Bubble Sort (499,004 comps, $20.17$ ms) by **$10.4\times$**.
- **Reverse-Sorted:** Selection Sort incurs the fewest array writes (**1,000 writes** vs Bubble's 999,000 writes and Insertion's 500,499 writes).
- **Identical Keys:** Bubble and Insertion Sort terminate in **999 comparisons** ($< 0.07$ ms) vs Selection's 499,500 comparisons.
- **Fulfilment Centre Recommendation:** **Deploy Insertion Sort** for online arrival streams.

### Q2: Sequential Search Operating Boundary & Facility Expansion
- Positional Lookups ($n=200$): Front = 1 comp, Middle = 100 comps, Absent = 200 comps.
- Multi-Facility Expansion (1 Hangar $\to$ 20 Facilities):
  - Single Hangar ($n=150, q=400$): $36\,000$ comparisons/day ($1.39$ ms).
  - 20 Facilities ($n=3000, q=8000$): $14\,362\,000$ comparisons/day ($638.5$ ms) — **$398.94\times$ workload surge**!
  - **Recommendation:** Replace list with an in-memory **Hash Table** for $O(1)$ lookups and mutations.

### Q3: Brute-Force String Matching Work Variance (Fixed $n=10,000, m=20$)
- Test 1 (Disjoint First Char): 9,981 comparisons ($0.71$ ms).
- Test 2 (Repeated Prefix Trap): 199,620 comparisons ($10.38$ ms) — **$20.0\times$ more comparisons** on identical dimensions!
- Test 3 (Realistic Syslog Stream): 12,988 comparisons ($0.87$ ms).
- **Insight:** Proves input size alone is insufficient for runtime prediction; alphabet entropy and prefix overlap govern practical throughput.

### Q4: Closest Pair Quadratic Scaling vs Real-Time SLA
- Mathematical Derivation: $P(n) = \sum_{i=0}^{n-2} (n - 1 - i) = \frac{n(n-1)}{2} = \Theta(n^2)$.
- Real-Time SLA: **$\le 50$ ms** (for 10 Hz drone telemetry).
- **SLA Breach:** Occurs at $n = 1,000$ drones ($52.42$ ms, 499,500 distance calculations). At $n = 4,000$, runtime balloons to **$805.97$ ms** ($16\times$ over budget).

### Q5: Convex Hull Derived from Geometric Principle
- Formulated boundary acceptance from the half-plane separation principle.
- Projection filter cleanly eliminated all collinear subsegments along boundary lines and filtered near-edge interior traps at $(500, 102)$ and $(848, 550)$ just 2m inside the boundary.
- Proved correctness via supporting hyperplanes and interior chord crossing.

### Q6: Exhaustive Search Combinatorial Growth (0/1 Knapsack)
- On $n=4, W=10$ kg, exhaustive bitmask enumeration verified global optimum {PKG-2, PKG-3} ($W=10, V=48$), beating greedy selection ($V=38$) by **+10 points**.
- Scaling: $n=4$ ($0.005$ ms) $\to n=16$ ($54.3$ ms) $\to n=22$ ($4\,806$ ms).
- Under a 5.0 s flight dispatch SLA, **$n_{\text{max}} = 22$ packages** is the strict maximum deployment limit.

### Q7: Day-4 Design Challenge – Closest Pair Redesign
- Diagnosed bottleneck: Blind $O(n^2)$ pair scanning and redundant floating-point `sqrt()`.
- Engineered **Adaptive-Axis Sweep-Window Algorithm**:
  1. Primary-axis spread detection in $O(n)$
  2. Primary-axis sorting in $O(n \log n)$
  3. Monotonic sweep-window pruning ($> 99.8\%$ check reduction)
  4. Secondary-axis 1D bounding box rejection
  5. Single deferred square root
- **Validation Results:**
  - At $n = 1,000$: Q4 = 499,500 pairs ($50.73$ ms) vs Q7 = 2,462 checks ($0.581$ ms) $\to \mathbf{87.3\times \text{ speedup}}$.
  - At $n = 4,000$: Q4 = 7,998,000 pairs ($817.34$ ms) vs Q7 = 7,589 checks, 9 full calcs ($2.124$ ms) $\to \mathbf{384.9\times \text{ speedup}}$!
  - **Latency:** $2.12$ ms, operating **$23\times$ comfortably below the 50 ms real-time SLA**.

---

## 🛠️ Execution and Verification

### Execute Individual Problem Scripts:
```powershell
python CO2_Assignment/Q1_Sorting_Algorithms/Implementation_Code/q1_sorting_algorithms.py
python CO2_Assignment/Q2_Sequential_Search/Implementation_Code/q2_sequential_search.py
python CO2_Assignment/Q3_Brute_Force_String_Matching/Implementation_Code/q3_string_matching.py
python CO2_Assignment/Q4_Brute_Force_Closest_Pair/Implementation_Code/q4_closest_pair.py
python CO2_Assignment/Q5_Brute_Force_Convex_Hull/Implementation_Code/q5_convex_hull.py
python CO2_Assignment/Q6_Exhaustive_Search/Implementation_Code/q6_exhaustive_search.py
python CO2_Assignment/Q7_Day4_Design_Challenge/Implementation_Code/q7_closest_pair_redesign.py
```

### Regenerate All Verification Plots & Output Screenshots:
```powershell
python CO2_Assignment/generate_co2_visuals.py
```

### Regenerate Master Capstone Report (.docx):
```powershell
python CO2_Assignment/generate_co2_report_docx.py
```
