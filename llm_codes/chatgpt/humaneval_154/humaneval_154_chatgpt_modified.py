############################
# @Authors
# Student Name: Fatih Baskın
# Student ID: 150210710
############################

# used LLM model:
#   GPT-4o
#
# prompt:
# def cycpattern_check(a , b):
#     You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
#     cycpattern_check("abcd","abd") => False
#     cycpattern_check("hello","ell") => True
#     cycpattern_check("whassup","psus") => False
#     cycpattern_check("abab","baa") => True
#     cycpattern_check("efef","eeff") => False
#     cycpattern_check("himenss","simen") => True
#     Be aware of cyclic patterns,  you must return True if b or any of its rotations is a substring of a.for example:
#     cycpattern_check("abcdefg", "fgabc") => True # be careful with this case
#     Empty strings are count as a substring.

# response:
#
def cycpattern_check(a, b):
    if b == "":
        return True
    double_b = b + b
    for i in range(len(b)):
        rotated = double_b[i:i+len(b)]
        if rotated in a:
            return True
    return False
