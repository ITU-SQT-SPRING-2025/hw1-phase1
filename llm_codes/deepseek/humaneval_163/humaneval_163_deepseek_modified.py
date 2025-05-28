############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "Given two non-negative integers a and b, return the even digits between a and b, in ascending order. \n\n Even digits are limited to the single-digit numbers in the set [0, 2, 4, 6, 8]. Return only those digits \n that lie numerically between a and b, inclusive. Do not consider any multi-digit numbers — only the digits themselves.    \n For example:    \n generate_integers(2, 8) => [2, 4, 6, 8]    \n generate_integers(8, 2) => [2, 4, 6, 8]    \n generate_integers(10, 14) => []    \n generate_integers(0, 2) => [0, 2]    \n \n If either a or b is negative, the function should raise a ValueError."   
#
# response:
#

def generate_integers(a, b):
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative")
    
    lower = min(a, b)
    upper = max(a, b)
    
    even_digits = [0, 2, 4, 6, 8]
    result = [d for d in even_digits if lower <= d <= upper]
    
    return result