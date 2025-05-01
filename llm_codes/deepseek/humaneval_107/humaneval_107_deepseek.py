############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef even_odd_palindrome(n):\n    \"\"\"\n    Given a positive integer n, return a tuple that has the number of even and odd\n    integer palindromes that fall within the range(1, n), inclusive.\n\n    Example 1:\n\n        Input: 3\n        Output: (1, 2)\n        Explanation:\n        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.\n\n    Example 2:\n\n        Input: 12\n        Output: (4, 6)\n        Explanation:\n        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.\n\n    Note:\n        1. 1 <= n <= 10^3\n        2. returned tuple has the number of even and odd integer palindromes respectively.\n    \"\"\"\n"   
#
# response:
#
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for num in range(1, n + 1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
