""" Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1. """

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash table of characters
        chars_dict = {}
        
        # build hash table with chars and char counts
        for char in s:
            chars_dict[char] = 1 + chars_dict.get(char, 0)
        
        # loop over string and check hash table for count, if it's 1, return the index
        for i, char in enumerate(s):
            if chars_dict[char] == 1:
                return i
        return -1