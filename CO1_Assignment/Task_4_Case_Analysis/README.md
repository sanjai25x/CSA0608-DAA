# TASK 4: Best, Average, and Worst-Case Analysis

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Overview of Analytical Cases
The execution efficiency of searching algorithms varies based on the relative position of the target registration number in the collection, or whether the registration number exists at all. We formally examine:
- **Best Case:** The configuration of inputs minimizing basic operations.
- **Average Case:** The expected operational count assuming a uniform probability distribution over input positions.
- **Worst Case:** The input configuration requiring the theoretical maximum operation count.

---

## 2. Approach 1: Iterative Linear Search

### 2.1 Best-Case Analysis
- **Trigger Condition:** The target registration number resides at the very first index ($A[0]$).
- **Operation Count:** The first loop iteration tests `A[0] == key`, evaluates to `True`, and immediately executes `return 0`.
- **Mathematical Expression:**
  $$C_{\text{best}}(n) = 1 \implies \boxed{T_{\text{best}}(n) = \Theta(1)}$$

### 2.2 Worst-Case Analysis
- **Trigger Condition:** The target key is at the final position ($A[n-1]$) or is completely absent from the database.
- **Operation Count:** The loop iterates $n$ times, evaluating `A[i] == key` for every $i \in \{0, 1, \dots, n-1\}$.
- **Mathematical Expression:**
  $$C_{\text{worst}}(n) = n \implies \boxed{T_{\text{worst}}(n) = \Theta(n)}$$

### 2.3 Average-Case Analysis
- **Assumptions:**
  1. The target registration number is present in the database with probability $p$.
  2. If present, it is equally likely to reside at any index $i \in \{0, 1, \dots, n-1\}$ with uniform probability:
     $$P(\text{index } i) = \frac{1}{n}$$
  3. If absent (probability $1 - p$), exactly $n$ comparisons are performed.
- **Derivation:**
  $$E[C(n)] = p \sum_{i=1}^{n} \left(i \cdot \frac{1}{n}\right) + (1 - p) \cdot n$$
  $$E[C(n)] = \frac{p}{n} \left(\frac{n(n+1)}{2}\right) + n(1 - p) = p \left(\frac{n+1}{2}\right) + n(1 - p)$$
  For a guaranteed successful search ($p = 1$):
  $$C_{\text{avg}}(n) = \frac{n + 1}{2} \implies \boxed{T_{\text{avg}}(n) = \Theta(n)}$$
- **Interpretation:** On average, linear search scans half the database. For $n = 1\,000\,000$, this requires approximately $500\,000$ comparisons per search.

---

## 3. Approach 2: Iterative Binary Search

### 3.1 Best-Case Analysis
- **Trigger Condition:** The target key matches the middle element $A[\lfloor(n-1)/2\rfloor]$ on the initial midpoint check.
- **Operation Count:** Exactly one comparison is performed.
- **Mathematical Expression:**
  $$C_{\text{best}}(n) = 1 \implies \boxed{T_{\text{best}}(n) = \Theta(1)}$$

### 3.2 Worst-Case Analysis
- **Trigger Condition:** The search key is absent, or is positioned at an extreme leaf of the implicit binary decision tree (requiring complete interval exhaustion down to an interval of size 1).
- **Operation Count:** Every comparison halves the remaining interval until $L \le 1$:
  $$C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1 \implies \boxed{T_{\text{worst}}(n) = \Theta(\log n)}$$
- For $n = 1\,000\,000$: $C_{\text{worst}}(10^6) = \lfloor \log_2 10^6 \rfloor + 1 = 19 + 1 = 20$ comparisons.

### 3.3 Average-Case Analysis
- **Mathematical Modeling:**  
  Represent the binary search process as an internal decision tree with $n$ nodes. The depth of node $i$ represents the number of comparisons needed to reach it.
  The total comparison count across all $n$ nodes equals the internal path length $I(n)$:
  $$I(n) = \sum_{j=1}^{k} j \cdot 2^{j-1} \approx (k - 1) 2^k + 1 \quad \text{where } k = \lceil \log_2(n+1) \rceil$$
  Dividing by $n \approx 2^k - 1$:
  $$C_{\text{avg}}(n) = \frac{I(n)}{n} \approx \log_2(n + 1) - 1$$
- **Asymptotic Classification:**
  $$\boxed{T_{\text{avg}}(n) = \Theta(\log n)}$$
- For $n = 10^6$: $C_{\text{avg}}(10^6) \approx 20 - 1 = 19$ comparisons.

---

## 4. Approach 3: Recursive Binary Search

### 4.1 Best, Average, and Worst Cases
The operation counts and mathematical derivations for Recursive Binary Search are identical to the iterative version:
- **Best Case:** $C_{\text{best}}(n) = 1 \implies \Theta(1)$ (root node hit).
- **Average Case:** $C_{\text{avg}}(n) \approx \log_2 n - 1 \implies \Theta(\log n)$.
- **Worst Case:** $C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1 \implies \Theta(\log n)$.

### 4.2 Stack Depth Impact
While time complexity is identical, the stack memory consumption varies:
- Best Case Stack Depth: $1$ frame ($\Theta(1)$ space).
- Worst Case Stack Depth: $\approx \log_2 n$ frames ($\Theta(\log n)$ space).

---

## 5. Comparative Case Analysis Table

| Algorithmic Approach | Best-Case Operations | Best-Case Class | Average-Case Operations | Average-Case Class | Worst-Case Operations | Worst-Case Class |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Iterative Linear Search** | $1$ | $\Theta(1)$ | $\frac{n+1}{2}$ | $\Theta(n)$ | $n$ | $\Theta(n)$ |
| **Iterative Binary Search** | $1$ | $\Theta(1)$ | $\approx \log_2 n - 1$ | $\Theta(\log n)$ | $\lfloor \log_2 n \rfloor + 1$ | $\Theta(\log n)$ |
| **Recursive Binary Search** | $1$ | $\Theta(1)$ | $\approx \log_2 n - 1$ | $\Theta(\log n)$ | $\lfloor \log_2 n \rfloor + 1$ | $\Theta(\log n)$ |
| **Hash Table Lookup** | $1$ | $\Theta(1)$ | $1 + \frac{\alpha}{2}$ | $\Theta(1)$ | $n$ | $\Theta(n)$ |
