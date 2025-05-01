############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_150_deepseek import x_or_y


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestXOrY(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEqual(x_or_y(2, 10, 20), 10)
        self.assertEqual(x_or_y(3, 10, 20), 10)
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(13, 5, 8), 5)

    def test_non_prime_numbers(self):
        self.assertEqual(x_or_y(4, 10, 20), 20)
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(9, 3, 7), 7)
        self.assertEqual(x_or_y(25, 1, 2), 2)

    def test_edge_cases(self):
        self.assertEqual(x_or_y(0, 10, 20), 20)
        self.assertEqual(x_or_y(1, 10, 20), 20)
        self.assertEqual(x_or_y(-5, 10, 20), 20)

    def test_large_numbers(self):
        self.assertEqual(x_or_y(29, 100, 200), 100)  # 29 is prime
        self.assertEqual(x_or_y(100, 100, 200), 200)  # 100 is not prime


if __name__ == '__main__':
    unittest.main()
