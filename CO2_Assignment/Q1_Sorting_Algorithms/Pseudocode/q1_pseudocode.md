# Q1 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Selection Sort (Non-Adaptive)

### Algorithmic Logic:
Iterates $n-1$ times. In each pass $i$, it exhaustively scans the unsorted suffix $A[i+1 \dots n-1]$ to locate the index of the absolute minimum element. Once found, it swaps $A[i]$ with $A[\text{min\_idx}]$ if $\text{min\_idx} \neq i$.

```text
ALGORITHM SelectionSort(A, n):
    Input: Array A of n elements
    Output: Array A sorted in ascending order

    for i ← 0 to n - 2 do
        min_idx ← i
        for j ← i + 1 to n - 1 do
            if A[j] < A[min_idx] then
                min_idx ← j
            end if
        end for
        if min_idx ≠ i then
            Swap(A[i], A[min_idx])
        end if
    end for
    return A
```

---

## 2. Adaptive Bubble Sort (Early-Exit Swapped Flag)

### Algorithmic Logic:
Performs adjacent element comparisons and swaps out-of-order pairs. Maintains a boolean flag `swapped`. If a full pass executes without any swaps, the collection is already sorted, and the algorithm halts immediately in $\Theta(n)$ time.

```text
ALGORITHM AdaptiveBubbleSort(A, n):
    Input: Array A of n elements
    Output: Array A sorted in ascending order

    for i ← 0 to n - 1 do
        swapped ← False
        for j ← 0 to n - 2 - i do
            if A[j] > A[j + 1] then
                Swap(A[j], A[j + 1])
                swapped ← True
            end if
        end for
        if not swapped then
            break  // Early exit: list is fully sorted
        end if
    end for
    return A
```

---

## 3. Insertion Sort (Adaptive Backward Shift)

### Algorithmic Logic:
Maintains a sorted prefix $A[0 \dots i-1]$ and incrementally inserts the element $A[i]$ (`key`) into its correct position by shifting larger elements one position to the right. Scans backward only as far as necessary, achieving $O(1)$ comparisons per element on sorted inputs.

```text
ALGORITHM InsertionSort(A, n):
    Input: Array A of n elements
    Output: Array A sorted in ascending order

    for i ← 1 to n - 1 do
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] > key do
            A[j + 1] ← A[j]   // Shift element right
            j ← j - 1
        end while
        A[j + 1] ← key        // Place key in correct slot
    end for
    return A
```
