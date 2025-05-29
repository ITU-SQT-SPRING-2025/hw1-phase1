############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#

import unittest
from implementation_deepseek import Secret

# follow-up prompt:
#   "Using PyUnit, implement an integration test that does the process over given string sentence and encode if the processed string is monotonic, else decode the processed string."

# response:
#

class TestSecretIntegration(unittest.TestCase):
    def test_process_and_encode_decode(self):
        test_cases = [
            # (input, expected_output)
            ("fun code", "kzs"),      # "fun code" -> process keeps fun (lengths 3) -> not monotonic -> decode
            ("coding is fun", "nx kzs"),        # "coding is fun" -> process keeps "is fun" (length 2, 3) -> monotonic increasing -> encode
            ("this is a test", "nx"),       # "this is a test" -> process keeps "is" (length 2) -> single word -> encode
            ("hello world", "czggj rjmgy"), # "hello world" -> process keeps all (lengths 5,5) -> not monotonic -> decode
            ("a bb ccc dddd", "gg hhh"),    # "a bb ccc dddd" -> process keeps "bb ccc" (lengths 2,3) -> monotonic increasing -> encode
            ("zzz yy x w", "eee dd"),         # "zzz yy x w" -> process keeps "yy x" (lengths 2,1) -> monotonic decreasing -> encode
            ("hi wow test", "mn btb"),              # "hi wow test" -> process keeps "hi wow" (length 2,3) -> monotonic increasing -> encode
            ("test", ""),                           # "test" -> process keeps none -> ""
            ("longest at now", "gjibzno vo ijr")    # "longest at now" -> process keeps all (length 7,2,3) -> not monotonic -> decode

        ]

        for input_str, expected_output in test_cases:
            with self.subTest(input=input_str):
                # Step 1: Process the sentence to keep only words with prime lengths
                processed = Secret.processSentence(input_str)
                
                # Step 2: Check if the processed sentence is monotonic
                if Secret.isMonotonic(processed):
                    # If monotonic, encode
                    result = Secret.encode(processed)
                else:
                    # If not monotonic, decode
                    result = Secret.decode(processed)
                
                # Verify the result matches expected output
                self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
