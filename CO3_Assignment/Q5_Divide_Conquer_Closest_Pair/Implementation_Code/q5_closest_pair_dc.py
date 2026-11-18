"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 5: CLOSEST PAIR OF POINTS (DIVIDE AND CONQUER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import math
import time
import random

class ClosestPairStats:
    def __init__(self):
        self.distance_computations = 0

def euclidean_dist(p1, p2, stats=None):
    if stats:
        stats.distance_computations += 1
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)

# ======================================================================================
# 1. BRUTE FORCE APPROACH (O(n^2))
# ======================================================================================

def closest_pair_brute_force(points, stats=None):
    n = len(points)
    min_d = float('inf')
    best_pair = None
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_dist(points[i], points[j], stats)
            if d < min_d:
                min_d = d
                best_pair = (points[i], points[j])
    return best_pair, min_d

# ======================================================================================
# 2. DIVIDE AND CONQUER APPROACH (O(n log n))
# ======================================================================================

def closest_pair_strip(strip, delta, best_pair, stats=None):
    """
    Checks points within the vertical strip sorted by y-coordinate.
    GEOMETRIC PROPERTY: At most 7 points can lie within a delta x 2delta box.
    Hence, inner loop runs at most 7 times!
    """
    min_d = delta
    current_best = best_pair
    n_strip = len(strip)
    
    for i in range(n_strip):
        # Look ahead at points whose y difference is strictly less than current min_d
        j = i + 1
        while j < n_strip and (strip[j][1] - strip[i][1]) < min_d:
            d = euclidean_dist(strip[i], strip[j], stats)
            if d < min_d:
                min_d = d
                current_best = (strip[i], strip[j])
            j += 1
            
    return current_best, min_d

def closest_pair_dc_recursive(Px, Py, stats=None):
    n = len(Px)
    if n <= 3:
        return closest_pair_brute_force(Px, stats)
    
    mid = n // 2
    mid_point = Px[mid]
    
    # Split Px
    Lx = Px[:mid]
    Rx = Px[mid:]
    
    # Split Py in O(n) preserving y-sorted order
    mid_x = mid_point[0]
    Ly = []
    Ry = []
    for p in Py:
        if p[0] <= mid_x and len(Ly) < mid:
            Ly.append(p)
        else:
            Ry.append(p)
            
    # Recursive conquer
    pair_left, delta_left = closest_pair_dc_recursive(Lx, Ly, stats)
    pair_right, delta_right = closest_pair_dc_recursive(Rx, Ry, stats)
    
    if delta_left < delta_right:
        delta = delta_left
        best_pair = pair_left
    else:
        delta = delta_right
        best_pair = pair_right
        
    # Combine step: inspect vertical strip [mid_x - delta, mid_x + delta]
    strip = [p for p in Py if abs(p[0] - mid_x) < delta]
    strip_pair, strip_delta = closest_pair_strip(strip, delta, best_pair, stats)
    
    return strip_pair, strip_delta

def closest_pair_divide_and_conquer(points):
    stats = ClosestPairStats()
    # Pre-sort points by X and by Y
    Px = sorted(points, key=lambda p: (p[0], p[1]))
    Py = sorted(points, key=lambda p: (p[1], p[0]))
    best_pair, min_d = closest_pair_dc_recursive(Px, Py, stats)
    return best_pair, min_d, stats.distance_computations

def run_q5_demo():
    print("=" * 80)
    print("QUESTION 5: CLOSEST PAIR OF POINTS (DIVIDE AND CONQUER)")
    print("=" * 80)
    
    # 1. Sample Dataset from Course Syllabus
    sample_pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"\n--- 1. Verification on Course Sample Dataset ---")
    print(f"Points: {sample_pts}")
    
    bf_stats = ClosestPairStats()
    bf_pair, bf_dist = closest_pair_brute_force(sample_pts, bf_stats)
    dc_pair, dc_dist, dc_comps = closest_pair_divide_and_conquer(sample_pts)
    
    print(f"Brute Force Result : {bf_pair} -> Distance = {bf_dist:.4f} (Computations: {bf_stats.distance_computations})")
    print(f"D&C Result         : {dc_pair} -> Distance = {dc_dist:.4f} (Computations: {dc_comps})")
    print(f"Verification       : {'MATCH' if abs(bf_dist - dc_dist) < 1e-9 else 'ERROR'}")
    
    # 2. Benchmarking Across Point Set Sizes (n = 10 to 5000)
    print(f"\n--- 2. Performance Comparison: Brute Force O(n^2) vs Divide & Conquer O(n log n) ---")
    print(f"{'Points (n)':<12} | {'BF Computations':<18} | {'D&C Computations':<18} | {'BF Time (ms)':<16} | {'D&C Time (ms)':<16}")
    print("-" * 88)
    
    test_sizes = [10, 50, 100, 250, 500, 1000, 2000, 4000]
    bench_results = []
    
    for n in test_sizes:
        pts = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        
        # Brute Force
        if n <= 2000:
            s_bf = ClosestPairStats()
            t0 = time.perf_counter()
            _, d_bf = closest_pair_brute_force(pts, s_bf)
            t_bf = (time.perf_counter() - t0) * 1000.0
            bf_c = s_bf.distance_computations
        else:
            bf_c = n * (n - 1) // 2
            t_bf = float('nan')
            
        # Divide and Conquer
        t0 = time.perf_counter()
        _, d_dc, dc_c = closest_pair_divide_and_conquer(pts)
        t_dc = (time.perf_counter() - t0) * 1000.0
        
        bf_time_str = f"{t_bf:12.4f} ms" if not math.isnan(t_bf) else "DNF / O(n^2)"
        print(f"{n:<12} | {bf_c:<18} | {dc_c:<18} | {bf_time_str:<16} | {t_dc:12.4f} ms")
        
        bench_results.append({
            'n': n, 'bf_c': bf_c, 'dc_c': dc_c, 't_bf': t_bf, 't_dc': t_dc
        })
        
    print("\n[SUCCESS] Q5 Implementation & Empirical Verification Complete.")
    return bench_results

if __name__ == "__main__":
    run_q5_demo()
