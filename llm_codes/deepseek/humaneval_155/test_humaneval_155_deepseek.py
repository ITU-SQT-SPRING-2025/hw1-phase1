############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_155_deepseek import even_odd_count

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
    
    def test_negative_numbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-2468), (4, 0))
        self.assertEqual(even_odd_count(-13579), (0, 5))
    
    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))
    
    def test_single_digit_numbers(self):
        self.assertEqual(even_odd_count(2), (1, 0))
        self.assertEqual(even_odd_count(3), (0, 1))
    
    def test_large_numbers(self):
        self.assertEqual(even_odd_count(1234567890), (5, 5))
        self.assertEqual(even_odd_count(987654321), (4, 5))
    
    def test_mixed_digits(self):
        self.assertEqual(even_odd_count(1029384756), (5, 5))
        self.assertEqual(even_odd_count(1122334455), (4, 6))

if __name__ == '__main__':
    unittest.main()
