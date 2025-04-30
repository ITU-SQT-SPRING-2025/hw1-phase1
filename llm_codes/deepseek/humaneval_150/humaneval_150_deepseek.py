############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef x_or_y(n, x, y):\n    \"\"\"A simple program which should return the value of x if n is \n    a prime number and should return the value of y otherwise.\n\n    Examples:\n    for x_or_y(7, 34, 12) == 34\n    for x_or_y(15, 8, 5) == 5\n    \n    \"\"\"\n"

# response:
#
def x_or_y(n, x, y):
    if n < 2:
        return y
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return y
    return x
