"""This file contains the tests for the continuous delivery pipeline"""

import unittest
import bubble_sort as bs
import quick_sort as qs

class testBubbleSort(unittest.TestCase):
    def testEmptyListBS(self):
        test_list = []
        self.assertEqual(bs.bubblesort(test_list), 0)

class testQuickSort(unittest.TestCase):
    def testEmptyListQS(self):
        test_list = []
        self.assertEqual(qs.bubblesort(test_list), 0)

if __name__ == '__main__':
    unittest.main()
