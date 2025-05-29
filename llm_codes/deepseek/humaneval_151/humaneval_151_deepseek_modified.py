############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
# def double_the_difference(lst):
#     '''
#     Given a list of numbers, return the sum of squares of the numbers
#     in the list that are odd. Ignore numbers that are negative or not integers.
#     Note that bools are not integers.
#
#     double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
#     double_the_difference([-1, -2, 0]) == 0
#     double_the_difference([9, -2]) == 81
#     double_the_difference([0]) == 0
#
#     If the input list is empty, return 0.
#     '''

# response:
#
def double_the_difference(lst):
    total = 0
    for num in lst:
        # Check if the number is an integer and not a boolean
        if isinstance(num, bool):
            continue
        if isinstance(num, int) and num >= 0:
            if num % 2 != 0:
                total += num * num
    return total
