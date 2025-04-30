import unittest
from humaneval_129_chatgpt import minPath

class TestMinPath(unittest.TestCase):
    def test_example1(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_example2(self):
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]
        ]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_single_cell_grid(self):
        grid = [[1]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

    def test_larger_grid(self):
        grid = [
            [10, 11, 12, 1],
            [13, 14, 2, 3],
            [15, 4, 5, 6],
            [16, 7, 8, 9]
        ]
        k = 4
        expected = [1, 2, 3, 6]
        self.assertEqual(minPath(grid, k), expected)

    def test_full_path(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        k = 4
        # Best path would be 1 -> 2 -> 1 -> 2 again or similar, but 1 2 1 2 is better than 1 2 3 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == "__main__":
    unittest.main()
