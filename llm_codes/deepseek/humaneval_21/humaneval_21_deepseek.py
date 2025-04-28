############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "from typing import List\n\n\ndef rescale_to_unit(numbers: List[float]) -> List[float]:\n    \"\"\" Given list of numbers (of at least two elements), apply a linear transform to that list,\n    such that the smallest number will become 0 and the largest will become 1\n    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])\n    [0.0, 0.25, 0.5, 0.75, 1.0]\n    \"\"\"\n"

# response:
# 
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0 for _ in numbers]
    return [(x - min_val) / range_val for x in numbers]
