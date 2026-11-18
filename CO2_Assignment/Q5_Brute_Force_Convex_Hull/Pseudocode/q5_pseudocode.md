# Q5 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Student-Derived Pseudocode: Brute-Force Convex Hull

```text
ALGORITHM BruteForceConvexHull(P, n):
    Input: Array P of n 2D points P[i] = (x_i, y_i)
    Output: List V of vertices forming the closed outer boundary in CCW order

    U ← DeduplicateCoordinates(P)
    n ← length(U)
    HullEdges ← empty list

    for i ← 0 to n - 2 do
        for j ← i + 1 to n - 1 do
            // Define line L(U[i], U[j]): a*x + b*y = c
            a ← U[j].y - U[i].y
            b ← U[i].x - U[j].x
            c ← U[i].x * U[j].y - U[i].y * U[j].x
            seg_len_sq ← (U[j].x - U[i].x)^2 + (U[j].y - U[i].y)^2

            has_pos ← False
            has_neg ← False
            valid_edge ← True

            for k ← 0 to n - 1 do
                if k == i or k == j then
                    continue
                end if

                side ← a * U[k].x + b * U[k].y - c

                if side > eps then
                    has_pos ← True
                else if side < -eps then
                    has_neg ← True
                else
                    // Collinear point: test if U[k] extends outside segment [U[i], U[j]]
                    proj ← (U[k].x - U[i].x)*(U[j].x - U[i].x) + (U[k].y - U[i].y)*(U[j].y - U[i].y)
                    if proj < -eps or proj > seg_len_sq + eps then
                        valid_edge ← False
                        break  // Reject proper sub-segments of collinear edges
                    end if
                end if

                // Early exit: points straddle both sides of the line (interior chord)
                if has_pos and has_neg then
                    valid_edge ← False
                    break
                end if
            end for

            if valid_edge then
                Append (U[i], U[j]) to HullEdges
            end if
        end for
    end for

    // Extract unique endpoints
    V ← UniqueEndpoints(HullEdges)
    (cx, cy) ← Centroid(V)
    Sort V in ascending order of atan2(v.y - cy, v.x - cx)
    return V
```

---

## 2. Geometric Correctness Proof

### Principle of Supporting Hyperplanes
1. **Definition of Convex Hull:** By definition, the convex hull $\text{Conv}(S)$ is the intersection of all closed half-planes containing the point set $S$:
   $$\text{Conv}(S) = \bigcap \{H \mid S \subseteq H\}$$
2. **Boundary Membership:** If a directed line $L(P_i, P_j)$ satisfies the condition that all remaining points $P_k \in S$ lie on one closed half-plane $H^+ = \{(x, y) \mid ax + by - c \ge 0\}$, then $L(P_i, P_j)$ forms a **supporting line** for $\text{Conv}(S)$. Since points $P_i$ and $P_j$ lie exactly on the boundary of $H^+$, the segment $[P_i, P_j]$ lies on the outer boundary $\partial\text{Conv}(S)$.
3. **Interior Chord Rejection:** Conversely, if points $P_u$ and $P_v$ exist such that $P_u \in H^+$ and $P_v \in H^-$, then the segment connecting $P_u$ and $P_v$ crosses $L(P_i, P_j)$ in its interior. Hence, $[P_i, P_j]$ penetrates the interior of $\text{Conv}(S)$ and cannot belong to the outer boundary.
4. **Maximal Collinear Filtering:** If $P_k$ is collinear with $P_i$ and $P_j$ but lies outside the interval $[P_i, P_j]$, then $[P_i, P_j]$ is merely a subset of the true edge $[P_i, P_k]$ or $[P_k, P_j]$. Enforcing the projection bounds guarantees that only maximal non-overlapping boundary edges are accepted.
