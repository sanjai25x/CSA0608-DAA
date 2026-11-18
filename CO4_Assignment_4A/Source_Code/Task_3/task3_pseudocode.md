# Task 3 – From Recurrence to Executable Logic: Dynamic Programming – 0/1 Knapsack
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Task 3.1 – Define the State
Let $DP[i][w]$ be the dynamic programming state defined as:
$$\mathbf{DP[i][w] = \text{The maximum total monetary value achievable by selecting a feasible subset of the first } i \text{ items } \{1, \dots, i\} \text{ such that their combined weight does not exceed } w.}$$
- **Indices:** $i \in \{0, 1, \dots, n\}$ denotes the item prefix index, and $w \in \{0, 1, \dots, W\}$ denotes the integer weight capacity budget.

---

## 2. Task 3.2 – Develop the Recurrence
The recurrence is constructed by decomposing the decision at stage $i$ into two mutually exclusive and exhaustive possibilities regarding item $i$:

### Boundary Conditions
1. $DP[0][w] = 0, \quad \forall w \in \{0, \dots, W\}$  
   *Interpretation:* With zero items available, the maximum achievable value is identically zero.
2. $DP[i][0] = 0, \quad \forall i \in \{0, \dots, n\}$  
   *Interpretation:* A knapsack with zero carrying capacity can accommodate zero weight, yielding zero value.

### Recurrence Relation
For $1 \le i \le n$ and $1 \le w \le W$:
$$DP[i][w] = \begin{cases} 
DP[i-1][w] & \text{if } w_i > w \\
\max\left(DP[i-1][w], \; DP[i-1][w - w_i] + v_i\right) & \text{if } w_i \le w 
\end{cases}$$

### Detailed Meaning of Terms
- **Condition $w_i > w$:** The weight of item $i$ exceeds the entire current budget $w$. Item $i$ cannot be accommodated; the optimal value is simply the best value achievable using the first $i-1$ items under capacity $w$.
- **Term $DP[i-1][w]$ (Exclude Decision):** The optimal solution if we choose to leave item $i$ behind. The capacity budget $w$ is entirely conserved for candidate items from $\{1 \dots i-1\}$.
- **Term $DP[i-1][w - w_i] + v_i$ (Include Decision):** The optimal solution if we choose to pack item $i$. Packing item $i$ guarantees value $v_i$ but consumes $w_i$ capacity, leaving a residual capacity of $w - w_i$ to be filled optimally by the remaining $i-1$ items.
- **$\max(\dots)$ Operator:** Asserts Bellman's Principle of Optimality by selecting the decision that yields the strictly superior cumulative payoff.

---

## 3. Task 3.3 – Translate the Recurrence into Pseudocode

```text
ALGORITHM ZeroOneKnapsackDP(Items, n, W)
    // Purpose: Determines maximum value and reconstructs selected items for 0/1 Knapsack
    // Inputs:
    //   Items[1...n] : Array of records with fields (id, weight, value)
    //   n            : Total number of indivisible items (integer >= 1)
    //   W            : Total weight capacity of vehicle (integer >= 1)
    // Outputs:
    //   optimal_value  : Maximum total value achievable within capacity W
    //   SelectedItems  : List of item records included in the optimal solution

    // Step 1: Initialize 2D DP Table of size (n + 1) x (W + 1)
    Create 2D array DP[0...n][0...W]

    FOR w <- 0 TO W DO
        DP[0][w] <- 0                   // Base case: 0 items
    END FOR

    FOR i <- 0 TO n DO
        DP[i][0] <- 0                   // Base case: 0 capacity
    END FOR

    // Step 2: Bottom-Up State Computation in Valid Dependency Order
    FOR i <- 1 TO n DO
        FOR w <- 1 TO W DO
            IF Items[i].weight > w THEN
                DP[i][w] <- DP[i - 1][w]                        // Cannot fit
            ELSE
                exclude_val <- DP[i - 1][w]
                include_val <- DP[i - 1][w - Items[i].weight] + Items[i].value
                IF include_val > exclude_val THEN
                    DP[i][w] <- include_val
                ELSE
                    DP[i][w] <- exclude_val
                END IF
            END IF
        END FOR
    END FOR

    optimal_value <- DP[n][W]

    // Step 3: Backtracking Reconstruction of Selected Items
    SelectedItems <- EMPTY_LIST
    current_w <- W

    FOR i <- n DOWNTO 1 DO
        // If current state differs from state without item i, item i was selected!
        IF DP[i][current_w] != DP[i - 1][current_w] THEN
            APPEND Items[i] TO SelectedItems
            current_w <- current_w - Items[i].weight
        END IF
    END FOR

    RETURN (optimal_value, SelectedItems)
END ALGORITHM
```

