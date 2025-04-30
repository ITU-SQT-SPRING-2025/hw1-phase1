############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
#   "\ndef find_max(words):\n    \"\"\"Write a function that accepts a list of strings.\n    The list contains different words. Return the word with maximum number\n    of unique characters. If multiple strings have maximum number of unique\n    characters, return the one which comes first in lexicographical order.\n\n    find_max([\"name\", \"of\", \"string\"]) == \"string\"\n    find_max([\"name\", \"enam\", \"game\"]) == \"enam\"\n    find_max([\"aaaaaaa\", \"bb\" ,\"cc\"]) == \"\"aaaaaaa\"\n    \"\"\"\n"

# response:
#
def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    return min(words, key=lambda word: (-len(set(word)), word))
