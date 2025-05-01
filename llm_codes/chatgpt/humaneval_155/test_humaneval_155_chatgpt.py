############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
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
    
    def test_positive_number(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        
    def test_negative_number(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        
    def test_all_even_digits(self):
        self.assertEqual(even_odd_count(2468), (4, 0))
        
    def test_all_odd_digits(self):
        self.assertEqual(even_odd_count(13579), (0, 5))
        
    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        
    def test_large_number(self):
        self.assertEqual(even_odd_count(1234567890), (5, 5))
        
    def test_single_digit_even(self):
        self.assertEqual(even_odd_count(8), (1, 0))
        
    def test_single_digit_odd(self):
        self.assertEqual(even_odd_count(5), (0, 1))
        
if __name__ == '__main__':
    unittest.main()
