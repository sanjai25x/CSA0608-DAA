# TASK 10: Comparison Between Theoretical Analysis and Experimental Behavior

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Comparative Overview

| Dimension | Theoretical Prediction | Experimental Finding | Correlation Status |
| :--- | :--- | :--- | :--- |
| **Linear Search Complexity** | $T(n) = \Theta(n)$ | Execution time scaled from $0.052$ ms ($n=10^3$) to $31.89$ ms ($n=10^6$) | **Strict Agreement** (Linear slope $R^2 > 0.998$) |
| **Binary Search Comparisons** | $C(n) = \lceil \log_2(n+1) \rceil$ | Measured: $10, 14, 17, 20$ comparisons | **Exact Match** ($100\%$ precision) |
| **Binary Search Time** | $T(n) = \Theta(\log n)$ | Scaled from $2.18$ $\mu\text{s}$ to $7.00$ $\mu\text{s}$ | **Strict Agreement** (Logarithmic curve) |
| **Hash Table Lookup** | Expected $\Theta(1)$ | Latency remained virtually constant ($0.80$ to $3.40$ $\mu\text{s}$) | **Strict Agreement** |
| **Recursive vs Iterative** | Identical operation counts | Both took identical comparisons ($20$ at $n=10^6$); execution times within $\pm 1$ $\mu\text{s}$ | **Strict Agreement** |

---

## 2. In-Depth Discrepancy and Hardware Interaction Analysis

While theoretical models assume a **Random Access Machine (RAM)** model where all memory accesses incur uniform unit cost $O(1)$, physical hardware introduces factors that cause nuanced variations:

### 2.1 CPU Cache Hierarchy and Spatial Locality
- **Linear Search:** Although executing $O(n)$ comparisons, sequential iteration benefits from hardware prefetching and CPU cache line fills (L1/L2 caches). The CPU pre-loads sequential elements ahead of the instruction pointer, allowing the inner loop to run at near-hardware throughput ($\approx 32$ ns per record).
- **Binary Search:** Binary search jumps across wide address strides ($n/2, n/4, \dots$). At $n = 1\,000\,000$, these strides exceed the L3 cache size ($\approx 12$ MB), causing occasional CPU cache misses. Nevertheless, because only $\le 20$ memory locations are probed, the absolute latency is capped at microseconds.

### 2.2 Interpreter and Virtual Machine Overhead
In Python, basic comparisons incur dynamic type checking and opcode dispatching (`COMPARE_OP`). At small $n$ ($n = 1\,000$), loop setup and function invocation dominate over raw comparison time, narrowing the visible gap between algorithms. However, as $n$ crosses $100\,000$, algorithmic asymptotic complexity completely overwhelms interpreter overhead.

### 2.3 Recursive Call Stack Overhead
Recursive binary search introduces function call stack frame allocation and pointer dereferencing on each recursive step. In our tests, recursive binary search executed at $5.83$ $\mu\text{s}$ compared to $7.00$ $\mu\text{s}$ for iterative search at $n=10^6$. Because the total recursion depth is so shallow ($\le 20$ frames), modern Python 3.13 frame caching renders the stack cost virtually negligible.

---

## 3. Scaling Assessment for $n \ge 1\,000\,000$

- **Linear Search:** As $n$ grows from $1\,000$ to $1\,000\,000$, linear search runtime increases by **$611 \times$**. If the university database reaches $10\,000\,000$ students, a single worst-case query would take $\approx 0.32$ seconds, completely stalling interactive web requests.
- **Binary Search:** Growing from $1\,000$ to $1\,000\,000$ records increased runtime by only **$3.2 \times$** (from $2.18$ $\mu\text{s}$ to $7.00$ $\mu\text{s}$). At $10^7$ records, it would require only $24$ comparisons ($\approx 8.5$ $\mu\text{s}$).

---

## 4. Conclusion of Validation
The empirical findings conclusively validate the theoretical models:
1. Operation counts match theoretical predictions with mathematical precision.
2. Binary search achieves logarithmic scaling, demonstrating orders-of-magnitude superiority over linear scanning on large datasets.
3. Theoretical asymptotic analysis accurately predicts physical system behavior under large-scale workloads.
