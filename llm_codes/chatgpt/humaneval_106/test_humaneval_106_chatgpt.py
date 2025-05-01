############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_106_chatgpt import f


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestFunctionF(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_empty_case(self):
        self.assertEqual(f(0), [])

    def test_single_element(self):
        self.assertEqual(f(1), [1])  # 1 is odd => sum from 1 to 1 = 1

    def test_two_elements(self):
        self.assertEqual(f(2), [1, 2])  # 1 (sum 1), 2 (factorial 2)

    def test_odd_index(self):
        self.assertEqual(f(3), [1, 2, 6])  # 1 (sum 1), 2 (fact 2), 3 (sum 6)

    def test_larger_input(self):
        self.assertEqual(f(6), [1, 2, 6, 24, 15, 720])


if __name__ == '__main__':
    unittest.main()
