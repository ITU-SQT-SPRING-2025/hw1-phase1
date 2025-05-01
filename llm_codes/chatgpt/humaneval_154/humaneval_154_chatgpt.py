############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef cycpattern_check(a , b):\n    \"\"\"You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word\n    cycpattern_check(\"abcd\",\"abd\") => False\n    cycpattern_check(\"hello\",\"ell\") => True\n    cycpattern_check(\"whassup\",\"psus\") => False\n    cycpattern_check(\"abab\",\"baa\") => True\n    cycpattern_check(\"efef\",\"eeff\") => False\n    cycpattern_check(\"himenss\",\"simen\") => True\n\n    \"\"\"\n"

# response:
#
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    if not b:
        return True  # An empty string is always a substring

    rotations = [b[i:] + b[:i] for i in range(len(b))]
    return any(rot in a for rot in rotations)
