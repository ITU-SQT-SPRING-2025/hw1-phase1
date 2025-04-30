############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_154_deepseek import cycpattern_check


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestCycPatternCheck(unittest.TestCase):
    def test_false_case(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))

    def test_true_case(self):
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_false_case_2(self):
        self.assertFalse(cycpattern_check("whassup", "psus"))

    def test_true_case_2(self):
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_false_case_3(self):
        self.assertFalse(cycpattern_check("efef", "eeff"))

    def test_true_case_3(self):
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_empty_b(self):
        self.assertTrue(cycpattern_check("anything", ""))

    def test_empty_a(self):
        self.assertFalse(cycpattern_check("", "abc"))

    def test_same_string(self):
        self.assertTrue(cycpattern_check("abc", "abc"))

    def test_rotation_at_end(self):
        self.assertTrue(cycpattern_check("xyzabc", "bca"))


if __name__ == '__main__':
    unittest.main()
