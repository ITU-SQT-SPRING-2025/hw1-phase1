############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_72_chatgpt import will_it_fly

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestWillItFly(unittest.TestCase):
    def test_balanced_and_within_weight(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([3], 5))
        self.assertTrue(will_it_fly([], 0))  # Empty list is palindromic and sum is 0

    def test_unbalanced(self):
        self.assertFalse(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([3, 2, 1], 6))

    def test_too_heavy(self):
        self.assertFalse(will_it_fly([3, 2, 3], 7))
        self.assertFalse(will_it_fly([3], 2))

    def test_balanced_but_too_heavy(self):
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_zero_weight_limit(self):
        self.assertTrue(will_it_fly([], 0))
        self.assertFalse(will_it_fly([0], 0))
        self.assertFalse(will_it_fly([1], 0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWillItFly)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
