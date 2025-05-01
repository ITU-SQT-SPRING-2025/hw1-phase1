############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\n\ndef largest_prime_factor(n: int):\n    \"\"\"Return the largest prime factor of n. Assume n > 1 and is not a prime.\n    >>> largest_prime_factor(13195)\n    29\n    >>> largest_prime_factor(2048)\n    2\n    \"\"\"\n"

# response:
#
import math


def largest_prime_factor(n: int):
    largest_factor = 1
    # Handle even factors
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    # Now n is odd, check odd divisors up to sqrt(n)
    i = 3
    max_factor = math.sqrt(n)
    while i <= max_factor:
        while n % i == 0:
            largest_factor = i
            n = n // i
            max_factor = math.sqrt(n)
        i += 2
    if n > 1:
        largest_factor = n
    return largest_factor
