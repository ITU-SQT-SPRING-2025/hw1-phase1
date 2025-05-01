############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef f(n):\n    \"\"\" Implement the function f that takes n as a parameter,\n    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even\n    or the sum of numbers from 1 to i otherwise.\n    i starts from 1.\n    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).\n    Example:\n    f(5) == [1, 2, 6, 24, 15]\n    \"\"\"\n"

# response:
#
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # Compute factorial of i
            factorial = 1
            for num in range(1, i+1):
                factorial *= num
            result.append(factorial)
        else:
            # Compute sum from 1 to i
            sum_i = i * (i + 1) // 2
            result.append(sum_i)
    return result
