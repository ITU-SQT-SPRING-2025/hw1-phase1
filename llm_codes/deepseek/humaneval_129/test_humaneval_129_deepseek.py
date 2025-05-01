import unittest
from humaneval_129_deepseek import minPath

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
    
    def test_k_equals_grid_size(self):
        grid = [[1, 2], [3, 4]]
        k = 4
        expected = [1, 2, 1, 2]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_larger_grid(self):
        grid = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
        k = 4
        expected = [10, 15, 10, 15]
        self.assertEqual(minPath(grid, k), expected)
    
    def test_min_path_with_repeats(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        k = 3
        expected = [1, 1, 1]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == '__main__':
    unittest.main()
