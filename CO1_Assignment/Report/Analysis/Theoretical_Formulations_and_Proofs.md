# Theoretical Formulations and Mathematical Proofs
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Author:** Sanjai S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Mathematical Derivations of Time Complexity

### 1.1 Iterative Linear Search
Let $A[0 \dots n-1]$ be an array of $n$ elements.
- **Worst-case:** The target key is at index $n-1$ or absent.
  $$C(n) = \sum_{i=0}^{n-1} 1 = n$$
  $$T(n) = c_{\text{comp}} \cdot n + c_{\text{loop}} = \Theta(n)$$
- **Average-case:** Assuming uniform probability $P(\text{index } i) = \frac{1}{n}$ for successful searches:
  $$E[C(n)] = \sum_{i=1}^n i \cdot \frac{1}{n} = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2} = \Theta(n)$$

### 1.2 Iterative Binary Search
Let the candidate interval length initially be $L_0 = n$.
At iteration $k$, the interval length is:
$$L_k = \left\lfloor \frac{n}{2^k} \right\rfloor$$
Termination condition occurs when $L_k \le 1$:
$$\frac{n}{2^k} \le 1 \implies 2^k \ge n \implies k \ge \log_2 n$$
$$C(n) = \lfloor \log_2 n \rfloor + 1 \implies T(n) = \Theta(\log n)$$

### 1.3 Preprocessing Amortization
For sorting an unsorted dataset of size $n$, using optimal comparison sorting:
$$P(n) = \Theta(n \log n)$$
If $q$ queries are conducted over the lifetime of the database:
$$T_{\text{amortized}}(n, q) = \frac{\Theta(n \log n) + q \cdot \Theta(\log n)}{q} = \frac{\Theta(n \log n)}{q} + \Theta(\log n)$$
As $q \to \infty$, the sorting cost per query approaches zero, leaving pure $\Theta(\log n)$ search cost.

---

## 2. Recurrence Relation Solution for Recursive Binary Search

### 2.1 Formulation
$$T(n) = T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + c \quad \text{for } n > 1, \quad T(1) = d$$

### 2.2 Solution via Master Theorem
Standard divide-and-conquer recurrence form:
$$T(n) = a T(n/b) + f(n)$$
Parameters:
- $a = 1$
- $b = 2$
- $f(n) = c = \Theta(n^0)$
- Watershed exponent: $\log_b a = \log_2 1 = 0 \implies n^{\log_b a} = n^0 = 1$

Since $f(n) = \Theta(n^{\log_b a} \log^0 n)$, this corresponds to **Case 2 of the Master Theorem**:
$$T(n) = \Theta(n^{\log_b a} \log^{0+1} n) = \Theta(1 \cdot \log n) = \boxed{\Theta(\log n)}$$

### 2.3 Mathematical Induction (Substitution Method)
- **Goal:** Prove $T(n) \le c' \log_2 n - d'$ for $c' \ge c$.
- **Inductive Step:**
  $$T(n) = T(n/2) + c \le \left(c' \log_2(n/2) - d'\right) + c$$
  $$= c' \log_2 n - c' \log_2 2 - d' + c = c' \log_2 n - (c' - c) - d'$$
  Since $c' \ge c$, $(c' - c) \ge 0$, which implies:
  $$T(n) \le c' \log_2 n - d' \quad \text{(Q.E.D.)}$$
