# Q2 – Pseudocode and Algorithmic Logic

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Student Name:** Sanjai S (192511018)  
**Department:** Computer Science and Engineering, SIMATS Engineering  

---

## 1. Sequential Search for Tool Tracking

### Algorithmic Logic:
Linearly iterates through the dynamic array of issued tool records. For each record $i \in [0 \dots n-1]$, it compares the record's `tool_id` with the query `target_id`. If a match is found, the technician assignment record is returned immediately. If the entire collection is traversed without finding a match, a sentinel value `NOT_FOUND` is returned.

```text
ALGORITHM SequentialToolSearch(ToolList, n, target_id):
    Input: Array ToolList of n tool assignment records, string target_id
    Output: Tool record if currently issued, otherwise NOT_FOUND

    for i ← 0 to n - 1 do
        if ToolList[i].tool_id == target_id then
            return ToolList[i]   // Match found; exit immediately
        end if
    end for
    return NOT_FOUND             // Exhausted list without match
```

---

## 2. Redesigned Hash Table Lookup (Changed Condition Architecture)

### Algorithmic Logic:
Direct addressing via an in-memory hash table (dictionary) maps each unique `tool_id` to its active assignment record. Computes the hash value $h(\text{tool\_id})$ and inspects the corresponding bucket in expected $\Theta(1)$ time, eliminating the $O(n)$ sequential scan and supporting instant $O(1)$ checkout/check-in updates.

```text
ALGORITHM HashToolLookup(ToolIndex, target_id):
    Input: Hash table ToolIndex, string target_id
    Output: Tool record if present, otherwise NOT_FOUND

    bucket ← ToolIndex.getBucket(hash(target_id))
    for entry in bucket do
        if entry.tool_id == target_id then
            return entry.record
        end if
    end for
    return NOT_FOUND
```
