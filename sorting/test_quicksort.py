import unittest
import quicksort
from random import randint

class testEx2(unittest.TestCase):

    def test_QuickSort(self):
        lst = [11,23,58,31, 58]
        result = quicksort.QuickSort(lst, 1, len(lst)-1, 0)
        expected = [11,23,31,58, 58]
        self.assertEqual(expected, result)

    def test_QuickSort_single(self):
        lst = [11]
        result = quicksort.QuickSort(lst, 1, len(lst)-1, 0)
        expected = lst
        self.assertEqual(expected, result)

    def test_QuickSort_empty(self):
        lst = []
        result = quicksort.QuickSort(lst,1, len(lst)-1, 0)
        expected = []
        self.assertEqual(expected, result)

    def test_QuickSort_random_size(self):
        lst = []
        for i in range(8):
                lst.append(randint(0,100000))
        result = quicksort.QuickSort(lst, 1, len(lst)-1, 0)
        expected = sorted(lst)
        self.assertEqual(expected, result)
        
if __name__ == '__main__':
    unittest.main()
