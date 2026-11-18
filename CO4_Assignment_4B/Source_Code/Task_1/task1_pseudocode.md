# Task 1: Word Wrap as a Document-Layout Engine
## Algorithm Pseudocode (SIMATS Engineering Standard)

```pascal
ALGORITHM WordWrapDP(words[1..n], M)
// Arranges words[1..n] into lines of maximum width M minimizing cubic slack penalty
// Input: words[1..n] array of strings, M integer maximum line width
// Output: minPenalty integer, lineBreak[1..n] reconstruction pointers

BEGIN
    // Step 1: Pre-validation of input constraints
    FOR i ← 1 TO n DO
        IF LENGTH(words[i]) > M THEN
            RAISE ERROR "Word length exceeds maximum line width"
        END IF
    END FOR

    // Step 2: Compute line cost matrix P[1..n, 1..n]
    DECLARE P[1..n, 1..n] OF REAL
    FOR i ← 1 TO n DO
        currentLength ← 0
        FOR j ← i TO n DO
            IF j = i THEN
                currentLength ← LENGTH(words[j])
            ELSE
                currentLength ← currentLength + 1 + LENGTH(words[j])
            END IF

            IF currentLength <= M THEN
                unusedSpaces ← M - currentLength
                IF j = n THEN
                    P[i, j] ← 0          // Final line carries zero penalty
                ELSE
                    P[i, j] ← (unusedSpaces)^3  // Cubic penalty for interior lines
                END IF
            ELSE
                P[i, j] ← ∞             // Line overflow is strictly invalid
            END IF
        END FOR
    END FOR

    // Step 3: Dynamic Programming table initialization
    DECLARE DP[0..n] OF REAL
    DECLARE parent[1..n] OF INTEGER
    DP[0] ← 0

    // Step 4: Optimal Substructure Evaluation
    FOR j ← 1 TO n DO
        DP[j] ← ∞
        parent[j] ← -1
        FOR i ← 1 TO j DO
            IF P[i, j] ≠ ∞ THEN
                candidateCost ← DP[i - 1] + P[i, j]
                IF candidateCost < DP[j] THEN
                    DP[j] ← candidateCost
                    parent[j] ← i
                END IF
            END IF
        END FOR
    END FOR

    // Step 5: Route Backtracking and Line Reconstruction
    DECLARE lines AS LIST OF STRINGS
    curr ← n
    WHILE curr > 0 DO
        start ← parent[curr]
        CONSTRUCT LINE FROM words[start..curr]
        PREPEND LINE TO lines
        curr ← start - 1
    END WHILE

    RETURN DP[n], lines
END ALGORITHM
```

### Complexity Analysis
- **Time Complexity:** 
  - Cost precomputation: $O(n^2)$
  - DP state evaluation: $O(n^2)$ nested loops ($j$ from $1$ to $n$, $i$ from $1$ to $j$).
  - Backtracking: $O(k)$ where $k \le n$ is the number of lines.
  - Overall Time Complexity: $\Theta(n^2)$.
- **Space Complexity:**
  - Cost matrix $P$: $O(n^2)$ (can be reduced to $O(n)$ with on-the-fly calculation).
  - DP arrays $DP[0..n]$ and $parent[1..n]$: $O(n)$.
  - Overall Space Complexity: $O(n^2)$ or $O(n)$.
