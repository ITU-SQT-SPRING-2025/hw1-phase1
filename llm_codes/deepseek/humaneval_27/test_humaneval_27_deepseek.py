############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_27_deepseek import flip_case

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestFlipCase(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('PyThOn'), 'pYtHoN')

    def test_all_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')
        self.assertEqual(flip_case('PYTHON'), 'python')

    def test_non_alphabetic(self):
        self.assertEqual(flip_case('123!@#'), '123!@#')
        self.assertEqual(flip_case('Hello123!'), 'hELLO123!')

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

if __name__ == '__main__':
    unittest.main()
