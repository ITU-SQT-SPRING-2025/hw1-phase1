############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "from typing import List\n\n def parse_nested_parens(paren_string: str) -> List[int]:\n""" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.\nFor each of the group, output the deepest level of nesting of parentheses.\nE.g. (()()) has maximum two levels of nesting while ((())) has three.\nReturn empty list for groups without parentheses.\nRaise IndexError if parentheses are unbalanced.\n\n>>> parse_nested_parens('(()()) ((())) () ((())()())')\n[2, 3, 1, 3]\n>>> parse_nested_parens('abc def')\n[]\n>>> parse_nested_parens('(()')\nTraceback (most recent call last):\n    ...\nIndexError: Unbalanced parentheses\n """"   
#
# response:
#

from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        has_parentheses = False
        for char in group:
            if char == '(':
                current_depth += 1
                has_parentheses = True
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                if current_depth < 0:
                    raise IndexError("Unbalanced parentheses")
            else:
                # Handle invalid characters? According to problem statement, input is groups of nested parentheses.
                pass
        if current_depth != 0:
            raise IndexError("Unbalanced parentheses")
        if has_parentheses:
            result.append(max_depth)
    return result
