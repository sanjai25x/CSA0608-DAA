# TASK 6: Recurrence Relation Formulation for Recursive Approach

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Algorithmic Source of the Recurrence
The recurrence relation is derived directly from the execution structure of **Recursive Binary Search**:

```text
RECURSIVE_BINARY_SEARCH(A, low, high, key):
    if low > high then                     // Base condition (1)
        return -1                          // Constant time c_0
    end if
    mid = low + (high - low) // 2          // Midpoint calculation (c_1)
    if A[mid] == key then                  // Comparison 1 (c_2)
        return mid
    else if key < A[mid] then              // Comparison 2 (c_3)
        return RECURSIVE_BINARY_SEARCH(A, low, mid - 1, key)   // Branch 1
    else
        return RECURSIVE_BINARY_SEARCH(A, mid + 1, high, key)  // Branch 2
    end if
```

---

## 2. Decomposition into Recurrence Components

### 2.1 Problem Input Size ($n$)
Let $n = \text{high} - \text{low} + 1$ denote the number of candidate registration numbers in the current search interval $[A[\text{low}] \dots A[\text{high}]]$.

### 2.2 Subproblem Size
When `A[mid] != key`, the algorithm decides to search either the strictly left half $[A[\text{low}] \dots A[\text{mid}-1]]$ or the strictly right half $[A[\text{mid}+1] \dots A[\text{high}]]$.
- Size of left subproblem: $(\text{mid} - 1) - \text{low} + 1 = \text{mid} - \text{low} = \lfloor \frac{n-1}{2} \rfloor \le \lfloor \frac{n}{2} \rfloor$.
- Size of right subproblem: $\text{high} - (\text{mid} + 1) + 1 = \text{high} - \text{mid} = \lceil \frac{n-1}{2} \rceil \le \lceil \frac{n}{2} \rceil$.

Thus, each subproblem contains at most $\lfloor n/2 \rfloor$ elements.

### 2.3 Number of Recursive Invocations ($a$)
Crucially, although two recursive calls are syntactically present in the code, they reside within mutually exclusive conditional branches (`if-else`).
Therefore, in any execution step:
$$\text{Number of recursive calls executed } a = 1$$

### 2.4 Work Performed Outside the Recursive Call ($f(n)$)
The non-recursive overhead includes:
1. Base condition check: `low > high` (1 comparison)
2. Midpoint arithmetic: `mid = low + (high - low) // 2` (1 subtraction, 1 division, 1 addition)
3. Array lookup & equality test: `A[mid] == key` (1 memory fetch, 1 comparison)
4. Inequality branch test: `key < A[mid]` (1 comparison)

All these operations execute in a fixed, constant sequence independent of $n$:
$$f(n) = c \quad \text{where } c \in \Theta(1)$$

### 2.5 Base Cases
- When the search interval is empty ($\text{low} > \text{high}$, corresponding to $n = 0$):
  $$T(0) = c_0$$
- When the search interval contains a single element ($n = 1$):
  $$T(1) = c_1$$

---

## 3. Formal Recurrence Formulation

Combining all structural components, the exact recurrence relation for the worst-case running time $T(n)$ is:

$$\boxed{T(n) = \begin{cases} c_0 & \text{for } n = 0 \\ c_1 & \text{for } n = 1 \\ T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + c & \text{for } n > 1 \end{cases}}$$

In standard asymptotic divide-and-conquer notation:
$$\boxed{T(n) = T\left(\frac{n}{2}\right) + \Theta(1)}$$
where:
- $a = 1$ (one subproblem solved recursively)
- $b = 2$ (subproblem size reduced by a factor of 2)
- $f(n) = c \in \Theta(n^0)$ (constant non-recursive work per invocation)
