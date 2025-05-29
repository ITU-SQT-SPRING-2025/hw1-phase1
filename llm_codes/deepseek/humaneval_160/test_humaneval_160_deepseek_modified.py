############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_160_deepseek_modified import do_algebra


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestDoAlgebra(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(do_algebra(['+', '+'], [1, 2, 3]), 6)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '-'], [10, 2, 3]), 5)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '*'], [2, 3, 4]), 24)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//', '//'], [10, 2, 3]), 1)

    def test_exponentiation(self):
        # Fix, operator precedece, it should be 64 since 2 ** 3 ** 2 = 8 ** 2 = 64
        self.assertEqual(do_algebra(['**', '**'], [2, 3, 2]), 64)

    def test_mixed_operations(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

    def test_single_operation(self):
        self.assertEqual(do_algebra(['+'], [1, 1]), 2)

    def test_large_numbers(self):
        self.assertEqual(do_algebra(['*', '+'], [1000, 50, 2]), 50002)

    def test_division_by_zero(self):
        with self.assertRaises(Exception):
            do_algebra(['//'], [1, 0])

    def test_empty_operand(self):
        with self.assertRaises(Exception):
            do_algebra([], [])

    def invalid_input_length(self):
        with self.assertRaises(Exception):
            do_algebra(['+'], [1, 2, 3])

    def test_invalid_operator(self):
        with self.assertRaises(Exception):
            do_algebra(['+', '$'], [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
