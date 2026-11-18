# SIMATS ENGINEERING
## Saveetha Institute of Medical and Technical Sciences
### Department of Computer Science and Engineering
### CSA0608 – Design and Analysis of Algorithms
# COURSE OUTCOME 4 – ASSIGNMENT 4B (PART II)
## ALGORITHM ENGINEERING: IMPLEMENT, TEST, DEBUG & OPTIMISE
### Dynamic Programming and Greedy Strategies for Real-World Engineering Systems

---

**Student Name:** SANJAI S  
**Register Number:** 192511018  
**Department:** Computer Science and Engineering, SIMATS Engineering  
**Academic Year:** 2026–2027  
**Total Marks:** 50 | **Nature of Assignment:** Individual Submission  

---

## Executive Summary
This laboratory capstone report delivers the complete algorithmic engineering, empirical validation, adversarial debugging, and architectural trade-off analysis for Course Outcome 4 (Assignment 4B). We build upon the pseudocode designs established in Part I, translating them into six fully instrumented, production-grade optimization engines:
1. **Task 1: Word Wrap Document Layout Engine** (Dynamic Programming with cubic slack penalty)
2. **Task 2: Greedy vs Dynamic Programming Knapsack** (Fractional vs 0/1 Knapsack, adversarial trap exposure, and FPTAS analysis)
3. **Task 3: Network Routing Engine Under Adverse Conditions** (Dijkstra failure proof, Bellman-Ford negative cycle detection, Floyd APSP, and Warshall reachability)
4. **Task 4: Smart Manufacturing Assembly Line Scheduling** (Linear-time DP engine, stay-vs-transfer decision exposure, and disruption handling)
5. **Task 5: Three Greedy Engineers, One Network** (Kruskal vs Prim vs Borůvka on non-unique MST graphs and deployment selection)
6. **Task 6: Last-Mile Delivery Route Optimisation** (Held-Karp TSP DP, brute-force validation, state-space growth benchmark, and reflection)

---

## Task 1: Build and Validate a Dynamic Programming Solution (8 Marks)
### Word Wrap as a Document-Layout Engine

### 1.1 Mathematical Model & Recurrence
Given a sequence of words $w_1, w_2, \dots, w_n$ with lengths $l_1, l_2, \dots, l_n$ and maximum line width $M$:
The length of placing words $i$ through $j$ on a single line (with single space separation) is:
$$L(i, j) = \sum_{k=i}^j l_k + (j - i)$$

The line penalty function $P(i, j)$ is defined as:
$$P(i, j) = \begin{cases} (M - L(i, j))^3 & \text{if } j < n \text{ and } L(i, j) \le M \\ 0 & \text{if } j = n \text{ and } L(i, j) \le M \quad (\text{Final line carries zero penalty}) \\ \infty & \text{if } L(i, j) > M \quad (\text{Line overflow is strictly prohibited}) \end{cases}$$

The optimal substructure recurrence is:
$$DP[0] = 0$$
$$DP[j] = \min_{1 \le i \le j} \{ DP[i - 1] + P(i, j) \}$$
$$\text{Choice Pointer: } parent[j] = \arg\min_{1 \le i \le j} \{ DP[i - 1] + P(i, j) \}$$

### 1.2 Execution Results (Base Width $M = 26$)
- **Document Text:** *"Buffering and layout management require rigorous dynamic programming to balance aesthetic readability"* (12 words)
- **Minimum Total Layout Penalty:** **1,792**
- **Total Lines Generated:** 5

| Line | Words Formatted on Line | Used Chars | Unused Slack | Penalty Contributed |
| :--- | :--- | :---: | :---: | :--- |
| **L1** | Buffering and layout | 20 | 6 chars | $6^3 = 216$ |
| **L2** | management require | 18 | 8 chars | $8^3 = 512$ |
| **L3** | rigorous dynamic | 16 | 10 chars | $10^3 = 1000$ |
| **L4** | programming to balance | 22 | 4 chars | $4^3 = 64$ |
| **L5** | aesthetic readability | 21 | 5 chars | **0 (Final Line)** |

