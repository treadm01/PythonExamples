import unittest
import sequential_search

class testEx1(unittest.TestCase):
    def test_Sequential_Search(self):
        result = sequential_search.Sequential_Search([11,23,58,31,56,77,43,12,65,19],31)
        expected = (True, 3)
        self.assertEqual(expected, result)

    def test_Sequential_Search(self):
        result = sequential_search.Sequential_Search([11,23,58,31,56,77,43,12,65,19],30)
        expected = (False, -1)
        self.assertEqual(expected, result)
        
    def test_Sequential_Search(self):
        result = sequential_search.Sequential_Search([1,-4],-5)
        expected = (False, -1)
        self.assertEqual(expected, result)
        
    def test_Sequential_Search(self):
        result = sequential_search.Sequential_Search([0.05,0],0.003)
        expected = (False, -1)
        self.assertEqual(expected, result)

    def test_Sequential_Search(self):
        result = sequential_search.Sequential_Search([0.05,0],0)
        expected = (True, 1)
        self.assertEqual(expected, result)
        

if __name__ == '__main__':
    unittest.main()
