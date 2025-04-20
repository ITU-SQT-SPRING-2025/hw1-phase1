# used LLM model: 
#   DeepSeek-V3
#
from humaneval_57_deepseek import monotonic

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(monotonic([1, 2, 3, 4]))
        self.assertTrue(monotonic([-10, -5, 0, 5]))
        self.assertTrue(monotonic([0, 0, 1, 1]))  # Non-strictly increasing

    def test_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([5, 0, -5, -10]))
        self.assertTrue(monotonic([1, 1, 0, 0]))  # Non-strictly decreasing

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 3, 2, 4]))
        self.assertFalse(monotonic([5, -10, 0, -5]))
        self.assertFalse(monotonic([1, 2, 1, 2]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_single_element(self):
        self.assertTrue(monotonic([42]))
        self.assertTrue(monotonic([-1]))

    def test_constant_list(self):
        self.assertTrue(monotonic([0, 0, 0]))
        self.assertTrue(monotonic([1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
