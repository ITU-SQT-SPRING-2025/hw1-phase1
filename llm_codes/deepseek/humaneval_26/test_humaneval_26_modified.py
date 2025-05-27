############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_26_deepseek import remove_duplicates

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])
    
    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])
    
    def test_some_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
    
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])
    
    def test_single_element(self):
        self.assertEqual(remove_duplicates([5]), [5])
    
    def test_multiple_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4]), [4])

    # The tests below are added by the author
    def test_negative_numbers(self):
        self.assertEqual(remove_duplicates([-2, -2, -1]), [-1])
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveDuplicates)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
