# used LLM model: 
#   GPT-4o
#
from humaneval_57_chatgpt import monotonic

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestMonotonicFunction(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(monotonic([1, 2, 3, 4]))

    def test_decreasing(self):
        self.assertTrue(monotonic([10, 5, 2, 1]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 3, 2, 4]))

    def test_single_element(self):
        self.assertTrue(monotonic([42]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_equal_elements(self):
        self.assertTrue(monotonic([5, 5, 5, 5]))

    def test_increasing_with_duplicates(self):
        self.assertTrue(monotonic([1, 2, 2, 3]))

    def test_decreasing_with_duplicates(self):
        self.assertTrue(monotonic([3, 3, 2, 1]))

    def test_fluctuating_values(self):
        self.assertFalse(monotonic([1, 3, 2, 4, 0]))

if __name__ == "__main__":
    unittest.main()
