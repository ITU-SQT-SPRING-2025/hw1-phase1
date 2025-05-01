############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef do_algebra(operator, operand):\n    \"\"\"\n    Given two lists operator, and operand. The first list has basic algebra operations, and \n    the second list is a list of integers. Use the two given lists to build the algebric \n    expression and return the evaluation of this expression.\n\n    The basic algebra operations:\n    Addition ( + ) \n    Subtraction ( - ) \n    Multiplication ( * ) \n    Floor division ( // ) \n    Exponentiation ( ** ) \n\n    Example:\n    operator['+', '*', '-']\n    array = [2, 3, 4, 5]\n    result = 2 + 3 * 4 - 5\n    => result = 9\n\n    Note:\n        The length of operator list is equal to the length of operand list minus one.\n        Operand is a list of of non-negative integers.\n        Operator list has at least one operator, and operand list has at least two operands.\n\n    \"\"\"\n"

# response:
#
def do_algebra(operator, operand):
    if not operand:
        return 0
    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        next_val = operand[i+1]
        if op == '+':
            result += next_val
        elif op == '-':
            result -= next_val
        elif op == '*':
            result *= next_val
        elif op == '//':
            result //= next_val
        elif op == '**':
            result **= next_val
    return result
