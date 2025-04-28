############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_94_deepseek import skjkasdkd

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestSkjkasdkd(unittest.TestCase):
    def test_example1(self):
        lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
        self.assertEqual(skjkasdkd(lst), 10)

    def test_example2(self):
        lst = [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]
        self.assertEqual(skjkasdkd(lst), 25)

    def test_example3(self):
        lst = [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]
        self.assertEqual(skjkasdkd(lst), 13)

    def test_example4(self):
        lst = [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]
        self.assertEqual(skjkasdkd(lst), 11)

    def test_example5(self):
        lst = [0, 81, 12, 3, 1, 21]
        self.assertEqual(skjkasdkd(lst), 3)

    def test_example6(self):
        lst = [0, 8, 1, 2, 1, 7]
        self.assertEqual(skjkasdkd(lst), 7)

    def test_empty_list(self):
        lst = []
        self.assertEqual(skjkasdkd(lst), 0)

    def test_no_primes(self):
        lst = [0, 1, 4, 6, 8, 9, 10]
        self.assertEqual(skjkasdkd(lst), 0)

    def test_single_prime(self):
        lst = [13]
        self.assertEqual(skjkasdkd(lst), 4)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSkjkasdkd)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
