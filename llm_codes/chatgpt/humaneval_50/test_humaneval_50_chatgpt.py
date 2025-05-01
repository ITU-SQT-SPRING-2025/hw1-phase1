############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_50_chatgpt import encode_shift, decode_shift

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestShiftEncoding(unittest.TestCase):
    
    def test_basic_encoding(self):
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(encode_shift("xyz"), "cde")
    
    def test_basic_decoding(self):
        self.assertEqual(decode_shift("fgh"), "abc")
        self.assertEqual(decode_shift("cde"), "xyz")

    def test_encode_decode_cycle(self):
        original = "helloworld"
        encoded = encode_shift(original)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, original)
        
    def test_empty_string(self):
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(decode_shift(""), "")
        
    def test_single_character(self):
        self.assertEqual(encode_shift("a"), "f")
        self.assertEqual(decode_shift("f"), "a")

    def test_full_alphabet(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encoded = encode_shift(alphabet)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, alphabet)

if __name__ == "__main__":
    unittest.main()
