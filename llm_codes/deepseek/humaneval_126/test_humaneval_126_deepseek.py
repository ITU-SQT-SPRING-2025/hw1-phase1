# used LLM model: 
#   DeepSeek-V3
#
from humaneval_126_deepseek import is_sorted

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestIsSorted(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(is_sorted([]))
    
    def test_single_element(self):
        self.assertTrue(is_sorted([5]))
    
    def test_sorted_no_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
    
    def test_sorted_with_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
    
    def test_unsorted_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
    
    def test_multiple_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))
    
    def test_negative_numbers(self):
        # Even though the problem says no negative numbers, testing robustness
        self.assertTrue(is_sorted([-3, -2, -1, 0, 1]))
        self.assertFalse(is_sorted([-1, -2, -3]))
        self.assertFalse(is_sorted([-1, -1, -1, 0]))

if __name__ == '__main__':
    unittest.main()
