############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_79_modified import decimal_to_binary

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# follow-up prompt is prompted after the modified prompt generated 
# the code in the humaneval_79_modified.py file

# response:
#
import unittest

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(0), "db0db")
        self.assertEqual(decimal_to_binary(1), "db1db")
        self.assertEqual(decimal_to_binary(1023), "db1111111111db")

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)
        with self.assertRaises(ValueError):
            decimal_to_binary(-15)
        with self.assertRaises(ValueError):
            decimal_to_binary(-100)

    def test_large_numbers(self):
        self.assertEqual(decimal_to_binary(1024), "db10000000000db")
        self.assertEqual(decimal_to_binary(123456789), "db111010110111100110100010101db")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecimalToBinary)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
