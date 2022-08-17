""" Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 

No two characters may map to the same character, but a character may map to itself. """

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # make hash table for s and t
        chars_st, chars_ts = {}, {}
        
        if len(s) != len(t):
            return False
        
        # populate hash tables
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            
            # want to check first if there is already a mapping to a diff char
            if ((c1 in chars_st and chars_st[c1] != c2) or (c2 in chars_ts and chars_ts[c2] != c1)):
                return False
            
            # insert key values for chars
            chars_st[c1] = c2
            chars_ts[c2] = c1
        
        # no duplicate mappings
        return True