### 1.3 Requirement Change & Multi-Width Benchmark
The layout engine was evaluated across three distinct line widths: $M = 20, 25, 30$:
- **At $M = 20$:** Forced narrow layout resulting in 8 lines, total penalty = **1,100**.
- **At $M = 25$:** Snug packaging yielding 6 lines, total penalty = **505** (lowest penalty).
- **At $M = 30$:** Wider lines accommodating 4–6 words per line, yielding 5 lines, total penalty = **819**.
  - *Engineering Insight:* While total lines decreased from 6 to 5, the penalty increased from 505 to 819 because Line 3 had unused slack of 8 ($8^3 = 512$). This confirms the non-linear sensitivity of cubic penalty functions!

### 1.4 Boundary Testing
1. **Exact Match Test ($L_i = M$):** Word length exactly matching line width ($M=15$) left 0 unused spaces, producing penalty $0^3 = 0$.
2. **Oversized Word Guard ($L_i > M$):** An unsplittable word of length 49 submitted to $M=20$ triggered an immediate `ValueError: Word length exceeds maximum line width`, preventing index out-of-bounds corruption.

![Task 1 Word Wrap Analysis](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_1/task1_word_wrap_analysis.png)

---

## Task 2: Greedy vs Dynamic Programming (9 Marks)
### Build It, Break It, Explain It

### 2.1 Normal Case: Fractional Knapsack (Greedy Optimum)
In freight logistics with divisible cargo (Capacity $W = 60$ kg), items are sorted by density ratio $v_i / w_i$:
- **PKG-A:** 10 kg, $60.00 $\implies$ Ratio 6.00 $/kg $\implies$ **100% Loaded**
- **PKG-B:** 20 kg, $100.00 $\implies$ Ratio 5.00 $/kg $\implies$ **100% Loaded**
- **PKG-C:** 30 kg, $120.00 $\implies$ Ratio 4.00 $/kg $\implies$ **100% Loaded**
- **Total Loaded:** 60 kg (100% Capacity), **Optimal Value Achieved:** **$280.00**.

### 2.2 Breaking Greedy Intuition: Adversarial 0/1 Counterexample
When cargo is strictly indivisible (0/1 Knapsack), greedy density sorting fails. We designed an adversarial instance with Capacity $W = 50$ kg:
- **ITEM-1:** Weight = 10 kg, Value = $60.00 (Density = 6.00 $/kg)
- **ITEM-2:** Weight = 20 kg, Value = $100.00 (Density = 5.00 $/kg)
- **ITEM-3:** Weight = 30 kg, Value = $120.00 (Density = 4.00 $/kg)

| Algorithm | Selected Items | Total Weight Loaded | Unused Capacity | Total Value Achieved | Optimality Gap |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Greedy 0/1 Heuristic** | {ITEM-1, ITEM-2} | 30 kg | 20 kg | **$160.00** | Sub-optimal (-$60.00) |
| **Dynamic Programming (0/1)** | {ITEM-2, ITEM-3} | 50 kg | 0 kg | **$220.00** | **Exact Mathematical Optimum** |

**Identification of the First Greedy Commitment Trap:**
Greedy commits ITEM-1 due to its highest ratio (6.00 $/kg), leaving 40 kg remaining. Next, it commits ITEM-2 (20 kg), leaving 20 kg remaining. When evaluating ITEM-3 (30 kg), it cannot fit! Greedy is trapped into taking only {ITEM-1, ITEM-2} yielding $160.00. Dynamic Programming evaluates combinations and selects {ITEM-2, ITEM-3}, achieving $220.00. The commitment to ITEM-1 was an irrevocable trap, resulting in a **27.3% value loss**.

### 2.3 Engineering Comparison & Changed Requirement (FPTAS)
| Dimension | Solution A (Greedy Heuristic) | Solution B (Dynamic Programming) |
| :--- | :--- | :--- |
| **Theoretical Time** | $O(n \log n)$ sorting | $\Theta(n \cdot W)$ pseudo-polynomial |
| **Computational Work** | 19 sorting/scan comparisons | 153 table state evaluations |
| **Auxiliary Memory** | $O(1)$ auxiliary (656 bytes) | $\Theta(n \cdot W)$ table (1,944 bytes) |
| **Optimality Guarantee** | Exact (Fractional only); Bounded for 0/1 | Guaranteed Global Optimum (0/1) |
| **Decision Latency** | $< 0.05$ milliseconds | Scales with capacity $W$ |

