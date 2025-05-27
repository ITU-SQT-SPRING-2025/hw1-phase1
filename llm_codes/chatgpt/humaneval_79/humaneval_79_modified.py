############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef decimal_to_binary(decimal):\n """You will be given a number in decimal form and your task is to convert it to\n binary format. The function only supports nonnegative numbers. The function should return a string, with each character representing a binary\n number. Each character in the string will be '0' or '1'.\n\n There will be an extra couple of characters 'db' at the beginning and at the end of the string.\n The extra characters are there to help with the format.\n\n Examples:\n decimal_to_binary(15) # returns "db1111db"\n decimal_to_binary(32) # returns "db100000db"\n """\n"
#
# The modification done to the prompt makes the function support only nonnegative numbers.
# "... The function only supports nonnegative numbers. ..."
# response:
#
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function only supports nonnegative numbers. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15) # returns "db1111db"
    decimal_to_binary(32) # returns "db100000db"
    """
    if decimal < 0:
        raise ValueError("Only nonnegative numbers are supported.")
    
    binary_str = bin(decimal)[2:]  # remove the '0b' prefix
    return f"db{binary_str}db"
