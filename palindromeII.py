""" Given a string s, return true if the s can be palindrome after deleting at most one character from it.

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # we need to check after removing right and left char
                l2,r2,l3,r3 = l + 1, r, l, r - 1
                # bool flags to judge char removal
                first, second = True, True
                # check the left side incremented by 1 (left char removal)
                while l2 < r2:
                    if s[l2] != s[r2]:
                        first = False
                        break
                    l2 += 1
                    r2 -= 1
                
                # check the right side (right char removal)
                while l3 < r3:
                    if s[l3] != s[r3]:
                        second = False
                        break
                    l3 += 1
                    r3 -= 1
                
                if first or second:
                    return True
                else:
                    return False
                    
            l += 1
            r -= 1
            
        return True
    