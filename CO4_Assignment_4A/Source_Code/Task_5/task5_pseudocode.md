# Task 5 – Same Graph, Different Algorithmic Reasoning: Dijkstra, Bellman-Ford, and Floyd
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Problem Graph Specification
Given directed weighted graph $G = (V, E, w)$ with vertices $V = \{A, B, C, D, E\}$ and edges:
- $A \to B: 4$
- $A \to C: 7$
- $B \to C: 2$
- $B \to D: 6$
- $C \to D: 1$
- $D \to E: 3$
- $C \to E: 8$

---

## 2. Task 5.1 – Greedy Shortest-Path Design (Dijkstra's Algorithm)

```text
ALGORITHM Dijkstra(V, E, w, source)
    // Purpose: Computes shortest paths from source to all vertices (Non-negative weights)
    // Inputs:
    //   V : Set of vertices {A, B, C, D, E}
    //   E : Set of directed edges
    //   w : Edge weight function (w(u, v) >= 0)
    //   source : Starting vertex (A)
    // Outputs:
    //   dist[v] : Shortest distance from source to vertex v
    //   pred[v] : Predecessor of vertex v on the shortest path

    // Step 1: Initialisation
    FOR EACH v IN V DO
        dist[v] <- INFINITY
        pred[v] <- NULL
    END FOR
    dist[source] <- 0

    UnvisitedSet <- COPY(V)

    // Step 2: Main Processing Loop
    WHILE UnvisitedSet is NOT EMPTY DO
        // Selection: Greedy choice of unvisited vertex with minimum tentative distance
        u <- EXTRACT_MIN(UnvisitedSet, dist)

        IF dist[u] == INFINITY THEN
            BREAK                       // Remaining vertices are unreachable
        END IF

        REMOVE u FROM UnvisitedSet

        // Step 3: Relaxation of Outgoing Adjacent Edges
        FOR EACH neighbor v ADJACENT TO u WHERE v IN UnvisitedSet DO
            new_distance <- dist[u] + w(u, v)
            IF new_distance < dist[v] THEN
                dist[v] <- new_distance         // Distance update
                pred[v] <- u                    // Predecessor update
            END IF
        END FOR
    END WHILE

    RETURN (dist, pred)
END ALGORITHM
```

### Trace on Given Graph from Source A
1. **Initial:** $dist = [A:0, B:\infty, C:\infty, D:\infty, E:\infty]$. Extract $A$. Relax $A \to B (4), A \to C (7) \implies dist[B]=4, dist[C]=7$.
2. **Step 1:** Extract $B$ ($dist[B]=4$).
   - Relax $B \to C: 4 + 2 = 6 < 7 \implies dist[C] \leftarrow 6, pred[C] \leftarrow B$.
   - Relax $B \to D: 4 + 6 = 10 \implies dist[D] \leftarrow 10, pred[D] \leftarrow B$.
3. **Step 2:** Extract $C$ ($dist[C]=6$).
   - Relax $C \to D: 6 + 1 = 7 < 10 \implies dist[D] \leftarrow 7, pred[D] \leftarrow C$.
   - Relax $C \to E: 6 + 8 = 14 \implies dist[E] \leftarrow 14, pred[E] \leftarrow C$.
4. **Step 3:** Extract $D$ ($dist[D]=7$).
   - Relax $D \to E: 7 + 3 = 10 < 14 \implies dist[E] \leftarrow 10, pred[E] \leftarrow D$.
5. **Step 4:** Extract $E$ ($dist[E]=10$). No outgoing unvisited neighbors.
- **Final Distances from A:** $A: 0, B: 4, C: 6, D: 7, E: 10$.

---

## 3. Task 5.2 – Change the Graph Assumption (Negative Weights & Bellman-Ford)

### Why the Greedy Assumption Fails
Dijkstra's greedy assumption states: *"Once a vertex $u$ with the minimum tentative distance is extracted from the unvisited set, its shortest path distance is permanently finalized and can never decrease."*  
With negative weights, this assumption is invalid: a longer path with positive edges may subsequently encounter a large negative edge, yielding a lower total distance to a vertex already declared "finalized."

### Bellman-Ford Core Relaxation Pseudocode
```text
ALGORITHM BellmanFord(V, E, w, source)
    FOR EACH v IN V DO
        dist[v] <- INFINITY
        pred[v] <- NULL
    END FOR
    dist[source] <- 0

    // Relax all edges |V| - 1 times
    FOR round <- 1 TO |V| - 1 DO
        FOR EACH (u, v) IN E DO
            IF dist[u] != INFINITY AND (dist[u] + w(u, v) < dist[v]) THEN
                dist[v] <- dist[u] + w(u, v)
                pred[v] <- u
            END IF
        END FOR
    END FOR

    // Check for reachable negative-weight cycles (|V|-th pass)
    FOR EACH (u, v) IN E DO
        IF dist[u] != INFINITY AND (dist[u] + w(u, v) < dist[v]) THEN
            REPORT "Reachable negative-weight cycle detected"
            RETURN (NULL, NULL)
        END IF
    END FOR

    RETURN (dist, pred)
END ALGORITHM
```

- **Why single greedy commitment fails:** A simple path in a graph with $|V|$ vertices contains at most $|V|-1$ edges. Without non-negativity guarantees, distance information must propagate hop-by-hop across all edges up to $|V|-1$ iterations.
- **Negative Cycle Detection:** If any edge can still be relaxed on the $|V|$-th iteration, distances can decrease infinitely, indicating a negative-weight cycle.

---

## 4. Task 5.3 – Change the Requirement (All-Pairs Shortest Path & Floyd-Warshall)

### Meaning of State $D^{(k)}[i][j]$
$$\mathbf{D^{(k)}[i][j] = \text{The length of the shortest path from vertex } i \text{ to vertex } j \text{ such that all intermediate vertices belong exclusively to the subset } \{1, 2, \dots, k\}.}$$

### Core State Transition Pseudocode
```text
ALGORITHM FloydWarshall(n, W)
    // W[i][j] is the initial direct edge weight matrix
    D <- COPY(W)

    FOR k <- 1 TO n DO                          // Intermediate vertex
        FOR i <- 1 TO n DO                      // Source vertex
            FOR j <- 1 TO n DO                  // Destination vertex
                IF D[i][k] + D[k][j] < D[i][j] THEN
                    D[i][j] <- D[i][k] + D[k][j]
                END IF
            END FOR
        END FOR
    END FOR

    RETURN D
END ALGORITHM
```

### Contrast with Single-Source Approaches
- **Single-Source (Dijkstra / Bellman-Ford):** Origin is fixed; states represent path lengths from source $s$ to vertex $v$ based on edge additions.
- **All-Pairs (Floyd-Warshall):** Dynamic programming over allowed intermediate vertex sets between all pairs $(i, j)$ simultaneously, solving $O(V^2)$ problems in $\Theta(V^3)$ time without edge-by-edge source restarts.
