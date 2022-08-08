""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters

and removing all non-alphanumeric characters, it reads the same forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        
        for char in s:
            if char.isalnum():
                result += char.lower()
                
        return result == result[::-1]

# solution using two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left and right pointers
        l,r = 0, len(s) - 1
        
        # loop while l < r
        while l < r:
        
        # check that character is alphanumeric, if not increment the pointer - use a while loop and not if because we want
        # to continue to skip over each non alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
        # if character at l.lower() is not character at r.lower(), return False
            if s[l].lower() != s[r].lower():
                return False
        
        # else increment the counter
            else:
                l, r = l + 1, r - 1
        
        # return True if we've reached the middle of the word/pointers overlap
        return True

