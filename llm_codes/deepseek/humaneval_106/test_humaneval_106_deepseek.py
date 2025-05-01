############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_106_deepseek import f


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestFactorialSumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_single_element(self):
        self.assertEqual(f(1), [1])

    def test_empty_list(self):
        self.assertEqual(f(0), [])

    def test_larger_input(self):
        self.assertEqual(f(6), [1, 2, 6, 24, 15, 720])

    def test_even_index_factorial(self):
        result = f(4)
        self.assertEqual(result[1], 2)   # i=2 (even), 2! = 2
        self.assertEqual(result[3], 24)  # i=4 (even), 4! = 24

    def test_odd_index_sum(self):
        result = f(5)
        self.assertEqual(result[0], 1)   # i=1 (odd), sum=1
        self.assertEqual(result[2], 6)    # i=3 (odd), sum=1+2+3=6
        self.assertEqual(result[4], 15)  # i=5 (odd), sum=1+2+3+4+5=15


if __name__ == '__main__':
    unittest.main()
