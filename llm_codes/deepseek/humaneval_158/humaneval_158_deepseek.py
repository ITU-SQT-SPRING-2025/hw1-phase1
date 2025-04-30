############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   DeepSeek-V3
#
# prompt:
#   "\ndef find_max(words):\n    \"\"\"Write a function that accepts a list of strings.\n    The list contains different words. Return the word with maximum number\n    of unique characters. If multiple strings have maximum number of unique\n    characters, return the one which comes first in lexicographical order.\n\n    find_max([\"name\", \"of\", \"string\"]) == \"string\"\n    find_max([\"name\", \"enam\", \"game\"]) == \"enam\"\n    find_max([\"aaaaaaa\", \"bb\" ,\"cc\"]) == \"\"aaaaaaa\"\n    \"\"\"\n"

# response:
#
def find_max(words):
    max_unique = -1
    candidates = []

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            candidates = [word]
        elif unique_chars == max_unique:
            candidates.append(word)

    if not candidates:
        return ""

    candidates.sort()
    return candidates[0]
