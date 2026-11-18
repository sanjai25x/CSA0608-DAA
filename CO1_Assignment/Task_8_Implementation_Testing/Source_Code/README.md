# TASK 8: Implementation and Testing Architecture

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Directory Structure of Implementation
All source code modules are organized cleanly inside `CO1_Assignment/Task_8_Implementation_Testing/Source_Code/`:

```
Source_Code/
├── linear_search.py            # Iterative linear search implementation
├── iterative_binary_search.py  # Iterative divide-and-conquer binary search
├── recursive_binary_search.py  # Recursive divide-and-conquer binary search
├── hash_search.py              # Hash table indexing implementation (Day-4 Architecture)
├── test_cases.py               # Automated unit test suite verifying correctness
├── benchmark.py                # High-precision performance & timing benchmark suite
└── benchmark_results.json      # Structured benchmark data across all scales
```

---

## 2. Source Code Descriptions

### 2.1 `linear_search.py`
Implements sequential searching. Returns a tuple `(index, comparisons)` to measure basic operations precisely without debugger or profiler interference.
- **Function Signature:** `linear_search(arr, key)`
- **Behavior:** Iterates through $0$ to $n-1$. Returns 0-based index if found, else -1.

### 2.2 `iterative_binary_search.py`
Implements iterative binary search on sorted data using two boundary pointers `low` and `high`.
- **Function Signature:** `iterative_binary_search(arr, key)`
- **Safety:** Uses `mid = (low + high) // 2` (or integer overflow safe arithmetic `low + (high - low) // 2`).

### 2.3 `recursive_binary_search.py`
Implements recursive divide-and-conquer with a state counter tracking comparison operations across recursive stack frames.
- **Function Signature:** `recursive_binary_search(arr, key)`
- **Helper:** `recursive_binary_search_helper(arr, low, high, key, cmp_container)`

### 2.4 `hash_search.py`
Implements a dynamic Hash Table with separate chaining buckets and automatic doubling when load factor $\alpha \ge 0.75$, demonstrating expected $\Theta(1)$ lookup for the Day-4 Design Challenge.

---

## 3. Unit Test Verification (`test_cases.py`)
The unit testing harness validates all algorithms against fundamental boundary and edge conditions:
1. **Best-case target at index 0:** Verifies linear search terminates in 1 comparison.
2. **Worst-case target at index $n-1$:** Verifies linear search takes exactly $n$ comparisons.
3. **Midpoint target:** Verifies binary search terminates in 1 comparison.
4. **Key absent from array:** Verifies proper sentinel return `-1` and full comparison exhaustion.
5. **Single-element array:** Boundary check for $n=1$.
6. **Empty array:** Boundary check for $n=0$.
7. **Hash table storage and collision handling:** Verifies lookup correctness with hashed bucket traversal.

### 3.1 Test Execution Output
```
PS C:\Users\SANJAI\CSA0608-DAA> python Task_8_Implementation_Testing\Source_Code\test_cases.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
All unit tests pass with zero errors.

---

## 4. Reproducible Execution Instructions

### Running Unit Tests:
```powershell
python Task_8_Implementation_Testing/Source_Code/test_cases.py
```

### Running the Full Experimental Benchmark:
```powershell
python Task_8_Implementation_Testing/Source_Code/benchmark.py
```
