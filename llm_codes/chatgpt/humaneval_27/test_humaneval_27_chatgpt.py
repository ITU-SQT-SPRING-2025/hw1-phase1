############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_27_chatgpt import flip_case

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestFlipCase(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
    
    def test_all_uppercase(self):
        self.assertEqual(flip_case('WORLD'), 'world')
    
    def test_all_lowercase(self):
        self.assertEqual(flip_case('python'), 'PYTHON')
    
    def test_mixed_characters(self):
        self.assertEqual(flip_case('PyThOn123'), 'pYtHoN123')
    
    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')
    
    def test_special_characters(self):
        self.assertEqual(flip_case('Hi! @#'), 'hI! @#')
    
    def test_numbers_only(self):
        self.assertEqual(flip_case('123456'), '123456')  # numbers unaffected

if __name__ == '__main__':
    unittest.main()
