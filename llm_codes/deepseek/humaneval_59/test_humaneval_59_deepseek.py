############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_59_deepseek import largest_prime_factor


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestLargestPrimeFactor(unittest.TestCase):
    def test_small_composite(self):
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(15), 5)
        self.assertEqual(largest_prime_factor(25), 5)

    def test_even_numbers(self):
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(16), 2)
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_large_composite(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(600851475143), 6857)

    def test_square_of_prime(self):
        self.assertEqual(largest_prime_factor(49), 7)
        self.assertEqual(largest_prime_factor(121), 11)

    def test_cube_of_prime(self):
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(27), 3)

    def test_product_of_primes(self):
        self.assertEqual(largest_prime_factor(2*3*5*7), 7)
        self.assertEqual(largest_prime_factor(11*13*17), 17)


if __name__ == '__main__':
    unittest.main()
