############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef even_odd_palindrome(n):\n    \"\"\"\n    Given a positive integer n, return a tuple that has the number of even and odd\n    integer palindromes that fall within the range(1, n), inclusive.\n\n    Example 1:\n\n        Input: 3\n        Output: (1, 2)\n        Explanation:\n        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.\n\n    Example 2:\n\n        Input: 12\n        Output: (4, 6)\n        Explanation:\n        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.\n\n    Note:\n        1. 1 <= n <= 10^3\n        2. returned tuple has the number of even and odd integer palindromes respectively.\n    \"\"\"\n"   
#
# response:
#
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:
        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. One of them is even, and two of them are odd.

    Example 2:
        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Four of them are even, and six of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. Returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # Check if the number is a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)
