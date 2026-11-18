# Empirical Performance and Scaling Analysis
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Author:** Sanjai S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Experimental Methodology
All experimental tests were conducted on an Intel x86_64 architecture running Windows 11 with 16 GB RAM and Python 3.13.2.
Timing was captured using `time.perf_counter_ns()` with nanosecond precision. For each input scale $N \in \{10^3, 10^4, 10^5, 10^6\}$, multiple benchmark executions were performed and median values recorded to avoid interference from operating system scheduler jitter.

---

## 2. Quantitative Summary Across Input Scales

| Metric | N = 1,000 | N = 10,000 | N = 100,000 | N = 1,000,000 |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search Comparisons** | $1\,000$ | $10\,000$ | $100\,000$ | $1\,000\,000$ |
| **Linear Search Latency (s)** | $0.000052$ | $0.000365$ | $0.003498$ | $0.031893$ |
| **Binary Search Comparisons** | $10$ | $14$ | $17$ | $20$ |
| **Iterative Binary Latency (s)**| $0.00000218$ | $0.00000228$ | $0.00002724$ | $0.00000700$ |
| **Recursive Binary Latency (s)**| $0.00000282$ | $0.00000280$ | $0.00000404$ | $0.00000583$ |
| **Hash Table Lookup (s)** | $0.00000080$ | $0.00000100$ | $0.00000140$ | $0.00000340$ |
| **Array Sorting Time (s)** | $0.0001$ | $0.0012$ | $0.0123$ | $0.2948$ |
| **Hash Table Build Time (s)** | $0.0002$ | $0.0011$ | $0.0130$ | $0.1318$ |

---

## 3. Analysis of Algorithmic Scaling Behaviors

1. **Linear Search:** Demonstrates strict $O(N)$ growth. Growing $N$ from $10^3$ to $10^6$ increased elapsed search time by a factor of $611 \times$. At $N = 10^6$, a single search took $31.89$ ms, which is unviable for high-throughput concurrent environments.
2. **Binary Search:** Confirms $O(\log N)$ growth. When $N$ grew by $1\,000 \times$, comparison operations increased by only an additive factor of $10$ ($10 \to 20$), and execution time increased by only $3.2 \times$.
3. **Hash Table Search:** Exhibits virtually flat $O(1)$ response time, remaining between $0.8$ $\mu\text{s}$ and $3.4$ $\mu\text{s}$ across all scales.
