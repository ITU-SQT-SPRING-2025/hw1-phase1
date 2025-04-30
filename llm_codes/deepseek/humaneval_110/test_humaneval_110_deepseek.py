############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_110_deepseek import exchange


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestExchangeFunction(unittest.TestCase):

    def test_all_even_in_lst1(self):
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_possible_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_impossible_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_single_element_possible(self):
        self.assertEqual(exchange([1], [2]), "YES")

    def test_single_element_impossible(self):
        self.assertEqual(exchange([1], [3]), "NO")

    def test_all_odd_in_lst1_possible(self):
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6]), "YES")

    def test_all_odd_in_lst1_impossible(self):
        self.assertEqual(exchange([1, 3, 5], [1, 3, 5]), "NO")

    def test_empty_lists(self):
        with self.assertRaises(AssertionError):
            exchange([], [])  # Assuming the function checks for non-empty lists


if __name__ == '__main__':
    unittest.main()