**Management Mandate (Rapid Decision Required):**
When $W$ scales to 100,000 and $n = 5,000$, DP requires 500 million operations (~500 MB memory), violating real-time SLAs. We recommend:
1. **Modified Greedy Heuristic:** $\max(\text{Greedy-0/1}, \text{Single Max Item})$, providing a guaranteed 2-approximation ($\ge 50\%$ optimal) in $O(n \log n)$ sub-millisecond time.
2. **FPTAS:** Scales values by $K = \frac{\epsilon \cdot V_{\max}}{n}$, running DP on scaled values in $O(n^3 / \epsilon)$ time to achieve $(1 - \epsilon)$-approximation.

![Task 2 Knapsack Comparison](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_2/task2_knapsack_comparison.png)

---

## Task 3: Routing Engine Under Changing Network Conditions (10 Marks)
### Dijkstra + Bellman-Ford + Floyd + Warshall

### 3.1 Network Topology & Stage A Normal Routing
Network consists of 8 vertices $\{A, B, C, D, E, F, G, H\}$ and 13 directed edges.
Dijkstra's SSSP from Source $A$:
- **Finalization Sequence:** $A(0.0) \to B(2.0) \to D(3.0) \to C(5.0) \to E(7.0) \to F(7.0) \to G(9.0) \to H(12.0)$.
- **Reconstructed Shortest Paths:**
  - $A \to B$ (Cost: 2.0)
  - $A \to C$ (Cost: 5.0)
  - $A \to B \to D$ (Cost: 3.0)
  - $A \to C \to E$ (Cost: 7.0)
  - $A \to B \to D \to F$ (Cost: 7.0)
  - $A \to B \to D \to G$ (Cost: 9.0)
  - $A \to B \to D \to G \to H$ (Cost: 12.0)

### 3.2 Stage B: Negative Edge Insertion & Dijkstra Failure Proof
**Intervention:** Directed edge $E \to D$ with negative weight $-6.0$ was inserted. Graph remains strictly acyclic.
- **Prediction:** Dijkstra will FAIL. It finalizes $D$ at distance 3.0 via $A \to B \to D$ before evaluating $E$ (dist 7.0). Once finalized, $D$ is never re-evaluated. However, path $A \to C \to E \to D$ has cost $5 + 2 - 6 = 1.0 < 3.0$.
- **Experimental Verification:**
  - **Node D:** Dijkstra reports **3.0** | Bellman-Ford finds **1.0** $\implies$ **Dijkstra Failed!**
  - **Node F:** Dijkstra reports **7.0** | Bellman-Ford finds **5.0** $\implies$ **Dijkstra Failed!**
  - **Node G:** Dijkstra reports **9.0** | Bellman-Ford finds **7.0** $\implies$ **Dijkstra Failed!**
  - **Node H:** Dijkstra reports **12.0** | Bellman-Ford finds **10.0** $\implies$ **Dijkstra Failed!**

### 3.3 Stage C: Reachable Negative Cycle Detection
**Intervention:** Edge $F \to E (-1.0)$ inserted, creating directed cycle $E \to D (w=-6.0) \to F (w=4.0) \to E (w=-1.0)$ with cycle sum $-3.0 < 0$.
- **Detection:** Bellman-Ford relaxed all edges for $|V|-1 = 7$ passes. On the 8th pass, distance to $D$ could still be decreased. The engine detected the cycle, extracted vertices $E \to D \to F \to E$, and safely raised an alarm to abort route dispatch.

### 3.4 Stage D: Floyd's APSP & Warshall's Transitive Closure
Floyd's algorithm generated the complete $8 \times 8$ distance matrix in $\Theta(|V|^3)$ operations, while Warshall's algorithm generated the boolean reachability matrix, enabling $O(1)$ reachability checks for logistics dispatch.

![Task 3 Routing Analysis](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_3/task3_routing_analysis.png)

---

## Task 4: Smart Manufacturing Optimisation (7 Marks)
### Assembly Line Scheduling Dynamic Programming

### 4.1 Base Optimization Engine & Route Flow
Two parallel lines with 6 stations, entry times $e_1=2, e_2=4$, exit times $x_1=3, x_2=2$:
- **Minimum Production Time:** **38 time units**
- **Optimal Route:**
  $$\text{Entry} \to \text{L1-S1} \xrightarrow{\text{Trans}} \text{L2-S2} \xrightarrow{\text{Trans}} \text{L1-S3} \xrightarrow{\text{Trans}} \text{L2-S4} \to \text{L2-S5} \xrightarrow{\text{Trans}} \text{L1-S6} \to \text{Exit}$$

