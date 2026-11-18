# Day 4 Design Challenge - Student A Initial Proposal
**Student Name:** Sanjai S  
**Registration Number:** 192511018  
**Department:** Computer Science and Engineering, SIMATS Engineering  
**Role:** Student A (Architectural Lead: Order Consolidation & Stream Analytics)

---

## 1. Problem Statement & Architecture Vision
KartIQ operates as a high-volume national e-commerce retail data analytics engine handling:
- **10,000,000 (10 Million)** orders daily arriving through distributed payment gateways.
- Repeated audits and financial reconciliations where orders share identical timestamps.
- Extreme price and order value monitoring requiring high-speed real-time detection of minimum and maximum transactions.

My initial proposal centers on establishing mathematical predictability and audit correctness for the high-volume transactional backbone through two core Divide-and-Conquer pipelines:
1. **Stable Two-Way Merge Sort with External Multi-Way Partitioning** for the 10M order stream.
2. **Recursive Tournament Tree Max-Min Engine** for stream metrics.

---

## 2. Module A: Stable Merge Sort for Nightly Order Consolidation
### 2.1 The Architectural Defect of Quick Sort in Auditing
Standard Quick Sort and unstable sorting primitives reorder duplicate keys based on partition mechanics. In financial audits, two transactions occurring at timestamp $t = 105$ (e.g., Order $O_1$ and Order $O_3$) must maintain their exact arrival sequence to resolve escrow and inventory race conditions.

### 2.2 Algorithmic Design
- **Divide:** Recursively bisect the order array $A[low \dots high]$ at $mid = \lfloor (low + high) / 2 \rfloor$.
- **Conquer:** Recursively sort subarrays $A[low \dots mid]$ and $A[mid+1 \dots high]$.
- **Combine (Stable Merge):** Merge two sorted subarrays using the invariant:
  $$\text{IF } L[i].timestamp \le R[j].timestamp \text{ THEN Select } L[i] \text{ ELSE Select } R[j]$$
  The strict $\le$ condition guarantees that the left subarray (earlier arrival) always wins ties, preserving audit stability.

### 2.3 Mathematical Complexity
- **Recurrence:**
  $$T(n) = 2T(n/2) + c \cdot n, \quad T(1) = \Theta(1)$$
- **Master Theorem Solution:**
  $a = 2, b = 2, f(n) = c \cdot n$.
  Since $n^{\log_b a} = n^{\log_2 2} = n^1 = \Theta(f(n))$, Master Theorem Case 2 applies:
  $$T(n) = \Theta(n \log_2 n)$$
- **For $n = 10,000,000$:**
  $$n \log_2 n = 10^7 \times 23.2535 \approx 232,535,000 \text{ comparisons}$$
  Worst-case comparison bound: $n \lceil \log_2 n \rceil - n + 1 = 230,000,001$ comparisons.
- **Memory Footprint:** 32 bytes/order $\times 10^7 = 320 \text{ MB}$ auxiliary buffer. When RAM is constrained to 64 MB, the same Divide-and-Conquer principle extends to External 4-Way Merge Sort with disk runs.

---

## 3. Module B: Tournament Divide-and-Conquer Max-Min Engine
### 3.1 Design
For detecting extreme transaction amounts (fraudulent high-value outliers and sub-penny microtransactions), naive linear search consumes $2n - 2$ comparisons.
The Tournament Divide-and-Conquer method pairs elements hierarchically:
- Divide into halves until pairs ($n=2$) or singletons ($n=1$) remain.
- Base case $n=2$: 1 comparison directly identifies local min and max.
- Combine: 2 comparisons (one between subproblem minimums, one between subproblem maximums).

### 3.2 Mathematical Advantage
- **Recurrence:**
  $$T(n) = 2T(n/2) + 2, \quad T(2) = 1, \quad T(1) = 0$$
- **Closed-Form Solution:**
  $$T(n) = \frac{3n}{2} - 2 \quad (\text{for } n = 2^k)$$
- **Comparisons for $n = 10,000,000$:**
  - Naive Linear Search: $2(10^7) - 2 = 19,999,998$ comparisons.
  - Tournament D&C: $1.5(10^7) - 2 = 14,999,998$ comparisons.
  - **Net Reduction:** Exactly $5,000,000$ fewer comparisons ($25.00\%$ reduction).

---

## 4. Student A Proposal Limitations & Need for Synthesis
While Merge Sort and Tournament D&C secure the order stream and statistical monitoring:
1. Merge Sort incurs an $O(n)$ auxiliary memory allocation which is suboptimal for the 100,000 live seller leaderboard that updates frequently in-place.
2. It lacks matrix recommendation acceleration for customer personalization.
3. Order lookup requires a dedicated logarithmic search mechanism.

These limitations will be addressed through integration with Student B's proposal.
