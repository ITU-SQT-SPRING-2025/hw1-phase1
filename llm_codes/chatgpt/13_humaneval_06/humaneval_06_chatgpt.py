from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string representing multiple groups of nested parentheses separated by spaces.
    For each group, output the deepest level of nesting of parentheses.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    results = []
    groups = paren_string.strip().split()

    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        results.append(max_depth)
    
    return results
