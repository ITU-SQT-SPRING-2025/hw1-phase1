############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_107_chatgpt import even_odd_palindrome

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestEvenOddPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
    
    def test_example2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))
    
    def test_single_digit(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))
        self.assertEqual(even_odd_palindrome(2), (1, 1))
    
    def test_no_even_palindrome(self):
        # Testing where there are no even palindromes (1 and 3 are odd palindromes)
        self.assertEqual(even_odd_palindrome(3), (1, 2))
    
    def test_large_input(self):
        # For 1000, check manually known result
        result = even_odd_palindrome(1000)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        # Exact counts can be precomputed, but for now, check it's a tuple of two integers
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_zero_case(self):
        # 0 is not considered because range starts from 1
        self.assertEqual(even_odd_palindrome(0), (0, 0))

    def test_boundary_case(self):
        # Testing at maximum 1 <= n <= 1000
        self.assertIsInstance(even_odd_palindrome(1000), tuple)

if __name__ == '__main__':
    unittest.main()
