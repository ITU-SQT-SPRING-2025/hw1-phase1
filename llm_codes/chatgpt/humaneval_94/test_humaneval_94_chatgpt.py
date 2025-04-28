############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_94_chatgpt import skjkasdkd

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestSkjkasdkd(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)
        self.assertEqual(skjkasdkd([0,8,1,2,1,7]), 7)

    def test_no_primes(self):
        self.assertEqual(skjkasdkd([0, 1, 0, 1, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(skjkasdkd([]), 0)

    def test_single_prime(self):
        self.assertEqual(skjkasdkd([17]), 8)  # 1 + 7

    def test_multiple_same_largest_prime(self):
        self.assertEqual(skjkasdkd([11, 11, 11]), 2)  # 1 + 1

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSkjkasdkd)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