---

## 4. Task 3.4 – Desk-Check on Given Problem Instance

**Given Instance:**
- Item P: $w = 2, v = 12$
- Item Q: $w = 3, v = 20$
- Item R: $w = 4, v = 25$
- Item S: $w = 5, v = 30$
- Vehicle Capacity $W = 7$

### Complete DP Table ($DP[i][w]$)
| Item ($i$) | $w=0$ | $w=1$ | $w=2$ | $w=3$ | $w=4$ | $w=5$ | $w=6$ | $w=7$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 (None)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1: P (2, 12)** | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| **2: Q (3, 20)** | 0 | 0 | 12 | 20 | 20 | **32** | 32 | 32 |
| **3: R (4, 25)** | 0 | 0 | 12 | 20 | 25 | 32 | 37 | **45** |
| **4: S (5, 30)** | 0 | 0 | 12 | 20 | 25 | 32 | 37 | **45** |

### Key State Transition Traces Leading to Optimal Solution
- At cell $DP[2][5]$: Item Q ($w=3, v=20$) evaluates $\max(DP[1][5]=12, DP[1][5-3]+20 = 12+20) = \mathbf{32}$ (Items P + Q).
- At cell $DP[3][7]$: Item R ($w=4, v=25$) evaluates $\max(DP[2][7]=32, DP[2][7-4]+25 = 20+25) = \mathbf{45}$ (Items Q + R).
- At cell $DP[4][7]$: Item S ($w=5, v=30$) evaluates $\max(DP[3][7]=45, DP[3][7-5]+30 = 12+30 = 42) = \mathbf{45}$ (Item S rejected in favor of 45).

### Backtracking Reconstruction
1. Start at $DP[4][7] = 45$. Compare with $DP[3][7] = 45$: Identical $\implies$ **Item S was NOT included**. Residual capacity $= 7$.
2. At $DP[3][7] = 45$. Compare with $DP[2][7] = 32$: Different $\implies$ **Item R WAS included!** Residual capacity $= 7 - 4 = 3$.
3. At $DP[2][3] = 20$. Compare with $DP[1][3] = 12$: Different $\implies$ **Item Q WAS included!** Residual capacity $= 3 - 3 = 0$.
4. At $DP[1][0] = 0$: Capacity exhausted $\implies$ **Item P was NOT included**.

**Final Selected Items:** **{Q, R}**  
- Total Weight: $3 + 4 = 7 \text{ kg} \le 7 \text{ kg}$  
- Maximum Total Value: $20 + 25 = \mathbf{\$45}$

---

## 5. Task 3.5 – Explain the Dependency
Every state computation for $DP[i][w]$ references exactly two predecessor states:
1. $DP[i-1][w]$ (directly above in the preceding row)
2. $DP[i-1][w - w_i]$ (in the preceding row at a strictly smaller or equal column index $w - w_i \le w$)

**Why row $i-1$ must precede row $i$:**  
Because state transitions depend strictly on solutions to subproblems restricted to the item prefix $\{1 \dots i-1\}$, row $i-1$ must be fully computed and immutable in memory before any cell in row $i$ can be evaluated. If row $i$ were evaluated without row $i-1$ being finalized, the decision between including and excluding item $i$ would read uninitialized or corrupt data. Thus, the outer loop must iterate forward $i = 1 \dots n$.
