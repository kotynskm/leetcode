""" Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only. """

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim off additional white space
        s = s.strip()
        # turn string into an array of words
        words_list = s.split(" ")
        
        # get the last index using length of words_list
        last_index = len(words_list) - 1
        
        # return the length of the last word
        return len(words_list[last_index])