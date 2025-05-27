############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_21_deepseek import rescale_to_unit

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_basic(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

    def test_uniform_list(self):
        numbers = [2.0, 2.0, 2.0]
        expected = [0.0, 0.0, 0.0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        numbers = [-2.0, -1.0, 0.0, 1.0, 2.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

    # the test just below is modified as it was expecting an error
    # whereas the implementation (and the prompt) did not expect it
    # to raise an error
    def test_single_element_list(self):
        numbers = [5.0]
        expected = [0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            rescale_to_unit(numbers)

    def test_floating_point_precision(self):
        numbers = [1.0, 1.0000001, 2.0]
        expected = [0.0, 0.0000001 / 1.0, 1.0]
        result = rescale_to_unit(numbers)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRescaleToUnit)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
