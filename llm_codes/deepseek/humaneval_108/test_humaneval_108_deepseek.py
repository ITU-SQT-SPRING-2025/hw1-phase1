############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_108_deepseek import count_nums

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestCountNums(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_all_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_all_negative_numbers(self):
        self.assertEqual(count_nums([-123, -456, -789]), 3)  # Sums: 4, 5, 6
        self.assertEqual(count_nums([-1, -2, -3]), 0)        # Sums: -1, -2, -3

    def test_zero_sum_digits(self):
        self.assertEqual(count_nums([0, -11, 22, -22]), 0)   # Sums: 0, 0, 4, 0

if __name__ == '__main__':
    unittest.main()
