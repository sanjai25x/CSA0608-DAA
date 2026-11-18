# Pseudocode Specification - Question 7: Day 4 Design Challenge
**Course:** CSA0608 – Design and Analysis of Algorithms  
**Authors:** Sanjai S (192511018) & Pair Partner  
**Topic:** KartIQ Retail Data Analytics Platform - Unified Divide-and-Conquer Engine

---

## 1. Master KartIQ Orchestration Architecture

```text
ALGORITHM KartIQ_Engine(DailyOrders_10M, SellerScores_100K, UserMatrix_1024, ItemMatrix_1024, LookupKey)
    // Purpose: End-to-end Divide and Conquer pipeline for national retail analytics
    
    // Step 1: Nightly Order Consolidation (Student A)
    ConsolidatedOrders <- StableMergeSort(DailyOrders_10M, 0, LENGTH(DailyOrders_10M) - 1)
    
    // Step 2: Live Leaderboard Ranking (Student B)
    RankedSellers <- MedianOfThreeIntrosort(SellerScores_100K)
    
    // Step 3: High-Speed Chronological Order Lookup (Student B)
    FirstArrivalIdx <- LowerBoundBinarySearch(ConsolidatedOrders, LookupKey)
    
    // Step 4A: Stream Transaction Extremes (Student A)
    (MinPrice, MaxPrice) <- TournamentMaxMin(ConsolidatedOrders.Prices, 0, LENGTH(ConsolidatedOrders) - 1)
    
    // Step 4B: Recommendation Matrix Scoring (Joint)
    RecommendationMatrix <- HybridStrassenMultiply(UserMatrix_1024, ItemMatrix_1024, threshold=64)
    
    RETURN (ConsolidatedOrders, RankedSellers, FirstArrivalIdx, (MinPrice, MaxPrice), RecommendationMatrix)
END ALGORITHM
```

---

## 2. Quantitative Performance Guarantees

| Module | Algorithm | Time Complexity | Auxiliary Space | Improvement over Naive Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Order Consolidation** | Stable Merge Sort | $\Theta(n \log n)$ | $O(n)$ ($320\text{ MB}$) | Exact stability guarantees audit compliance; cuts erratic comparisons |
| **Seller Leaderboard** | Median-of-3 Introsort | $\Theta(n \log n)$ | $O(\log n)$ (in-place) | Reduces comparisons from $5\times 10^9$ to $1.66\times 10^6$ on nearly-sorted data ($99.967\%$ reduction) |
| **Order Lookup** | Lower-Bound Binary Search | $\Theta(\log n)$ | $O(1)$ | Locates timestamp in $\le 24$ steps vs $10,000,000$ linear steps ($99.99976\%$ reduction) |
| **Price Extremes** | Tournament Tree Max-Min | $\Theta(n)$ | $O(\log n)$ stack | Exactly $1.5n - 2$ comparisons vs $2n - 2$ ($25.00\%$ reduction) |
| **Recommendation Engine** | Hybrid Strassen Multiplier | $\Theta(n^{2.807})$ | $O(n^2)$ | Drops scalar multiplications from $1.074\times 10^9$ to $2.825\times 10^8$ ($73.69\%$ reduction) |
