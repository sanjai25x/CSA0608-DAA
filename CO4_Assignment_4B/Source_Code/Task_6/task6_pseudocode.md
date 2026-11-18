# Task 6: Last-Mile Delivery Route Optimisation (TSP DP)
## Algorithm Pseudocode (SIMATS Engineering Standard)

```pascal
ALGORITHM HeldKarpTSP(cost[0..n-1, 0..n-1])
// Computes exact optimal Travelling Salesperson tour using bitmask Dynamic Programming
// Input: cost[0..n-1, 0..n-1] distance matrix where node 0 is Central Hub
// Output: minTourCost real, optimalTour[0..n] ordered sequence of vertices

BEGIN
    numSubsets ← 2^n
    DECLARE DP[0..numSubsets - 1, 0..n - 1] OF REAL
    DECLARE parent[0..numSubsets - 1, 0..n - 1] OF INTEGER

    // Initialize DP table to infinity
    FOR mask ← 0 TO numSubsets - 1 DO
        FOR j ← 0 TO n - 1 DO
            DP[mask, j] ← ∞
            parent[mask, j] ← -1
        END FOR
    END FOR

    // Base case: Starting at Hub (node 0) with visited set {0} (mask = 1)
    DP[1, 0] ← 0

    // Dynamic Programming iteration by subset size
    FOR size ← 2 TO n DO
        FOR EACH subset S OF {1..n-1} WITH |S| = size - 1 DO
            mask ← 1 BITWISE_OR (BITMASK OF S)

            FOR EACH j IN S DO
                prevMask ← mask BITWISE_XOR (1 BITWISE_SHIFT_LEFT j)
                bestCost ← ∞
                bestK ← -1

                IF size = 2 THEN
                    bestCost ← DP[prevMask, 0] + cost[0, j]
                    bestK ← 0
                ELSE
                    FOR EACH k IN S WITH k ≠ j DO
                        candidateCost ← DP[prevMask, k] + cost[k, j]
                        IF candidateCost < bestCost THEN
                            bestCost ← candidateCost
                            bestK ← k
                        END IF
                    END FOR
                END IF

                DP[mask, j] ← bestCost
                parent[mask, j] ← bestK
            END FOR
        END FOR
    END FOR

    // Final tour completion: return to Hub (node 0)
    fullMask ← (2^n) - 1
    minTourCost ← ∞
    lastNode ← -1
    FOR j ← 1 TO n - 1 DO
        tourCost ← DP[fullMask, j] + cost[j, 0]
        IF tourCost < minTourCost THEN
            minTourCost ← tourCost
            lastNode ← j
        END IF
    END FOR

    // Reconstruct optimal tour by backtracking parent pointers
    DECLARE tour AS LIST
    currMask ← fullMask
    currNode ← lastNode
    WHILE currNode ≠ 0 DO
        PREPEND currNode TO tour
        prevNode ← parent[currMask, currNode]
        currMask ← currMask BITWISE_XOR (1 BITWISE_SHIFT_LEFT currNode)
        currNode ← prevNode
    END WHILE
    PREPEND 0 TO tour
    APPEND 0 TO tour

    RETURN minTourCost, tour
END ALGORITHM
```

### Complexity Analysis
- **Time Complexity:** $\Theta(n^2 \cdot 2^n)$
  - There are $2^n$ subsets. For each subset $S$ and ending node $j$, we consider $|S| - 1 \le n$ transitions.
  - Total operations: $\sum_{k=1}^n \binom{n}{k} \cdot k \cdot (k-1) = \Theta(n^2 \cdot 2^n)$.
  - Comparing with brute force $O(n!)$, this is exponentially faster (e.g., for $n=20$: $20! \approx 2.4 \times 10^{18}$ vs $20^2 \cdot 2^{20} \approx 4.2 \times 10^8$ operations).
- **Space Complexity:** $\Theta(n \cdot 2^n)$
  - The DP memoization table requires $2^n$ rows and $n$ columns.
