"""
Linear Search Implementation
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018

Description:
Sequential search algorithm for locating a student registration number
in an unsorted or sorted array of records.
"""

def linear_search(arr, key):
    """
    Performs sequential linear search for `key` in `arr`.
    
    Parameters:
        arr (list): List of student registration numbers.
        key (int/str): The target registration number to search for.
        
    Returns:
        tuple: (index, comparisons) where index is the 0-based position of
               the key if found, or -1 if not found; comparisons is the
               total number of basic comparison operations performed.
    """
    comparisons = 0
    n = len(arr)
    for i in range(n):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons

if __name__ == "__main__":
    sample_records = [1005, 1012, 1023, 1045, 1089, 1102, 1150]
    target = 1045
    idx, comps = linear_search(sample_records, target)
    print(f"Linear Search: Key {target} found at index {idx} with {comps} comparisons.")
