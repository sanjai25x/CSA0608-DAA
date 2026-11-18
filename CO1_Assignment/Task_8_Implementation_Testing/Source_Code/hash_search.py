"""
Hash Table Search Implementation
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018

Description:
Direct indexing / Hash Map implementation for large-scale student record retrieval.
Addresses the Day-4 Design Challenge (50,000 queries/hour on 1,000,000 records).
"""

class StudentHashTable:
    """
    Hash Table with separate chaining and dynamic resizing to maintain
    load factor alpha < 0.75 for guaranteed expected O(1) retrieval time.
    """
    def __init__(self, initial_capacity=1024):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        
    def _hash(self, key):
        # Uses built-in hash modulated by capacity
        return hash(key) % self.capacity

    def insert(self, key, record):
        """
        Inserts (key, record) into the hash table.
        Replaces value if key already exists.
        """
        if self.size / self.capacity >= 0.75:
            self._resize(self.capacity * 2)
            
        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, record)
                return
        bucket.append((key, record))
        self.size += 1

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for k, rec in bucket:
                self.insert(k, rec)

    def search(self, key):
        """
        Searches for key in the hash table.
        
        Returns:
            tuple: (record, comparisons) where record is the retrieved object
                   or None if not found, and comparisons is the count of key
                   equality comparisons executed within the bucket chain.
        """
        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]
        comparisons = 0
        for k, rec in bucket:
            comparisons += 1
            if k == key:
                return rec, comparisons
        return None, comparisons

if __name__ == "__main__":
    ht = StudentHashTable()
    sample_records = [
        (1005, {"name": "Alice", "dept": "CSE"}),
        (1012, {"name": "Bob", "dept": "ECE"}),
        (1045, {"name": "Charlie", "dept": "IT"}),
    ]
    for k, rec in sample_records:
        ht.insert(k, rec)
        
    res, comps = ht.search(1045)
    print(f"Hash Table Search: Found {res} with {comps} comparisons.")
