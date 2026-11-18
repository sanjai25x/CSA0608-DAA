"""
Comprehensive Unit Test Suite for Search Algorithms
Course: CSA0608 - Design and Analysis of Algorithms
Student Name: Sanjai S
Register Number: 192511018
"""

import unittest
from linear_search import linear_search
from iterative_binary_search import iterative_binary_search
from recursive_binary_search import recursive_binary_search
from hash_search import StudentHashTable

class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        self.sorted_data = [1001, 1005, 1012, 1025, 1033, 1045, 1058, 1070, 1099]
        self.ht = StudentHashTable(initial_capacity=32)
        for val in self.sorted_data:
            self.ht.insert(val, f"Student_{val}")

    def test_key_at_first_position_best_case_linear(self):
        key = self.sorted_data[0]
        idx, comps = linear_search(self.sorted_data, key)
        self.assertEqual(idx, 0)
        self.assertEqual(comps, 1)

    def test_key_at_last_position_worst_case_linear(self):
        key = self.sorted_data[-1]
        idx, comps = linear_search(self.sorted_data, key)
        self.assertEqual(idx, len(self.sorted_data) - 1)
        self.assertEqual(comps, len(self.sorted_data))

    def test_key_in_middle_best_case_binary(self):
        mid_idx = (0 + len(self.sorted_data) - 1) // 2
        key = self.sorted_data[mid_idx]
        idx_it, comps_it = iterative_binary_search(self.sorted_data, key)
        idx_rec, comps_rec = recursive_binary_search(self.sorted_data, key)
        self.assertEqual(idx_it, mid_idx)
        self.assertEqual(idx_rec, mid_idx)
        self.assertEqual(comps_it, 1)
        self.assertEqual(comps_rec, 1)

    def test_key_absent_all_algorithms(self):
        absent_key = 9999
        idx_lin, comps_lin = linear_search(self.sorted_data, absent_key)
        idx_it, comps_it = iterative_binary_search(self.sorted_data, absent_key)
        idx_rec, comps_rec = recursive_binary_search(self.sorted_data, absent_key)
        rec_ht, comps_ht = self.ht.search(absent_key)
        
        self.assertEqual(idx_lin, -1)
        self.assertEqual(comps_lin, len(self.sorted_data))
        self.assertEqual(idx_it, -1)
        self.assertEqual(idx_rec, -1)
        self.assertIsNone(rec_ht)

    def test_hash_table_lookup(self):
        key = 1045
        rec, comps = self.ht.search(key)
        self.assertEqual(rec, f"Student_{key}")
        self.assertGreaterEqual(comps, 1)

    def test_single_element_array(self):
        single = [5001]
        self.assertEqual(linear_search(single, 5001)[0], 0)
        self.assertEqual(iterative_binary_search(single, 5001)[0], 0)
        self.assertEqual(recursive_binary_search(single, 5001)[0], 0)
        self.assertEqual(linear_search(single, 9999)[0], -1)
        self.assertEqual(iterative_binary_search(single, 9999)[0], -1)
        self.assertEqual(recursive_binary_search(single, 9999)[0], -1)

    def test_empty_array(self):
        empty = []
        self.assertEqual(linear_search(empty, 5001)[0], -1)
        self.assertEqual(iterative_binary_search(empty, 5001)[0], -1)
        self.assertEqual(recursive_binary_search(empty, 5001)[0], -1)

if __name__ == "__main__":
    unittest.main()
