""" Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 

characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not). """

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointers
        p1, p2 = 0,0
        
        # loop while pointers are less than length
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
         
        # we've reached the end of s with all matching sequence
        if p1 == len(s):
            return True
                    
        # we reached the end of t without finding all char in sequence  
        return False