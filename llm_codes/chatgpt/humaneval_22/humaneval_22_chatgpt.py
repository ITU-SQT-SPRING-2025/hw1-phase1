############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "from typing import List, Any\n\n\ndef filter_integers(values: List[Any]) -> List[int]:\n    \"\"\" Filter given list of any python values only for integers\n    >>> filter_integers(['a', 3.14, 5])\n    [5]\n    >>> filter_integers([1, 2, 3, 'abc', {}, []])\n    [1, 2, 3]\n    \"\"\"\n"   
#
# response:
#
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
