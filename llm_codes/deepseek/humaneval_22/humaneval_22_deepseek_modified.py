############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "from typing import List, Any\n\n\ndef filter_integers(values: List[Any]) -> List[int]:\n    \"\"\" Filter given list of any python values only for integers\n    Note: In Python, bool is a subclass of int, so boolean values like True and False should also be included.\n    >>> filter_integers(['a', 3.14, 5])\n    [5]\n    >>> filter_integers([1, 2, 3, 'abc', {}, []])\n    [1, 2, 3]\n    >>> filter_integers([True, False, 1, 0])\n    [True, False, 1, 0]\n    \"\"\"\n"   
#
# response:
#

from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = []
    for value in values:
        if isinstance(value, bool):
            result.append(value)
        elif isinstance(value, int):
            result.append(value)
    return result