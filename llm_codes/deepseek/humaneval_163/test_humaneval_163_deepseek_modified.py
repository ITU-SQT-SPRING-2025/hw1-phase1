############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_163_deepseek_modified import generate_integers

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#

import unittest

class TestGenerateIntegers(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(0, 2), [0, 2])
        self.assertEqual(generate_integers(10, 14), [])

    def test_edge_cases(self):
        self.assertEqual(generate_integers(0, 0), [0])
        self.assertEqual(generate_integers(8, 8), [8])
        self.assertEqual(generate_integers(9, 9), [])

    def test_error_cases(self):
        with self.assertRaises(ValueError):
            generate_integers(-1, 5)
        with self.assertRaises(ValueError):
            generate_integers(5, -1)

    def test_large_numbers(self):
        self.assertEqual(generate_integers(100, 200), [])

if __name__ == '__main__':
    unittest.main()