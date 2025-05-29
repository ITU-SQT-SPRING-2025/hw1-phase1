############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\n def words_in_sentence(sentence):    \n'''    \n You are given a string representing a sentence,    \n the sentence contains some words separated by a space,    \n and you have to return a string that contains the words from the original sentence,    \n whose lengths are prime numbers,    \n the order of the words in the new string should be the same as the original one.\n   \n Prime Number Rules:    \n 1. A prime number is a natural number greater than 1    \n 2. It must have exactly two distinct positive divisors: 1 and itself    \n 3. Special cases:     \n  - 1 is NOT prime (only one divisor)     \n  - 2 is the only even prime number      \n - All other primes are odd    \n\n Example 1:        \n Input: "This is a test"        \n Output: "is" (lengths: 4,2,1,4 → only 2 is prime)    \n\nExample 2:        \nInput: "lets go for swimming"        \nOutput: "go for" (lengths: 4,2,3,7 → 2 and 3 are prime)    \n\nConstraints:        \n* 1 <= len(sentence) <= 100        \n* sentence contains only letters    \n'''"
#
# response:
#
def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    words = sentence.split()
    filtered_words = [word for word in words if is_prime(len(word))]
    return ' '.join(filtered_words)
