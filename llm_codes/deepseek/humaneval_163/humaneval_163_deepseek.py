############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "generate_integers(a, b):\n    \"\"\"\n    Given two positive integers a and b, return the even digits between a\n    and b, in ascending order.\n\n    For example:\n    generate_integers(2, 8) => [2, 4, 6, 8]\n    generate_integers(8, 2) => [2, 4, 6, 8]\n    generate_integers(10, 14) => []\n    \"\"\"\n"   
#
# response:
#
def generate_integers(a, b):
    start = min(a, b)
    end = max(a, b)
    result = []
    for num in range(start, end + 1):
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            result.append(num)
    return result
