############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef will_it_fly(q,w):\n '''\n Write a function that returns True if the object q will fly, and False otherwise.\n The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.\n\n Example:\n will_it_fly([1, 2], 5) \u279e False \n # 1+2 is less than the maximum possible weight, but it's unbalanced.\n\n will_it_fly([3, 2, 3], 1) \u279e False\n # it's balanced, but 3+2+3 is more than the maximum possible weight.\n\n will_it_fly([3, 2, 3], 9) \u279e True\n # 3+2+3 is less than the maximum possible weight, and it's balanced.\n\n will_it_fly([3], 5) \u279e True\n # 3 is less than the maximum possible weight, and it's balanced.\n '''\n"

# response:
#
def will_it_fly(q, w):
    # Check if the list is a palindrome
    is_palindrome = q == q[::-1]
    # Check if the sum of elements is <= w
    sum_ok = sum(q) <= w
    return is_palindrome and sum_ok
