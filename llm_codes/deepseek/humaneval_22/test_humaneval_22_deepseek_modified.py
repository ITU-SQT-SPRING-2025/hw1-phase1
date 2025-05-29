############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_22_deepseek_modified import filter_integers

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#

import unittest
from typing import List, Any

class TestFilterIntegers(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_boolean_handling(self):
        self.assertEqual(filter_integers([True, False, 1, 0]), [True, False, 1, 0])

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, {}]), [])
        self.assertEqual(filter_integers([[], 'abc']), [])

    def test_mixed_types(self):
        self.assertEqual(filter_integers([1, 'a', True, 3.14, False, 42]), [1, True, False, 42])

if __name__ == '__main__':
    unittest.main()