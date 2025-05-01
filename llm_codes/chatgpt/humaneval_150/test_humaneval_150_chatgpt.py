############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_150_chatgpt import x_or_y


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestXOrYFunction(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(x_or_y(2, "yes", "no"), "yes")
        self.assertEqual(x_or_y(3, 10, 20), 10)
        self.assertEqual(x_or_y(13, "prime", "not prime"), "prime")
        self.assertEqual(x_or_y(97, 1, 0), 1)

    def test_non_prime_numbers(self):
        self.assertEqual(x_or_y(1, 100, 200), 200)
        self.assertEqual(x_or_y(4, "x", "y"), "y")
        self.assertEqual(x_or_y(0, "prime", "not prime"), "not prime")
        self.assertEqual(x_or_y(100, "yes", "no"), "no")

    def test_negative_numbers(self):
        self.assertEqual(x_or_y(-3, "yes", "no"), "no")
        self.assertEqual(x_or_y(-7, 1, 2), 2)


if __name__ == '__main__':
    unittest.main()