### 4.2 Intermediate DP Decision Exposure (Stay vs Transfer)
| Station | L1 Stay | L1 Trans | L1 Choice | L2 Stay | L2 Trans | L2 Choice |
| :---: | :---: | :---: | :--- | :---: | :---: | :--- |
| **St 2** | 18 | 23 | **STAY (L1)** | 17 | 16 | **TRANSFER (from L1)** |
| **St 3** | 21 | 20 | **TRANSFER (from L2)** | 22 | 27 | **STAY (L2)** |
| **St 4** | 24 | 28 | **STAY (L1)** | 26 | 25 | **TRANSFER (from L1)** |
| **St 5** | 32 | 35 | **STAY (L1)** | 30 | 32 | **STAY (L2)** |
| **St 6** | 36 | 35 | **TRANSFER (from L2)** | 37 | 43 | **STAY (L2)** |

### 4.3 Disruption Handling & 3-Line Extension
1. **Transfer Penalty Spike:** Increasing transfer penalty $t_1[0]$ from 2 to 25 eliminated the early transfer, shifting the route to enter Line 1 and stay until Station 4, raising total time to 39.
2. **Machine Slowdown:** Surging Line 2 Station 5 processing time from 5 to 22 caused the DP to automatically divert production to Line 1 at Station 5 ($a_1[4]=8$).
3. **Generalization to 3 Lines:** State representation becomes $DP[3][n+1]$. Recurrence:
   $$f_i[j] = \min_{1 \le k \le 3} (f_k[j-1] + t_{k,i}[j-1]) + a_i[j-1]$$
   Complexity scales to $O(M^2 n)$, remaining strictly linear with respect to stations.

![Task 4 Assembly Line Route](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_4/task4_assembly_line_route.png)

---

## Task 5: Three Greedy Engineers, One Network (7 Marks)
### Kruskal + Prim + Borůvka

### 5.1 Stress Testing: Non-Unique Edge Weights & Multiple MSTs
On a network containing symmetric weight ties (cycle $A-B-C$ with weight 2.0, and dual connections to $H$ of weight 4.0):
- **Kruskal's Algorithm:** Total Cost = **19.0** | Edges: `(D-E:1), (B-C:2), (A-C:2), (F-G:2), (E-F:3), (G-H:4), (B-D:5)`
- **Prim's Algorithm:** Total Cost = **19.0** | Edges: `(A-B:2), (A-C:2), (B-D:5), (D-E:1), (E-F:3), (F-G:2), (F-H:4)`
- **Borůvka's Algorithm:** Total Cost = **19.0** | Edges: `(B-C:2), (A-C:2), (D-E:1), (F-G:2), (G-H:4), (B-D:5), (E-F:3)`

**Can algorithms return different edge sets while all still being correct?**
**YES!** Kruskal and Prim returned different edge sets (`Kruskal == Prim: False`), yet both are valid Minimum Spanning Trees with identical total weight of 19.0. Kruskal broke ties by edge list order, while Prim broke ties by priority queue insertion order from root $A$.

### 5.2 Industry Architecture Deployment Decisions
| Target Environment | Recommended Algorithm | Architectural & Hardware Justification |
| :--- | :--- | :--- |
| **Sparse Network ($E \approx V$)** | Kruskal's Algorithm | Sorts $E$ edges in $O(E \log V)$ with near $O(1)$ DSU operations; minimal memory overhead. |
| **Dense Network ($E \approx V^2$)** | Prim's (Adjacency Matrix) | Runs in $O(V^2)$, completely eliminating priority queue heap overhead and cache misses. |
| **Distributed Cloud Cluster** | Borůvka's Algorithm | Components contract in parallel; perfectly fits MapReduce/Spark distributed graphs. |

![Task 5 MST Comparison](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_5/task5_mst_comparison.png)

---

## Task 6: Last-Mile Delivery Route Optimisation (9 Marks)
### Travelling Salesperson Problem Using Dynamic Programming (Held-Karp)

