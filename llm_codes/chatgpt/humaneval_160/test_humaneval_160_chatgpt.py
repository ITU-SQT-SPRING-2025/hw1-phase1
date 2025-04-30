############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_160_chatgpt import do_algebra


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestDoAlgebra(unittest.TestCase):

    def test_addition_and_multiplication(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

    def test_all_operators(self):
        self.assertEqual(do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]), 1)

    def test_only_addition(self):
        self.assertEqual(do_algebra(['+', '+', '+'], [1, 2, 3, 4]), 10)

    def test_only_subtraction(self):
        self.assertEqual(do_algebra(['-', '-', '-'], [10, 2, 3, 1]), 4)

    def test_only_multiplication(self):
        self.assertEqual(do_algebra(['*', '*'], [2, 3, 4]), 24)

    def test_only_floor_division(self):
        self.assertEqual(do_algebra(['//', '//'], [100, 5, 2]), 10)

    def test_only_exponentiation(self):
        self.assertEqual(do_algebra(['**', '**'], [2, 3, 1]), 8)  # 2 ** 3 = 8, then 8 ** 1 = 8

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '$'], [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
