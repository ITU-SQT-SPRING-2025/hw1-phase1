############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_109_chatgpt import move_one_ball


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_rotated_sorted_array(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
        self.assertTrue(move_one_ball([2, 3, 4, 5, 1]))
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))

    def test_unsortable_array(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))
        self.assertFalse(move_one_ball([2, 1, 3, 4, 5]))
        self.assertFalse(move_one_ball([1, 3, 2, 4, 5]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([42]))

    def test_two_elements(self):
        self.assertTrue(move_one_ball([2, 1]))
        self.assertTrue(move_one_ball([1, 2]))

    def all_equal_elements(self):
        self.assertTrue(move_one_ball([5, 5, 5, 5, 5]))

    def some_equal_elements_one_rotation(self):
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4, 5]))
        self.assertFalse(move_one_ball([5, 1, 2, 3, 4, 5, 4]))

    def some_equal_elements_couple_rotations(self):
        self.assertTrue(move_one_ball([5, 5, 1, 2, 3, 4]))
        self.assertFalse(move_one_ball([5, 4,  5, 1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
