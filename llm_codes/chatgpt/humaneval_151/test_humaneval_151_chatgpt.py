############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_151_chatgpt import double_the_difference


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestDoubleTheDifference(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)

    def test_mixed_types(self):
        self.assertEqual(double_the_difference([1.5, 3, '5', 7]), 49)  # only 3 and 7 are valid

    def test_all_even(self):
        self.assertEqual(double_the_difference([2, 4, 6]), 0)

    def test_negative_odds(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_non_integers(self):
        self.assertEqual(double_the_difference([1.1, 3.3, 5.5]), 0)

    def test_large_input(self):
        self.assertEqual(double_the_difference(list(range(1, 1000))), sum(x**2 for x in range(1, 1000) if x % 2 == 1))


if __name__ == '__main__':
    unittest.main()
