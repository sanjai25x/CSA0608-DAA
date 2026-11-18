# Task 4 – Pseudocode Forensics: Find, Explain and Repair an Algorithmic Defect
**Course Code & Name:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Assignment 4A – Part I (CO4)  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Given Faulty Pseudocode
```text
ALGORITHM WordBreak(Text, Dictionary)
INPUT:
Text – string of length n
Dictionary – collection of valid words
OUTPUT:
TRUE if Text can be completely segmented
FALSE otherwise
BEGIN
DP[0] ← TRUE
FOR i ← 1 TO n DO
    DP[i] ← FALSE
    FOR j ← 0 TO i - 1 DO
        IF substring(Text, j, i) is in Dictionary THEN
            DP[i] ← TRUE
            BREAK
        END IF
    END FOR
END FOR
RETURN DP[n]
END
```

---

## 2. Task 4.1 – Locate the Defect
### The Incomplete Decision
The decision condition:
$$\text{IF } \text{substring}(Text, j, i) \text{ is in Dictionary THEN}$$
is fatally incomplete because it evaluates **only the suffix slice** $\text{Text}[j \dots i-1]$ while completely ignoring whether the preceding prefix $\text{Text}[0 \dots j-1]$ was validly segmentable.

### Algorithmic Reason Why Substring Presence Alone Fails
Dynamic programming requires optimal substructure and state chaining. For a prefix of length $i$ to be segmentable, two conditions must hold simultaneously:
1. The prefix of length $j$ must already be completely segmentable ($\mathbf{DP[j] == TRUE}$).
2. The remaining substring from index $j$ to $i$ must be a recognized word in the dictionary ($\mathbf{\text{substring}(Text, j, i) \in \text{Dictionary}}$).

By checking only dictionary membership of $\text{substring}(Text, j, i)$, the algorithm accepts isolated words occurring anywhere in the text even if they are preceded by unsegmentable junk characters.

---

## 3. Task 4.2 – Construct a Failing Input (Adversarial Counterexample)

### Student-Designed Test Instance
- **Input Text:** `Text = "abcat"` (length $n = 5$)
- **Dictionary:** `Dictionary = {"cat"}`
- **Ground Truth:** **FALSE** (The prefix `"ab"` cannot be segmented into words from the dictionary, so `"abcat"` is unsegmentable).

### Step-by-Step State Execution Trace on Faulty Algorithm
- $DP[0] \leftarrow \text{TRUE}$.
- $i = 1$: Slices `"a"` not in Dictionary $\implies DP[1] = \text{FALSE}$.
- $i = 2$: Slices `"ab"`, `"b"` not in Dictionary $\implies DP[2] = \text{FALSE}$.
- $i = 3$: Slices `"abc"`, `"bc"`, `"c"` not in Dictionary $\implies DP[3] = \text{FALSE}$.
- $i = 4$: Slices `"abca"`, `"bca"`, `"ca"`, `"a"` not in Dictionary $\implies DP[4] = \text{FALSE}$.
- $i = 5$:
  - $j = 0$: $\text{substring}(0, 5) = \text{"abcat"} \notin \text{Dict}$.
  - $j = 1$: $\text{substring}(1, 5) = \text{"bcat"} \notin \text{Dict}$.
  - $j = 2$: $\text{substring}(2, 5) = \text{"cat"} \in \text{Dict}$!
    - **FATAL ERROR:** Faulty algorithm triggers `DP[5] <- TRUE` and `BREAK`!
    - Note that $DP[2] = \text{FALSE}$ (the prefix `"ab"` is invalid), yet $DP[5]$ is corrupted to $\text{TRUE}$.

**Outcome:** Faulty algorithm returns **TRUE** (False Positive).

---

## 4. Task 4.3 – Repair the Algorithm (Minimal Surgical Correction)

Only line 9 of the original pseudocode requires modification.

### Corrected Decision Logic
```text
ALGORITHM WordBreak(Text, Dictionary)
INPUT:
Text – string of length n
Dictionary – collection of valid words
OUTPUT:
TRUE if Text can be completely segmented
FALSE otherwise
BEGIN
DP[0] ← TRUE
FOR i ← 1 TO n DO
    DP[i] ← FALSE
    FOR j ← 0 TO i - 1 DO
        // REPAIRED LOGIC: Check DP[j] == TRUE to ensure valid prefix chaining
        IF (DP[j] == TRUE) AND (substring(Text, j, i) is in Dictionary) THEN
            DP[i] ← TRUE
            BREAK
        END IF
    END FOR
END FOR
RETURN DP[n]
END
```

---

## 5. Task 4.4 – Regression Check

### Regression Test Instance
- **Input Text:** `Text = "applepie"` (length $n = 8$)
- **Dictionary:** `Dictionary = {"apple", "pie"}`
- **Ground Truth:** **TRUE** (`"apple"` + `"pie"`)

### State Trace on Repaired Algorithm
- $i = 1 \dots 4$: At $i = 5$, $j = 0$: $DP[0] = \text{TRUE}$ and $\text{substring}(0, 5) = \text{"apple"} \in \text{Dict} \implies DP[5] \leftarrow \text{TRUE}$.
- $i = 6 \dots 7$: No valid chaining.
- $i = 8$: At $j = 5$: $DP[5] = \text{TRUE}$ and $\text{substring}(5, 8) = \text{"pie"} \in \text{Dict} \implies DP[8] \leftarrow \text{TRUE}$.
- **Result:** Repaired algorithm returns **TRUE**, preserving expected valid behavior while eliminating false positives.
