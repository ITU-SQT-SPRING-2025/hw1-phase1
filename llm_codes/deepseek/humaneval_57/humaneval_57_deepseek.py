############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\n\ndef monotonic(l: list):\n """Return True is list elements are monotonically increasing or decreasing.\n >>> monotonic([1, 2, 4, 20])\n True\n >>> monotonic([1, 20, 4, 10])\n False\n >>> monotonic([4, 1, 0, -10])\n True\n """\n"

# response:
#
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            increasing = False
        if l[i] < l[i+1]:
            decreasing = False
    
    return increasing or decreasing
