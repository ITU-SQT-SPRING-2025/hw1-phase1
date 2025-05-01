############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_163_deepseek import generate_integers

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestGenerateIntegers(unittest.TestCase):
    def test_normal_range(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
    
    def test_reverse_range(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
    
    def test_no_even_digit_numbers(self):
        self.assertEqual(generate_integers(10, 14), [])
    
    def test_single_number_with_even_digits(self):
        self.assertEqual(generate_integers(2, 2), [2])
    
    def test_single_number_without_even_digits(self):
        self.assertEqual(generate_integers(1, 1), [])
    
    def test_large_range(self):
        self.assertEqual(generate_integers(200, 220), [200, 202, 204, 206, 208, 220])
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            generate_integers(-2, 2)
    
    def test_zero_in_range(self):
        self.assertEqual(generate_integers(0, 2), [0, 2])

if __name__ == '__main__':
    unittest.main()
