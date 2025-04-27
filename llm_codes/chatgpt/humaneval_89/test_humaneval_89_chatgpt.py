# used LLM model: 
#   GPT-4o
#
from humaneval_89_chatgpt import encrypt

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestEncryptFunction(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_wraparound(self):
        self.assertEqual(encrypt('wxyz'), 'abcd')  # wrap from z to a

    def test_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_non_alpha_characters(self):
        self.assertEqual(encrypt('a! b@c#'), 'e! f@g#')  # punctuation and spaces preserved

    def test_all_letters(self):
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'), 'efghijklmnopqrstuvwxyzabcd')

if __name__ == '__main__':
    unittest.main()
