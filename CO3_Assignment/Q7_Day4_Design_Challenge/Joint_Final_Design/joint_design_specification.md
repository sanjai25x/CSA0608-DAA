# Day 4 Design Challenge - Joint Final Design Specification
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Project:** KartIQ Retail Data Analytics Platform – Divide-and-Conquer Engine  
**Team Members:**  
- **Student A:** Sanjai S (192511018)  
- **Student B:** Pair Partner  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences

---

## 1. Executive Summary & Problem Synthesis
KartIQ processes **10,000,000 orders daily**, updates **100,000 live seller ranks**, serves **sub-millisecond order lookups**, and calculates personalized **$1024 \times 1024$ recommendation matrices**. 

Through a peer review of Student A's and Student B's initial proposals, the joint team recognized that no single algorithm solves all bottlenecks. The unified KartIQ Engine synthesizes four specialized Divide-and-Conquer modules into an integrated data processing pipeline:

```
                                  [Incoming Stream of 10M Orders]
                                                 │
                                                 ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │ Module 1: Stable External Merge Sort (Student A Lead)                  │
             │ • Preserves timestamp arrival order for audit compliance               │
             │ • Complexity: O(n log n) | Max Cmps: 230,000,001 | RAM: 320 MB buffer  │
             └───────────────────────────────────┬────────────────────────────────────┘
                                                 │
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                 ▼
     ┌─────────────────────────────────────┐           ┌─────────────────────────────────────┐
     │ Module 2: Live Leaderboard          │           │ Module 3: Instant Order Lookup      │
     │ Median-of-Three Introsort           │           │ Lower-Bound Binary Search           │
     │ (Student B Lead)                    │           │ (Student B Lead)                    │
     │ • 100K nearly-sorted sellers        │           │ • 10M sorted consolidated orders    │
     │ • Avoids O(n^2) freezing            │           │ • Exact chronological duplicate res │
     │ • In-place: O(log n) stack space    │           │ • Max 24 steps vs 10M linear scans  │
     └─────────────────────────────────────┘           └─────────────────────────────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 │
                                                 ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │ Module 4: Real-Time Stream Analytics & Personalization                 │
             │ ├─ Tournament Max-Min Engine (Student A): 3n/2 - 2 (25% saving)        │
             │ └─ Hybrid Strassen Matrix Engine (Student B): 73.69% mult reduction    │
             └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Integrated Architectural Matrix

| Pipeline Module | Selected Algorithm | Primary Responsibility | Time Complexity | Auxiliary Space | Key Performance Metric |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Module 1: Order Consolidation** | Stable Two-Way Merge Sort | Student A | $\Theta(n \log n)$ | $O(n)$ ($320\text{ MB}$) | Exact stability on equal timestamps; eliminates audit discrepancies |
| **Module 2: Live Seller Leaderboard** | Improved Median-of-3 Quick Sort (Introsort) | Student B | Avg $\Theta(n \log n)$, Worst $O(n \log n)$ | $O(\log n)$ (in-place) | Cuts comparisons from $\sim 5\text{ Billion}$ to $1.66\text{ Million}$ on nearly-sorted data |
| **Module 3: Order Retrieval** | Lower-Bound Modified Binary Search | Student B | $\Theta(\log n)$ | $O(1)$ | Worst-case $\le 24$ iterations for $10\text{M}$ records ($99.99976\%$ reduction) |
| **Module 4A: Extremes Detection** | Tournament Tree Max-Min Engine | Student A | $\Theta(n)$ | $O(\log n)$ recursion | Comparisons $= 1.5n - 2$ ($25\%$ comparison savings over linear) |
| **Module 4B: Recommendation Scoring** | Hybrid Strassen's Matrix Multiplier | Student B & A | $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$ | $O(n^2)$ block buffers | Reduces scalar multiplications by $73.69\%$ on $1024 \times 1024$ matrices |

---

## 3. Mathematical Recurrence Formulations & Proofs

### 3.1 Module 1: Merge Sort Recurrence
$$T(n) = 2T\left(\frac{n}{2}\right) + c \cdot n, \quad T(1) = d$$
Applying Master Theorem: $a = 2, b = 2, f(n) = cn$. Since $n^{\log_2 2} = n = \Theta(f(n))$, Case 2 yields:
$$T(n) = \Theta(n \log_2 n)$$
Tight worst-case comparisons for $n = 10^7$:
$$C(n) = n \lceil \log_2 n \rceil - 2^{\lceil \log_2 n \rceil} + 1 \approx 230,000,001 \text{ comparisons}$$

### 3.2 Module 2: Median-of-Three Introsort
Balanced partitioning produces recurrence:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n) \implies \Theta(n \log n)$$
Median-of-three guarantees that the pivot is bounded away from extremes:
$$\text{Rank}(pivot) \in [n/4, 3n/4] \implies T(n) \le T(n/4) + T(3n/4) + cn = O(n \log n)$$
If recursion depth breaches $2 \lfloor \log_2 n \rfloor \approx 34$, the engine switches to Heapsort, guaranteeing an absolute upper bound of $O(n \log n)$ and preventing any worst-case quadratic disaster.

### 3.3 Module 3: Lower-Bound Binary Search
$$T(n) = T\left(\frac{n}{2}\right) + \Theta(1)$$
By Master Theorem Case 2 ($a = 1, b = 2, f(n) = 1$):
$$T(n) = \Theta(\log_2 n)$$
Maximum steps: $\lfloor \log_2(10^7) \rfloor + 1 = 23 + 1 = 24$.

### 3.4 Module 4A: Tournament Max-Min
$$T(n) = 2T\left(\frac{n}{2}\right) + 2, \quad T(2) = 1, \quad T(1) = 0$$
Using induction for $n = 2^k$:
$$T(n) = 2^{k-1} T(2) + \sum_{i=1}^{k-1} 2^i = \frac{n}{2}(1) + 2(n - 2) = \frac{3n}{2} - 2$$
Versus naive linear search ($2n - 2$), the savings is:
$$\text{Savings} = \frac{(2n - 2) - (1.5n - 2)}{2n - 2} = \frac{0.5n}{2n - 2} \approx 25.00\%$$

### 3.5 Module 4B: Strassen Matrix Multiplication
$$T(n) = 7T\left(\frac{n}{2}\right) + \Theta(n^2)$$
Applying Master Theorem: $a = 7, b = 2, f(n) = \Theta(n^2)$.
Since $n^{\log_2 7} \approx n^{2.8074} > n^2$, Master Theorem Case 1 applies:
$$T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.8074})$$
For $n = 1024 = 2^{10}$:
$$\text{Conventional Multiplications} = 1024^3 = 1,073,741,824$$
$$\text{Strassen Multiplications} = 7^{10} = 282,475,249$$
$$\text{Reduction} = \frac{1,073,741,824 - 282,475,249}{1,073,741,824} \times 100\% = 73.69\%$$

---

## 4. Cross-Defense and Pair Evaluation
- **Student A Defends to Student B:** Why not use Quick Sort for the 10M orders to save 320 MB RAM?  
  *Defense:* Quick Sort is inherently unstable. If two transactions share timestamp $t = 105$, partitioning reorders them unpredictably. Financial audit compliance mandates that arrival order is strictly maintained. 320 MB RAM is modest in modern server infrastructure, and external merge runs handle memory-constrained nodes.
- **Student B Defends to Student A:** Why not use Merge Sort for the 100K live seller leaderboard?  
  *Defense:* The leaderboard updates continuously in real time. Allocating $O(n)$ temporary buffers every 2 seconds creates garbage collection churn and memory bus contention. Median-of-Three Introsort sorts in-place using only $\approx 17$ stack frames while eliminating quadratic worst-case degradation.

---

## 5. Summary Conclusion
The Joint Final Design successfully proves that a single algorithmic family—Divide and Conquer—can solve batch sorting, real-time in-place ranking, logarithmic searching, extreme statistical analytics, and high-dimensional linear algebra when engineered with mathematical precision.
