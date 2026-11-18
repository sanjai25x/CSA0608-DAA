# Pseudocode Specification - Question 5: Closest Pair of Points
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Divide and Conquer - Computational Geometry

---

## 1. Algorithmic Formulation

```text
ALGORITHM ClosestPairDC(Px, Py)
    // Purpose: Finds closest pair of points in O(n log n) time
    // Input: Points pre-sorted by X (Px) and by Y (Py)
    // Output: Pair (p1, p2) with minimum Euclidean distance delta

    n <- LENGTH(Px)

    // Base Case: 2 or 3 points (solve directly via brute force)
    IF n <= 3 THEN
        RETURN BruteForceClosest(Px)
    END IF

    // Divide Phase: Vertical split line at median X coordinate
    mid <- FLOOR(n / 2)
    mid_point <- Px[mid]
    mid_x <- mid_point.x

    Lx <- Px[0...mid-1]
    Rx <- Px[mid...n-1]

    Split Py into Ly and Ry in O(n) preserving Y-order

    // Conquer Phase
    (pair_L, delta_L) <- ClosestPairDC(Lx, Ly)
    (pair_R, delta_R) <- ClosestPairDC(Rx, Ry)

    delta <- MIN(delta_L, delta_R)
    best_pair <- (delta == delta_L) ? pair_L : pair_R

    // Combine Phase: Inspect points within strip [mid_x - delta, mid_x + delta]
    strip <- [p IN Py WHERE |p.x - mid_x| < delta]

    // Check at most 7 neighbors ahead in Y-order (Geometric Bound)
    FOR i <- 0 TO LENGTH(strip) - 1 DO
        j <- i + 1
        WHILE j < LENGTH(strip) AND (strip[j].y - strip[i].y) < delta DO
            d <- Dist(strip[i], strip[j])
            IF d < delta THEN
                delta <- d
                best_pair <- (strip[i], strip[j])
            END IF
            j <- j + 1
        END WHILE
    END FOR

    RETURN (best_pair, delta)
END ALGORITHM
```

---

## 2. Mathematical Complexity & Geometric Proof
- **Geometric Constant Proof:**
  Consider a rectangle of width $2\delta$ and height $\delta$ centered on the dividing line. Any two points in the left half are separated by $\ge \delta$, and any two points in the right half are separated by $\ge \delta$. By packing circles of radius $\delta/2$, at most 8 points can reside in this rectangle without violating the minimum distance condition. Subtracting the point itself, each point needs to be compared with **at most 7 subsequent points**.
- **Recurrence:**
  $$T(n) = 2T(n/2) + O(n)$$
- **Master Theorem Solution:**
  $$T(n) = \Theta(n \log_2 n) \quad (\text{compared to } \Theta(n^2) \text{ for brute force})$$
