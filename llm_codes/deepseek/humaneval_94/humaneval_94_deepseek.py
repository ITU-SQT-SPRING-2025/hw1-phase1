############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\n\ndef skjkasdkd(lst):\n """You are given a list of integers.\n You need to find the largest prime value and return the sum of its digits.\n\n Examples:\n For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10\n For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25\n For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13\n For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11\n For lst = [0,81,12,3,1,21] the output should be 3\n For lst = [0,8,1,2,1,7] the output should be 7\n """\n"

# response:
#
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    max_prime = -1
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num
    
    if max_prime == -1:
        return 0  # though examples suggest it's not needed
    
    sum_digits = sum(int(d) for d in str(max_prime))
    return sum_digits
