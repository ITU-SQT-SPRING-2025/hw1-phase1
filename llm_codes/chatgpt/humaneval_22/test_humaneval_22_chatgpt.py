############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_22_chatgpt import filter_integers

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestFilterIntegers(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_all_integers(self):
        self.assertEqual(filter_integers([10, -5, 0]), [10, -5, 0])

    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 2.71, None, [], {}]), [])

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_with_booleans(self):
        # Since bool is a subclass of int, True and False are technically ints
        self.assertEqual(filter_integers([True, False, 1, 0]), [True, False, 1, 0])

    def test_nested_structures(self):
        # Lists and dicts inside lists should not be filtered as ints
        self.assertEqual(filter_integers([[1, 2], {'a': 1}, 3]), [3])

if __name__ == "__main__":
    unittest.main()
