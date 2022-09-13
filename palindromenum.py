""" Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not. """

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to str and use two pointers
        str_num = str(x)
        
        l, r = 0, len(str_num) - 1
        
        while l < r:
            if str_num[l] != str_num[r]:
                return False
            
            else:
                l += 1
                r -= 1
                
        return True