############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
# def do_algebra(operator, operand):
#     Given two lists operator, and operand. The first list has basic algebra operations, and
#     the second list is a list of integers. Use the two given lists to build the algebric
#     expression and return the evaluation of this expression.
#     The basic algebra operations:
#     Addition ( + )
#     Subtraction ( - )
#     Multiplication ( * )
#     Floor division ( // )
#     Exponentiation ( ** )
#     Example:
#     operator['+', '*', '-']
#     array = [2, 3, 4, 5]
#     result = 2 + 3 * 4 - 5
#     => result = 9
#     Note:
#         The length of operator list is equal to the length of operand list minus one. But you should do explicit checks and raise a ValueError if necessary.
#         You should check for operand correctness and raise ValueError if necessary.
#         Operand is a list of of non-negative integers.
#         Operator list has at least one operator, and operand list has at least two operands.
#         You should consider operator precedence as well. Operator precedence is:
#             Exponentiation ( ** ) > Multiplication ( * ) = Floor division ( // ) > Addition ( + ) = Subtraction ( - )
#             Same level operations are concluded from left to right.

# response:
#
import operator as op
import ast


def do_algebra(operators, operands):
    # Validate input types and structure
    if not isinstance(operators, list) or not isinstance(operands, list):
        raise ValueError("Both inputs must be lists.")

    if len(operators) != len(operands) - 1:
        raise ValueError("Number of operators must be one less than number of operands.")

    if len(operands) < 2:
        raise ValueError("Operand list must contain at least two elements.")

    if not all(isinstance(x, int) and x >= 0 for x in operands):
        raise ValueError("Operand list must contain only non-negative integers.")

    if not all(op in {'+', '-', '*', '//', '**'} for op in operators):
        raise ValueError("Operators must be one of '+', '-', '*', '//', '**'.")

    # Build the expression as a string
    expression = ""
    for i in range(len(operators)):
        expression += str(operands[i]) + operators[i]
    expression += str(operands[-1])

    # Evaluate the expression with correct operator precedence
    try:
        result = eval(expression)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

    return result
