############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_156_deepseek import even_odd_count


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestEvenOddCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(2468), (4, 0))
        self.assertEqual(even_odd_count(13579), (0, 5))
        self.assertEqual(even_odd_count(123456), (3, 3))

    def test_negative_numbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-2468), (4, 0))
        self.assertEqual(even_odd_count(-13579), (0, 5))
        self.assertEqual(even_odd_count(-123456), (3, 3))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_single_digit(self):
        self.assertEqual(even_odd_count(2), (1, 0))
        self.assertEqual(even_odd_count(3), (0, 1))


if __name__ == '__main__':
    unittest.main()
