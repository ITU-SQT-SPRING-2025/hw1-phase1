############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\n\ndef flip_case(string: str) -> str:\n    \"\"\" For a given string, flip lowercase characters to uppercase and uppercase to lowercase.\n    >>> flip_case('Hello')\n    'hELLO'\n    \"\"\"\n"
#
# response:
#
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()
