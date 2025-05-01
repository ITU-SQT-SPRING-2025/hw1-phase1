############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef count_nums(arr):\n    \"\"\"\n    Write a function count_nums which takes an array of integers and returns\n    the number of elements which has a sum of digits > 0.\n    If a number is negative, then its first signed digit will be negative:\n    e.g. -123 has signed digits -1, 2, and 3.\n    >>> count_nums([]) == 0\n    >>> count_nums([-1, 11, -11]) == 1\n    >>> count_nums([1, 1, 2]) == 3\n    \"\"\"\n"   
#
# response:
#
def count_nums(arr):
    count = 0
    for num in arr:
        s = str(num)
        total = 0
        i = 0
        if s[0] == '-':
            # The first digit after '-' is negative
            if len(s) > 1:
                total += -int(s[1])
            i = 2
        else:
            i = 0
        # Process remaining digits
        while i < len(s):
            total += int(s[i])
            i += 1
        if total > 0:
            count += 1
    return count
