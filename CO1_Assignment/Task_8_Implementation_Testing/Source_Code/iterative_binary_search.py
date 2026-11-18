"""
Iterative Binary Search Implementation
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018

Description:
Divide-and-conquer iterative binary search algorithm for locating a student
registration number in a sorted array of records.
"""

def iterative_binary_search(arr, key):
    """
    Performs iterative binary search for `key` in sorted `arr`.
    
    Parameters:
        arr (list): Sorted list of student registration numbers in ascending order.
        key (int/str): The target registration number to search for.
        
    Returns:
        tuple: (index, comparisons) where index is the 0-based position of
               the key if found, or -1 if not found; comparisons is the
               total number of basic comparison operations performed.
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons

if __name__ == "__main__":
    sample_records = [1005, 1012, 1023, 1045, 1089, 1102, 1150]
    target = 1045
    idx, comps = iterative_binary_search(sample_records, target)
    print(f"Iterative Binary Search: Key {target} found at index {idx} with {comps} comparisons.")
