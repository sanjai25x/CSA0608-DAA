# TASK 3: Mathematical Derivation of Time-Complexity Functions

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Mathematical Framework
Let $n$ represent the number of student records maintained in the academic database.
Let $C(n)$ denote the exact number of basic operation executions (comparisons).
The execution time function $T(n)$ is formulated as:
$$T(n) = c_{\text{op}} \cdot C(n) + c_{\text{overhead}}$$
where $c_{\text{op}}$ is the machine-dependent time per basic operation and $c_{\text{overhead}}$ encompasses initialization, function entry/exit, and loop termination checks.

---

## 2. Derivation 1: Iterative Linear Search

### 2.1 Operation Count Formulation
In the worst-case scenario, the target registration number is either located at the final index $A[n-1]$ or is absent from the entire array.
The loop executes for $i = 0, 1, 2, \dots, n-1$:
$$C_{\text{worst}}(n) = \sum_{i=0}^{n-1} 1 = \underbrace{1 + 1 + 1 + \dots + 1}_{n \text{ terms}} = n$$

### 2.2 Time Complexity Function
Substituting $C(n) = n$ into the time function:
$$T(n) = c_1 \cdot n + c_2$$
where:
- $c_1$ = combined cost of loop counter increment, array indexing $A[i]$, and equality comparison.
- $c_2$ = cost of loop initialization ($i \leftarrow 0$) and final sentinel return (`return -1`).

Since $c_1 > 0$, taking limits as $n \to \infty$:
$$\lim_{n \to \infty} \frac{T(n)}{n} = c_1 \implies \boxed{T(n) = \Theta(n)}$$

### 2.3 Preprocessing Cost
Linear search functions directly on raw unsorted data:
$$P(n) = 0$$

### 2.4 Overall System Cost for $q$ Queries
For an administrative session executing $q$ independent lookups:
$$T_{\text{total}}(n, q) = P(n) + q \cdot T(n) = 0 + q \cdot \Theta(n) = \boxed{\Theta(q \cdot n)}$$

---

## 3. Derivation 2: Iterative Binary Search

### 3.1 Operation Count Formulation
Let the search interval size initially be $L_0 = n$.
- After 1 comparison, the active interval is at most:
  $$L_1 = \left\lfloor \frac{n}{2} \right\rfloor$$
- After 2 comparisons:
  $$L_2 = \left\lfloor \frac{L_1}{2} \right\rfloor \le \frac{n}{2^2}$$
- After $k$ comparisons:
  $$L_k \le \frac{n}{2^k}$$

The algorithm terminates when the remaining candidate space is reduced to at most 1 element ($L_k \le 1$):
$$\frac{n}{2^k} \le 1 \implies 2^k \ge n$$
Applying the base-2 logarithm to both sides:
$$k \ge \log_2 n \implies k = \lceil \log_2(n + 1) \rceil$$

Thus, the exact maximum number of midpoint comparisons is:
$$C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1$$

### 3.2 Time Complexity Function
$$T(n) = c_1 \cdot (\lfloor \log_2 n \rfloor + 1) + c_2 = c_1 \log_2 n + (c_1 + c_2) \implies \boxed{T(n) = \Theta(\log n)}$$

### 3.3 Preprocessing Cost
If student records arrive in arbitrary order, the database must sort them initially:
$$P(n) = \Theta(n \log n) \quad (\text{using Optimal Comparison Sort such as Merge Sort})$$

### 3.4 Overall System Cost for $q$ Queries
$$T_{\text{total}}(n, q) = P(n) + q \cdot T(n) = c_{\text{sort}} \cdot n \log_2 n + q \cdot (c_1 \log_2 n + c_2)$$
$$T_{\text{total}}(n, q) = \boxed{\Theta(n \log n + q \log n)}$$

**Amortization Insight:**  
When $q \gg 1$, the initial sorting cost is distributed over all queries:
$$\frac{T_{\text{total}}(n, q)}{q} = \frac{\Theta(n \log n)}{q} + \Theta(\log n) \xrightarrow{q \to \infty} \Theta(\log n)$$

---

## 4. Derivation 3: Recursive Binary Search

### 4.1 Recursive Call Formulation
Each recursive invocation splits the array into two halves, compares the midpoint, and calls itself on at most one subproblem of size $\lfloor n/2 \rfloor$:
$$T(n) = T(\lfloor n/2 \rfloor) + c$$
with base condition $T(1) = c_0$.

### 4.2 Expansion (Iteration) Derivation
Assuming $n = 2^k$:
$$T(n) = T(n/2) + c$$
$$T(n) = (T(n/4) + c) + c = T(n/4) + 2c$$
$$T(n) = (T(n/8) + c) + 2c = T(n/8) + 3c$$
$$\dots$$
$$T(n) = T\left(\frac{n}{2^k}\right) + k \cdot c$$

The expansion terminates when $\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$:
$$T(n) = T(1) + c \log_2 n = c_0 + c \log_2 n$$
$$\boxed{T(n) = \Theta(\log n)}$$

### 4.3 Space Complexity Function
Unlike iterative search ($S(n) = \Theta(1)$), each recursive step allocates an activation record on the runtime stack storing `(A, low, high, key, mid, return_address)`:
$$S(n) = S(n/2) + \Theta(1) \implies \boxed{S(n) = \Theta(\log n)}$$

---

## 5. Summary of Mathematical Functions

| Strategy | Search Time $T(n)$ | Preprocessing $P(n)$ | Total Cost for $q$ Searches | Auxiliary Space $S(n)$ |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $c_1 n + c_2 = \Theta(n)$ | $0$ | $\Theta(q \cdot n)$ | $\Theta(1)$ |
| **Iterative Binary Search** | $c_1 \log_2 n + c_2 = \Theta(\log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n + q \log n)$ | $\Theta(1)$ |
| **Recursive Binary Search** | $c_1 \log_2 n + c_0 = \Theta(\log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n + q \log n)$ | $\Theta(\log n)$ |
| **Hash Table Lookup** | $c_1 \cdot (1 + \alpha) = \Theta(1)$ | $\Theta(n)$ | $\Theta(n + q)$ | $\Theta(n)$ |
