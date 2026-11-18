"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO3 ASSIGNMENT - QUESTION 6: ADVANCED DIVIDE AND CONQUER (UNIFIED RUNNER)
STUDENT A: SANJAI S (192511018) | STUDENT B: PAIR PARTNER
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import sys
import os

# Add parent directory to path to import both submodules
current_dir = os.path.dirname(os.path.abspath(__file__))
q6_root = os.path.dirname(current_dir)
sys.path.append(os.path.join(q6_root, "Median_of_Medians"))
sys.path.append(os.path.join(q6_root, "Meet_in_the_Middle"))

from median_of_medians import run_median_of_medians_demo
from meet_in_the_middle import run_meet_in_the_middle_demo

def main():
    print("=" * 80)
    print("CSA0608 - QUESTION 6: ADVANCED DIVIDE AND CONQUER")
    print("PART A: DETERMINISTIC O(n) SELECTION VIA MEDIAN OF MEDIANS (STUDENT A)")
    print("PART B: EXPONENTIAL REDUCTION VIA MEET IN THE MIDDLE (STUDENT B)")
    print("=" * 80)
    
    print("\n[SECTION 1: STUDENT A - MEDIAN OF MEDIANS]")
    run_median_of_medians_demo()
    
    print("\n" + "=" * 80)
    print("[SECTION 2: STUDENT B - MEET IN THE MIDDLE]")
    run_meet_in_the_middle_demo()
    
    print("\n" + "=" * 80)
    print("[SUCCESS] All Q6 Advanced Divide and Conquer Mini-Investigations Completed!")
    print("=" * 80)

if __name__ == "__main__":
    main()
