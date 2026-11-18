# TASK 12: Day-4 Design Challenge – Large-Scale High-Throughput Adaptation

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S  
**Register Number:** 192511018  
**Faculty / Department:** Department of Computer Science and Engineering, SIMATS Engineering  

---

## 1. Challenge Specification
The university expands system requirements under new operational parameters:
- **Database Scale ($N$):** $1\,000\,000$ active student records.
- **Search Query Load ($Q$):** $50\,000$ search requests per hour.
- **Update Frequency:** New student records are ingested **only once per day** in a scheduled batch.
- **Task Objective:** Re-evaluate the original algorithmic design and determine whether it should be **RETAINED**, **MODIFIED**, or **REDESIGNED**.

---

## Part A: Impact Analysis (2 Marks)

### A.1 Shift in Operational Dynamics
1. **Query-Intensive Workload:**
   - Hourly search rate: $50\,000$ requests/hour $\approx 13.89$ requests/second continuous load.
   - Daily search volume: $50\,000 \times 24 = 1\,200\,000$ queries/day.
   - Peak bursts may reach $100$ to $200$ queries/second during registration periods.
2. **Update Asymmetry:**
   - Record insertions occur only once per 24-hour cycle (e.g., midnight batch run).
   - The ratio of search reads to record writes is:
     $$\text{Read-to-Write Ratio} = \frac{1\,200\,000 \text{ reads/day}}{1\,000 \text{ writes/day}} = 1\,200 : 1$$
3. **Invalidation of Naive Assumptions:**
   - In single-user or batch settings, occasional $30$ ms latency (Linear Search) might be tolerated. Under $50\,000$ queries/hour, per-query latency directly compounds into thread pool starvation and severe queue congestion.
   - Because updates are rare, **preprocessing costs can be amortized over 1.2 million queries per day**, making aggressive indexing economically justifiable.

---

## Part B: Evaluation of the Original Design (2 Marks)

### B.1 Mathematical Stress-Testing Under 50,000 Searches/Hour

#### 1. Iterative Linear Search (Catastrophic Failure):
- Average comparisons per search: $\frac{n+1}{2} = 500\,000$.
- Hourly comparison load:
  $$50\,000 \times 500\,000 = \mathbf{25\,000\,000\,000 \text{ comparisons/hour (25 Billion)}}$$
- Worst-case load: $50\,000 \times 1\,000\,000 = \mathbf{50 \text{ Billion comparisons/hour}}$.
- Total CPU processing time:
  $$\text{Hourly Time} = 50\,000 \times 0.0159 \text{ s} \approx \mathbf{797.33 \text{ seconds (13.3 minutes of 100\% CPU saturation)}}$$
- **Verdict:** Completely unacceptable.

#### 2. Original Recommended Iterative Binary Search (Viable but Optimization Opportunity):
- Comparisons per search: $\lceil \log_2(1\,000\,001) \rceil = 20$.
- Hourly comparison load:
  $$50\,000 \times 20 = \mathbf{1\,000\,000 \text{ comparisons/hour (1 Million)}}$$
- Total CPU processing time:
  $$\text{Hourly Time} = 50\,000 \times 7.00 \times 10^{-6} \text{ s} = \mathbf{0.35 \text{ seconds per hour}}$$
- **Verdict:** Highly practical, stable, and easily handles the load with $< 0.01\%$ CPU utilization.

#### 3. Hash Indexing Evaluation:
- Expected comparisons per search: $1$.
- Hourly comparison load:
  $$50\,000 \times 1 = \mathbf{50\,000 \text{ comparisons/hour}}$$
- Total CPU processing time:
  $$\text{Hourly Time} = 50\,000 \times 3.40 \times 10^{-6} \text{ s} = \mathbf{0.17 \text{ seconds per hour}}$$
- Hash Table construction overhead: $0.1318$ s (incurred once per day).

---

## Part C: Adaptation Decision and Strategy: MODIFY (2 Marks)

### C.1 Engineering Decision
**Decision: $\mathbf{MODIFY}$**  
Rather than completely discarding the sorted array or relying solely on a basic hash table, we architect a **High-Performance Hybrid Indexing Architecture**:
1. **Primary Search Engine:** An In-Memory Hash Table index keyed by `registration_number` for $O(1)$ exact-match point queries.
2. **Secondary Analytical Engine:** A sorted registration index / B+ Tree view maintained for range searches, alphabetically ordered roster generation, and graduation reports.
3. **Daily Ingestion Pipeline:** An off-peak batch merger that updates both structures during scheduled maintenance.

