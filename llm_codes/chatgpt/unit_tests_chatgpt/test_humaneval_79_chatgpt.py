# used LLM model: 
#   GPT-4o
#
from humaneval_79_chatgpt import decimal_to_binary

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#

import unittest

class TestDecimalToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_small_number(self):
        self.assertEqual(decimal_to_binary(1), "db1db")
        self.assertEqual(decimal_to_binary(2), "db10db")
        self.assertEqual(decimal_to_binary(5), "db101db")

    def test_larger_number(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(255), "db11111111db")

    def test_negative_number(self):
        # Optional: If function is not meant to support negative numbers, check for that
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)

# Optional enhancement: Modify the original function to raise ValueError on negative input
# def decimal_to_binary(decimal):
#     if decimal < 0:
#         raise ValueError("Negative numbers are not supported")
#     binary_str = bin(decimal)[2:]
#     return f"db{binary_str}db"

if __name__ == '__main__':
    unittest.main()
