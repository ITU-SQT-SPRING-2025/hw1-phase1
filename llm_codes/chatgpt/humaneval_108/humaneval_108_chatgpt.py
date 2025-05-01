############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef count_nums(arr):\n    \"\"\"\n    Write a function count_nums which takes an array of integers and returns\n    the number of elements which has a sum of digits > 0.\n    If a number is negative, then its first signed digit will be negative:\n    e.g. -123 has signed digits -1, 2, and 3.\n    >>> count_nums([]) == 0\n    >>> count_nums([-1, 11, -11]) == 1\n    >>> count_nums([1, 1, 2]) == 3\n    \"\"\"\n"   
#
# response:
#
def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        digits = []
        str_num = str(abs(num))
        if num < 0:
            digits.append(-int(str_num[0]))
            digits.extend(int(d) for d in str_num[1:])
        else:
            digits.extend(int(d) for d in str_num)
        
        if sum(digits) > 0:
            count += 1
    return count
