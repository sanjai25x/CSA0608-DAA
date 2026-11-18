"""
Q3: Engineer the Behaviour of Brute-Force String Matching
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S (192511018)
Institution: SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences

Investigates how text and pattern structure influences computational effort
while holding dimensions strictly fixed at n = 10,000 and m = 20:
Test 1: Low-Work Pair (Disjoint Leading Character)
Test 2: High-Work Pair (Repeated Prefix Trap)
Test 3: Realistic Syslog Prefix Trap (249 Benign + 1 Alert Line)
"""

import time

def brute_force_string_match(text, pattern):
    """
    Executes standard brute-force string matching.
    Returns (matches, comparisons, time_ms).
    """
    n = len(text)
    m = len(pattern)
    comparisons = 0
    matches = []
    
    t0 = time.perf_counter_ns()
    # Number of possible alignment shifts is n - m + 1
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
    t1 = time.perf_counter_ns()
    return matches, comparisons, (t1 - t0) / 1e6

def run_q3_experiments():
    print("================================================================================")
    print("       Q3: BRUTE-FORCE STRING MATCHING BEHAVIOR UNDER FIXED DIMENSIONS          ")
    print("       Author: Sanjai S (192511018) | Fixed Dimensions: n = 10,000, m = 20      ")
    print("================================================================================")
    
    n = 10000
    m = 20
    alignments = n - m + 1 # 9,981
    
    # 1. Test 1: Low-Work Pair
    text_1 = "ABCD" * 2500
    pattern_1 = "X" + "A" * 19
    pred_comps_1 = alignments * 1
    
    # 2. Test 2: High-Work Pair
    text_2 = "A" * 10000
    pattern_2 = "A" * 19 + "B"
    pred_comps_2 = alignments * m
    
    # 3. Test 3: Realistic Syslog Prefix Trap
    line_benign = "[INFO] AUTH_SUCCESS usr=admin sess=123\n" # 40 chars
    line_alert  = "[INFO] AUTH_FAILURE usr=root ip=1.2.3.4\n"  # 40 chars
    text_3 = (line_benign * 249) + line_alert # exactly 250 * 40 = 10,000 chars
    pattern_3 = "[INFO] AUTH_FAILURE " # 20 chars
    # Theoretical prediction:
    # 9,981 alignments. Non-'[' positions fail on j=0 (1 comp).
    # 249 benign lines match 12 chars '[INFO] AUTH_' before failing on 'S' vs 'F' (13 comps, +12 extra)
    # 1 alert line matches all 20 chars (20 comps, +19 extra)
    pred_comps_3 = alignments + (249 * 12) + 19 # 9981 + 2988 + 19 = 12,988
    
    tests = [
        ("Test 1: Low-Work (Disjoint Leading Char)", text_1, pattern_1, pred_comps_1),
        ("Test 2: High-Work (Repeated Prefix Trap)", text_2, pattern_2, pred_comps_2),
        ("Test 3: Realistic Syslog Prefix Trap", text_3, pattern_3, pred_comps_3)
    ]
    
    print(f"\n{'Test Condition':<40} | {'Alignments':<10} | {'Pred Comps':<10} | {'Obs Comps':<10} | {'Comps/Shift':<11} | {'Matches':<7} | {'Time (ms)'}")
    print("-" * 108)
    
    for desc, t, p, pred_c in tests:
        matches, obs_c, t_ms = brute_force_string_match(t, p)
        assert obs_c == pred_c, f"Prediction mismatch! Expected {pred_c}, got {obs_c}"
        cps = obs_c / alignments
        print(f"{desc:<40} | {alignments:<10} | {pred_c:<10,d} | {obs_c:<10,d} | {cps:<11.4f} | {len(matches):<7} | {t_ms:.4f}")

    print("\n[CONCLUSION] Holding (n, m) = (10,000, 20) fixed, operational work varied from 9,981 to 199,620 comparisons.")
    print("This 20.0x work variation demonstrates that input size alone is insufficient for runtime prediction;")
    print("alphabet cardinality, prefix repetition, and failure offsets critically dictate algorithmic performance.")

if __name__ == "__main__":
    run_q3_experiments()
