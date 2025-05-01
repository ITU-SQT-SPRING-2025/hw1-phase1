############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_161_deepseek import solve


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestSolveFunction(unittest.TestCase):
    def test_no_letters_reverse_string(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("!@#$"), "$#@!")
        self.assertEqual(solve(""), "")

    def test_with_letters_reverse_case(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("AB"), "ab")
        self.assertEqual(solve("aBcD"), "AbCd")

    def test_mixed_characters(self):
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("1a2B3c"), "1A2b3C")
        self.assertEqual(solve("a1B2c3"), "A1b2C3")

    def test_single_character(self):
        self.assertEqual(solve("a"), "A")
        self.assertEqual(solve("Z"), "z")
        self.assertEqual(solve("1"), "1")
        self.assertEqual(solve("@"), "@")


if __name__ == '__main__':
    unittest.main()
