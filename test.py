"""This file contains the tests for the continuous delivery pipeline"""

import unittest
import bubble_sort as bs
import quick_sort as qs

class TestBubbleSort(unittest.TestCase):
    """class for the tests concerning the bubble sort algorithm"""
    def test_empty_list_bs(self):
        test_list = []
        self.assertEqual(bs.bubblesort(test_list), [])

class TestQuickSort(unittest.TestCase):
    """class for the tests concerning the quick sort algorithm"""
    def test_empty_list_qs(self):
        test_list = []
        self.assertEqual(qs.quicksort(test_list), [])

if __name__ == '__main__':
    unittest.main()
