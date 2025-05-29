############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
# def largest_prime_factor(n: int):
#     Return the largest prime factor of n.
#     Assume n > 1 and is not a prime.
#     In cases of invalid inputs, return -1 (for ex: input being smaller than one).
#     largest_prime_factor(13195) >>> 29
#     largest_prime_factor(2048) >>>   2
#     largest_prime_factor(0) >>> -1

# response:
#
def largest_prime_factor(n: int) -> int:
    if n <= 1:
        return -1

    # Start dividing n by 2 until it is odd
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Try odd divisors from 3 upwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            max_prime = factor
            n //= factor
        factor += 2

    # If n becomes a prime number greater than 2
    if n > 2:
        max_prime = n

    return max_prime
