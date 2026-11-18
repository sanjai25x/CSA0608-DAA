# TASK 7: Step-by-Step Solution of the Recurrence Relation

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Recurrence Specification
From Task 6, the recurrence relation governing Recursive Binary Search is:
$$T(n) = T\left(\frac{n}{2}\right) + c \quad \text{for } n > 1$$
with base case $T(1) = d$.

We solve this recurrence using **three complementary analytical methods**:
1. **Method 1: Iteration / Repeated Substitution Method**
2. **Method 2: Master Theorem (Divide-and-Conquer)**
3. **Method 3: Substitution Method (Mathematical Induction)**

---

## 2. Solution Method 1: Iteration (Expansion) Method

### 2.1 Step-by-Step Unfolding
Assume without loss of generality that $n = 2^k$ for some positive integer $k$, so that $k = \log_2 n$.

- **Initial Equation:**
  $$T(n) = T\left(\frac{n}{2}\right) + c \quad \text{--- [Eq. 1]}$$

- **Step 1 (First Expansion):** Substitute $T(n/2) = T(n/4) + c$ into Eq. 1:
  $$T(n) = \left[T\left(\frac{n}{4}\right) + c\right] + c = T\left(\frac{n}{4}\right) + 2c \quad \text{--- [Eq. 2]}$$

- **Step 2 (Second Expansion):** Substitute $T(n/4) = T(n/8) + c$ into Eq. 2:
  $$T(n) = \left[T\left(\frac{n}{8}\right) + c\right] + 2c = T\left(\frac{n}{8}\right) + 3c \quad \text{--- [Eq. 3]}$$

- **Step 3 (Third Expansion):** Substitute $T(n/8) = T(n/16) + c$ into Eq. 3:
  $$T(n) = T\left(\frac{n}{16}\right) + 4c$$

- **General Step (After $i$ Expansions):**
  $$T(n) = T\left(\frac{n}{2^i}\right) + i \cdot c \quad \text{--- [General Expression]}$$

### 2.2 Reaching the Base Case
The recursion terminates when the argument reaches the base case:
$$\frac{n}{2^i} = 1 \implies 2^i = n \implies i = \log_2 n$$

### 2.3 Closed-Form Evaluation
Substitute $i = \log_2 n$ into the general expression:
$$T(n) = T(1) + c \log_2 n$$
Since $T(1) = d$:
$$T(n) = d + c \log_2 n$$

Taking the asymptotic limit as $n \to \infty$:
$$\boxed{T(n) = \Theta(\log n)}$$

---

## 3. Solution Method 2: Master Theorem

### 3.1 Theorem Applicability
The Master Theorem applies to recurrences of the canonical form:
$$T(n) = a T\left(\frac{n}{b}\right) + f(n)$$
where $a \ge 1, b > 1$, and $f(n)$ is an asymptotically positive function.

For our recurrence $T(n) = T(n/2) + c$:
- $a = 1$
- $b = 2$
- $f(n) = c = \Theta(1) = \Theta(n^0)$

### 3.2 Critical Exponent Calculation
Compute the watershed value $n^{\log_b a}$:
$$\log_b a = \log_2 1 = 0 \implies n^{\log_b a} = n^0 = 1$$

### 3.3 Case Determination
Compare $f(n)$ with $n^{\log_b a}$:
$$f(n) = \Theta(1) = \Theta(n^{\log_b a})$$
This corresponds precisely to **Case 2 of the Master Theorem**:
$$\text{If } f(n) = \Theta(n^{\log_b a} \log^k n) \text{ with } k = 0, \text{ then:}$$
$$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$

Substituting $a=1, b=2, k=0$:
$$T(n) = \Theta(n^0 \log^{0+1} n) = \Theta(1 \cdot \log n)$$
$$\boxed{T(n) = \Theta(\log n)}$$

---

## 4. Solution Method 3: Substitution Method (Inductive Proof)

### 4.1 Inductive Hypothesis
We prove that $T(n) \le c' \log_2 n - d'$ for suitable constants $c', d' > 0$.

### 4.2 Inductive Step
Assume the inductive hypothesis holds for all values less than $n$, specifically for $n/2$:
$$T\left(\frac{n}{2}\right) \le c' \log_2\left(\frac{n}{2}\right) - d'$$

Substitute into the recurrence:
$$T(n) \le \left[c' \log_2\left(\frac{n}{2}\right) - d'\right] + c$$
$$T(n) \le c' (\log_2 n - \log_2 2) - d' + c$$
$$T(n) \le c' \log_2 n - c' - d' + c$$
To satisfy $T(n) \le c' \log_2 n - d'$, we require:
$$-c' - d' + c \le -d' \implies -c' + c \le 0 \implies c' \ge c$$
Choosing $c' \ge c$ guarantees the upper bound holds.

By symmetric argument for the lower bound, $T(n) \ge c'' \log_2 n$.  
Hence, by mathematical induction:
$$\boxed{T(n) = \Theta(\log n)}$$

---

## 5. Physical and Practical Interpretation
1. **Extremely Low Rate of Growth:** Because the recurrence solves to $\Theta(\log n)$, doubling the size of the student database requires only **one additional comparison**.
2. **Computational Validation:**
   - At $n = 10^3$: $k \approx 10$ steps.
   - At $n = 10^6$: $k \approx 20$ steps.
   - At $n = 10^9$ (one billion records): $k \approx 30$ steps.
3. **Space Overhead Consideration:**
   Unlike iterative binary search which runs in $O(1)$ space, each expansion in the recurrence creates a physical call stack frame. The maximum call stack depth is:
   $$\text{Stack Depth} = \lfloor \log_2 n \rfloor + 1 \implies \text{Stack Space} = \Theta(\log n)$$
   For $n = 1\,000\,000$, the recursion consumes at most $20$ stack frames ($\approx 1.5 \text{ KB}$ of RAM), which easily executes within standard Python stack limits (`sys.getrecursionlimit() = 1000`).
