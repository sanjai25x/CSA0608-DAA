# Task 3: Routing Engine Under Changing Network Conditions
## Algorithm Pseudocode (SIMATS Engineering Standard)

### Algorithm 3A: Dijkstra's Single-Source Shortest Path
```pascal
ALGORITHM DijkstraSSSP(Graph(V, E), source)
// Computes single-source shortest paths on non-negative weighted graphs
// Input: Graph(V, E), source vertex s
// Output: dist[V] shortest distances, pred[V] predecessors, finalizedOrder list

BEGIN
    FOR EACH v IN V DO
        dist[v] ← ∞
        pred[v] ← NIL
        visited[v] ← FALSE
    END FOR
    dist[source] ← 0
    INSERT (0, source) INTO PriorityQueue PQ
    DECLARE finalizedOrder AS LIST

    WHILE PQ IS NOT EMPTY DO
        (d, u) ← EXTRACT_MIN(PQ)
        IF visited[u] = TRUE THEN
            CONTINUE
        END IF
        visited[u] ← TRUE
        APPEND u TO finalizedOrder

        FOR EACH neighbor v OF u WITH EDGE WEIGHT w DO
            IF visited[v] = FALSE AND dist[u] + w < dist[v] THEN
                dist[v] ← dist[u] + w
                pred[v] ← u
                INSERT (dist[v], v) INTO PQ
            END IF
        END FOR
    END WHILE

    RETURN dist, pred, finalizedOrder
END ALGORITHM
```

### Algorithm 3B: Bellman-Ford Negative Cycle Aware SSSP
```pascal
ALGORITHM BellmanFord(V, E, source)
// Computes SSSP and detects reachable negative cycles
// Input: Vertices V, Edges E, source vertex s
// Output: dist[V], pred[V], hasNegativeCycle boolean

BEGIN
    FOR EACH v IN V DO
        dist[v] ← ∞
        pred[v] ← NIL
    END FOR
    dist[source] ← 0

    // Relax all edges |V| - 1 times
    FOR pass ← 1 TO |V| - 1 DO
        changed ← FALSE
        FOR EACH (u, v, w) IN E DO
            IF dist[u] ≠ ∞ AND dist[u] + w < dist[v] THEN
                dist[v] ← dist[u] + w
                pred[v] ← u
                changed ← TRUE
            END IF
        END FOR
        IF changed = FALSE THEN
            BREAK // Early termination optimization
        END IF
    END FOR

    // |V|-th pass: Check for negative-weight cycles
    FOR EACH (u, v, w) IN E DO
        IF dist[u] ≠ ∞ AND dist[u] + w < dist[v] THEN
            RETURN NULL, NULL, TRUE // Negative cycle detected!
        END IF
    END FOR

    RETURN dist, pred, FALSE
END ALGORITHM
```

### Algorithm 3C: Floyd-Warshall (APSP) & Warshall (Transitive Closure)
```pascal
ALGORITHM FloydWarshallAPSP(V, E)
// Computes all-pairs shortest path distance matrix D and reachability matrix R
// Input: Graph with vertices V and edges E
// Output: D[1..n, 1..n] real matrix, R[1..n, 1..n] boolean matrix

BEGIN
    n ← |V|
    DECLARE D[1..n, 1..n] OF REAL
    DECLARE R[1..n, 1..n] OF BOOLEAN

    FOR i ← 1 TO n DO
        FOR j ← 1 TO n DO
            IF i = j THEN
                D[i, j] ← 0
                R[i, j] ← TRUE
            ELSE
                D[i, j] ← ∞
                R[i, j] ← FALSE
            END IF
        END FOR
    END FOR

    FOR EACH (u, v, w) IN E DO
        D[u, v] ← MIN(D[u, v], w)
        R[u, v] ← TRUE
    END FOR

    // Dynamic Programming over intermediate vertices k
    FOR k ← 1 TO n DO
        FOR i ← 1 TO n DO
            FOR j ← 1 TO n DO
                // Floyd distance update
                IF D[i, k] ≠ ∞ AND D[k, j] ≠ ∞ THEN
                    D[i, j] ← MIN(D[i, j], D[i, k] + D[k, j])
                END IF
                // Warshall boolean reachability update
                R[i, j] ← R[i, j] OR (R[i, k] AND R[k, j])
            END FOR
        END FOR
    END FOR

    RETURN D, R
END ALGORITHM
```
