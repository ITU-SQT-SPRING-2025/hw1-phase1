############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef is_sorted(lst):\n '''\n Given a list of numbers, return whether or not they are sorted\n in ascending order. If list has more than 1 duplicate of the same\n number, return False. Assume no negative numbers and only integers.\n\n Examples\n is_sorted([5]) \u279e True\n is_sorted([1, 2, 3, 4, 5]) \u279e True\n is_sorted([1, 3, 2, 4, 5]) \u279e False\n is_sorted([1, 2, 3, 4, 5, 6]) \u279e True\n is_sorted([1, 2, 3, 4, 5, 6, 7]) \u279e True\n is_sorted([1, 3, 2, 4, 5, 6, 7]) \u279e False\n is_sorted([1, 2, 2, 3, 3, 4]) \u279e True\n is_sorted([1, 2, 2, 2, 3, 4]) \u279e False\n '''\n"

# response:
#
def is_sorted(lst):
    if lst != sorted(lst):
        return False
    
    from collections import Counter
    counts = Counter(lst)
    
    for count in counts.values():
        if count > 2:
            return False
    
    return True
