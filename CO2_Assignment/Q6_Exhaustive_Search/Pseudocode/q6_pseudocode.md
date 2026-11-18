# Q6 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Student-Designed Exhaustive Knapsack Search

### Algorithmic Logic:
Each candidate load configuration among $n$ available packages is encoded as an $n$-bit binary integer mask $m \in [0 \dots 2^n - 1]$. The $i$-th bit of mask $m$ represents whether package $i$ is loaded ($1$) or excluded ($0$). The algorithm enumerates all $2^n$ binary selection vectors, accumulates total weight and value by bitwise inspection, verifies feasibility against payload limit $W$, and retains the candidate yielding the global maximum humanitarian value.

```text
ALGORITHM ExhaustiveKnapsack(weights, values, n, W):
    Input: Arrays weights and values of n packages, maximum payload capacity W
    Output: Tuple (best_selection, best_weight, best_value)

    total_subsets ← 2^n
    best_value ← 0
    best_weight ← 0
    best_mask ← 0

    for mask ← 0 to total_subsets - 1 do
        current_weight ← 0
        current_value ← 0

        for i ← 0 to n - 1 do
            if (mask >> i) & 1 == 1 then
                current_weight ← current_weight + weights[i]
                current_value ← current_value + values[i]
            end if
        end for

        if current_weight ≤ W then
            if current_value > best_value then
                best_value ← current_value
                best_weight ← current_weight
                best_mask ← mask
            end if
        end if
    end for

    best_selection ← DecodeActiveIndices(best_mask, n)
    return (best_selection, best_weight, best_value)
```

---

## 2. Combinatorial Growth Derivation and Deployment Boundary

1. **Solution Space Growth:**  
   By the fundamental counting principle, each package offers 2 binary decisions ($\text{exclude} = 0$, $\text{include} = 1$).  
   Total subsets:
   $$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$
   Adding one additional package doubles the search space:
   $$2^{n+1} = 2 \cdot 2^n$$
2. **Computational Effort:**  
   Each subset evaluation requires $n$ bit-checks, resulting in total time complexity:
   $$T(n) = \Theta(n \cdot 2^n)$$
3. **Deployment Boundary (5.0-Second SLA):**  
   Emergency airlift logistics mandate flight manifest turnaround within $\le 5.0$ seconds.  
   - At $n = 22$: Evaluates $4\,194\,304$ subsets in $\approx 4.8$ seconds (compliant).
   - At $n = 23$: Requires $\approx 9.6$ seconds (violates SLA).
   - At $n = 30$: Evaluates $1\,073\,741\,824$ subsets ($\approx 25$ minutes).  
   Hence, $n_{\text{max}} = 22$ represents the strict operational boundary for exhaustive enumeration.
