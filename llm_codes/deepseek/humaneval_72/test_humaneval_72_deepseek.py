############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_72_deepseek import will_it_fly

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestWillItFly(unittest.TestCase):
    def test_palindrome_and_sum_less_than_w(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([1, 2, 3, 2, 1], 10))
        self.assertTrue(will_it_fly([5], 5))

    def test_palindrome_but_sum_greater_than_w(self):
        self.assertFalse(will_it_fly([3, 2, 3], 1))
        self.assertFalse(will_it_fly([1, 2, 3, 2, 1], 5))
        self.assertFalse(will_it_fly([10], 9))

    def test_non_palindrome(self):
        self.assertFalse(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([1, 2, 3, 4], 100))
        self.assertFalse(will_it_fly([1, 3, 2], 6))

    def test_empty_list(self):
        self.assertTrue(will_it_fly([], 0))
        self.assertTrue(will_it_fly([], 10))
        self.assertFalse(will_it_fly([], -1))

    def test_single_element_list(self):
        self.assertTrue(will_it_fly([3], 5))
        self.assertTrue(will_it_fly([0], 0))
        self.assertFalse(will_it_fly([7], 6))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWillItFly)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
