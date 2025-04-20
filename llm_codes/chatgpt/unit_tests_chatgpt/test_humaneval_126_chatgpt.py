# used LLM model: 
#   GPT-4o
#
from humaneval_126_chatgpt import is_sorted

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestIsSorted(unittest.TestCase):
    def test_single_element(self):
        self.assertTrue(is_sorted([5]))
    
    def test_strictly_ascending(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
    
    def test_unsorted_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
    
    def test_allowed_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
    
    def test_excessive_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))
    
    def test_empty_list(self):
        self.assertTrue(is_sorted([]))
    
    def test_duplicates_unsorted(self):
        self.assertFalse(is_sorted([1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
