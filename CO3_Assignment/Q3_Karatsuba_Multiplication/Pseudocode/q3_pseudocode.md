# Pseudocode Specification - Question 3: Karatsuba Multiplication
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** Divide and Conquer - Fast Integer Multiplication

---

## 1. Algorithmic Formulation

```text
ALGORITHM Karatsuba(x, y)
    // Purpose: Multiplies two large integers x and y using 3 recursive subproblems
    // Input: Large integers x, y
    // Output: Product x * y

    // Base Case: Single-digit integers
    IF x < 10 OR y < 10 THEN
        RETURN x * y
    END IF

    n <- MAX(Length(x), Length(y))
    m <- FLOOR(n / 2)
    p <- 10^m

    // Divide Phase: Split into high and low digit blocks
    a <- FLOOR(x / p)
    b <- x MOD p
    c <- FLOOR(y / p)
    d <- y MOD p

    // Conquer Phase: 3 recursive calls instead of 4
    ac <- Karatsuba(a, c)
    bd <- Karatsuba(b, d)
    ad_plus_bc <- Karatsuba(a + b, c + d) - ac - bd

    // Combine Phase: Polynomial power-of-10 reconstruction
    product <- ac * (p * p) + ad_plus_bc * p + bd

    RETURN product
END ALGORITHM
```

---

## 2. Mathematical Complexity Derivation
Standard grade-school multiplication:
$$xy = ac \cdot 10^{2m} + (ad + bc) \cdot 10^m + bd$$
Requires 4 recursive calls ($ac, ad, bc, bd$):
$$T(n) = 4T(n/2) + O(n) \implies \Theta(n^{\log_2 4}) = \Theta(n^2)$$

Karatsuba's algebraic substitution:
$$(a+b)(c+d) = ac + (ad + bc) + bd \implies (ad + bc) = (a+b)(c+d) - ac - bd$$
Reduces recursive multiplications to 3:
$$T(n) = 3T(n/2) + O(n)$$
By Master Theorem ($a = 3, b = 2, f(n) = O(n)$):
Since $n^{\log_2 3} \approx n^{1.585} > n^1$:
$$T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$$
