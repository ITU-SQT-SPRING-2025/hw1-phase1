############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef exchange(lst1, lst2):\n    \"\"\"In this problem, you will implement a function that takes two lists of numbers,\n    and determines whether it is possible to perform an exchange of elements\n    between them to make lst1 a list of only even numbers.\n    There is no limit on the number of exchanged elements between lst1 and lst2.\n    If it is possible to exchange elements between the lst1 and lst2 to make\n    all the elements of lst1 to be even, return \"YES\".\n    Otherwise, return \"NO\".\n    For example:\n    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => \"YES\"\n    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => \"NO\"\n    It is assumed that the input lists will be non-empty.\n    \"\"\"\n"

# response:
#
def exchange(lst1, lst2):
    odd_in_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    even_in_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"
