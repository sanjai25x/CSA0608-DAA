# Pseudocode Specification - Question 1: Max-Min & Binary Search
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Divide and Conquer - Finding Minimum & Maximum and Binary Search

---

## 1. Algorithm 1: Divide-and-Conquer Max-Min (Tournament Method)

```text
ALGORITHM MaxMinDC(A, low, high)
    // Purpose: Finds minimum and maximum elements using Divide and Conquer
    // Input: Array A[low...high]
    // Output: Pair (min_val, max_val)

    IF low == high THEN
        RETURN (A[low], A[low])             // Base case 1: Single element
    END IF

    IF high == low + 1 THEN                 // Base case 2: Exactly two elements
        IF A[low] < A[high] THEN
            RETURN (A[low], A[high])
        ELSE
            RETURN (A[high], A[low])
        END IF
    END IF

    // Divide Phase
    mid <- FLOOR((low + high) / 2)

    // Conquer Phase
    (min1, max1) <- MaxMinDC(A, low, mid)
    (min2, max2) <- MaxMinDC(A, mid + 1, high)

    // Combine Phase (2 comparisons)
    IF min1 < min2 THEN
        final_min <- min1
    ELSE
        final_min <- min2
    END IF

    IF max1 > max2 THEN
        final_max <- max1
    ELSE
        final_max <- max2
    END IF

    RETURN (final_min, final_max)
END ALGORITHM
```

### Mathematical Recurrence
$$T(n) = 2T(n/2) + 2, \quad \text{for } n > 2$$
$$T(2) = 1, \quad T(1) = 0$$
$$\text{Total Comparisons } = \frac{3n}{2} - 2 \quad (\text{vs. } 2n - 2 \text{ for linear search})$$

---

## 2. Algorithm 2: Modified Binary Search (First Occurrence / Lower-Bound)

```text
ALGORITHM LowerBoundBinarySearch(A, n, target)
    // Purpose: Locates earliest index of target in sorted array containing duplicates
    // Input: Sorted array A[0...n-1], search target
    // Output: Index of first occurrence, or -1 if target is not present

    low <- 0
    high <- n - 1
    result <- -1

    WHILE low <= high DO
        mid <- FLOOR((low + high) / 2)

        IF A[mid] == target THEN
            result <- mid               // Record candidate match
            high <- mid - 1             // Bisect left to find earlier occurrences
        ELSE IF A[mid] < target THEN
            low <- mid + 1              // Target lies in right half
        ELSE
            high <- mid - 1             // Target lies in left half
        END IF
    END WHILE

    RETURN result
END ALGORITHM
```

### Mathematical Recurrence
$$T(n) = T(n/2) + \Theta(1) \implies \Theta(\log_2 n)$$
Maximum comparisons for $n = 10,000,000$ records: $\lfloor \log_2(10^7) \rfloor + 1 = 24$ steps.
