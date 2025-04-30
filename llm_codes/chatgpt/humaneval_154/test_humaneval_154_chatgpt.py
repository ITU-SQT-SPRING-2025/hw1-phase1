############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from llm_codes.chatgpt.humaneval_154.humaneval_154_chatgpt import cycpattern_check


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestCycPatternCheck(unittest.TestCase):

    def test_case_1(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))

    def test_case_2(self):
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_case_3(self):
        self.assertFalse(cycpattern_check("whassup", "psus"))

    def test_case_4(self):
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_case_5(self):
        self.assertFalse(cycpattern_check("efef", "eeff"))

    def test_case_6(self):
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_empty_b(self):
        self.assertTrue(cycpattern_check("anything", ""))

    def test_b_longer_than_a(self):
        self.assertFalse(cycpattern_check("abc", "abcdef"))

    def test_exact_match(self):
        self.assertTrue(cycpattern_check("rotation", "rotation"))

    def test_rotation_at_end(self):
        self.assertTrue(cycpattern_check("abcdefg", "fgabc"))


if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()
