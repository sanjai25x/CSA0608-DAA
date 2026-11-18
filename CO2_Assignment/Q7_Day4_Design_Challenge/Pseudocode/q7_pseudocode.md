# Q7 – Pseudocode and Algorithmic Logic (Day-4 Design Challenge)

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Redesigned Adaptive-Axis Sweep-Window Closest Pair

```text
ALGORITHM RedesignedClosestPair(P, n):
    Input: Array P of n 2D points representing drone coordinates P[i] = (x_i, y_i)
    Output: Tuple (best_pair, min_dist)

    if n < 2 then
        return (null, +infinity)
    end if

    // 1. Adaptive Primary-Axis Selection in O(n)
    span_X ← max(P.x) - min(P.x)
    span_Y ← max(P.y) - min(P.y)
    primary ← X if span_X ≥ span_Y else Y
    secondary ← opposite axis

    // 2. Sort indexed points along primary axis in O(n log n)
    S ← SortIndexedPoints(P, key = primary)

    min_dist_sq ← +infinity
    best_pair ← null

    // 3. Sweep-Window with Monotonic Early Termination
    for i ← 0 to n - 2 do
        for j ← i + 1 to n - 1 do
            d_prim ← S[j][primary] - S[i][primary]
            d_prim_sq ← d_prim * d_prim

            // Monotonic Pruning: Because S is sorted ascending along primary axis,
            // all future points k > j have d_prim(k, i) ≥ d_prim.
            // Hence, Euclidean distance must exceed min_dist_sq.
            if d_prim_sq ≥ min_dist_sq then
                break  // Terminate inner loop immediately!
            end if

            // Secondary-Axis Bounding Box Pruning
            d_sec ← S[j][secondary] - S[i][secondary]
            d_sec_sq ← d_sec * d_sec
            if d_sec_sq ≥ min_dist_sq then
                continue  // Skip without adding
            end if

            // Full 2D distance squared check
            dist_sq ← d_prim_sq + d_sec_sq
            if dist_sq < min_dist_sq then
                min_dist_sq ← dist_sq
                best_pair ← (S[i].orig_id, S[j].orig_id)
            end if
        end for
    end for

    // 4. Single Deferred Square Root
    min_dist ← sqrt(min_dist_sq)
    return (best_pair, min_dist)
```

---

## 2. Theoretical Complexity and Slab Physics
1. **Airspace Density:** In a uniform $L \times L$ airspace with $n$ drones, the average closest pair distance scales as $d_{\text{min}} \sim O(L / \sqrt{n})$.
2. **Window Candidate Bound:** The 1D slab $[x_i, x_i + d_{\text{min}}]$ contains on average:
   $$\text{Points in Slab} = n \cdot \frac{d_{\text{min}}}{L} \sim n \cdot \frac{L / \sqrt{n}}{L} = O(\sqrt{n})$$
3. **Complexity Reduction:**
   - Inner loop window checks drop from $O(n)$ to $O(\sqrt{n})$, giving total window checks $O(n \sqrt{n})$ (a $> 99.8\%$ check reduction).
   - Points falling within the $d_{\text{min}} \times d_{\text{min}}$ bounding box drop to $O(1)$, resulting in only $O(n)$ full distance evaluations.
   - Sqrt calls drop from $n(n-1)/2$ to exactly $1$.
