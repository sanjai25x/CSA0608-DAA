"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 4: PSEUDOCODE FORENSICS - WORD BREAK DEFECT DIAGNOSIS & REPAIR
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

def faulty_word_break(text, dictionary):
    """
    Junior Engineer's Faulty WordBreak Algorithm.
    Flaw: Fails to verify DP[j] == True before accepting dictionary match.
    """
    n = len(text)
    DP = [False] * (n + 1)
    DP[0] = True
    trace = []

    for i in range(1, n + 1):
        for j in range(0, i):
            sub = text[j:i]
            if sub in dictionary:
                DP[i] = True
                trace.append({
                    "i": i,
                    "j": j,
                    "sub": sub,
                    "dp_j": DP[j],
                    "action": f"MATCH: DP[{i}] set to TRUE (Ignored DP[{j}]={DP[j]}!)"
                })
                break
        if not DP[i]:
            trace.append({
                "i": i,
                "j": "-",
                "sub": "-",
                "dp_j": "-",
                "action": f"NO MATCH: DP[{i}] remains FALSE"
            })

    return DP[n], DP, trace


def repaired_word_break(text, dictionary):
    """
    Repaired WordBreak Algorithm.
    Fix: Requires BOTH DP[j] == True AND substring(text, j, i) in dictionary.
    """
    n = len(text)
    DP = [False] * (n + 1)
    DP[0] = True
    trace = []

    for i in range(1, n + 1):
        for j in range(0, i):
            sub = text[j:i]
            # THE ESSENTIAL MINIMAL FIX: Check DP[j] == True!
            if DP[j] and (sub in dictionary):
                DP[i] = True
                trace.append({
                    "i": i,
                    "j": j,
                    "sub": sub,
                    "dp_j": DP[j],
                    "action": f"VALID TRANSITION: DP[{j}]=True & '{sub}' in Dict -> DP[{i}]=TRUE"
                })
                break
        if not DP[i]:
            trace.append({
                "i": i,
                "j": "-",
                "sub": "-",
                "dp_j": "-",
                "action": f"NO VALID PREFIX: DP[{i}] remains FALSE"
            })

    return DP[n], DP, trace


def run_task4_demo():
    print("=" * 80)
    print("TASK 4: PSEUDOCODE FORENSICS - WORD BREAK DEFECT DIAGNOSIS & REPAIR")
    print("=" * 80)

    # 1. Failing Counterexample (Task 4.2)
    failing_text = "abcat"
    failing_dict = {"cat"}
    
    print("\n--- 1. Testing Failing Input on Faulty vs Repaired Algorithm ---")
    print(f"Input Text       : \"{failing_text}\"")
    print(f"Dictionary       : {failing_dict}")
    print(f"Ground Truth     : FALSE (Prefix 'ab' cannot be segmented!)")

    faulty_res, faulty_dp, faulty_trace = faulty_word_break(failing_text, failing_dict)
    repaired_res, repaired_dp, repaired_trace = repaired_word_break(failing_text, failing_dict)

    print(f"\nFaulty Algorithm Result   : {faulty_res}  <-- ERRONEOUS (False Positive!)")
    print(f"Repaired Algorithm Result : {repaired_res} <-- CORRECT")
    
    print("\nFaulty Algorithm State Trace:")
    for t in faulty_trace:
        print(f"  Step i={t['i']}: {t['action']}")
        
    print("\nRepaired Algorithm State Trace:")
    for t in repaired_trace:
        print(f"  Step i={t['i']}: {t['action']}")

    # 2. Regression Test on Valid Case (Task 4.4)
    reg_text = "applepie"
    reg_dict = {"apple", "pie"}
    print("\n--- 2. Regression Verification on Valid Instance ---")
    print(f"Input Text   : \"{reg_text}\"")
    print(f"Dictionary   : {reg_dict}")
    print(f"Ground Truth : TRUE ('apple' + 'pie')")

    reg_faulty, _, _ = faulty_word_break(reg_text, reg_dict)
    reg_repaired, _, _ = repaired_word_break(reg_text, reg_dict)
    print(f"Faulty Result   : {reg_faulty}")
    print(f"Repaired Result : {reg_repaired} (Regression preserved!)")

    print("\n[SUCCESS] Task 4 Verification Complete.")
    return faulty_res, repaired_res

if __name__ == "__main__":
    run_task4_demo()
