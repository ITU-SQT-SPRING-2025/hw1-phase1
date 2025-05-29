############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
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
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    Note that bools are not integers.

    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  

    If the input list is empty, return 0.
    '''
    return sum(x**2 for x in lst if isinstance(x, int) and not isinstance(x, bool) and x > 0 and x % 2 == 1)
