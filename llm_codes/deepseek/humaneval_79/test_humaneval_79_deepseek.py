# used LLM model: 
#   DeepSeek-V3
#
from humaneval_79_deepseek import decimal_to_binary

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(1), "db1db")
        self.assertEqual(decimal_to_binary(10), "db1010db")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_negative_numbers(self):
        # Assuming the function is expected to handle negative numbers by their two's complement
        # or other representation, but the problem statement doesn't specify.
        # Here, we test how the function behaves with negative input.
        self.assertEqual(decimal_to_binary(-1), "db-1db")  # This might not be the intended behavior

    def test_large_numbers(self):
        self.assertEqual(decimal_to_binary(1023), "db1111111111db")
        self.assertEqual(decimal_to_binary(1024), "db10000000000db")

    # Optional: Test for non-integer inputs if the function is expected to handle them
    # def test_non_integer_inputs(self):
    #     with self.assertRaises(TypeError):
    #         decimal_to_binary("10")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecimalToBinary)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
