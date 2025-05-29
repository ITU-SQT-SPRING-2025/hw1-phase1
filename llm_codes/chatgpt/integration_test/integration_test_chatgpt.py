############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
from implementation_chatgpt import Secret

# follow-up prompt:
#   "Using PyUnit, implement an integration test that does the process over given string sentence and encode if the processed string is monotonic, else decode the processed string."

# response:
#
import unittest

class TestSecretIntegration(unittest.TestCase):
    def test_monotonic_increasing_encode(self):
        sentence = "fun code"
        processed = Secret.processSentence(sentence)  # "fun code"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "kzs htij")

    def test_monotonic_increasing_case2(self):
        sentence = "coding is fun"
        processed = Secret.processSentence(sentence)  # "is fun"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "nx kzs")

    def test_monotonic_decreasing_encode(self):
        sentence = "three go to"
        # lengths = [5, 2, 2] -> decreasing
        processed = Secret.processSentence(sentence)  # "three"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "wmmfj")  # encode "three" with +5 shift

    def test_not_monotonic_then_decode(self):
        sentence = "longest at now"
        # processed: "at now" -> lengths = [2, 3] => increasing → encode
        processed = Secret.processSentence(sentence)
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "fy stb")  # "at now" encoded

    def test_not_monotonic_case2_decode(self):
        sentence = "hi wow test"
        # processed: "hi wow" → lengths = [2, 3] → increasing → encode
        processed = Secret.processSentence(sentence)
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "mn btb")

    def test_empty_processed(self):
        sentence = "a bb cccc"  # lengths 1, 2, 4 — none are prime
        processed = Secret.processSentence(sentence)  # ""
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "")  # Nothing to encode/decode

    def test_single_prime_word(self):
        sentence = "test"
        processed = Secret.processSentence(sentence)  # "test"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "yjxy")  # test → yjxy


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSecretIntegration)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
