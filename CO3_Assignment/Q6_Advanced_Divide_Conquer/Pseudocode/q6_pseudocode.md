# Pseudocode Specification - Question 6: Advanced Divide and Conquer
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Advanced Divide and Conquer Mini-Investigations

---

## 1. Submodule A: Median of Medians (Deterministic O(n) Selection) - Student A

```text
ALGORITHM MedianOfMedians(A, k)
    // Purpose: Selects the k-th smallest element in deterministic O(n) worst-case time
    // Input: Unsorted array A of size n, integer k (1 <= k <= n)
    // Output: Value of the k-th smallest element

    n <- LENGTH(A)

    // Base Case
    IF n <= 5 THEN
        Sort A
        RETURN A[k - 1]
    END IF

    // Step 1: Divide into groups of 5 and find medians
    medians <- EMPTY_LIST
    FOR i <- 0 TO n - 1 STEP 5 DO
        block <- A[i ... MIN(i + 4, n - 1)]
        Sort block
        APPEND block[FLOOR(LENGTH(block) / 2)] TO medians
    END FOR

    // Step 2: Recursively find median of medians as pivot
    mom_pivot <- MedianOfMedians(medians, CEIL(LENGTH(medians) / 2))

    // Step 3: Partition A into 3 sets around mom_pivot
    left <- [x IN A WHERE x < mom_pivot]
    equal <- [x IN A WHERE x == mom_pivot]
    right <- [x IN A WHERE x > mom_pivot]

    // Step 4: Recurse into appropriate subproblem
    IF k <= LENGTH(left) THEN
        RETURN MedianOfMedians(left, k)
    ELSE IF k <= LENGTH(left) + LENGTH(equal) THEN
        RETURN mom_pivot
    ELSE
        RETURN MedianOfMedians(right, k - LENGTH(left) - LENGTH(equal))
    END IF
END ALGORITHM
```

### Recurrence and Complexity
- At least half of the $\lceil n/5 \rceil$ block medians are $\ge \text{mom\_pivot}$.
- Each of these groups contributes at least 3 elements $\ge \text{mom\_pivot}$.
- Thus at least $3 \times \frac{1}{2} \times \frac{n}{5} = \frac{3n}{10}$ elements are $\ge \text{mom\_pivot}$, meaning the remaining subproblem has size at most $n - \frac{3n}{10} = \frac{7n}{10}$.
- Recurrence:
  $$T(n) \le T(n/5) + T(7n/10) + c \cdot n$$
- By substitution method (since $1/5 + 7/10 = 9/10 < 1$):
  $$T(n) = \Theta(n) \quad \text{strictly linear in the worst case!}$$

---

## 2. Submodule B: Meet in the Middle (Subset Sum Problem) - Student B

```text
ALGORITHM MeetInTheMiddleSubsetSum(A, n, target)
    // Purpose: Determines if a subset sum equals target in O(2^(n/2) * n) time
    // Input: Array A of n elements, target integer
    // Output: True if valid subset exists, False otherwise

    mid <- FLOOR(n / 2)
    left <- A[0 ... mid - 1]
    right <- A[mid ... n - 1]

    // Generate subset sums for both halves (size 2^(n/2) each)
    S1 <- GenerateAllSubsetSums(left)
    S2 <- GenerateAllSubsetSums(right)

    // Sort S2 for logarithmic lookup
    Sort S2

    // For each sum s in S1, binary search for (target - s) in S2
    FOR EACH s IN S1 DO
        needed <- target - s
        IF BinarySearch(S2, needed) == TRUE THEN
            RETURN TRUE
        END IF
    END FOR

    RETURN FALSE
END ALGORITHM
```

### Complexity Advantage
- **Naive Brute Force:** Generates $2^n$ subsets $\implies \Theta(2^n)$.
- **Meet in the Middle:** Generates $2 \times 2^{n/2}$ subsets $\implies O(2^{n/2} \cdot n)$ time and $O(2^{n/2})$ space.
- **For $n = 40$:** Naive evaluates $1.099 \times 10^{12}$ subsets; Meet-in-the-Middle evaluates only $2 \times 10^6$ subsets — a **$524,288\times$ speedup**!
