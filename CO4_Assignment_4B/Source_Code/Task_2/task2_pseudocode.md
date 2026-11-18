# Task 2: Greedy vs Dynamic Programming Knapsack
## Algorithm Pseudocode (SIMATS Engineering Standard)

### Algorithm 2A: Fractional Knapsack (Greedy Strategy)
```pascal
ALGORITHM FractionalKnapsackGreedy(items[1..n], capacity)
// Selects items/fractions maximizing value within vehicle capacity
// Input: items array containing (id, weight, value), capacity integer
// Output: totalValue real, selectedFractions array

BEGIN
    // Step 1: Compute density ratio and sort descending
    FOR i ← 1 TO n DO
        items[i].ratio ← items[i].value / items[i].weight
    END FOR
    SORT items BY items.ratio IN DESCENDING ORDER

    currentWeight ← 0
    totalValue ← 0.0
    DECLARE selections AS LIST

    // Step 2: Greedy item commitment
    FOR i ← 1 TO n DO
        IF currentWeight + items[i].weight <= capacity THEN
            currentWeight ← currentWeight + items[i].weight
            totalValue ← totalValue + items[i].value
            APPEND (items[i].id, 1.0, items[i].value) TO selections
        ELSE
            remainingCapacity ← capacity - currentWeight
            IF remainingCapacity > 0 THEN
                fraction ← remainingCapacity / items[i].weight
                fractionalValue ← items[i].value * fraction
                currentWeight ← currentWeight + remainingCapacity
                totalValue ← totalValue + fractionalValue
                APPEND (items[i].id, fraction, fractionalValue) TO selections
            END IF
            EXIT FOR  // Knapsack filled to capacity
        END IF
    END FOR

    RETURN totalValue, selections
END ALGORITHM
```

### Algorithm 2B: 0/1 Knapsack (Dynamic Programming)
```pascal
ALGORITHM Knapsack01DP(items[1..n], W)
// Computes exact global optimal subset of indivisible items fitting in capacity W
// Input: items array containing (weight, value), capacity W integer
// Output: maxProfit real, selectedItems list

BEGIN
    DECLARE DP[0..n, 0..W] OF REAL

    // Base cases
    FOR w ← 0 TO W DO
        DP[0, w] ← 0
    END FOR

    // Dynamic Programming table filling
    FOR i ← 1 TO n DO
        FOR w ← 0 TO W DO
            IF items[i].weight <= w THEN
                DP[i, w] ← MAX(DP[i - 1, w], DP[i - 1, w - items[i].weight] + items[i].value)
            ELSE
                DP[i, w] ← DP[i - 1, w]
            END IF
        END FOR
    END FOR

    // Backtracking to reconstruct chosen items
    DECLARE selectedItems AS LIST
    wRem ← W
    FOR i ← n DOWNTO 1 DO
        IF DP[i, wRem] ≠ DP[i - 1, wRem] THEN
            APPEND items[i] TO selectedItems
            wRem ← wRem - items[i].weight
        END IF
    END FOR

    RETURN DP[n, W], selectedItems
END ALGORITHM
```

### Theoretical Complexity Comparison
- **Fractional Knapsack (Greedy):**
  - Time Complexity: $O(n \log n)$ due to sorting.
  - Space Complexity: $O(1)$ auxiliary memory.
- **0/1 Knapsack (Dynamic Programming):**
  - Time Complexity: $\Theta(n \cdot W)$ pseudo-polynomial operations.
  - Space Complexity: $\Theta(n \cdot W)$ table memory (reducible to $\Theta(W)$ with 1D array).
