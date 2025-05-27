############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef sort_array(arr):\n """\n In this Kata, you have to sort an array of non-negative integers according to\n number of ones in their binary representation in ascending order.\n For similar number of ones, sort based on decimal value.\n\n It must be implemented like this:\n >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]\n >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 4, 3]\n """\n"

# response:
#

def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