### C.2 Algorithmic Structure of Hybrid Architecture
```text
SYSTEM UniversityStudentRecordEngine:
    state:
        HashTable: H          // Primary O(1) exact-match index
        SortedArray: A        // Secondary O(log n) ordered index

    PROCEDURE InitializeEngine(database_records):
        H ← BuildHashTable(database_records)       // O(N) time, O(N) memory
        A ← SortRecords(database_records)           // O(N log N) time

    FUNCTION PointQuery(reg_no):
        // Handles 50,000 queries/hour in expected O(1) time
        return H.search(reg_no)

    FUNCTION RangeQuery(start_reg_no, end_reg_no):
        // Uses sorted array and binary search for interval lookups
        start_idx ← IterativeBinarySearch(A, start_reg_no)
        end_idx ← IterativeBinarySearch(A, end_reg_no)
        return A[start_idx .. end_idx]

    PROCEDURE DailyBatchUpdate(new_records):
        // Executed once every 24 hours during off-peak maintenance (e.g. 02:00 AM)
        for record in new_records do:
            H.insert(record.reg_no, record)         // O(1) per record
        A ← MergeSorted(A, Sort(new_records))      // O(N + K) linear merge
```

### C.3 Complexity Impact of the Modification

| Operational Dimension | Original Design (Binary Search) | Revised Hybrid Design (Hash + Sorted View) |
| :--- | :--- | :--- |
| **Exact Point Search Time** | $\Theta(\log n)$ ($\approx 20$ comps, $7$ $\mu\text{s}$) | $\mathbf{\Theta(1)}$ ($\approx 1$ comp, $3.4$ $\mu\text{s}$) |
| **Range / Prefix Query Time** | $O(\log n + k)$ | $\mathbf{O(\log n + k)}$ (retained via sorted view) |
| **Memory Footprint** | $\approx 8$ MB (contig array) | $\approx 49.5$ MB (array + hash table) |
| **Daily Ingestion Overhead** | Re-sort or merge: $O(N)$ | Linear insertion: $O(K)$ into hash + $O(N)$ merge |

---

## Part D: Evidence-Based Defense (2 Marks)

### D.1 Mathematical and Quantitative Justification

#### 1. Dramatic Reduction in Daily Point Operations
Over a 24-hour cycle serving $1\,200\,000$ point requests:
- **Binary Search:** $1\,200\,000 \times 20 = \mathbf{24\,000\,000 \text{ comparisons/day}}$.
- **Hybrid Hash Engine:** $1\,200\,000 \times 1 = \mathbf{1\,200\,000 \text{ comparisons/day}}$.
- **Net Daily Savings:** **$22\,800\,000$ comparison operations eliminated daily** ($95\%$ reduction in CPU comparison workload).

#### 2. Negligible Memory Overhead
For $1\,000\,000$ student records:
- A Python hash table storing integer keys and 64-bit pointers requires approximately **$41.5$ MB** of heap memory.
- Modern enterprise servers possess $32$ GB to $256$ GB of RAM. Allocating $41.5$ MB accounts for **$< 0.13\%$ of available memory**, making the space-time trade-off extraordinarily favorable.

#### 3. Low Preprocessing Overhead vs Tremendous Benefit
- Building the hash index takes only **$0.1318$ seconds** once per day during the midnight maintenance window.
- Daily batch insertion of $1\,000$ new enrollments takes **$1.5$ milliseconds** ($1\,000 \times O(1)$ inserts).
- The daily maintenance cost ($< 0.14$ seconds) is recovered within the first **$20$ queries** of the day.

#### 4. System Resilience and Graceful Degradation
Under unexpected traffic surges (e.g., examination result publication exceeding $200\,000$ requests/hour), the expected $O(1)$ lookup guarantees that average request latency remains under $4$ microseconds, preventing thread exhaustion in the university's web application servers.

---

## 5. Summary Conclusion of Day-4 Challenge
The evidence conclusively establishes that **MODIFYING** the architecture into a **Hybrid Hash-Indexed System with Daily Batch Synchronization** delivers optimal asymptotic efficiency, sub-millisecond responsiveness for $50\,000+$ requests/hour, and full support for both point and range queries on $1\,000\,000$ records.
