############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef do_algebra(operator, operand):\n    \"\"\"\n    Given two lists operator, and operand. The first list has basic algebra operations, and \n    the second list is a list of integers. Use the two given lists to build the algebric \n    expression and return the evaluation of this expression.\n\n    The basic algebra operations:\n    Addition ( + ) \n    Subtraction ( - ) \n    Multiplication ( * ) \n    Floor division ( // ) \n    Exponentiation ( ** ) \n\n    Example:\n    operator['+', '*', '-']\n    array = [2, 3, 4, 5]\n    result = 2 + 3 * 4 - 5\n    => result = 9\n\n    Note:\n        The length of operator list is equal to the length of operand list minus one.\n        Operand is a list of of non-negative integers.\n        Operator list has at least one operator, and operand list has at least two operands.\n\n    \"\"\"\n"

# response:
#
def do_algebra(operator, operand):
    """
    Given two lists: 'operator' and 'operand'. The first list contains basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.
    """
    # Start with the first operand
    result = operand[0]

    # Loop through the operator list and apply each operation to the current result
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Unsupported operator: {op}")

    return result
