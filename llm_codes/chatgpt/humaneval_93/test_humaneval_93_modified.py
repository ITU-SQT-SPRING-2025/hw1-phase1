############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_93_chatgpt import encode

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestEncodeFunction(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(encode("test"), "TGST")

    def test_example_2(self):
        self.assertEqual(encode("This is a message"), "tHKS KS C MGSSCGG")

    def test_all_vowels_lowercase(self):
        self.assertEqual(encode("aeiou"), "CGKQW")

    def test_all_vowels_uppercase(self):
        self.assertEqual(encode("AEIOU"), "cgkqw")

    def test_mixed_case(self):
        self.assertEqual(encode("HeLLo"), "hGllQ")

    def test_no_vowels(self):
        self.assertEqual(encode("bcdfg"), "BCDFG")

    def test_all_consonants_uppercase(self):
        self.assertEqual(encode("BCDFG"), "bcdfg")

    def test_empty_string(self):
        self.assertEqual(encode(""), "")

    # The tests below are added by the author

    def test_numbers(self):
        # The function expects string, therefore sending an int type
        # should throw error
        with self.assertRaises(TypeError):
            # the function throws "'int' object is not iterable"
            # it should be handled better but still works fine
            encode(1234), "1234"
        self.assertEqual(encode("1234"), "1234")
        self.assertEqual(encode("ab123"), "CB123")
    
    def test_symbols(self):
        self.assertEqual(encode("Hello, World!"), "hGLLQ, wQRLD!")
        self.assertEqual(encode("Hi!?_@"), "hK!?_@")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncodeFunction)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
