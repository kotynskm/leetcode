""" Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,

typically using all the original letters exactly once. """

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make hash table of chars in s and t
        countS, countT = {}, {}
        
        # if lengths are not the same they are not anagrams
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # use .get to check for the key, set default value to 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # iterate keys and check countT has that key
        for key in countS:
            if key not in countT:
                return False
            else:
                # check if count at that key is not the same
                if countT[key] != countS[key]:
                    return False
                
        return True