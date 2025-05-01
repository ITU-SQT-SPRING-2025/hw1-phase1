############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
from humaneval_143_deepseek import words_in_sentence

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestWordsInSentence(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_no_prime_length_words(self):
        self.assertEqual(words_in_sentence("Hello world"), "")
        self.assertEqual(words_in_sentence("Python programming"), "")

    def test_all_prime_length_words(self):
        self.assertEqual(words_in_sentence("I am"), "I am")
        self.assertEqual(words_in_sentence("a be"), "a be")

    def test_single_word_sentence(self):
        self.assertEqual(words_in_sentence("a"), "a")
        self.assertEqual(words_in_sentence("abc"), "")
        self.assertEqual(words_in_sentence("ab"), "ab")

    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")

if __name__ == '__main__':
    unittest.main()
