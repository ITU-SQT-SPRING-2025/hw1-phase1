############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt1:
# def exchange(lst1, lst2):
#     In this problem, you will implement a function that takes two lists of numbers,
#     and determines whether it is possible to perform an exchange of elements
#     between them to make lst1 a list of only even numbers.
#     There is no limit on the number of exchanged elements between lst1 and lst2.
#     If it is possible to exchange elements between the lst1 and lst2 to make
#     all the elements of lst1 to be even, return YES.
#     Otherwise, return NO.
#     For example:
#     exchange([1, 2, 3, 4], [1, 2, 3, 4]) => YES
#     exchange([1, 2, 3, 4], [1, 5, 3, 4]) => NO
#     It is assumed that the input lists will be non-empty. However you should check for these cases and if it is possible to make all elements in lst1 to be even, then code would return "YES". If lst1 would remain empty then answer should be "NO".
#     For example:

# response:
# def exchange(lst1, lst2):
#     # Check if either list is empty
#     if not lst1 or not lst2:
#         return "NO"
#
#     # Count number of odd elements in lst1
#     odd_count = sum(1 for x in lst1 if x % 2 != 0)
#
#     # Count number of even elements in lst2
#     even_count_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)
#
#     # If there are enough even numbers in lst2 to replace all odd numbers in lst1
#     if even_count_in_lst2 >= odd_count:
#         return "YES"
#     else:
#         return "NO"

# result 1: passed 8/9

# prompt2:
# def exchange(lst1, lst2):
#     In this problem, you will implement a function that takes two lists of numbers,
#     and determines whether it is possible to perform an exchange of elements
#     between them to make lst1 a list of only even numbers.
#     There is no limit on the number of exchanged elements between lst1 and lst2.
#     If it is possible to exchange elements between the lst1 and lst2 to make
#     all the elements of lst1 to be even, return YES.
#     Otherwise, return NO.
#     For example:
#     exchange([1, 2, 3, 4], [1, 2, 3, 4]) => YES
#     exchange([1, 2, 3, 4], [1, 5, 3, 4]) => NO
#     It is assumed that the input lists will be non-empty. However you should check for these cases and if it is possible to make all elements in lst1 to be even, then code would return "YES". If lst1 would remain empty then answer should be "NO".
#     For example:
#     exchange([2], []) => YES


# response:
#
def exchange(lst1, lst2):
    # If lst1 is empty, return "NO"
    if not lst1:
        return "NO"

    # Count odd numbers in lst1 (these need to be replaced)
    odd_in_lst1 = sum(1 for x in lst1 if x % 2 != 0)

    # Count even numbers in lst2 (these can replace the odd numbers)
    even_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)

    # If lst1 already contains only even numbers, return "YES"
    if odd_in_lst1 == 0:
        return "YES"

    # If we have enough even numbers in lst2 to replace all odd numbers in lst1
    if even_in_lst2 >= odd_in_lst1:
        return "YES"

    return "NO"
