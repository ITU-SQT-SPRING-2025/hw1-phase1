############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_161_chatgpt import solve


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestSolveFunction(unittest.TestCase):

    def test_all_digits(self):
        self.assertEqual(solve("1234"), "4321")

    def test_all_lowercase_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_mixed_symbols_and_letters(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_uppercase_letters(self):
        self.assertEqual(solve("HELLO"), "hello")

    def test_mixed_case_letters(self):
        self.assertEqual(solve("HeLLo"), "hEllO")

    def test_only_symbols(self):
        self.assertEqual(solve("@#$%^"), "^%$#@")

    def test_digits_and_symbols(self):
        self.assertEqual(solve("123!@#"), "#@!321")

    def test_letters_digits_symbols(self):
        self.assertEqual(solve("a1B2#"), "A1b2#")


if __name__ == "__main__":
    unittest.main()
