############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef solve(s):\n    \"\"\"You are given a string s.\n    if s[i] is a letter, reverse its case from lower to upper or vise versa, \n    otherwise keep it as it is.\n    If the string contains no letters, reverse the string.\n    The function should return the resulted string.\n    Examples\n    solve(\"1234\") = \"4321\"\n    solve(\"ab\") = \"AB\"\n    solve(\"#a@C\") = \"#A@c\"\n    \"\"\"\n"

# response:
#
def solve(s):
    has_letter = any(c.isalpha() for c in s)
    if has_letter:
        result = []
        for c in s:
            if c.isupper():
                result.append(c.lower())
            elif c.islower():
                result.append(c.upper())
            else:
                result.append(c)
        return ''.join(result)
    else:
        return s[::-1]
