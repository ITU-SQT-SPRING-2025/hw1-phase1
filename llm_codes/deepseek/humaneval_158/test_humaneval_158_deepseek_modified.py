############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
from humaneval_158_deepseek import find_max


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestFindMax(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(find_max(["hello"]), "hello")

    def test_multiple_words_unique_chars(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_tie_lexicographical_order(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_all_same_unique_chars(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_empty_list(self):
        self.assertEqual(find_max([]), "")

    def test_same_unique_chars_different_lengths(self):
        self.assertEqual(find_max(["abc", "aabbcc", "def"]), "aabbcc")  # fixed

    def test_same_unique_chars_scrambled(self):
        self.assertEqual(find_max(["acb", "bca", "abc", "cba", "bac", "a",
                         "b", "c", "ba", "ab", "ca" "ac", "bc", "cb"]), "abc")


if __name__ == '__main__':
    unittest.main()
