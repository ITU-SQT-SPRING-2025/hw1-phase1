# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "from typing import List\n\n\ndef remove_duplicates(numbers: List[int]) -> List[int]:\n """ From a list of integers, remove all elements that occur more than once.\n Keep order of elements left the same as in the input.\n >>> remove_duplicates([1, 2, 3, 2, 4])\n [1, 3, 4]\n """\n"

# response:
#
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] == 1]
