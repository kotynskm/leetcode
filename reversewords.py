""" Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order. """

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []
        reverse = ""

        for word in words:
            # loop word backwards to build in reverse
            for i in range(len(word)-1,-1,-1):
                reverse += word[i]
            # add word with a space
            reverse += " "
        
        result.append(reverse)
       
        
        
        return ' '.join(result).rstrip()