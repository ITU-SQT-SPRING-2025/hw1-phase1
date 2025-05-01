############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef even_odd_count(num):\n    \"\"\"Given an integer. return a tuple that has the number of even and odd digits respectively.\n\n     Example:\n        even_odd_count(-12) ==> (1, 1)\n        even_odd_count(123) ==> (1, 2)\n    \"\"\"\n"   
#
# response:
#
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)  # Handle negative numbers
    even = odd = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
