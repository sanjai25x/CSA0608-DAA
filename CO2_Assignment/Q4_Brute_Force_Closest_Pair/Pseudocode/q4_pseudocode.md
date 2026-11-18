# Q4 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Brute-Force Closest Pair Algorithm

### Algorithmic Logic:
Iterates over all unique 2D point pairs by enforcing strict upper-triangular indexing $0 \le i < j < n$. For each pair, it computes the Euclidean distance $\sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$. If this distance is strictly smaller than the running minimum, it updates the minimum distance and records the pair coordinates.

```text
ALGORITHM BruteForceClosestPair(P, n):
    Input: Array P of n 2D points representing drone positions P[i] = (x_i, y_i)
    Output: Tuple (best_pair, min_dist) of closest drones and their separation

    min_dist ← +infinity
    best_pair ← null

    for i ← 0 to n - 2 do
        for j ← i + 1 to n - 1 do
            dx ← P[i].x - P[j].x
            dy ← P[i].y - P[j].y
            dist ← sqrt(dx * dx + dy * dy)
            if dist < min_dist then
                min_dist ← dist
                best_pair ← (P[i], P[j])
            end if
        end for
    end for
    return (best_pair, min_dist)
```

---

## 2. Mathematical Derivation of Unique Candidate Pairs

To avoid self-pairs ($i = j$) and symmetric duplicates ($(i, j) \equiv (j, i)$), the outer index $i$ ranges from $0$ to $n-2$, and the inner index $j$ ranges from $i+1$ to $n-1$.
The number of inner loop executions for a fixed outer index $i$ is:
$$\text{Inner iterations} = (n - 1) - (i + 1) + 1 = n - 1 - i$$

Summing over all values of $i \in [0 \dots n-2]$:
$$P(n) = \sum_{i=0}^{n-2} (n - 1 - i) = (n - 1) + (n - 2) + \dots + 2 + 1$$
Let $k = n - 1 - i$. As $i$ ranges from $0$ to $n-2$, $k$ ranges from $n-1$ down to $1$:
$$P(n) = \sum_{k=1}^{n-1} k = \frac{(n-1)((n-1) + 1)}{2} = \frac{n(n-1)}{2} = \binom{n}{2} = \frac{n^2 - n}{2}$$

Asymptotically:
$$P(n) = \Theta(n^2)$$

When doubling the problem size ($n \to 2n$):
$$\frac{P(2n)}{P(n)} = \frac{2n(2n-1)/2}{n(n-1)/2} = \frac{2(2n-1)}{n-1} \xrightarrow{n \to \infty} 4\times$$
This proves that pairwise distance checks quadruple whenever the fleet size doubles.
