############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_116_chatgpt import sort_array

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestSortArray(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 4, 3])

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(sort_array([7]), [7])

    def test_all_same_number(self):
        self.assertEqual(sort_array([3, 3, 3]), [3, 3, 3])

    def test_with_duplicates(self):
        self.assertEqual(sort_array([2, 3, 2, 1, 3]), [1, 2, 2, 3, 3])

    def test_large_values(self):
        self.assertEqual(sort_array([1023, 512, 3, 7]), [512, 3, 7, 1023])
        # binary: 512 (1), 3 (2), 7 (3), 1023 (10)

    # The tests below are added by the author to increase the coverage of the test
    def test_same_number_of_ones(self):
        self.assertEqual(sort_array([6, 3, 5]), [3, 5, 6])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortArray)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
