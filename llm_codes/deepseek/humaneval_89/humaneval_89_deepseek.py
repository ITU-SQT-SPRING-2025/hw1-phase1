############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef encrypt(s):\n """Create a function encrypt that takes a string as an argument and\n returns a string encrypted with the alphabet being rotated. \n The alphabet should be rotated in a manner such that the letters \n shift down by two multiplied to two places.\n For example:\n encrypt('hi') returns 'lm'\n encrypt('asdfghjkl') returns 'ewhjklnop'\n encrypt('gf') returns 'kj'\n encrypt('et') returns 'ix'\n """\n"

# response:
#
def encrypt(s):
    encrypted = []
    for char in s:
        if char.islower():
            original_pos = ord(char) - ord('a')
            new_pos = (original_pos + 4) % 26
            new_char = chr(new_pos + ord('a'))
            encrypted.append(new_char)
        elif char.isupper():
            original_pos = ord(char) - ord('A')
            new_pos = (original_pos + 4) % 26
            new_char = chr(new_pos + ord('A'))
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
