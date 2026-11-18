# Task 1 – Algorithm Design Review: Diagnose and Repair Poor Pseudocode
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Problem Context
A logistics company loads divisible packages with weight $w_i > 0$ and value $v_i > 0$ into a delivery vehicle of maximum weight capacity $C$. The objective is to maximize the total value loaded without exceeding $C$.

### Junior Engineer's Proposed Pseudocode
```text
ALGORITHM LoadVehicle
BEGIN
Read packages
Arrange packages
Select the best package
WHILE vehicle has space DO
Add suitable package
END WHILE

Calculate value
RETURN result
END
```

---

## 2. Task 1.1 – Diagnose the Design (Algorithmic Deficiencies)

| No. | Algorithmic Deficiency | Technical Explanation & Implementation Failure |
| :--- | :--- | :--- |
| **1** | **Undefined Inputs and Outputs** | The algorithm header declares no formal parameters or data structures (packages $P[1 \dots n]$, weights $W[1 \dots n]$, values $V[1 \dots n]$, and vehicle capacity $C$). An implementing engineer cannot determine how data is supplied, structured, or returned. |
| **2** | **Ambiguous Selection Criterion ("Arrange" & "Best")** | The directives `Arrange packages` and `Select the best package` conceal the essential greedy choice property. Does "best" denote maximum value, minimum weight, or maximum value-to-weight density ratio ($v_i / w_i$)? Without specifying the density sorting rule, an engineer might sort by absolute value, producing a provably suboptimal solution. |
| **3** | **Missing Remaining Capacity Tracking & Feasibility Check** | The condition `vehicle has space` is informal English. The algorithm fails to initialize a state variable $C_{\text{rem}} \leftarrow C$, decrement it when packages are added, or test whether a candidate package satisfies $w_i \le C_{\text{rem}}$. |
| **4** | **Failure to Handle Divisibility (Fractional Loading)** | The requirement explicitly states that packages may be divided. However, `Add suitable package` provides no mechanism to compute the fractional ratio $f \leftarrow C_{\text{rem}} / w_i$ when a package exceeds available room, leaving the vehicle underfilled. |
| **5** | **Undefined Loop Advancement & Non-Termination Trap** | The `WHILE` loop contains no iteration pointer ($i \leftarrow i + 1$) or element removal mechanism. If `Add suitable package` does not exhaust the capacity, the loop repeats indefinitely on the same package, causing an infinite loop. |
| **6** | **Incomplete Result Construction** | `Calculate value` and `RETURN result` fail to specify how allocated item fractions ($x_i \in [0, 1]$) or the cumulative numerical value ($\sum x_i \cdot v_i$) are accumulated and structured for the caller. |

---

## 3. Task 1.2 – Repair the Design (Complete & Precise Pseudocode)

```text
ALGORITHM FractionalKnapsack(P, W, V, n, C)
    // Purpose: Maximizes total value loaded into vehicle allowing divisible packages
    // Inputs:
    //   P[1...n] : Array of package identifiers
    //   W[1...n] : Array of positive package weights (W[i] > 0)
    //   V[1...n] : Array of positive package values (V[i] > 0)
    //   n        : Total number of packages (integer >= 1)
    //   C        : Total vehicle weight carrying capacity (real number > 0)
    // Outputs:
    //   X[1...n] : Array of loaded fractions (0.0 <= X[i] <= 1.0)
    //   total_value : Maximum total value loaded into vehicle

    // Step 1: Compute value-to-weight density ratio for each package
    Create array R[1...n]
    FOR i <- 1 TO n DO
        R[i] <- V[i] / W[i]
        X[i] <- 0.0                     // Initialize all allocation fractions to 0
    END FOR

    // Step 2: Sort packages in descending order of density ratio (Greedy Ordering)
    SORT P, W, V, R in descending order according to ratio R

    // Step 3: Initialize tracking variables
    current_capacity <- C
    total_value <- 0.0
    i <- 1

    // Step 4: Greedy Allocation Loop
    WHILE (i <= n) AND (current_capacity > 0) DO
        IF W[i] <= current_capacity THEN
            // Case A: Package fits completely
            X[i] <- 1.0
            total_value <- total_value + V[i]
            current_capacity <- current_capacity - W[i]
        ELSE
            // Case B: Package exceeds remaining capacity -> Take fractional portion
            X[i] <- current_capacity / W[i]
            total_value <- total_value + (X[i] * V[i])
            current_capacity <- 0.0     // Vehicle is now fully loaded
        END IF
        i <- i + 1
    END WHILE

    RETURN (X, total_value)
END ALGORITHM
```

---

## 4. Task 1.3 – Design Defence
This solution qualifies as **pseudocode** rather than code because it uses language-independent mathematical abstractions (`SORT ... in descending order`, `FOR i <- 1 TO n DO`) and explicit input/output contracts without syntax-specific boilerplate (memory pointers, class declarations, or I/O imports). It qualifies as pseudocode rather than informal English because every algorithmic state transition, feasibility boundary (`W[i] <= current_capacity`), greedy ratio calculation ($V[i]/W[i]$), and fractional division rule ($C_{\text{rem}}/W[i]$) is mathematically deterministic, unambiguous, and directly implementable by any software engineer. *(92 words)*
