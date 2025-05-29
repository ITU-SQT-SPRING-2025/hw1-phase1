############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
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
#

# response:
#
def do_algebra(operators, operands):
    # Input validation
    if len(operators) != len(operands) - 1:
        raise ValueError("Length of operators must be one less than the length of operands")

    if len(operators) < 1 or len(operands) < 2:
        raise ValueError("Operators list must have at least one operator, and operands list at least two operands")

    for num in operands:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Operands must be non-negative integers")

    valid_ops = {'+', '-', '*', '//', '**'}
    for op in operators:
        if op not in valid_ops:
            raise ValueError(f"Invalid operator {op}")

    # Make copies to avoid modifying the original lists
    ops = operators.copy()
    nums = operands.copy()

    # Helper function to process operations of a certain type
    def process_operations(operation_types):
        i = 0
        while i < len(ops):
            if ops[i] in operation_types:
                op = ops[i]
                a = nums[i]
                b = nums[i+1]
                if op == '**':
                    res = a ** b
                elif op == '*':
                    res = a * b
                elif op == '//':
                    if b == 0:
                        raise ValueError("Division by zero")
                    res = a // b
                elif op == '+':
                    res = a + b
                elif op == '-':
                    res = a - b
                else:
                    raise ValueError("Unexpected operator")

                # Update nums and ops
                nums[i] = res
                del nums[i+1]
                del ops[i]
                # Since we removed an operator, the next operator is now at the same index
                i -= 1  # because after deletion, the next operation to check is at current i
            i += 1

    # Process exponentiation first
    process_operations(['**'])

    # Then process multiplication and floor division
    process_operations(['*', '//'])

    # Finally process addition and subtraction
    process_operations(['+', '-'])

    return nums[0]
