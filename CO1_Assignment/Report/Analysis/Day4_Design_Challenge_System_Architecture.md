# Day-4 Design Challenge: System Architecture and Defense
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Author:** Sanjai S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Challenge Parameters
- **Database Records ($N$):** $1\,000\,000$ active students
- **Search Rate ($Q$):** $50\,000$ queries per hour ($\approx 13.89$ requests/second)
- **Record Insertions:** Daily batch insertion (once every 24 hours)

---

## 2. Comparative Evaluation Under 50,000 Searches / Hour

### 2.1 Operation Load
- **Linear Search (Worst Case):**
  $$50\,000 \times 1\,000\,000 = \mathbf{50\,000\,000\,000 \text{ comparisons/hour (50 Billion)}}$$
  Estimated CPU time: $797.33$ seconds ($\approx 13.3$ minutes of 100% single-core saturation).
- **Iterative Binary Search:**
  $$50\,000 \times 20 = \mathbf{1\,000\,000 \text{ comparisons/hour (1 Million)}}$$
  Estimated CPU time: $0.35$ seconds per hour.
- **In-Memory Hash Index:**
  $$50\,000 \times 1 = \mathbf{50\,000 \text{ comparisons/hour}}$$
  Estimated CPU time: $0.17$ seconds per hour.

---

## 3. Recommended Hybrid Architecture (MODIFY)
Rather than an isolated single-algorithm model, the system is designed as a **Hybrid Dual-Engine**:
1. **Primary Key-Value Hash Index:** Provides expected $\Theta(1)$ exact registration number lookups for 50,000 queries/hour.
2. **Secondary Sorted Array View:** Preserves registration number ordering for range queries (e.g., retrieving all students enrolled in a department cohort).
3. **Daily Batch Synchronizer:** Daily batch records ($k \approx 1\,000$) are inserted in $O(k)$ time into the hash table, and merged in $O(N)$ time into the sorted array during the midnight maintenance window.
