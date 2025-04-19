# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "from typing import List\n\n\ndef rescale_to_unit(numbers: List[float]) -> List[float]:\n    \"\"\" Given list of numbers (of at least two elements), apply a linear transform to that list,\n    such that the smallest number will become 0 and the largest will become 1\n    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])\n    [0.0, 0.25, 0.5, 0.75, 1.0]\n    \"\"\"\n"

# response:
#
# Here's the completed implementation of your rescale_to_unit function:

from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0 for _ in numbers]  # All elements are equal; avoid division by zero
    return [(x - min_val) / range_val for x in numbers]

# This function:
# - Finds the minimum and maximum values in the list.
# - Computes the range.
# - Applies the formula (x - min) / (max - min) to each number.
# - Handles the edge case where all numbers are the same by returning a list of zeros.
# Let me know if you want it to raise an error or handle single-element lists differently!
