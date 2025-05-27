############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_116_deepseek import sort_array

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestSortArray(unittest.TestCase):
    def test_sort_by_binary_ones(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])
        self.assertEqual(sort_array([0, 1, 2, 3, 4]), [0, 1, 2, 4, 3])
    
    def test_tie_breaking_by_decimal(self):
        self.assertEqual(sort_array([2, 3, 4, 5]), [2, 4, 3, 5])
        self.assertEqual(sort_array([1, 2, 4, 8]), [1, 2, 4, 8])
    
    def test_edge_cases(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([7]), [7])
        self.assertEqual(sort_array([3, 3, 3]), [3, 3, 3])

    # Removed as the expected input is nonnegative.    
    # def test_negative_numbers(self):
    #     self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-4, -2, -6, -5, -3])
    #     self.assertEqual(sort_array([-1, 0, 1]), [0, -1, 1])
    
    # The tests below are added by the author to increase the coverage of the test
    def test_same_number_of_ones(self):
        self.assertEqual(sort_array([6, 3, 5]), [3, 5, 6])
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortArray)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
