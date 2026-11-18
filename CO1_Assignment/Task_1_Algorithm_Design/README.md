# TASK 1: Algorithm Design

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Problem Context
A university maintains an academic database containing student records identified uniquely by a **Registration Number**. As student enrollment expands from $n = 1\,000$ to $n = 1\,000\,000+$ records, the university administrative and faculty portal requires an algorithm that can rapidly locate a student's record or determine whether it exists.

To address this challenge, we design and investigate **three meaningfully different algorithmic strategies** along with an indexing strategy:
1. **Iterative Linear Search** (Sequential Scan Strategy)
2. **Iterative Binary Search** (Iterative Divide-and-Conquer Strategy)
3. **Recursive Binary Search** (Recursive Divide-and-Conquer Strategy)
4. *Day-4 Extension:* **Direct Hash Table Search** (Direct Address / Key-to-Bucket Indexing Strategy)

---

## 2. Approach 1: Iterative Linear Search

### 2.1 Design Strategy
**Sequential Search (Brute Force / Exhaustive Scan)**.  
The algorithm sequentially iterates through the records array $A[0 \dots n-1]$ from index $0$ to $n-1$, inspecting each student registration number one by one until a match is detected or the collection is exhausted.

### 2.2 Basic Idea
Each stored registration number is directly compared against the target `key`. If `A[i] == key`, the search terminates immediately returning the index `i`. If the loop finishes without matching `key`, the sentinel value `-1` is returned indicating that the student record does not exist.

### 2.3 Preprocessing Requirements
**None ($P(n) = 0$).**  
Linear search functions directly on unsorted, dynamically appended, or arbitrary arrays. No prior ordering, indexing, or memory restructuring is required.

### 2.4 Pseudocode
```text
ALGORITHM IterativeLinearSearch(A, n, key):
    Input: Array A of n student registration numbers, target key
    Output: Index of key if present, otherwise -1

    for i ← 0 to n - 1 do
        if A[i] == key then
            return i
        end if
    end for
    return -1
```

### 2.5 Justification for Investigation
Linear search establishes the foundational performance baseline. Because it requires zero preprocessing, it is immediately applicable to newly ingested, unsorted records. It represents the lower operational complexity threshold for simple scripts and small datasets ($n \le 1\,000$).

---

## 3. Approach 2: Iterative Binary Search

### 3.1 Design Strategy
**Iterative Divide-and-Conquer (Search Space Pruning)**.  
The algorithm maintains two pointers, `low` and `high`, defining the active search space. By leveraging monotonic ordering, it halves the candidate search window during each step.

### 3.2 Basic Idea
At each iteration, the midpoint index `mid = low + (high - low) // 2` is calculated. The target `key` is compared against `A[mid]`:
- If `A[mid] == key`: Target is found; return `mid`.
- If `A[mid] < key`: Target must lie in the upper half; narrow the window by setting `low = mid + 1`.
- If `A[mid] > key`: Target must lie in the lower half; narrow the window by setting `high = mid - 1`.

The process repeats while `low <= high`. If `low > high`, the element is absent.

### 3.3 Preprocessing Requirements
**Sorting Required ($P(n) = \Theta(n \log n)$).**  
Records must be sorted in ascending order of registration numbers prior to execution. If records arrive unsorted, an initial sort (e.g., Dual-Pivot Quicksort or Merge Sort) must be executed once.

### 3.4 Pseudocode
```text
ALGORITHM IterativeBinarySearch(A, n, key):
    Input: Monotonically sorted array A of n registration numbers, target key
    Output: Index of key if present, otherwise -1

    low ← 0
    high ← n - 1

    while low ≤ high do
        mid ← low + ⌊(high - low) / 2⌋
        if A[mid] == key then
            return mid
        else if A[mid] < key then
            low ← mid + 1
        else
            high ← mid - 1
        end if
    end while
    return -1
```

### 3.5 Justification for Investigation
Iterative Binary Search provides logarithmic time complexity $\Theta(\log n)$ while preserving constant auxiliary space $\Theta(1)$. It eliminates call stack overhead and prevents recursion stack overflow, making it standard for high-throughput production lookups on in-memory sorted arrays.

---

## 4. Approach 3: Recursive Binary Search

### 4.1 Design Strategy
**Recursive Divide-and-Conquer (Inductive Subproblem Reduction)**.  
Rather than controlling state via loop counters, this strategy expresses search interval elimination through formal recursive self-invocation.

### 4.2 Basic Idea
The problem instance $(A, \text{low}, \text{high}, \text{key})$ is mapped to an identical subproblem of size $\approx n/2$. The base condition checks if $\text{low} > \text{high}$ (element absent). Otherwise, the midpoint element is evaluated:
- If `A[mid] == key`, return `mid`.
- If `key < A[mid]`, recursively invoke `RecursiveBinarySearch(A, low, mid - 1, key)`.
- If `key > A[mid]`, recursively invoke `RecursiveBinarySearch(A, mid + 1, high, key)`.

### 4.3 Preprocessing Requirements
**Sorting Required ($P(n) = \Theta(n \log n)$).**  
Requires array $A$ to be strictly ordered.

### 4.4 Pseudocode
```text
ALGORITHM RecursiveBinarySearch(A, low, high, key):
    Input: Sorted array A, lower bound low, upper bound high, target key
    Output: Index of key if present, otherwise -1

    if low > high then
        return -1
    end if

    mid ← low + ⌊(high - low) / 2⌋

    if A[mid] == key then
        return mid
    else if key < A[mid] then
        return RecursiveBinarySearch(A, low, mid - 1, key)
    else
        return RecursiveBinarySearch(A, mid + 1, high, key)
    end if
```

### 4.5 Justification for Investigation
Recursive binary search demonstrates clean recurrence formulation amenable to Master Theorem and Substitution Method analysis. It models tree-based hierarchical lookups (such as B-Trees and Binary Search Trees) used extensively in relational database indexing.

---

## 5. Comparative Architectural Summary

| Dimension | Approach 1: Linear Search | Approach 2: Iterative Binary Search | Approach 3: Recursive Binary Search |
| :--- | :--- | :--- | :--- |
| **Algorithmic Paradigm** | Brute-force Sequential Scan | Iterative Divide-and-Conquer | Recursive Divide-and-Conquer |
| **Preprocessing Requirement** | None ($0$) | Sorting ($\Theta(n \log n)$) | Sorting ($\Theta(n \log n)$) |
| **Search Time Complexity** | $\Theta(n)$ worst-case | $\Theta(\log n)$ worst-case | $\Theta(\log n)$ worst-case |
| **Auxiliary Memory** | $\Theta(1)$ constant space | $\Theta(1)$ constant space | $\Theta(\log n)$ call stack space |
| **Suitability for $n=10^6$** | Unusable for heavy traffic | Highly efficient & scalable | Scalable (requires stack limit care) |
