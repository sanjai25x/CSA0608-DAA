# Q3 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Brute-Force String Matching

### Algorithmic Logic:
Slides a search pattern window of length $m$ over a host text string of length $n$ across all possible alignment offsets $i \in [0 \dots n - m]$. For each shift $i$, it tests pattern characters $P[0 \dots m-1]$ sequentially against text characters $T[i \dots i+m-1]$. If any character mismatches, it immediately aborts the current alignment and shifts the window forward by 1 position ($i \leftarrow i + 1$), discarding all previously matched character information.

```text
ALGORITHM BruteForceStringMatch(T, n, P, m):
    Input: Text string T of length n, pattern string P of length m
    Output: List of starting indices where pattern P occurs in text T

    matches ← empty list
    for i ← 0 to n - m do
        j ← 0
        while j < m and T[i + j] == P[j] do
            j ← j + 1
        end while
        if j == m then
            Append i to matches  // Complete match found at alignment i
        end if
    end for
    return matches
```

---

## 2. Structural Characteristics Leading to Repeated Comparisons

1. **Low Effective Alphabet Cardinality:** Texts composed of highly repetitive tokens (e.g. unary streams or identical log headers) force repeated inner loop advancements.
2. **High Prefix Self-Similarity:** When substrings in $T$ match the prefix $P[0 \dots k]$ for large $k < m$, the algorithm incurs $k$ comparisons per shift before failing.
3. **Late Mismatch Position:** Mismatches occurring near the pattern tail (index $m-1$) maximize wasted work because the window is shifted by only 1 index without reusing verified character data.
