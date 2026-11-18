# Pseudocode Specification - Question 2: Merge Sort & Quick Sort
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Divide and Conquer - Quality of Decomposition in Sorting

---

## 1. Algorithm 1: Stable Merge Sort

```text
ALGORITHM MergeSort(A, low, high)
    // Purpose: Sorts array stably using Divide and Conquer
    // Input: Array A[low...high]
    // Output: In-place sorted subarray A[low...high]

    IF low < high THEN
        mid <- FLOOR((low + high) / 2)
        MergeSort(A, low, mid)
        MergeSort(A, mid + 1, high)
        Merge(A, low, mid, high)
    END IF
END ALGORITHM

ALGORITHM Merge(A, low, mid, high)
    n1 <- mid - low + 1
    n2 <- high - mid
    Create temporary arrays L[0...n1-1] and R[0...n2-1]

    FOR i <- 0 TO n1 - 1 DO L[i] <- A[low + i]
    FOR j <- 0 TO n2 - 1 DO R[j] <- A[mid + 1 + j]

    i <- 0, j <- 0, k <- low

    WHILE i < n1 AND j < n2 DO
        IF L[i] <= R[j] THEN              // '<=' enforces sorting stability!
            A[k] <- L[i]
            i <- i + 1
        ELSE
            A[k] <- R[j]
            j <- j + 1
        END IF
        k <- k + 1
    END WHILE

    WHILE i < n1 DO A[k] <- L[i]; i <- i + 1; k <- k + 1
    WHILE j < n2 DO A[k] <- R[j]; j <- j + 1; k <- k + 1
END ALGORITHM
```

### Mathematical Recurrence
$$T(n) = 2T(n/2) + c \cdot n \implies \Theta(n \log_2 n) \quad \text{across all inputs!}$$

---

## 2. Algorithm 2: Improved Median-of-Three Quick Sort

```text
ALGORITHM MedianOfThree(A, low, high)
    mid <- FLOOR((low + high) / 2)
    IF A[mid] < A[low] THEN SWAP A[low] WITH A[mid]
    IF A[high] < A[low] THEN SWAP A[low] WITH A[high]
    IF A[mid] < A[high] THEN SWAP A[mid] WITH A[high]
    RETURN A[high]                        // Median placed at A[high]
END ALGORITHM

ALGORITHM ImprovedQuickSort(A, low, high)
    IF low < high THEN
        IF high - low == 1 THEN
            IF A[low] > A[high] THEN SWAP A[low] WITH A[high]
            RETURN
        END IF

        pivot <- MedianOfThree(A, low, high)
        i <- low - 1
        FOR j <- low TO high - 1 DO
            IF A[j] <= pivot THEN
                i <- i + 1
                SWAP A[i] WITH A[j]
            END IF
        END FOR
        SWAP A[i + 1] WITH A[high]
        p <- i + 1

        ImprovedQuickSort(A, low, p - 1)
        ImprovedQuickSort(A, p + 1, high)
    END IF
END ALGORITHM
```

### Comparison Summary
- **First-Element Pivot on Sorted Data:** $T(n) = T(n-1) + (n-1) = \Theta(n^2)$, depth $n$.
- **Median-of-Three Pivot:** $T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$, depth $\log_2 n$.
