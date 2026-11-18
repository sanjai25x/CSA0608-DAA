# DESIGN, MATHEMATICAL ANALYSIS, AND EMPIRICAL EVALUATION OF DIVIDE-AND-CONQUER ALGORITHMS FOR HIGH-THROUGHPUT ENTERPRISE AND RETAIL ANALYTICS

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Course Outcome 3 (CO3) Assignment & Case Study  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Authors:**  
- **Student A (Primary Lead):** SANJAI S (Reg. No: 192511018)  
- **Student B (Pair Collaborator):** PAIR PARTNER (Reg. No: 192511025)  
**Date:** November 2026  

---

## BONAFIDE CERTIFICATE
This is to certify that this capstone report entitled **"DESIGN, MATHEMATICAL ANALYSIS, AND EMPIRICAL EVALUATION OF DIVIDE-AND-CONQUER ALGORITHMS FOR HIGH-THROUGHPUT ENTERPRISE AND RETAIL ANALYTICS"** is a bonafide collaborative record of work performed by **SANJAI S (192511018)** and **PAIR PARTNER (192511025)** under Course Outcome 3 (CO3) in CSA0608 – Design and Analysis of Algorithms at SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai.

---

## CANDIDATE DECLARATION
We hereby declare that this assignment represents our original intellectual work. All algorithmic designs, mathematical recurrence formulations, Master Theorem proofs, pseudocode specifications, Python implementations, test datasets, and Day-4 Design Challenge solutions were developed and validated by our pair group.

---

## STUDENT CONTRIBUTION RECORD

| Question / Module | Student A Responsibilities (Sanjai S - 192511018) | Student B Responsibilities (Pair Partner) | Collaborative Work |
| :--- | :--- | :--- | :--- |
| **Q1: Max-Min & Binary Search** | Tournament recurrence formulation ($T(n) = 2T(n/2)+2$), base cases, 25% comparison reduction proof. | Lower-bound modified binary search logic for duplicate handling, edge-case test suite. | Implementation benchmarking across $n=16$ to $65,536$; comparative graph generation. |
| **Q2: Merge Sort & Quick Sort** | Quick Sort worst-case $O(n^2)$ mathematical proof on sorted data; Lomuto vs Hoare partitioning. | Merge Sort stability mechanics and strict $\le$ invariant proof; recursion tree height analysis. | Comparative experiments on 4 contrasting distributions; recursion stack depth profiling. |
| **Q3: Karatsuba Multiplication** | Mathematical derivation of 3-multiplication recurrence ($T(n)=3T(n/2)+O(n)$); operation count analysis. | Hybrid Karatsuba threshold design; digit-by-digit naive multiplication simulator. | Empirical crossover analysis from 4 to 2048 digits; verification against native big-int arithmetic. |
| **Q4: Strassen Matrix Mult** | Mathematical derivation of 7 intermediate products ($M_1 \dots M_7$); Master Theorem Case 1 proof ($O(n^{2.807})$). | Matrix block partitioning, zero-padding for non-powers of 2, hybrid threshold switching ($n \le 16$). | Verification on $2 	imes 2$ assignment matrices; empirical benchmarking across dimensions $n=4$ to $64$. |
| **Q5: Closest Pair of Points** | Geometric proof bounding strip comparisons to at most 7 points; recurrence formulation ($O(n \log n)$). | X- and Y-coordinate presorting pipeline; strip filtering mechanics and Euclidean distance counter. | Comparative benchmarking against $O(n^2)$ brute force for $n=10$ to $4000$ points. |
| **Q6: Advanced D&C** | Submodule A: Median of Medians (BFPRT) deterministic $O(n)$ selection; 5-element block grouping. | Submodule B: Meet-in-the-Middle subset sum; $2^{n/2}$ search space reduction and binary search. | Empirical scaling benchmarks; asymptotic comparison tables ($2^n$ vs $2^{n/2}$). |
| **Q7: Day 4 Challenge (KartIQ)** | Student A Initial Proposal: External Stable Merge Sort for 10M orders, Tournament Max-Min engine. | Student B Initial Proposal: Median-of-3 Introsort for 100K leaderboard, Hybrid Strassen, Lower-Bound Search. | Joint Final Design synthesis, cross-defense, system integration, end-to-end benchmark suite. |

