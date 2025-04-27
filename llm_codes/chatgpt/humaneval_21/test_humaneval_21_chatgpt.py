# used LLM model: 
#   GPT-4o
#
from humaneval_21_chatgpt import rescale_to_unit

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_regular_range(self):
        self.assertEqual(
            rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]),
            [0.0, 0.25, 0.5, 0.75, 1.0]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            rescale_to_unit([-10.0, 0.0, 10.0]),
            [0.0, 0.5, 1.0]
        )

    def test_all_same_values(self):
        self.assertEqual(
            rescale_to_unit([3.0, 3.0, 3.0]),
            [0.0, 0.0, 0.0]
        )

    def test_two_elements(self):
        self.assertEqual(
            rescale_to_unit([10.0, 20.0]),
            [0.0, 1.0]
        )

    def test_float_precision(self):
        result = rescale_to_unit([1.0, 1.5, 2.0])
        expected = [0.0, 0.5, 1.0]
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=6)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRescaleToUnit)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