### 6.1 Computational Model & State Space Design
- **Why Current Location (j) Alone Fails:** A state $(j)$ cannot record which customers remain unvisited. To guarantee a valid Hamiltonian cycle, the state must retain both the current location $j$ and the visited subset $S \subseteq V$.
- **Held-Karp Recurrence:**
  $$DP[S][j] = \min_{k \in S \setminus \{j\}} (DP[S \setminus \{j\}][k] + C[k][j]), \quad DP[\{0\}][0] = 0$$
  $$\text{Final Tour Cost: } \text{OPT} = \min_{j \in V, j \ne 0} (DP[V][j] + C[j][0])$$

### 6.2 Validation (Hub + 4 Delivery Locations)
- **Brute Force (4! = 24 perms):** Tour `Hub -> A -> B -> C -> D -> Hub`, Cost = **58.0 km**.
- **Held-Karp DP (57 states):** Tour `Hub -> D -> C -> B -> A -> Hub`, Cost = **58.0 km** (Exact match confirmed).

### 6.3 Route Prototype (1 Hub + 6 Delivery Locations, N = 7)
- **Optimal Route:** `Central-Hub -> Loc-D -> Loc-E -> Loc-F -> Loc-C -> Loc-B -> Loc-A -> Central-Hub`
- **Minimum Travel Cost:** **75.0 km** (Evaluated in 493 states).

### 6.4 Empirical State-Space Growth Benchmark ($N = 4 \dots 10$)
| Locations ($N$) | DP States Evaluated | Execution Time (ms) | Memory Consumed | Brute Force Permutations |
| :---: | :---: | :---: | :---: | :---: |
| **4** | 19 | 0.016 ms | 1,592 bytes | 6 |
| **5** | 57 | 0.022 ms | 3,384 bytes | 24 |
| **6** | 171 | 0.043 ms | 7,224 bytes | 120 |
| **7** | 493 | 0.124 ms | 15,416 bytes | 720 |
| **8** | 1,359 | 0.232 ms | 32,920 bytes | 5,040 |
| **9** | 3,601 | 0.605 ms | 69,752 bytes | 40,320 |
| **10** | 9,235 | 1.495 ms | 148,120 bytes | 362,880 |

### 6.5 Scaling to 200 Locations
At $N = 200$, the state space contains $2^{200} \approx 1.6 \times 10^{60}$ subsets, rendering exact DP impossible. We propose:
- **Nearest Neighbor + 2-Opt / 3-Opt Local Search** ($O(N^2)$).
- **Christofides' Algorithm** ($1.5$-approximation on metric TSP in $O(N^3)$).
- **Trade-off:** Accepting $\approx 2\%$ bounded suboptimality in exchange for instant 2-second route generation.

### 6.6 Technical Reflection (Mandated $\le 150$ Words)
> *"Dynamic Programming achieves dramatic efficiency gains over brute force by memoizing overlapping subproblems, reducing TSP from O(N!) to O(N^2 * 2^N). However, DP scalability is strictly bounded by its state-space representation. For TSP, the Markovian property fails without retaining the unvisited customer set; hence, the state requires a subset S. Because the power set grows exponentially as 2^N, our empirical benchmarks show memory and operations doubling with every increment in N. While polynomial DP succeeds for problems with linear states like Assembly Line Scheduling (O(N)) or Word Wrap (O(N^2)), it cannot overcome the fundamental combinatorial explosion of NP-hard problems with subset-based states. DP optimizes overlapping subproblem traversal, but it does not alter the underlying exponential dimensionality of the state space itself."*  
> **(Word Count: 121 words — Compliant with $\le 150$ words requirement)**

![Task 6 TSP State Growth](file:///C:/Users/SANJAI/.gemini/antigravity/scratch/CSA0608-DAA/CO4_Assignment_4B/Source_Code/Task_6/task6_tsp_state_growth.png)

---

## Conclusion
CO4 Assignment 4B successfully completes the full algorithm engineering life cycle. Through rigorous implementation, instrumentation, and adversarial testing, we demonstrated that:
1. Greedy heuristics offer exceptional speed but require the matroid greedy-choice property to guarantee optimality.
2. Dynamic Programming provides mathematical optimality through memoized subproblem reuse, but its scalability is fundamentally bounded by the dimensionality of its state space.
3. Defensive engineering (cycle detection, boundary checks, input assertions) is mandatory when deploying optimization algorithms to production environments.
