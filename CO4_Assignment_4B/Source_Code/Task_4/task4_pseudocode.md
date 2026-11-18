# Task 4: Smart Manufacturing Optimisation (Assembly Line Scheduling)
## Algorithm Pseudocode (SIMATS Engineering Standard)

```pascal
ALGORITHM AssemblyLineSchedulingDP(a1[1..n], a2[1..n], t1[1..n-1], t2[1..n-1], e1, e2, x1, x2)
// Determines minimum production time and optimal station route across two assembly lines
// Input: Processing times a1, a2; Transfer times t1, t2; Entry times e1, e2; Exit times x1, x2
// Output: minTime integer, optimalRoute[1..n] array of line choices

BEGIN
    DECLARE f1[1..n] OF INTEGER
    DECLARE f2[1..n] OF INTEGER
    DECLARE l1[2..n] OF INTEGER
    DECLARE l2[2..n] OF INTEGER

    // Base cases: entering station 1
    f1[1] ← e1 + a1[1]
    f2[1] ← e2 + a2[1]

    // Dynamic Programming table filling
    FOR j ← 2 TO n DO
        // Line 1 station j evaluation
        IF (f1[j - 1] + a1[j]) <= (f2[j - 1] + t2[j - 1] + a1[j]) THEN
            f1[j] ← f1[j - 1] + a1[j]
            l1[j] ← 1  // Stay on Line 1
        ELSE
            f1[j] ← f2[j - 1] + t2[j - 1] + a1[j]
            l1[j] ← 2  // Transfer from Line 2 to Line 1
        END IF

        // Line 2 station j evaluation
        IF (f2[j - 1] + a2[j]) <= (f1[j - 1] + t1[j - 1] + a2[j]) THEN
            f2[j] ← f2[j - 1] + a2[j]
            l2[j] ← 2  // Stay on Line 2
        ELSE
            f2[j] ← f1[j - 1] + t1[j - 1] + a2[j]
            l2[j] ← 1  // Transfer from Line 1 to Line 2
        END IF
    END FOR

    // Final exit stage determination
    IF (f1[n] + x1) <= (f2[n] + x2) THEN
        fStar ← f1[n] + x1
        lStar ← 1
    ELSE
        fStar ← f2[n] + x2
        lStar ← 2
    END IF

    // Backtracking optimal line sequence
    DECLARE route[1..n] OF INTEGER
    route[n] ← lStar
    FOR j ← n DOWNTO 2 DO
        IF route[j] = 1 THEN
            route[j - 1] ← l1[j]
        ELSE
            route[j - 1] ← l2[j]
        END IF
    END FOR

    RETURN fStar, route
END ALGORITHM
```

### Complexity Analysis
- **Time Complexity:** $\Theta(n)$ where $n$ is the number of stations. Each station requires constant $O(1)$ comparisons and arithmetic operations.
- **Space Complexity:** $\Theta(n)$ auxiliary arrays for memoizing states and choice pointers. Can be optimized to $O(1)$ space if only the minimum cost is needed, but $\Theta(n)$ is required to reconstruct the complete route.
