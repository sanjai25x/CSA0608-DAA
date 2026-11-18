# TASK 5: Asymptotic Analysis and Growth Rate Comparison

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Formal Asymptotic Notations
To characterize algorithmic scalability independent of hardware constants, compiler flags, or operating systems, we apply standard asymptotic bounding notations:

1. **Big-O ($O$) – Asymptotic Upper Bound:**
   $$f(n) \in O(g(n)) \iff \exists c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0$$
2. **Big-Omega ($\Omega$) – Asymptotic Lower Bound:**
   $$f(n) \in \Omega(g(n)) \iff \exists c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \quad \forall n \ge n_0$$
3. **Big-Theta ($\Theta$) – Asymptotically Tight Bound:**
   $$f(n) \in \Theta(g(n)) \iff f(n) \in O(g(n)) \land f(n) \in \Omega(g(n))$$

---

## 2. Asymptotic Classification of Proposed Approaches

| Algorithm | Best-Case Bound | Worst-Case Bound | Average-Case Bound | Overall Asymptotic Tight Bound |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $\Omega(1)$ | $O(n)$ | $\Theta(n)$ | $\Theta(n)$ (worst case) |
| **Iterative Binary Search**| $\Omega(1)$ | $O(\log n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ (worst case) |
| **Recursive Binary Search**| $\Omega(1)$ | $O(\log n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ (worst case) |
| **Hash Table Lookup** | $\Omega(1)$ | $O(n)$ | $\Theta(1)$ | $\Theta(1)$ (expected average) |

---

## 3. Growth Behavior Analysis Across Dataset Scales

To visualize the practical implications of asymptotic growth, we evaluate operation counts as the university database expands across the mandatory evaluation thresholds:
$$n = 1\,000 \longrightarrow 10\,000 \longrightarrow 100\,000 \longrightarrow 1\,000\,000+$$

### 3.1 Quantitative Operation Comparison

| Input Size $n$ | Linear Search: $C_{\text{worst}}(n) = n$ | Binary Search: $C_{\text{worst}}(n) = \lceil \log_2(n+1) \rceil$ | Growth Divergence Ratio $\frac{C_{\text{linear}}}{C_{\text{binary}}}$ | Hash Table: Expected $C(n)$ |
| :--- | :--- | :--- | :--- | :--- |
| **1,000** | $1\,000$ | $10$ | $100 \times$ | $1$ |
| **10,000** | $10\,000$ | $14$ | $714 \times$ | $1$ |
| **100,000** | $100\,000$ | $17$ | $5\,882 \times$ | $1$ |
| **1,000,000** | $1\,000\,000$ | $20$ | **$50\,000 \times$** | $1$ |
| **10,000,000** | $10\,000\,000$ | $24$ | $416\,667 \times$ | $1$ |

### 3.2 Graphical Growth Interpretation
- **Linear Growth ($\Theta(n)$):** Every tenfold ($10\times$) increase in database records increases execution time by exactly $10\times$. For $n = 10^6$, the processor must execute one million iterations for an unsuccessful search or worst-case record retrieval.
- **Logarithmic Growth ($\Theta(\log n)$):** A tenfold ($10\times$) increase in database records adds merely $\approx 3.32$ comparisons ($\log_2 10 \approx 3.3219$). Growing from $1\,000$ records to $1\,000\,000$ records (a $1\,000\times$ increase) increases comparisons from $10$ to $20$ (an increase of only $10$ comparisons).
- **Constant Growth ($\Theta(1)$):** Average hash table lookup remains invariant with respect to $n$, requiring 1 bucket hash calculation and $\approx 1$ comparison regardless of whether the database contains $10^3$ or $10^6$ records.

---

## 4. Engineering Impact for the University Database
At $n = 1\,000\,000$, Linear Search performs **$50\,000$ times more basic operations** than Binary Search per query. Under concurrent faculty/student queries, Linear Search rapidly saturates the system CPU and exhausts memory bandwidth, causing severe latency spikes. Conversely, Binary Search and Hash Indexing exhibit exceptional asymptotic scalability, keeping response times well below milliseconds.
