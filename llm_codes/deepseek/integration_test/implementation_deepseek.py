############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#

# prompt: 
# You will implement a Python class named Secret that has methods of encoding a given string by shifting forward 5, wrapping around z to a in the alphabet, and decoding in the reverse manner. The class will also have a method that takes a string representing a sentence. The sentence contains some words separated by a space, and it will find a new string that contains the words from the original sentence whose lengths are prime numbers. The order of words in the original sentence will be preserved in the new sentence. Another method for this class is going to find if length of words of a sentence is monotonically increasing, or monotonically decreasing or neither of them. 
# Examples:
# Secret.encode("fun code") => "kzs htij"
# Secret.encode("quick fox") => "vznhp ktc"
# Secret.decode("vznhp ktc") => "quick fox"
# Secret.isMonotonic("fun code") => True
# Secret.isMonotonic("coding is fun") => False
# Secret.processSentence("fun code") => "fun code"
# Secret.processSentence("this is a test") => "is"
#
# response:
#

class Secret:
    @staticmethod
    def _shift_char(c, shift):
        if 'a' <= c <= 'z':
            return chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
        else:
            return c

    @staticmethod
    def encode(s):
        return ''.join(Secret._shift_char(c, 5) for c in s)

    @staticmethod
    def decode(s):
        return ''.join(Secret._shift_char(c, -5) for c in s)

    @staticmethod
    def _is_prime(n):
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

    @staticmethod
    def processSentence(sentence):
        words = sentence.split()
        filtered_words = [word for word in words if Secret._is_prime(len(word))]
        return ' '.join(filtered_words)

    @staticmethod
    def isMonotonic(sentence):
        words = sentence.split()
        if len(words) <= 1:
            return True
        
        lengths = [len(word) for word in words]
        
        increasing = True
        for i in range(1, len(lengths)):
            if lengths[i] <= lengths[i-1]:
                increasing = False
                break
                
        if increasing:
            return True
            
        decreasing = True
        for i in range(1, len(lengths)):
            if lengths[i] >= lengths[i-1]:
                decreasing = False
                break
                
        return decreasing
