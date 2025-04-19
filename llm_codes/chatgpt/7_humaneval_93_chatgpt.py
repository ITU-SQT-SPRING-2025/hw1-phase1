# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef encode(message):\n """\n Write a function that takes a message, and encodes in such a \n way that it swaps case of all letters, replaces all vowels in \n the message with the letter that appears 2 places ahead of that \n vowel in the english alphabet. \n Assume only letters. \n \n Examples:\n >>> encode('test')\n 'TGST'\n >>> encode('This is a message')\n 'tHKS KS C MGSSCGG'\n """\n"

# response:
#

# Sure! Here's how the function can be written according to the rules:
#   1. Swap case: Uppercase becomes lowercase and vice versa.
#   2. Replace vowels (a, e, i, o, u, and their uppercase variants) with the letter two places ahead in the alphabet.
# Let's put that into code:

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

# Explanation:
# - replacement dict maps each vowel to the letter two positions ahead.
# - .swapcase() flips the case of the character.
# - All other letters are just case-swapped.
# Let me know if you'd like to make it work with punctuation or numbers too!
