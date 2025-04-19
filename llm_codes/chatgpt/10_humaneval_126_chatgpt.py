# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef is_sorted(lst):\n '''\n Given a list of numbers, return whether or not they are sorted\n in ascending order. If list has more than 1 duplicate of the same\n number, return False. Assume no negative numbers and only integers.\n\n Examples\n is_sorted([5]) \u279e True\n is_sorted([1, 2, 3, 4, 5]) \u279e True\n is_sorted([1, 3, 2, 4, 5]) \u279e False\n is_sorted([1, 2, 3, 4, 5, 6]) \u279e True\n is_sorted([1, 2, 3, 4, 5, 6, 7]) \u279e True\n is_sorted([1, 3, 2, 4, 5, 6, 7]) \u279e False\n is_sorted([1, 2, 2, 3, 3, 4]) \u279e True\n is_sorted([1, 2, 2, 2, 3, 4]) \u279e False\n '''\n"

# response:
#

# Here's a Python function is_sorted(lst) that follows the specified rules:
# - The list must be in ascending order.
# - Duplicates are allowed only once; if a number appears more than twice, return False.
# Here's how to implement that:

def is_sorted(lst):
    if lst != sorted(lst):
        return False
    
    from collections import Counter
    counts = Counter(lst)
    
    for count in counts.values():
        if count > 2:
            return False
    
    return True

# How it works:
#   1. lst != sorted(lst) checks if the list is not in ascending order.
#   2. Counter(lst) counts how many times each number appears.
#   3. If any number appears more than twice, it returns False.
# Examples:
# print(is_sorted([5]))                      # True
# print(is_sorted([1, 2, 3, 4, 5]))          # True
# print(is_sorted([1, 3, 2, 4, 5]))          # False
# print(is_sorted([1, 2, 3, 4, 5, 6]))       # True
# print(is_sorted([1, 2, 3, 4, 5, 6, 7]))    # True
# print(is_sorted([1, 3, 2, 4, 5, 6, 7]))    # False
# print(is_sorted([1, 2, 2, 3, 3, 4]))       # True
# print(is_sorted([1, 2, 2, 2, 3, 4]))       # False
# Let me know if you want to tweak how duplicates are handled!
