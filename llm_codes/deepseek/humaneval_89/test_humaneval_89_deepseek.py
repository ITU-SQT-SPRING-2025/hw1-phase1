# used LLM model: 
#   DeepSeek-V3
#
from humaneval_89_deepseek import encrypt

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestEncryptFunction(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_edge_cases(self):
        self.assertEqual(encrypt(''), '')  # Empty string
        self.assertEqual(encrypt('z'), 'd')  # Wrap around from 'z'
        self.assertEqual(encrypt('y'), 'c')  # Wrap around from 'y'
        self.assertEqual(encrypt('a'), 'e')  # No wrap around

    def test_non_alphabetic_characters(self):
        self.assertEqual(encrypt('h2i'), 'l2m')  # Numeric character
        self.assertEqual(encrypt('h!i'), 'l!m')  # Special character
        self.assertEqual(encrypt('hi '), 'lm ')  # Space character

    def test_case_sensitivity(self):
        self.assertEqual(encrypt('Hi'), 'Lm')  # Mixed case
        self.assertEqual(encrypt('HI'), 'LM')  # All uppercase
        self.assertEqual(encrypt('hI'), 'lM')  # Mixed case

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptFunction)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
