############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef cycpattern_check(a , b):\n    \"\"\"You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word\n    cycpattern_check(\"abcd\",\"abd\") => False\n    cycpattern_check(\"hello\",\"ell\") => True\n    cycpattern_check(\"whassup\",\"psus\") => False\n    cycpattern_check(\"abab\",\"baa\") => True\n    cycpattern_check(\"efef\",\"eeff\") => False\n    cycpattern_check(\"himenss\",\"simen\") => True\n\n    \"\"\"\n"

# response:
#
def cycpattern_check(a, b):
    """Check if any rotation of b is a substring of a."""
    if not b:
        return True  # assuming empty string is considered present
    n = len(b)
    for i in range(n):
        rotated = b[i:] + b[:i]
        if rotated in a:
            return True
    return False
