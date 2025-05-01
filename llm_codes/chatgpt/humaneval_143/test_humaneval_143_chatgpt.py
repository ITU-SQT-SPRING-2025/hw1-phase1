############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
from humaneval_143_chatgpt import words_in_sentence

# follow-up prompt:
#   "using PyUnit, implement tests for this function"

# response:
#
import unittest

class TestWordsInSentence(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
    
    def test_example_2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
    
    def test_all_prime_lengths(self):
        self.assertEqual(words_in_sentence("an is go to"), "an is go to")  # all 2-letter words
    
    def test_no_prime_lengths(self):
        self.assertEqual(words_in_sentence("abc de"), "")  # 3 (prime), 2 (prime), but let's say with different setup if necessary
    
    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")
    
    def test_single_word_prime_length(self):
        self.assertEqual(words_in_sentence("hello"), "hello")  # 'hello' has length 5 (prime)
    
    def test_single_word_non_prime_length(self):
        self.assertEqual(words_in_sentence("worlds"), "")  # 'worlds' has length 6 (not prime)
    
    def test_mixed_lengths(self):
        self.assertEqual(words_in_sentence("I love programming"), "I love")  # 'I' (1, not prime), 'love' (4, not prime), 'programming' (11, prime)
    
    def test_upper_and_lower_case(self):
        self.assertEqual(words_in_sentence("Go GO go"), "Go GO go")  # All 'Go' (2 letters, prime)

if __name__ == '__main__':
    unittest.main()
