############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef x_or_y(n, x, y):\n    \"\"\"A simple program which should return the value of x if n is \n    a prime number and should return the value of y otherwise.\n\n    Examples:\n    for x_or_y(7, 34, 12) == 34\n    for x_or_y(15, 8, 5) == 5\n    \n    \"\"\"\n"

# response:
#
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return x if is_prime(n) else y
