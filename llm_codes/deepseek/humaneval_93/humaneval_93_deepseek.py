############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef encode(message):\n """\n Write a function that takes a message, and encodes in such a \n way that it swaps case of all letters, replaces all vowels in \n the message with the letter that appears 2 places ahead of that \n vowel in the english alphabet. \n Assume only letters. \n \n Examples:\n >>> encode('test')\n 'TGST'\n >>> encode('This is a message')\n 'tHKS KS C MGSSCGG'\n """\n"

# response:
#
def encode(message):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # First, swap the case of all letters in the message
    swapped_case = []
    for char in message:
        if char.isupper():
            swapped_case.append(char.lower())
        elif char.islower():
            swapped_case.append(char.upper())
        else:
            swapped_case.append(char)
    swapped_str = ''.join(swapped_case)
    
    # Now, replace each vowel in the swapped_str with the letter two places ahead
    encoded_message = []
    for char in swapped_str:
        if char in vowels:
            if char.islower():
                new_char = chr(((ord(char) - ord('a') + 2) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') + 2) % 26) + ord('A'))
            encoded_message.append(new_char)
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)
