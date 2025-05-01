############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\n\ndef flip_case(string: str) -> str:\n    \"\"\" For a given string, flip lowercase characters to uppercase and uppercase to lowercase.\n    >>> flip_case('Hello')\n    'hELLO'\n    \"\"\"\n"
#
# response:
#
def flip_case(string: str) -> str:
    flipped = []
    for char in string:
        if char.isupper():
            flipped.append(char.lower())
        elif char.islower():
            flipped.append(char.upper())
        else:
            flipped.append(char)
    return ''.join(flipped)