---

## ABSTRACT
Divide-and-Conquer (D&C) is a fundamental paradigm that solves complex problems by breaking them recursively into independent subproblems of identical structure, solving each subproblem, and recombining partial results into a globally optimal output. This capstone investigation examines the theoretical, mathematical, and empirical behavior of core Divide-and-Conquer algorithms: Tournament Max-Min, Lower-Bound Binary Search, Stable Merge Sort, Median-of-Three Introsort, Karatsuba Fast Multiplication, Strassen Matrix Multiplication, Closest Pair of Points, Blum-Floyd-Pratt-Rivest-Tarjan (BFPRT) Median of Medians, and Meet-in-the-Middle Subset Sum. 

In response to the Day-4 Design Challenge, the investigation formulates the architecture of KartIQ, a national e-commerce retail data analytics engine handling 10,000,000 daily transactions and 100,000 live seller rankings. Mathematical recurrence modeling via the Master Theorem proves that the D&C engine delivers a 25.00% comparison reduction for stream extremes ($3n/2 - 2$ vs $2n - 2$), a 99.967% comparison reduction on nearly-sorted seller leaderboards ($1.66\text{M}$ vs $\sim 5\text{B}$ comparisons), an instantaneous 24-step logarithmic order retrieval over 10M records ($99.99976\%$ reduction), and a 73.69% decrease in scalar multiplications for $1024 \times 1024$ recommendation matrices ($7^{10}$ vs $1024^3$). Empirical benchmarks closely mirror theoretical bounds, confirming Divide and Conquer as an indispensable paradigm for high-scale enterprise computing.

---

## 1. Algorithmic Overview & Mathematical Formulations

### 1.1 Question 1: Tournament Max-Min and Binary Search
- **Tournament Max-Min Recurrence:**
  $$T(n) = 2T(n/2) + 2, \quad T(2) = 1, \quad T(1) = 0$$
  Total comparisons: $\frac{3n}{2} - 2$, saving exactly $25.00\%$ comparisons compared to linear search ($2n - 2$).
- **Lower-Bound Binary Search:**
  $$T(n) = T(n/2) + \Theta(1) \implies \Theta(\log_2 n)$$
  Worst-case comparisons for $10^7$ records: $\lfloor \log_2(10^7) \rfloor + 1 = 24$ steps.

### 1.2 Question 2: Merge Sort vs Quick Sort
- **Merge Sort:**
  $$T(n) = 2T(n/2) + c \cdot n \implies \Theta(n \log n) \quad \text{stable, predictable across all distributions}$$
- **Quick Sort First-Pivot on Sorted Data:**
  $$T(n) = T(n-1) + (n-1) \implies \Theta(n^2), \quad \text{recursion depth } n$$
- **Quick Sort Median-of-Three:**
  $$T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n), \quad \text{recursion depth } \log_2 n$$

### 1.3 Question 3: Karatsuba Multiplication
- Algebraic substitution $(ad + bc) = (a + b)(c + d) - ac - bd$ reduces recursive multiplications from 4 to 3:
  $$T(n) = 3T(n/2) + O(n) \implies \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$$
  Saves $91.69\%$ of scalar multiplications on 1024-digit integers.

### 1.4 Question 4: Strassen Matrix Multiplication
- 7 matrix products $M_1 \dots M_7$ and 18 matrix additions:
  $$T(n) = 7T(n/2) + \Theta(n^2) \implies \Theta(n^{\log_2 7}) \approx \Theta(n^{2.8074})$$
  Cuts scalar multiplications by $73.69\%$ on $1024 \times 1024$ recommendation matrices.

### 1.5 Question 5: Closest Pair of Points
- Geometric circle packing limits strip checks to at most 7 neighbors:
  $$T(n) = 2T(n/2) + O(n) \implies \Theta(n \log n) \quad (\text{vs. } \Theta(n^2) \text{ brute force})$$

### 1.6 Question 6: Advanced Divide and Conquer
- **BFPRT Median of Medians (Student A):**
  $$T(n) \le T(n/5) + T(7n/10) + c \cdot n \implies \Theta(n) \quad \text{deterministic worst-case selection}$$
