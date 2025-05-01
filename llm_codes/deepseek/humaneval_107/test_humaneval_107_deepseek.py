import unittest
from humaneval_107_deepseek import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))
        self.assertEqual(even_odd_palindrome(2), (1, 1))
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_medium_numbers(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))
        self.assertEqual(even_odd_palindrome(20), (6, 10))

    def test_large_numbers(self):
        self.assertEqual(even_odd_palindrome(100), (9, 19))
        self.assertEqual(even_odd_palindrome(1000), (54, 246))

    def test_edge_cases(self):
        self.assertEqual(even_odd_palindrome(9), (4, 5))
        self.assertEqual(even_odd_palindrome(11), (4, 7))

if __name__ == '__main__':
    unittest.main()
