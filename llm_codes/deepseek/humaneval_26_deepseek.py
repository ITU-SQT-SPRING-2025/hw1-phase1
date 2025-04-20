# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "from typing import List\n\n\ndef remove_duplicates(numbers: List[int]) -> List[int]:\n """ From a list of integers, remove all elements that occur more than once.\n Keep order of elements left the same as in the input.\n >>> remove_duplicates([1, 2, 3, 2, 4])\n [1, 3, 4]\n """\n"

# response:
#
from typing import List
from collections import defaultdict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count_dict = defaultdict(int)
    for num in numbers:
        count_dict[num] += 1
    
    result = [num for num in numbers if count_dict[num] == 1]
    return result