- **Meet in the Middle (Student B):**
  $$O(2^{n/2} \cdot n) \text{ time and } O(2^{n/2}) \text{ space, speeding up } n=40 \text{ by } 524,288\times \text{ over } O(2^n).$$

---

## 2. Day-4 Design Challenge: KartIQ Analytics Engine
The unified KartIQ engine integrates:
1. **Module 1 (Stable Merge Sort):** Consolidates 10M nightly orders with guaranteed arrival order preservation for financial audit compliance.
2. **Module 2 (Median-of-Three Introsort):** Sorts 100K live seller scores in-place without $O(n^2)$ freezing.
3. **Module 3 (Lower-Bound Binary Search):** Instantaneous order retrieval in $\le 24$ steps.
4. **Module 4A (Tournament Max-Min):** Real-time price stream extremes detection with $25\%$ comparison savings.
5. **Module 4B (Hybrid Strassen Multiplier):** Recommendation matrix scoring with $73.69\%$ fewer multiplications.

---

## 3. Empirical Performance Summary Table

| Module & Algorithm | Test Size (n) | Theoretical Complexity | Empirical Performance | Quantitative Improvement |
| :--- | :--- | :--- | :--- | :--- |
| **Tournament Max-Min** | $n = 65,536$ | $1.5n - 2$ cmps | 98,302 cmps ($8.92\text{ ms}$) | $25.00\%$ fewer comparisons vs Linear |
| **Lower-Bound Binary Search** | $n = 10,000,000$ | $\lfloor \log_2 n \rfloor + 1$ | 24 steps ($0.003\text{ ms}$) | $99.99976\%$ reduction vs Linear |
| **Merge Sort (Sorted)** | $n = 2,000$ | $\Theta(n \log n)$ | 10,864 cmps ($1.86\text{ ms}$) | Balanced depth 11; stable |
| **Quick Sort (First Pivot)** | $n = 2,000$ | $\Theta(n^2)$ | 1,999,000 cmps ($73.14\text{ ms}$) | Quadratic degradation; depth 1,999 |
| **Quick Sort (Med-of-3)** | $n = 2,000$ | $\Theta(n \log n)$ | 20,892 cmps ($1.25\text{ ms}$) | $98.95\%$ comparison reduction |
| **Karatsuba Mult** | 1024 digits | $\Theta(n^{1.585})$ | 87,129 mults ($26.77\text{ ms}$) | $91.69\%$ reduction vs Naive ($1.05\text{M}$) |
| **Strassen Matrix Mult** | $1024 \times 1024$ | $\Theta(n^{2.807})$ | $282,475,249$ mults | $73.69\%$ reduction vs Conventional |
| **Closest Pair D&C** | $n = 2,000$ pts | $\Theta(n \log n)$ | 2,248 calcs ($3.90\text{ ms}$) | $99.88\%$ reduction vs Brute Force |
| **Median of Medians** | $n = 50,000$ | Strictly $O(n)$ | $11.29\text{ ms}$ runtime | Deterministic linear guarantee |
| **Meet in the Middle** | $n = 30$ elements | $O(2^{n/2} \cdot n)$ | 65,536 subsets | $16,384\times$ state reduction vs $2^n$ |

---

## 4. Verification and Repository Organization
The complete implementation and artifacts are committed to the GitHub repository:
- `Q1_MaxMin_Binary_Search/`: Code, Pseudocode, Screenshots.
- `Q2_MergeSort_QuickSort/`: Code, Pseudocode, Screenshots.
- `Q3_Karatsuba_Multiplication/`: Code, Pseudocode, Screenshots.
- `Q4_Strassen_Matrix_Multiplication/`: Code, Pseudocode, Screenshots.
- `Q5_Divide_Conquer_Closest_Pair/`: Code, Pseudocode, Screenshots.
- `Q6_Advanced_Divide_Conquer/`: Code, Submodules, Pseudocode, Screenshots.
- `Q7_Day4_Design_Challenge/`: Student A & B initial proposals, Joint specification, Code, Screenshots.
- `Final_Report/`: `CO3_Assignment_Report.docx`, `Student_Contribution_Record.docx`, `CO3_Assignment_Report.md`.
