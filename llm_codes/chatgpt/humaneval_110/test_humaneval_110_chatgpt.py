############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_110_chatgpt import exchange


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestExchangeFunction(unittest.TestCase):

    def test_example_yes(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_example_no(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_all_even_in_lst1(self):
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_no_even_in_lst2(self):
        self.assertEqual(exchange([1, 3], [1, 3, 5]), "NO")

    def test_enough_evens_in_lst2(self):
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    def test_not_enough_evens_in_lst2(self):
        self.assertEqual(exchange([1, 3, 5], [2]), "NO")

    def test_exact_even_replacement(self):
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    def test_more_even_than_needed(self):
        self.assertEqual(exchange([1], [2, 4, 6]), "YES")


if __name__ == "__main__":
    unittest.main()
