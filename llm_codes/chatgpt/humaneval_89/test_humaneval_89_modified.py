############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_89_modified import encrypt

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

    # The cases below are added by the author in order to show the missed cases
    def test_numbers(self):
        # Should not change the numbers into any other value
        self.assertEqual(encrypt('ab123'), 'ef123')

    # The test cases below are not supported by the code that is generated
    # by the original HumanEval/89 prompt. Thus, a modified prompt is used
    # to generate code for these features. The prompt did not mention about any
    # capitalization, and since the examples did not contain any capital letter
    # it seems it did not expect to cover them.

    def test_capital_letters(self):
        # Should keep the capital letters as capital and still encrypt
        self.assertEqual(encrypt('WXYZ'), 'ABCD')
        self.assertEqual(encrypt('ABcdEf'), 'EFghIj')

    def test_Turkish_alphabet(self):
        # The function is not expected to work with Turkish alphabet
        # because there is no standard alphabet.
        # This test can be extended to other alphabets such as Cyrillic alphabet,
        # Arabic alphabet, Greek alphabet and so on.
        self.assertNotEqual(encrypt('ışĞÜ'), 'mvJA')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptFunction)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
