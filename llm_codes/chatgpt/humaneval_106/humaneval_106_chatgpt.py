############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef f(n):\n    \"\"\" Implement the function f that takes n as a parameter,\n    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even\n    or the sum of numbers from 1 to i otherwise.\n    i starts from 1.\n    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).\n    Example:\n    f(5) == [1, 2, 6, 24, 15]\n    \"\"\"\n"

# response:
#
def f(n):
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def summation(x):
        return x * (x + 1) // 2  # Efficient way to compute 1 + 2 + ... + x

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(summation(i))
    return result
