############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_155_chatgpt import even_odd_count


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestEvenOddCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(2468), (4, 0))
        self.assertEqual(even_odd_count(1357), (0, 4))

    def test_negative_numbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-13579), (0, 5))
        self.assertEqual(even_odd_count(-24680), (5, 0))

    def test_single_digit(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(7), (0, 1))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_large_number(self):
        self.assertEqual(even_odd_count(1234567890), (5, 5))


if __name__ == '__main__':
    unittest.main()
