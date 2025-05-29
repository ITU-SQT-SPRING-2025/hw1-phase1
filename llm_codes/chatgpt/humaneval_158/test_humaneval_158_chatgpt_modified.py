############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
from humaneval_158_chatgpt import find_max


# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest


class TestFindMax(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_lexicographical_tiebreaker(self):
        self.assertEqual(find_max(["abc", "acb", "bac"]), "abc")  # All have 3 unique letters

    def test_single_element(self):
        self.assertEqual(find_max(["only"]), "only")

    def test_case_sensitivity(self):
        self.assertEqual(find_max(["abc", "ABC"]), "ABC")  # 3 unique uppercase vs lowercase

    def test_empty_strings(self):
        self.assertEqual(find_max(["", "a", "aa"]), "a")  # "" has 0 unique, "a" and "aa" both have 1

    def test_all_same_unique_count(self):
        self.assertEqual(find_max(["cat", "dog", "bat"]), "bat")  # all have 3 unique letters, bat is first lexically

    def test_same_unique_chars_scrambled(self):
        self.assertEqual(find_max(["acb", "bca", "abc", "cba", "bac", "a",
                         "b", "c", "ba", "ab", "ca" "ac", "bc", "cb"]), "abc")


if __name__ == "__main__":
    unittest.main()
