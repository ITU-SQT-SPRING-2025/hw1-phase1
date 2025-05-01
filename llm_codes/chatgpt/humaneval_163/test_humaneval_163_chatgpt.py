############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_163_chatgpt import generate_integers

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestGenerateIntegers(unittest.TestCase):

    def test_normal_order(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_reverse_order(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_even_digits(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_single_value_even(self):
        self.assertEqual(generate_integers(4, 4), [4])

    def test_single_value_odd(self):
        self.assertEqual(generate_integers(5, 5), [])

    def test_includes_zero(self):
        self.assertEqual(generate_integers(0, 2), [0, 2])

    def test_range_full(self):
        self.assertEqual(generate_integers(0, 9), [0, 2, 4, 6, 8])

    def test_below_zero(self):
        self.assertEqual(generate_integers(-5, 3), [0, 2])

    def test_large_numbers(self):
        self.assertEqual(generate_integers(100, 200), [])

if __name__ == '__main__':
    unittest.main()
