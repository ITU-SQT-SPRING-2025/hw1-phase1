############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\n\ndef monotonic(l: list):\n """Return True is list elements are monotonically increasing or decreasing.\n >>> monotonic([1, 2, 4, 20])\n True\n >>> monotonic([1, 20, 4, 10])\n False\n >>> monotonic([4, 1, 0, -10])\n True\n """\n"

# response:
#
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True  # A list with 0 or 1 elements is trivially monotonic

    increasing = all(l[i] <= l[i+1] for i in range(len(l) - 1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l) - 1))

    return increasing or decreasing
