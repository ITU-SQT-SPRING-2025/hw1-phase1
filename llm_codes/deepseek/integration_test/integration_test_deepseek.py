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

# The integration test below are implemented by correcting the test cases of DeepSeek-V3 and adding more

class TestSecretIntegration(unittest.TestCase):
    def test_process_and_encode_decode(self):
        test_cases = [
            # (input, expected_output)
            ("fun code", "kzs htij"),      # "fun code" -> process keeps all (lengths 3,4) -> not monotonic -> decode
            ("coding is fun", "is"),        # "coding is fun" -> process keeps "is" (length 2) -> single word counts as monotonic -> encode
            ("this is a test", "xn"),       # "this is a test" -> process keeps "is" (length 2) -> single word -> encode
            ("hello world", "mjqqt btwqi"), # "hello world" -> process keeps all (lengths 5,5) -> not monotonic -> decode
            ("a bb ccc dddd", "bb ccc"),    # "a bb ccc dddd" -> process keeps "bb ccc" (lengths 2,3) -> monotonic increasing -> encode
            ("zzz yy x w", "yy x"),         # "zzz yy x w" -> process keeps "yy x" (lengths 2,1) -> monotonic decreasing -> encode
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
