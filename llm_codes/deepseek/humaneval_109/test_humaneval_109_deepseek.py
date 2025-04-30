############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_109_deepseek import move_one_ball


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestMoveOneBall(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))
        self.assertTrue(move_one_ball([10, 20, 30, 40]))

    def test_single_rotation_needed(self):
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))
        self.assertTrue(move_one_ball([4, 5, 1, 2, 3]))

    def test_multiple_rotations_needed(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
        self.assertTrue(move_one_ball([2, 3, 4, 5, 1]))

    def test_unsorted_array(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))
        self.assertFalse(move_one_ball([5, 4, 3, 2, 1]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([1]))
        self.assertTrue(move_one_ball([100]))


if __name__ == '__main__':
    unittest.main()
