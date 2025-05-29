############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_129_chatgpt import minPath

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#

import unittest

class TestMinPath(unittest.TestCase):

    def test_example1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_example2(self):
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_single_cell_grid(self):
        grid = [[1]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_larger_grid(self):
        grid = [[10, 11, 12, 1], 
                [13, 14, 2, 3], 
                [15, 4, 5, 6], 
                [16, 7, 8, 9]]
        k = 4
        expected = [1, 3, 1, 3]
        self.assertEqual(minPath(grid, k), expected)

    def test_path_with_repetition(self):
        grid = [[1, 2], [3, 4]]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == "__main__":
    unittest.main()
