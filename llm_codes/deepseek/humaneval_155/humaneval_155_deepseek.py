############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef even_odd_count(num):\n    \"\"\"Given an integer. return a tuple that has the number of even and odd digits respectively.\n\n     Example:\n        even_odd_count(-12) ==> (1, 1)\n        even_odd_count(123) ==> (1, 2)\n    \"\"\"\n"   
#
# response:
#
def even_odd_count(num):
    even = 0
    odd = 0
    num_str = str(abs(num))
    for digit in num_str:
        d = int(digit)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
