import unittest
from humaneval_22_deepseek import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
    
    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])
    
    def test_only_integers(self):
        self.assertEqual(filter_integers([1, 2, 3]), [1, 2, 3])
    
    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, {}]), [])
    
    def test_boolean_values(self):
        self.assertEqual(filter_integers([True, False, 1, 0]), [])  # Since type(True) is bool, not int
    
    def test_nested_lists(self):
        self.assertEqual(filter_integers([[1, 2], 3, '4']), [3])

if __name__ == '__main__':
    unittest.main()
