############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_59_chatgpt import largest_prime_factor


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestLargestPrimeFactor(unittest.TestCase):

    def test_example_case_1(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_example_case_2(self):
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_small_composite(self):
        self.assertEqual(largest_prime_factor(10), 5)

    def test_large_power_of_two(self):
        self.assertEqual(largest_prime_factor(2**20), 2)

    def test_number_with_large_prime_factor(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)

    def test_square_of_prime(self):
        self.assertEqual(largest_prime_factor(13 * 13), 13)

    def test_product_of_primes(self):
        self.assertEqual(largest_prime_factor(17 * 19 * 23), 23)


if __name__ == '__main__':
    unittest.main()
