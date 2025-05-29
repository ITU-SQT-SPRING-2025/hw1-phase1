############################
# @Authors
# Student Name: Onur Yavri
# Student ID: 150220760
############################

# used LLM model: 
#   GPT-4o
#
# In this prompt, we have mixed up the functionality of HumanEval/143, HumanEval/57 and HumanEval/50
# prompt: 
# "You will implement a Python class named Secret that has methods of encoding a given string by shifting forward 5, wrapping around z to a in the alphabet, and decoding in the reverse manner. The class will also have a method that takes a string representing a sentence. The sentence contains some words separated by a space, and it will find a new string that contains the words from the original sentence whose lengths are prime numbers. The order of words in the original sentence will be preserved in the new sentence. Another method for this class is going to find if length of words of a sentence is monotonically increasing, or monotonically decreasing or neither of them. \nExamples: \nSecret.encode("fun code") => "kzs htij" \nSecret.encode("quick fox") => "vznhp ktc" \nSecret.decode("vznhp ktc") => "quick fox" \nSecret.isMonotonic("fun code") => True \nSecret.isMonotonic("coding is fun") => False \nSecret.processSentence("fun code") => "fun code" \nSecret.processSentence("this is a test") => "is""

# response:
#

class Secret:
    @staticmethod
    def encode(text):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                shifted = (ord(char) - base + 5) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def decode(text):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                shifted = (ord(char) - base - 5) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def processSentence(sentence):
        words = sentence.split()
        return ' '.join([word for word in words if Secret.is_prime(len(word))])

    @staticmethod
    def isMonotonic(sentence):
        lengths = [len(word) for word in sentence.split()]
        return (
            all(x <= y for x, y in zip(lengths, lengths[1:])) or
            all(x >= y for x, y in zip(lengths, lengths[1:]))
        )
