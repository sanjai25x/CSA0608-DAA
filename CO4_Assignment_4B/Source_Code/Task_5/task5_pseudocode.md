# Task 5: Three Greedy Engineers, One Network
## Algorithm Pseudocode (SIMATS Engineering Standard)

### Algorithm 5A: Kruskal's MST Algorithm
```pascal
ALGORITHM KruskalMST(V, E)
// Constructs MST by sorting all edges globally and uniting disjoint sets
// Input: Vertices V, Edges E with weights w
// Output: MST edge list, totalCost

BEGIN
    DECLARE mstEdges AS LIST
    totalCost ← 0
    INITIALIZE DisjointSetUnion DSU FOR ALL v IN V
    SORT E BY WEIGHT ASCENDING

    FOR EACH (u, v, w) IN E DO
        rootU ← DSU.FIND(u)
        rootV ← DSU.FIND(v)
        IF rootU ≠ rootV THEN
            DSU.UNION(rootU, rootV)
            APPEND (u, v, w) TO mstEdges
            totalCost ← totalCost + w
            IF LENGTH(mstEdges) = |V| - 1 THEN
                BREAK
            END IF
        END IF
    END FOR

    RETURN mstEdges, totalCost
END ALGORITHM
```

### Algorithm 5B: Prim's MST Algorithm
```pascal
ALGORITHM PrimMST(V, E, startVertex)
// Grows single MST tree from arbitrary start vertex using priority queue cut exploration
// Input: Vertices V, Edges E, root startVertex
// Output: MST edge list, totalCost

BEGIN
    DECLARE visited AS SET
    DECLARE mstEdges AS LIST
    totalCost ← 0
    INITIALIZE PriorityQueue PQ

    ADD startVertex TO visited
    FOR EACH (neighbor, w) ADJACENT TO startVertex DO
        INSERT (w, startVertex, neighbor) INTO PQ
    END FOR

    WHILE PQ IS NOT EMPTY AND LENGTH(mstEdges) < |V| - 1 DO
        (w, u, v) ← EXTRACT_MIN(PQ)
        IF v IN visited THEN
            CONTINUE
        END IF

        ADD v TO visited
        APPEND (u, v, w) TO mstEdges
        totalCost ← totalCost + w

        FOR EACH (nextNeighbor, nextW) ADJACENT TO v DO
            IF nextNeighbor NOT IN visited THEN
                INSERT (nextW, v, nextNeighbor) INTO PQ
            END IF
        END FOR
    END WHILE

    RETURN mstEdges, totalCost
END ALGORITHM
```

### Algorithm 5C: Borůvka's MST Algorithm
```pascal
ALGORITHM BoruvkaMST(V, E)
// Constructs MST in parallel rounds by contracting components along cheapest edges
// Input: Vertices V, Edges E
// Output: MST edge list, totalCost

BEGIN
    DECLARE mstEdges AS LIST
    totalCost ← 0
    INITIALIZE DisjointSetUnion DSU FOR ALL v IN V
    numComponents ← |V|

    WHILE numComponents > 1 DO
        DECLARE cheapest[1..numComponents] AS NIL

        // Find cheapest incident edge for each connected component
        FOR EACH (u, v, w) IN E DO
            rootU ← DSU.FIND(u)
            rootV ← DSU.FIND(v)
            IF rootU ≠ rootV THEN
                IF cheapest[rootU] = NIL OR w < cheapest[rootU].weight THEN
                    cheapest[rootU] ← (u, v, w)
                END IF
                IF cheapest[rootV] = NIL OR w < cheapest[rootV].weight THEN
                    cheapest[rootV] ← (u, v, w)
                END IF
            END IF
        END FOR

        // Contract components along selected safe edges
        FOR EACH edge IN cheapest DO
            IF edge ≠ NIL THEN
                rootU ← DSU.FIND(edge.u)
                rootV ← DSU.FIND(edge.v)
                IF rootU ≠ rootV THEN
                    DSU.UNION(rootU, rootV)
                    APPEND edge TO mstEdges
                    totalCost ← totalCost + edge.weight
                    numComponents ← numComponents - 1
                END IF
            END IF
        END FOR
    END WHILE

    RETURN mstEdges, totalCost
END ALGORITHM
```
