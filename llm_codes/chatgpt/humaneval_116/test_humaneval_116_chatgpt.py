# used LLM model: 
#   GPT-4o
#
from humaneval_116_chatgpt import sort_array

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestSortArray(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_zeros(self):
        self.assertEqual(sort_array([0, 0, 0]), [0, 0, 0])

    def test_same_number_of_ones(self):
        # binary: 3 = 11, 5 = 101, 6 = 110 => all have 2 ones
        self.assertEqual(sort_array([6, 3, 5]), [3, 5, 6])  # sorted by value

    def test_mixed_integers(self):
        self.assertEqual(sort_array([7, -7, 3, -3]), [-7, -3, 3, 7])

    def test_large_numbers(self):
        self.assertEqual(sort_array([1023, 1, 512]), [1, 512, 1023])  # 1023 = 10 ones, 512 = 1 one

    def test_negative_and_positive_mix(self):
        # Check sorting handles both
        self.assertEqual(sort_array([3, -3, 2, -2]), [-2, -3, 2, 3])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortArray)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
