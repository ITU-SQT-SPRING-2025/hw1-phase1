# used LLM model: 
#   DeepSeek-V3
#
from humaneval_93_deepseek import encode

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#

import unittest

class TestEncode(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(encode('test'), 'TGST')
    
    def test_mixed_case_word(self):
        self.assertEqual(encode('TeSt'), 'tGsT')
    
    def test_sentence(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
    
    def test_all_vowels(self):
        self.assertEqual(encode('aeiou'), 'CGKQW')
        self.assertEqual(encode('AEIOU'), 'cgkqw')
    
    def test_no_vowels(self):
        self.assertEqual(encode('xyz'), 'XyZ')
        self.assertEqual(encode('XYZ'), 'xYz')
    
    def test_special_characters(self):
        self.assertEqual(encode('123!@#'), '123!@#')

if __name__ == '__main__':
    unittest.main()
