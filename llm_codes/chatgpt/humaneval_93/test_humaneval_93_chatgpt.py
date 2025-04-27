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

if __name__ == "__main__":
    unittest.main()
