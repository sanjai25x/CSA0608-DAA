# TASK 2: Identification and Justification of Basic Operations

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Concept of Basic Operation
In theoretical computer science and algorithm analysis, the **basic operation** is defined as the most time-consuming or most frequently executed atomic instruction in the algorithm's innermost loop. The total running time $T(n)$ of an algorithm is directly proportional to the count of basic operations executed:
$$T(n) \approx c_{\text{op}} \cdot C(n)$$
where $c_{\text{op}}$ is the execution time of one basic operation and $C(n)$ is the number of times it is executed as a function of input size $n$.

---

## 2. Approach 1: Iterative Linear Search

### 2.1 Basic Operation Identification
The basic operation is the **equality comparison between the current array element and the target key**:
$$\text{Operation: } A[i] == \text{key}$$

### 2.2 Location within the Algorithm
This operation resides inside the single `for` loop body, executed at each step of the sequential iteration prior to checking the termination condition or incrementing the loop index.

### 2.3 Justification for Selection
- **Dominance:** Loop counter incrementing (`i++`) and boundary checking (`i < n`) are simple hardware register increments; the element equality comparison requires memory dereferencing (`A[i]`), cache retrieval, and word-level ALU comparison.
- **Proportionality:** If $k$ elements are traversed, exactly $k$ comparisons occur. The overall CPU time tracks the comparison count with strict linear correlation.

### 2.4 Behavior as Input Size $n$ Increases
- When $n = 1\,000$, worst-case comparisons = $1\,000$.
- When $n = 1\,000\,000$, worst-case comparisons = $1\,000\,000$.
- The number of times the operation executes increases **strictly linearly**:
  $$C(n) \propto n$$

---

## 3. Approach 2: Iterative Binary Search

### 3.1 Basic Operation Identification
The basic operation is the **three-way key comparison at the midpoint element**:
$$\text{Operation: } A[\text{mid}] == \text{key} \quad (\text{followed by } A[\text{mid}] < \text{key})$$

### 3.2 Location within the Algorithm
This operation is situated within the `while (low <= high)` loop immediately following midpoint calculation $\text{mid} = \lfloor(\text{low} + \text{high}) / 2\rfloor$.

### 3.3 Justification for Selection
- **Decision Engine:** The outcome of this comparison dictates whether the algorithm returns successfully or eliminates half ($\lfloor n/2 \rfloor$) of the remaining candidate records.
- **Runtime Dependency:** Every iteration executes exactly one midpoint comparison block. The total loop cycles equal the number of midpoint comparisons performed.

### 3.4 Behavior as Input Size $n$ Increases
- At each comparison, the candidate interval shrinks by a factor of 2:
  $$n \to \frac{n}{2} \to \frac{n}{4} \to \dots \to 1$$
- For $n = 1\,000$: $C(n) \le \lceil \log_2(1001) \rceil = 10$.
- For $n = 1\,000\,000$: $C(n) \le \lceil \log_2(1000001) \rceil = 20$.
- While the dataset grows by $1\,000\times$, the basic operation count increases only by an additive constant of $10$ comparisons. The execution count grows **logarithmically**:
  $$C(n) \propto \log_2 n$$

---

## 4. Approach 3: Recursive Binary Search

### 4.1 Basic Operation Identification
The basic operation is the **comparison of the target key with the midpoint element $A[\text{mid}]$**:
$$\text{Operation: } A[\text{mid}] == \text{key}$$

### 4.2 Location within the Algorithm
Located in the body of each recursive invocation `RecursiveBinarySearch(A, low, high, key)` immediately following the base-case validation (`low > high`).

### 4.3 Justification for Selection
- **Recursion Driver:** Each comparison directly branches into either a return statement or exactly one tail-recursive subproblem call with half the original interval.
- **Stack Correlation:** The number of comparisons precisely matches the call stack depth and frame allocations.

### 4.4 Behavior as Input Size $n$ Increases
- Identical to iterative binary search in terms of operation count:
  $$C(n) = \lfloor \log_2 n \rfloor + 1 \quad (\text{worst case})$$
- For $n = 10^6$, at most $20$ recursive invocations and $20$ comparisons are performed.

---

## 5. Summary Table of Basic Operations

| Algorithm | Basic Operation | Exact Program Location | Worst-Case Count $C(n)$ | Growth Classification |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | `A[i] == key` | Inside `for` loop body | $n$ | Linear: $\Theta(n)$ |
| **Iterative Binary Search** | `A[mid] == key` | Inside `while` loop body | $\lceil \log_2(n+1) \rceil$ | Logarithmic: $\Theta(\log n)$ |
| **Recursive Binary Search** | `A[mid] == key` | Inside recursive function body | $\lceil \log_2(n+1) \rceil$ | Logarithmic: $\Theta(\log n)$ |
| **Hash Table Lookup** | `bucket[k].key == key` | Inside linked chain / bucket | $1$ (expected) | Constant: $\Theta(1)$ |
