############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_151_deepseek_modified import double_the_difference


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestDoubleTheDifference(unittest.TestCase):
    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 5]), 35)  # 1 + 9 + 25
        self.assertEqual(double_the_difference([7]), 49)
        self.assertEqual(double_the_difference([1, 2, 3, 4, 5]), 35)  # 1 + 9 + 25

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)
        self.assertEqual(double_the_difference([-2, 3, -4]), 9)  # only 3 counts

    def test_zero_and_even_numbers(self):
        self.assertEqual(double_the_difference([0, 2, 4, 6]), 0)
        self.assertEqual(double_the_difference([0]), 0)

    def test_non_integer_numbers(self):
        self.assertEqual(double_the_difference([1.5, 2.0, 3.3]), 0)
        self.assertEqual(double_the_difference([2.0, 3.0, 5]), 25)  # only 5 counts (3.0 is float)

    def test_mixed_values(self):
        self.assertEqual(double_the_difference([1, -2, 3.0, 4, 5.5, 7]), 50)  # 1 + 49
        self.assertEqual(double_the_difference([-1, 0, 1, 2, 3]), 10)  # 1 + 9

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_large_numbers(self):
        self.assertEqual(double_the_difference([9999]), 9999**2)

    # Instead of assertion, value must be zero
    # def test_string_input(self):
    #     with self.assertRaises(TypeError):
    #         double_the_difference(["1", "2"])  # should raise TypeError

    def test_string_array(self):
        self.assertEqual(double_the_difference(["0", "1"]), 0)

    def test_string_number_mixed(self):
        self.assertEqual(double_the_difference([1, "1", 2, "2", 3]), 10)
        self.assertEqual(double_the_difference(["1", 2, "3"]), 0)

    def test_boolean_input(self):
        self.assertEqual(double_the_difference([True, False]), 0)  # Fix: Bools are not numbers


if __name__ == '__main__':
    unittest.main()
