############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef words_in_sentence(sentence):\n    \"\"\"\n    You are given a string representing a sentence,\n    the sentence contains some words separated by a space,\n    and you have to return a string that contains the words from the original sentence,\n    whose lengths are prime numbers,\n    the order of the words in the new string should be the same as the original one.\n\n    Example 1:\n        Input: sentence = \"This is a test\"\n        Output: \"is\"\n\n    Example 2:\n        Input: sentence = \"lets go for swimming\"\n        Output: \"go for\"\n\n    Constraints:\n        * 1 <= len(sentence) <= 100\n        * sentence contains only letters\n    \"\"\"\n"
#
# response:
#
def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    words = sentence.split()
    filtered_words = [word for word in words if is_prime(len(word))]
    return ' '.join(filtered_words)
