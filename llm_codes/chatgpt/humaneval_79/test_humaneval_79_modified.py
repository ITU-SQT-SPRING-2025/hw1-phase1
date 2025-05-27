############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_79_modified import decimal_to_binary

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# Notes:
# As the modified prompt resolved the problem with negative numbers, there is no need
# to modify the previous test cases. Moreover, the model did a good job on creating
# test cases with high coverage.

# response:
#
import unittest

class TestDecimalToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_positive_numbers(self):
        self.assertEqual(decimal_to_binary(1), "db1db")
        self.assertEqual(decimal_to_binary(2), "db10db")
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(255), "db11111111db")

    def test_large_number(self):
        self.assertEqual(decimal_to_binary(1024), "db10000000000db")

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecimalToBinary)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
