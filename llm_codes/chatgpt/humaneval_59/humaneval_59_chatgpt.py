############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\n\ndef largest_prime_factor(n: int):\n    \"\"\"Return the largest prime factor of n. Assume n > 1 and is not a prime.\n    >>> largest_prime_factor(13195)\n    29\n    >>> largest_prime_factor(2048)\n    2\n    \"\"\"\n"

# response:
#
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Remove all factors of 2
    while n % 2 == 0:
        n //= 2
        last_factor = 2

    # Check odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
            last_factor = factor
        factor += 2

    # If what's left is greater than 2, it must be a prime factor
    if n > 2:
        return n
    return last_factor
