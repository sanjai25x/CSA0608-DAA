# Pseudocode Specification - Question 4: Strassen Matrix Multiplication
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Divide and Conquer - Fast Matrix Multiplication

---

## 1. Algorithmic Formulation

```text
ALGORITHM HybridStrassen(A, B, threshold)
    // Purpose: Multiplies two n x n matrices A and B using Strassen's 7 products
    // Input: Square matrices A, B; recursion cutoff threshold
    // Output: Product matrix C = A x B

    n <- ROWS(A)

    // Base Case / Hybrid Cutoff
    IF n <= threshold THEN
        RETURN ConventionalMatrixMultiply(A, B)
    END IF

    // Divide Phase: Partition into 4 submatrices of size (n/2) x (n/2)
    Partition A into [A11, A12], [A21, A22]
    Partition B into [B11, B12], [B21, B22]

    // Conquer Phase: 7 Recursive Matrix Multiplications
    M1 <- HybridStrassen(A11 + A22, B11 + B22, threshold)
    M2 <- HybridStrassen(A21 + A22, B11, threshold)
    M3 <- HybridStrassen(A11, B12 - B22, threshold)
    M4 <- HybridStrassen(A22, B21 - B11, threshold)
    M5 <- HybridStrassen(A11 + A12, B22, threshold)
    M6 <- HybridStrassen(A21 - A11, B11 + B12, threshold)
    M7 <- HybridStrassen(A12 - A22, B21 + B22, threshold)

    // Combine Phase: Quadrant Reconstruction via Matrix Additions
    C11 <- M1 + M4 - M5 + M7
    C12 <- M3 + M5
    C21 <- M2 + M4
    C22 <- M1 - M2 + M3 + M6

    RETURN ReconstructMatrix(C11, C12, C21, C22)
END ALGORITHM
```

---

## 2. Mathematical Complexity Derivation
- **Conventional Matrix Multiplication:**
  Requires 8 recursive multiplications of size $n/2$:
  $$T(n) = 8T(n/2) + \Theta(n^2) \implies \Theta(n^{\log_2 8}) = \Theta(n^3)$$

- **Strassen's Reduction:**
  Requires 7 recursive multiplications and 18 matrix additions:
  $$T(n) = 7T(n/2) + \Theta(n^2)$$
  By Master Theorem Case 1 ($a = 7, b = 2, f(n) = \Theta(n^2)$):
  Since $n^{\log_2 7} \approx n^{2.8074} > n^2$:
  $$T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.8074})$$

- **Operation Savings on $1024 \times 1024$ Matrices:**
  $$\text{Conventional Multiplications} = 1024^3 = 1,073,741,824$$
  $$\text{Strassen Multiplications} = 7^{10} = 282,475,249 \quad (73.69\% \text{ reduction})$$
