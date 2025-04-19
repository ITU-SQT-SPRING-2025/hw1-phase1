# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "from typing import List\n\n\ndef remove_duplicates(numbers: List[int]) -> List[int]:\n """ From a list of integers, remove all elements that occur more than once.\n Keep order of elements left the same as in the input.\n >>> remove_duplicates([1, 2, 3, 2, 4])\n [1, 3, 4]\n """\n"

# response:
#
# To complete the remove_duplicates function, you want to return a new list containing only the integers that appear exactly once in the input list, preserving their original order.
# Here's the completed function:

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

# How it works:
# - Counter(numbers) creates a frequency map of the numbers.
# - The list comprehension filters out numbers that appear more than once.
# Would you like it to also remove duplicates regardless of count (i.e., keep only the first occurrence), or is this behavior exactly what you wanted?
