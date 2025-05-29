############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#

from implementation_chatgpt import Secret
import unittest

# The integration test below are implemented by correcting the test cases of GPT-4o and adding more

class TestSecretIntegration(unittest.TestCase):
    def test_monotonic_increasing_case2(self):
        sentence = "coding is fun"
        processed = Secret.processSentence(sentence)  # "is fun"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "nx kzs")

    def test_not_monotonic_case2_decode(self):
        sentence = "hi wow test"
        # processed: "hi wow" → lengths = [2, 3] → increasing → encode
        processed = Secret.processSentence(sentence)
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "mn btb")

    # Below are added/edited by the author
    def test_monotonic_decreasing_encode(self):
        sentence = "three go to"
        processed = Secret.processSentence(sentence)  # "three go to"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "ymwjj lt yt")

    def test_monotonic_increasing_encode(self):
        sentence = "fun code"
        processed = Secret.processSentence(sentence)  # "fun"
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "kzs")

    def test_empty_after_process(self):
        sentence = "test"
        processed = Secret.processSentence(sentence)
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "")

    def test_not_monotonic(self):
        sentence = "longest at now"
        # processed: "longest at now" -> neither
        processed = Secret.processSentence(sentence)
        result = Secret.encode(processed) if Secret.isMonotonic(processed) else Secret.decode(processed)
        self.assertEqual(result, "gjibzno vo ijr")  # "longest at now" encoded



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSecretIntegration)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
