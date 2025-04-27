# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef encrypt(s):\n """Create a function encrypt that takes a string as an argument and\n returns a string encrypted with the alphabet being rotated. \n The alphabet should be rotated in a manner such that the letters \n shift down by two multiplied to two places.\n For example:\n encrypt('hi') returns 'lm'\n encrypt('asdfghjkl') returns 'ewhjklnop'\n encrypt('gf') returns 'kj'\n encrypt('et') returns 'ix'\n """\n"

# response:
#
def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places (i.e., 2 * 2 = 4).
    
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    shift = 4  # 2 * 2 = 4
    result = ""

    for char in s:
        if char.isalpha():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char  # preserve non-alpha characters if needed

    return result
