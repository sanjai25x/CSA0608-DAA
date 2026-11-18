"""
Recursive Binary Search Implementation
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018

Description:
Divide-and-conquer recursive binary search algorithm for locating a student
registration number in a sorted array of records.
"""

def recursive_binary_search_helper(arr, low, high, key, cmp_container):
    """
    Helper function executing recursive divide-and-conquer steps.
    """
    if low > high:
        return -1
    
    mid = (low + high) // 2
    cmp_container[0] += 1
    
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return recursive_binary_search_helper(arr, mid + 1, high, key, cmp_container)
    else:
        return recursive_binary_search_helper(arr, low, mid - 1, key, cmp_container)

def recursive_binary_search(arr, key):
    """
    Performs recursive binary search for `key` in sorted `arr`.
    
    Parameters:
        arr (list): Sorted list of student registration numbers.
        key (int/str): The target registration number to search for.
        
    Returns:
        tuple: (index, comparisons) where index is the 0-based position of
               the key if found, or -1 if not found; comparisons is the
               total number of basic comparison operations performed.
    """
    cmp_container = [0]
    idx = recursive_binary_search_helper(arr, 0, len(arr) - 1, key, cmp_container)
    return idx, cmp_container[0]

if __name__ == "__main__":
    sample_records = [1005, 1012, 1023, 1045, 1089, 1102, 1150]
    target = 1045
    idx, comps = recursive_binary_search(sample_records, target)
    print(f"Recursive Binary Search: Key {target} found at index {idx} with {comps} comparisons.")
