############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_50_deepseek import encode_shift, decode_shift

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestShiftCipher(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift("abc"), "fgh")  # a->f, b->g, c->h
        self.assertEqual(encode_shift("xyz"), "cde")  # x->c, y->d, z->e (wrap-around)
        self.assertEqual(encode_shift("hello"), "mjqqt")  # hello -> mjqqt
        self.assertEqual(encode_shift(""), "")  # Empty string
        self.assertEqual(encode_shift("a"), "f")  # Single character

    def test_decode_shift(self):
        self.assertEqual(decode_shift("fgh"), "abc")  # f->a, g->b, h->c
        self.assertEqual(decode_shift("cde"), "xyz")  # c->x, d->y, e->z (wrap-around)
        self.assertEqual(decode_shift("mjqqt"), "hello")  # mjqqt -> hello
        self.assertEqual(decode_shift(""), "")  # Empty string
        self.assertEqual(decode_shift("f"), "a")  # Single character

    def test_encode_decode_roundtrip(self):
        original = "testing"
        encoded = encode_shift(original)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, original)  # Ensure decode(encode(s)) == s

if __name__ == "__main__":
    unittest.main()
