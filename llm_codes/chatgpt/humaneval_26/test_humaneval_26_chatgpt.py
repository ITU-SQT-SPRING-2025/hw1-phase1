# used LLM model: 
#   GPT-4o
#
from humaneval_26_chatgpt import remove_duplicates

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_all_unique(self):
        self.assertEqual(remove_duplicates([5, 6, 7]), [5, 6, 7])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([42]), [42])

    def test_multiple_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5]), [2, 4])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -2, -3, -1]), [-3])

    def test_mixed_order(self):
        self.assertEqual(remove_duplicates([10, 20, 10, 30, 20, 40, 50]), [30, 40, 50])

if __name__ == '__main__':
    unittest.main()
