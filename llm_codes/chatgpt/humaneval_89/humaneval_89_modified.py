############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef encrypt(s):\n """Create a function encrypt that takes a string as an argument and\n returns a string encrypted with the alphabet being rotated. \n The alphabet should be rotated in a manner such that the letters \n shift down by two multiplied to two places.\n For example:\n encrypt('hi') returns 'lm'\n encrypt('asdfghjkl') returns 'ewhjklnop'\n encrypt('gf') returns 'kj'\n encrypt('et') returns 'ix'\n """\n"

# response:
#

def encrypt(s):
    """Encrypt a string by rotating each letter forward by 4 positions."""
    result = ""
    for char in s:
        if char.islower():
            # Rotate within lowercase alphabet
            shifted = (ord(char) - ord('a') + 4) % 26 + ord('a')
            result += chr(shifted)
        elif char.isupper():
            # Rotate within uppercase alphabet
            shifted = (ord(char) - ord('A') + 4) % 26 + ord('A')
            result += chr(shifted)
        else:
            # Keep non-letter characters unchanged
            result += char
    return result
