############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef move_one_ball(arr):\n    \"\"\"We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The\n    numbers in the array will be randomly ordered. Your task is to determine if\n    it is possible to get an array sorted in non-decreasing order by performing \n    the following operation on the given array:\n        You are allowed to perform right shift operation any number of times.\n    \n    One right shift operation means shifting all elements of the array by one\n    position in the right direction. The last element of the array will be moved to\n    the starting position in the array i.e. 0th index. \n\n    If it is possible to obtain the sorted array by performing the above operation\n    then return True else return False.\n    If the given array is empty then return True.\n\n    Note: The given list is guaranteed to have unique elements.\n\n    For Example:\n    \n    move_one_ball([3, 4, 5, 1, 2])==>True\n    Explanation: By performin 2 right shift operations, non-decreasing order can\n                 be achieved for the given array.\n    move_one_ball([3, 5, 4, 1, 2])==>False\n    Explanation:It is not possible to get non-decreasing order for the given\n                array by performing any number of right shift operations.\n                \n    \"\"\"\n"

# response:
#
def move_one_ball(arr):
    if not arr:
        return True

    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
            if count > 1:
                return False

    return True
