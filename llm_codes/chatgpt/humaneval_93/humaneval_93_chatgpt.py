############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef encode(message):\n """\n Write a function that takes a message, and encodes in such a \n way that it swaps case of all letters, replaces all vowels in \n the message with the letter that appears 2 places ahead of that \n vowel in the english alphabet. \n Assume only letters. \n \n Examples:\n >>> encode('test')\n 'TGST'\n >>> encode('This is a message')\n 'tHKS KS C MGSSCGG'\n """\n"

# response:
# 
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the English alphabet. 
    Assume only letters.
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    replacement = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }

    encoded = ''
    for char in message:
        if char in vowels:
            new_char = replacement[char]
        else:
            new_char = char
        encoded += new_char.swapcase()
    
    return encoded
